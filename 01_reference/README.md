# 01_reference — 参考小说源登记

本目录存放 15 本参考小说的**来源登记与元数据**（入库）：

- `SOURCE_ACQUISITION_MATRIX.md` + `source_acquisition.json` —— 15 本获取矩阵（2026-09-13 实证核验）
- `global/_SOURCE_MANIFEST.md` —— GLOBAL 组源采集登记
- 各书目录下的 `metadata.md` / `toc_and_metadata.md` —— 元数据

**版权源文本（官方试读摘录 .txt 等）被 .gitignore 排除在公开仓库之外**（匹配 `01_reference/**/*.txt|epub|pdf|mobi|azw3|docx`），仅保留在本地 Mac mini 工作副本上。当前被排除的本地文件：

- `global/it-ends-with-us/official_excerpt_simon_schuster.txt`
- `global/lessons-in-chemistry/official_extract_penguin_au.txt`
- `global/fourth-wing/official_peek_inside_entangled.txt`
- `global/the-midnight-library/douban_trial_opening.txt`

其他设备克隆本仓库后，若分析工作需要这些试读文本，请通过官方渠道重新获取并放入对应目录（不会影响 Git 状态）。**禁止下载盗版源文件**（见 `00_system/COPYRIGHT_RULES.md`）。

15 本的完整分析结论在 `02_analysis/`，跨作品机制库在 `03_story_dna/`。
