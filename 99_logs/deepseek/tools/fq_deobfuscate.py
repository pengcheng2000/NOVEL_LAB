#!/usr/bin/env python3
"""番茄小说 webfont PUA 混淆解码器 v2
用法:
  fq_deobfuscate.py map <font.woff2> <freq_list.txt> <html...>   -> mapping.json
  fq_deobfuscate.py clean <input.html> <output.txt>              -> 解码章节正文
v2 改进:
  - 候选集限制为字频表 top-N 常用字
  - 用真实章节文本统计 PUA 码位频率, 作为分配先验
  - scipy 全局最优分配 (视觉相似度 + 频率匹配), 保证映射单射
仅用于研究抽样章节的文本恢复, 不批量重建整本书。
"""
import sys, os, re, json, html as H
import numpy as np
import freetype
from PIL import Image
from fontTools.ttLib import TTFont
from scipy.optimize import linear_sum_assignment

TOOLS = os.path.dirname(os.path.abspath(__file__))
MAPPING_JSON = os.path.join(TOOLS, "mapping.json")
DIM = 56

def load_freq_list(path, top=2000):
    raw = open(path, "rb").read().decode("gb18030", "ignore")
    chars = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0].strip().isdigit():
            chars.append(parts[1].strip())
    return chars[:top]

def render(face, charcode, size=112):
    face.set_char_size(size * 64)
    idx = face.get_char_index(charcode)
    if idx == 0:
        return None
    face.load_glyph(idx, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
    bmp = face.glyph.bitmap
    if bmp.width == 0 or bmp.rows == 0:
        return None
    a = np.array(bmp.buffer, dtype=np.uint8).reshape(bmp.rows, bmp.width)
    ink = a > 40
    if not ink.any():
        return None
    ys, xs = np.where(ink)
    a = ink[ys.min():ys.max()+1, xs.min():xs.max()+1].astype(np.uint8)
    img = Image.fromarray(a * 255).resize((DIM, DIM), Image.BILINEAR)
    return np.array(img, dtype=np.float32) / 255.0

def pua_counts(html_paths):
    """从章节 HTML 统计 PUA 码位出现次数 + 估算全文总字数"""
    cnt = {}
    total = 0
    for p in html_paths:
        raw = open(p, encoding="utf-8").read()
        paras = re.findall(r"<p>(.*?)</p>", raw, re.S)
        text = H.unescape(re.sub(r"<[^>]+>", "", "".join(paras)))
        for c in text:
            total += 1
            if 0xE000 <= ord(c) <= 0xF8FF:
                cnt[c] = cnt.get(c, 0) + 1
    return cnt, total

def build_mapping(woff2_path, freq_path, html_paths):
    # --- 1. 混淆字体 PUA 字形 ---
    ttf_path = os.path.splitext(woff2_path)[0] + "_conv.ttf"
    _tf = TTFont(woff2_path)
    _tf.flavor = None
    _tf.save(ttf_path)
    obf = freetype.Face(ttf_path)
    pua_cps = sorted(cp for cp in _tf.getBestCmap() if 0xE000 <= cp <= 0xF8FF)
    print(f"PUA glyphs: {len(pua_cps)}", file=sys.stderr)
    obf_mats = {cp: render(obf, cp) for cp in pua_cps}
    pua_cps = [cp for cp in pua_cps if obf_mats[cp] is not None]

    # --- 2. 候选集: 字频表 top 字符, 双系统字体取最大相似 ---
    cand_chars = [c for c in load_freq_list(freq_path) if c.strip()]
    # 确保覆盖 (362 个 PUA 大概率都在 top 800 内, top 2000 兜底)
    sys_fonts = [f for f in ["/System/Library/Fonts/Hiragino Sans GB.ttc",
                             "/System/Library/Fonts/STHeiti Medium.ttc"] if os.path.exists(f)]
    faces = []
    for sf in sys_fonts:
        for i in range(4):
            try:
                f = freetype.Face(sf, i)
                if f.get_char_index(ord("永")) != 0:
                    faces.append(f); break
            except Exception:
                break
    print(f"cand: {len(cand_chars)}, ref faces: {len(faces)}", file=sys.stderr)

    cand_mats = []  # 每个候选字: {face_idx: mat}
    for ch in cand_chars:
        per = [render(f, ord(ch)) for f in faces]
        cand_mats.append(per)

    # --- 3. 文本频率统计 ---
    cnt, total = pua_counts(html_paths)
    print(f"corpus: {total} chars, {len(cnt)} PUA observed", file=sys.stderr)
    # PUA 字符在文中的占比; 未见过的给极小值
    obs = np.array([cnt.get(chr(cp), 0.5) / max(total, 1) for cp in pua_cps])
    # 候选字的期望占比: 用名次近似 zipf: rank r -> 0.042/r (的≈4%)
    ranks = np.arange(1, len(cand_chars) + 1)
    exp_rate = 0.042 / ranks

    # --- 4. 相似度矩阵 ---
    n, m = len(pua_cps), len(cand_chars)
    vis = np.zeros((n, m), dtype=np.float32)
    for i, cp in enumerate(pua_cps):
        om = obf_mats[cp]
        best_per_cand = np.full(m, -1.0, dtype=np.float32)
        for fi in range(len(faces)):
            stack = np.stack([cand_mats[j][fi] for j in range(m) if cand_mats[j][fi] is not None])
            idxs = [j for j in range(m) if cand_mats[j][fi] is not None]
            inter = np.minimum(stack, om).sum(axis=(1, 2))
            union = np.maximum(stack, om).sum(axis=(1, 2)) + 1e-6
            iou = inter / union
            sm = (stack - stack.mean(axis=(1, 2), keepdims=True)).reshape(len(stack), -1)
            sv = (om - om.mean()).ravel()
            corr = (sm @ sv) / (np.linalg.norm(sm, axis=1) * np.linalg.norm(sv) + 1e-6)
            sc = (0.65 * iou + 0.35 * np.clip(corr, 0, 1))
            for k, j in enumerate(idxs):
                if sc[k] > best_per_cand[j]:
                    best_per_cand[j] = sc[k]
        vis[i] = best_per_cand
    # 频率兼容项: 观测 rate vs zipf 期望 rate, 对数距离
    fr = np.log(obs[:, None] + 1e-7) - np.log(exp_rate[None, :])
    freq_pen = -np.abs(fr) * 0.15  # 软惩罚
    score = vis + freq_pen

    # --- 5. 全局分配 (n < m, 选 n 个候选) ---
    row, col = linear_sum_assignment(-score)
    mapping = {}
    detail = {}
    for r, c in zip(row, col):
        cp, ch = pua_cps[r], cand_chars[c]
        mapping[chr(cp)] = ch
        if vis[r, c] < 0.82:
            top3 = np.argsort(-vis[r])[:3]
            detail[chr(cp)] = {"chosen": ch, "vis": float(vis[r, c]),
                               "alts": [(cand_chars[t], float(vis[r, t])) for t in top3 if t != c]}
    with open(MAPPING_JSON, "w", encoding="utf-8") as f:
        json.dump({"font": os.path.basename(woff2_path), "map": mapping, "detail": detail},
                  f, ensure_ascii=False, indent=1)
    print(f"mapped: {len(mapping)}, low-vis(<0.82): {len(detail)}", file=sys.stderr)
    for k, v in list(detail.items())[:25]:
        alts = " ".join(f"{a}:{s:.2f}" for a, s in v["alts"][:2])
        print(f"  U+{ord(k):04X} -> {v['chosen']} ({v['vis']:.2f}) alts {alts}", file=sys.stderr)

def clean_page(html_path, out_path):
    with open(MAPPING_JSON, encoding="utf-8") as f:
        mp = json.load(f)["map"]
    raw = open(html_path, encoding="utf-8").read()
    title = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    paras = re.findall(r"<p>(.*?)</p>", raw, re.S)
    dec = lambda s: "".join(mp.get(c, c) for c in s)
    strip = lambda t: H.unescape(re.sub(r"<[^>]+>", "", t)).strip()
    out = [dec(strip(t)) for t in paras]
    with open(out_path, "w", encoding="utf-8") as f:
        if title:
            f.write(strip(title.group(1)) + "\n\n")
        f.write("\n\n".join(p for p in out if p))

if __name__ == "__main__":
    if sys.argv[1] == "map":
        build_mapping(sys.argv[2], sys.argv[3], sys.argv[4:])
    else:
        clean_page(sys.argv[2], sys.argv[3])
