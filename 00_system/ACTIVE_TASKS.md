# ACTIVE_TASKS — 当前活动任务

最后更新：2026-09-14（GPT-5.6 Sol / Codex：Batch A Ch2–3 Editorial Review 完成；Ch2 ACCEPT WITH REVISION，Ch3 MAJOR REVISION；下一任务 Gemini Batch Rewrite；未 Canon Update）

## 当前

| 任务 | 状态 | 备注 |
|---|---|---|
| Phase 3：证据有界 Story DNA 提取 | **COMPLETED** | 2026-09-13 |
| Phase 4：原创 IP 孵化（8 候选 → Top 3） | **COMPLETED** | 2026-09-13 |
| Phase 4.5：Finalist 压力测试（C03/C05/C06） | **COMPLETED** | 2026-09-14；产出见下；已提交最终汇报 |
| 第一部原创 IP 选择 | **COMPLETED** | 用户确认 C05《雨天旧衣店》；C03/C06 保留未来候选 |
| Phase 5：Story Bible Development | **COMPLETED** | 产出位于 `04_original_project/C05_rainy_old_clothes/`；00–08 设计与 11_reviews 已完成，未写正文 |
| **GitHub 跨设备迁移** | **COMPLETED** | 2026-09-14（Claude/GLM）：138 文件 → `github.com/pengcheng2000/NOVEL_LAB`（main，`5a13830`）；AGENT_PROTOCOL / MODEL_ROLES / HANDOFF 建立；详见 PROJECT_STATUS.md 迁移行 |
| Phase 6A：Novel Production Setup | **COMPLETED** | `12_production/` 工作流、文风规范、模板、缺口检查、Writer Instructions、验收标准与 Chapter 001–003 Brief 已落盘 |
| Chapter 001 Draft | **COMPLETED** | 2026-09-14 Gemini 3.8 Flash 完成 `09_manuscript/drafts/chapter_001_draft.md`（约 8,373 字，超建议区间，待 Sol 裁决压缩） |
| Chapter 001 Continuity Pass | **COMPLETED** | 2026-09-14 GLM 完成，产出 `12_production/editorial/chapter_001_continuity.md`；结论 PASS WITH NOTES，无 BLOCKER；Canon 未更新 |
| Chapter 001 Editorial Review | **COMPLETED** | 2026-09-14 Sol 完成 `chapter_001_editorial_review.md`；结论 MAJOR REVISION / READY FOR GEMINI REWRITE；目标 6,000–6,500 字 |
| Chapter 001 Rewrite | **COMPLETED** | 2026-09-14 Gemini 3.8 Flash 完成 `09_manuscript/drafts/chapter_001_rewrite.md`（6,058 字） |
| Chapter 001 Final Acceptance | **COMPLETED** | Sol FINAL VERDICT：ACCEPT，88/100；`09_manuscript/final/chapter_001_final.md` 已通过总编辑验收 |
| Chapter 001 Final Patch | **COMPLETED** | Gemini commit `e5c3a13`；三项补丁全部正确，未超范围修改 |
| Chapter 001 Canon Update | **COMPLETED** | 2026-09-14 GLM 完成：人物（PROTAGONIST / TANG_LI / 新增 ZHAO_WEIMIN）、关系引擎、Master Timeline（含 2024-03-11 / 1988 冬 / 6-7 事件序列）、旧衣规则 Reveal State、Secret Matrix 知识状态、伏笔植入登记均已更新；新增 `09_manuscript/canon/chapter_001_canon_summary.md` 与 `12_production/CHAPTER_002_READINESS.md`（**READY**）。Chapter 001 状态 = CANON_UPDATED |
| Phase 6 Batch 01 Planning（Ch2–6） | **COMPLETED** | Mini-Arc、信息释放表、节奏/指标/生产组合与 Chapter 002–006 五份执行级 Brief 已落盘；无正文 |
| Chapter 002–003 Draft（Batch A） | **COMPLETED** | 2026-09-14 Gemini 完成（commit `4aaec0d`）：Ch2 4,814 字（超建议区间，待 Sol 裁决压缩）、Ch3 4,731 字（正常浮动） |
| Batch A Continuity Pass（Ch2–3） | **COMPLETED** | 2026-09-14 GLM 完成，产出 `12_production/editorial/batch_01_ch02_03_continuity.md`；结论 PASS WITH NOTES，无 BLOCKER；4 项 ERROR-lite（Ch3 缺"暂停清产"节拍、纸角偶然崩线缺赵授权、周序认出未点明父亲、Ch2 姨母电话超 Brief 台词）+ 7 项 C 类待 Sol 裁决；Canon 未更新 |
| Batch A Editorial Review（Ch2–3） | **COMPLETED** | Sol 联合审稿：Ch2 ACCEPT WITH REVISION，建议 4,250–4,500；Ch3 MAJOR REVISION，建议 4,500–5,000；允许联合 Batch Rewrite |
| Batch A Rewrite（Ch2–3） | **PENDING** | Gemini 3.8 Flash 按 `batch_01_ch02_03_editorial_review.md` 一次性修改两章；分章输出，不进入 Ch4 |

## Phase 4.5 产出清单（2026-09-14，全部落盘）

- `04_original_project/04_stress_test/C03/STRESS_TEST.md` — 调解书：10 测试 + TOP5 失败模式 + 反方 10 条（3 条真实风险：AI 长内容/短剧受众错位/执行可行性工艺债）→ **80 分**，MEDIUM
- `04_original_project/04_stress_test/C05/STRESS_TEST.md` — 雨天旧衣店：10 测试 + TOP5 失败模式 + 反方 11 条（3 条真实风险：治愈疲劳/红海同质化/记忆规则逻辑攻防）→ **81 分**，MEDIUM
- `04_original_project/04_stress_test/C06/STRESS_TEST.md` — 本草遗方：10 测试 + TOP5 失败模式 + 反方 10 条（3 条真实风险：中医舆论/网文流量错配/归类引力）→ **82 分**，MEDIUM-HIGH
- `04_original_project/04_stress_test/FINAL_DECISION_MATRIX.md` — 100 分制重评 + 11 项对比 + Agent 五个 Best + 推荐顺序 C06>C05>C03（按目标换轨规则）+ USER DECISION REQUIRED
- 评分校准记录：C03 的 AI Video 由 Phase 4 潜力分 9 校准为执行分 7（"当前工具能否稳定做"标准）；C05/C06 的 Addiction/Emotional Range 按压力测试实证校准


## Phase 4 产出清单（2026-09-13，全部落盘）

- `04_original_project/00_design_principles/PHASE4_RULES.md`
- `04_original_project/01_candidates/C01–C08/`：CANDIDATE.md ×8（27 字段，Primary Genes 全部标注 MM 编号 + Transformation）+ ORIGINALITY_REVIEW.md ×8（originality-reviewer 七项清单 + 反拼盘 + 因果完整性；8/8 无 HIGH，零重构）
- `04_original_project/02_comparison/CANDIDATE_MATRIX.md`：100 分制对比（Top 3：C05 雨天旧衣店 82 / C06 本草遗方 82 / C03 调解书 81；C02 单王 80.5 第四为最强备选）
- `04_original_project/03_finalists/FINALIST_1–3.md` + `99_rejected/README.md`（备选池说明）
- `05_originality_review/INDEX_PHASE4_CANDIDATES.md`
- 待办：ORIGINAL_PROJECT_DISCOVERY 两项（典籍负空间数据库/规则武器职业化）待用户确认后收入 MASTER 库

## 当前待办队列（按优先级，用户确认后执行）

| # | 任务 | 依赖 |
|---|---|---|
| 1 | Gemini 3.8 Flash：Batch Rewrite Chapter 002–003 | 落实联合 Review 全部 MUST FIX；Ch2 4,250–4,500，Ch3 4,500–5,000；不得进入 Ch4 |
| 2 | GLM Batch Rewrite Continuity | 重点查 Ch1 原话、Ch2→Ch3 信息边界、转述对象、灰衣/寄存联/纸角链与 9/5 时钟 |
| 3 | Sol Batch A Approval | Rewrite + Continuity 完成后；未批准不得 Canon Update 或进入 Ch4 |
| 4 | Phase 6 生产监控：单元语法重复率 / 主谜场景占比 / 谢念主动行动占比 | 随正文生产持续执行 |
| 5 | ORIGINAL_PROJECT_DISCOVERY 反向入库（C06 负空间数据库 + C08 规则武器职业化） | 用户确认；不影响 C05 |
| 6 | Schema v1.1 修订裁决 / Source 政策边界裁决（历史遗留） | 用户裁决 |

## Phase 3 产出清单（2026-09-13，全部落盘）

- `02_analysis/global|china_print|china_web/<book>/STORY_DNA_REPORT.md + NOVEL_DNA.yaml` ×15
- `03_story_dna/global/` GLOBAL_SYNTHESIS.md + GLOBAL_MECHANISMS.yaml
- `03_story_dna/china_print/` CHINA_PRINT_SYNTHESIS.md + CHINA_PRINT_MECHANISMS.yaml
- `03_story_dna/china_web/` CHINA_WEB_SYNTHESIS.md + CHINA_WEB_MECHANISMS.yaml
- `03_story_dna/master/` 10 文件：MASTER_STORY_DNA.md / MASTER_MECHANISM_LIBRARY.yaml（MM01–MM40）/ READER_ADDICTION / RELATIONSHIP / REWARD / GROUNDEDNESS / HOOK / STORY_RENEWAL / AI_VIDEO_STORY / ORIGINALITY_RISK 库 + TOP_STORY_GENES.md（Top 30）
- 四个机制 YAML 已全部通过语法校验（Ruby YAML parse）。

## Phase 3 遗留研究项（不影响当前 C05 开发）

| # | 任务 | 依赖 |
|---|---|---|
| 1 | FULL_SOURCE 升级关键复核（优先级：长安的荔枝→IEWU→十日终焉），复核对应 MASTER 结论 | 用户提供合法源文件 |
| 2 | 网文开篇研究，提升 CHINA_WEB 组 LOW-MEDIUM 结论置信度 | 用户确认启动 |
| 3 | Schema v1.1 修订裁决（SCHEMA_PILOT_REVIEW.md 7 条建议） | 用户裁决 |
| 4 | Source 政策边界最终裁决（HANDOFF_AUDIT.md §9 冲突记录） | 用户裁决 |

## 已完成（历史）

| 任务 | 完成时间 | 执行者 | 备注 |
|---|---|---|---|
| 项目初始化（目录/Schema/规则/Skill） | 2026-09-13 | Kimi | |
| 10 本源文件磁盘扫描（结论：缺失） | 2026-09-13 | Kimi + DeepSeek 独立复核 + Claude 三重复核 | 结论一致可信 |
| GLOBAL 5 本官方试读/元数据采集 | 2026-09-13 | Kimi | 4 PARTIAL + 1 METADATA |
| 网文选目 + 12 维度分析框架 | 2026-09-13 | DeepSeek | |
| 番茄 webfont 反混淆工具链（代码级） | 2026-09-13（Session 中断） | DeepSeek | mapping.json 已产出，正文提取未完成 |
| 接管审计 + SINGLE_AGENT_MODE 切换 | 2026-09-13 | Claude | HANDOFF_AUDIT.md；重写两个状态文件 |
| 15 本平台来源实证调研（211 次工具调用） | 2026-09-13 | Claude（后台 Agent） | SOURCE_ACQUISITION_MATRIX.md + source_acquisition.json |
| IEWU 第 1 章 PARTIAL ANALYSIS + 4 张 Opening Mechanism Cards | 2026-09-13 | Claude | 诚实上限，未凑数 |
| Schema 试跑评估 | 2026-09-13 | Claude | SCHEMA_PILOT_REVIEW.md（仅建议层） |
| Phase 3 BATCH 1：GLOBAL 5 本 STORY_DNA | 2026-09-13 | Claude | 证据分层 + 置信度；Housemaid 剧情级结论声明不可引用 |
| Phase 3 BATCH 2：CHINA_PRINT 5 本 + 组综合 | 2026-09-13 | Claude | 产品逻辑 vs 作品逻辑元结论 |
| Phase 3 BATCH 3：CHINA_WEB 5 本 + 组综合 | 2026-09-13 | Claude | 容器工程学元结论 |
| Phase 3 MASTER 库 + TOP_STORY_GENES | 2026-09-13 | Claude | MM01–MM40 跨书抽象；Top 30 基因七维评分 |

## 中断待续

| 任务 | 中断点 | 恢复方式 |
|---|---|---|
| 番茄章节提取管线 | mapping.json 建成（7 个低置信码位待复核）；woff2/章节 HTML/解码文本均未落盘 | 重新获取番茄页面 + 字体 → 复核 7 个冲突码位 → 跑 clean → 00_source_index.md 登记覆盖范围（工具注释限定研究抽样） |
