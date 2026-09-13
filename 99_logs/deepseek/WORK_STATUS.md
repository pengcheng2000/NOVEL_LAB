# DeepSeek 侧工作状态 — CHINA_WEB 网文研究

最后更新：2026-09-13（DeepSeek 初始化）

## 角色

- 负责【2020—2025 中国热门网络小说】商业叙事机制研究
- 目标：拆解网文为什么能让普通年轻读者连读几十万至几百万字
- 核心维度：黄金开局 / 主角代入 / 接地气 / 美女帅哥恋爱机制 / 装逼打脸结构 / 金手指与信息差 / 爽点工程 / 章末 Hook / 长篇续航 / 幽默 / 信息密度 / Reader Addiction Loop / AI 视频适配 / 原创性边界
- 遵循 `00_system/ANALYSIS_SCHEMA.md`（v1.0，A–Q 全维度）与 `novel-dna-analyzer` 等 Skill

## 5本选目与源文件状态

| # | 作品 | 作者 | 源文件状态 | 分析状态 |
|---|---|---|---|---|
| 1 | 《我真没想重生啊》 | 柳岸花又明 | MISSING_SOURCE | TODO |
| 2 | 《大奉打更人》 | 卖报小郎君 | MISSING_SOURCE | TODO |
| 3 | 《我在精神病院学斩神》 | 三九音域 | MISSING_SOURCE | TODO |
| 4 | 《十日终焉》 | 杀虫队队员 | MISSING_SOURCE | TODO |
| 5 | 《都重生了谁谈恋爱啊》 | 错哪儿了 | MISSING_SOURCE | TODO |

选目覆盖网文主要流派：都市重生校园创业（1、5）/ 仙侠探案（2）/ 都市超自然新怪谈（3）/ 无限流悬疑（4），可保证横向比较的机制多样性。

## 源文件扫描记录

- 2026-09-13：`01_reference/china_web/` 为空。
- 2026-09-13：定向搜索 Documents / Downloads / Desktop / OneDrive / Doubao（按书名关键词 + 大体积 txt/epub/mobi），未发现任何匹配文件。
- 结论：**5本全部 MISSING_SOURCE。在用户提供合法源文件前不开始正文分析，不伪装已读全文，不从盗版渠道下载。**

## 用户需要做什么

将任意一本或多本的小说文本（合法来源：自有购买的正版 txt/epub 等）放入：

```
NOVEL_LAB/01_reference/china_web/
```

建议命名（便于识别）：

- `wozhen_meixiang_chongsheng.txt`（我真没想重生啊）
- `dafeng_dagengren.txt`（大奉打更人）
- `zhan_shen.txt`（我在精神病院学斩神）
- `shiri_zhongyan.txt`（十日终焉）
- `dou_chongsheng_le.txt`（都重生了谁谈恋爱啊）

不要求一次给全。给哪本我先分析哪本。长篇可以只给部分章节（如前30章 + 若干中期卷），分析时会在 `00_source_index.md` 如实标注章节覆盖范围，不做超出覆盖范围的断言。

## 分析计划（源文件到位后）

每本执行 `novel-dna-analyzer` 流程，输出至 `02_analysis/china_web/<novel-slug>/`（16个 md 文件 + NOVEL_DNA.yaml，≥10张机制卡），并在网文维度额外深挖：

1. 黄金开局（前1000字 / 第1章 / 前3章 / 前10章 / 前30章的钩子与奖励时刻）
2. 主角代入机制（Relatability vs Wish Fulfillment 的配比）
3. Groundedness Score（附机制解释）
4. 恋爱/吸引力机制（appearance / status / competence / scarcity / push-pull / delayed confirmation 等）
5. Status Reversal Pattern Library（装逼打脸8步结构 + 出现频率 + 变形方式）
6. 金手指与信息差（优势的给予节奏 / 成本 / 失效 / 防无敌）
7. Reward Ledger（11类奖励的间隔、大小、延迟兑现）
8. Chapter Hook Library（章末钩子分类与轮换规律）
9. Story Renewal Engine（百万字不崩的续航机制）
10. Reader Addiction Loop（主/次/长期循环 + 时间尺度）
11. AI Video Adaptation Pattern（60秒 / 3分钟 / 10分钟 / 长剧分层）
12. 原创性 GREEN / YELLOW / RED 分档

5本完成后输出 `03_story_dna/china_web/` 下 8 份综合文件 + `DEEPSEEK_HANDOFF.md` 交 Kimi。

## 与 Kimi 的协作

- 共享读取：`00_system/`，不改 ANALYSIS_SCHEMA.md（如有修改建议写入 `99_logs/deepseek/SCHEMA_CHANGE_PROPOSAL.md`）
- 不触碰 Kimi 的写入区（02_analysis/global、02_analysis/china_print、03_story_dna/global、03_story_dna/china_print）
- 交接一律通过新文件，不与其同时编辑同一文件
- 第一阶段不自动 git commit

## 事件日志

- 2026-09-13：初始化。读取全部共享规范。5本源文件确认缺失，登记 MISSING_SOURCE。建立本状态文件。等待用户提供源文件。
