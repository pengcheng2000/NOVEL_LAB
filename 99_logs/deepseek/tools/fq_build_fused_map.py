#!/usr/bin/env python3
"""三信号融合构建番茄 PUA 映射表: Vision OCR + 字形视觉匹配 + 文本频率先验
用法: fq_build_fused_map.py <font.woff2> <freq_list.txt> <ocr.json> <html...>
输出: mapping.json (与 fq_deobfuscate.py clean 兼容)
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

def load_freq_list(path, top=2500):
    raw = open(path, "rb").read().decode("gb18030", "ignore")
    chars = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0].strip().isdigit():
            chars.append(parts[1].strip())
    chars.extend("0123456789")
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
    cnt, total = {}, 0
    for p in html_paths:
        raw = open(p, encoding="utf-8").read()
        paras = re.findall(r"<p>(.*?)</p>", raw, re.S)
        text = H.unescape(re.sub(r"<[^>]+>", "", "".join(paras)))
        for c in text:
            total += 1
            if 0xE000 <= ord(c) <= 0xF8FF:
                cnt[c] = cnt.get(c, 0) + 1
    return cnt, total

def main(woff2, freq_path, ocr_path, html_paths):
    ttf_path = os.path.splitext(woff2)[0] + "_conv.ttf"
    _tf = TTFont(woff2); _tf.flavor = None; _tf.save(ttf_path)
    obf = freetype.Face(ttf_path)
    pua_cps = sorted(cp for cp in TTFont(woff2).getBestCmap() if 0xE000 <= cp <= 0xF8FF)
    obf_mats = {cp: render(obf, cp) for cp in pua_cps}
    pua_cps = [cp for cp in pua_cps if obf_mats[cp] is not None]
    n = len(pua_cps)

    ocr = json.load(open(ocr_path))
    freq_chars = load_freq_list(freq_path)

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

    # 视觉相似度: 只对 OCR 候选 + 字频 top600 计算 (省时)
    focus = set()
    for k, cands in ocr.items():
        for c in cands:
            t = c.get("text", "")
            if len(t) == 1:
                focus.add(t)
    focus.update(freq_chars[:600])
    focus = [c for c in focus if c.strip()]
    cand_mats = {c: [render(f, ord(c)) for f in faces] for c in focus}
    vis = {}
    for cp in pua_cps:
        om = obf_mats[cp]
        scored = {}
        for c in focus:
            best = -1.0
            for fi in range(len(faces)):
                cm = cand_mats[c][fi]
                if cm is None: continue
                inter = np.minimum(cm, om).sum()
                union = np.maximum(cm, om).sum() + 1e-6
                iou = inter / union
                sm = (cm - cm.mean()).ravel(); sv = (om - om.mean()).ravel()
                corr = (sm @ sv) / (np.linalg.norm(sm) * np.linalg.norm(sv) + 1e-6)
                best = max(best, 0.6 * iou + 0.4 * np.clip(corr, 0, 1))
            scored[c] = best
        vis[cp] = scored

    cnt, total = pua_counts(html_paths)
    obs = np.array([cnt.get(chr(cp), 0.3) / max(total, 1) for cp in pua_cps])
    ranks = {c: i + 1 for i, c in enumerate(freq_chars)}

    # 融合得分矩阵 (PUA x 候选)
    all_cands = sorted(set(focus) | set(c for c in freq_chars[:50]))
    m = len(all_cands)
    cand_idx = {c: j for j, c in enumerate(all_cands)}
    S = np.zeros((n, m), dtype=np.float64)
    for i, cp in enumerate(pua_cps):
        key = f"U{cp:04X}"
        for c, conf in [(x.get("text", ""), x.get("conf", 0)) for x in ocr.get(key, [])]:
            if len(c) == 1 and c in cand_idx:
                S[i, cand_idx[c]] += 2.2 * conf + 0.3
        for c, v in vis[cp].items():
            if c in cand_idx:
                S[i, cand_idx[c]] += v
        # 频率软约束
        for c, j in cand_idx.items():
            if c in ranks and ranks[c] <= 1000:
                exp_rate = 0.042 / ranks[c] if not c.isdigit() else 0.001
                S[i, j] -= 0.10 * abs(np.log(obs[i] + 1e-7) - np.log(exp_rate))
    # 兜底: 全字频表候选的默认弱惩罚已隐含 (S=0)
    row, col = linear_sum_assignment(-S)
    mapping, detail = {}, {}
    for r, c in zip(row, col):
        cp, ch = pua_cps[r], all_cands[c]
        mapping[chr(cp)] = ch
        ocr_top = [(x.get("text"), round(x.get("conf", 0), 2)) for x in ocr.get(f"U{cp:04X}", [])[:2]]
        if ocr_top and ocr_top[0][0] != ch:
            detail[chr(cp)] = {"chosen": ch, "ocr": ocr_top,
                               "vis_top": [(c, float(s)) for c, s in
                                           sorted(vis[cp].items(), key=lambda kv: -kv[1])[:3]]}
    json.dump({"font": os.path.basename(woff2), "map": mapping, "detail": detail},
              open(MAPPING_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    agree = sum(1 for cp in pua_cps
                if ocr.get(f"U{cp:04X}") and ocr[f"U{cp:04X}"][0].get("text") == mapping[chr(cp)])
    print(f"mapped {len(mapping)}; OCR首选一致: {agree}/{n}; 冲突待复核: {len(detail)}", file=sys.stderr)
    for k, v in list(detail.items())[:30]:
        print(f"  U+{ord(k):04X} -> {v['chosen']} | OCR {v['ocr']} | vis {[(c, round(s,2)) for c,s in v['vis_top']]}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
