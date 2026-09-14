# MODEL_ROLES — 模型职责分工

> 2026-09-14 起按用户最新决策执行。职责是“主责”而非“垄断”，但为防止正文文风漂移，小说正文的日常文字执行固定由 Gemini 3.8 Flash 主责，重大创作决策与最终质量由 GPT-5.6 Sol / Codex 审定。

## GPT-5.6 Sol / Codex

**Role：Editor-in-Chief / Head Writer / Story Architect / Lead Story Editor**

主要负责：

- IP 核心方向与 Story Bible 重大决策。
- 故事框架、卷结构、前 20 章结构与每章 Chapter Brief。
- 人物弧、人物关系重大节点与 Story Engine。
- 伏笔、信息释放与兑现设计。
- 章节结构、连续性逻辑与正文质量审查。
- 正文编辑意见、重大章节示范稿与最终创作标准。

**原则：Sol 负责控制作品上限，但不是日常正文产量模型。** 审稿优先诊断并给出可执行修改意见；除重大示范外，不默认整章改写。单次示范通常控制在 300–800 字，整章最终重写仍交回 Gemini。

## Gemini 3.8 Flash

**Role：Main Writer / Prose Writer / Screenwriter**

主要负责：

- 小说正文初稿与最终正文文字执行。
- 场景扩写、人物互动、对白、情绪表达与描写。
- 根据 Sol 编辑意见完成整章重写。
- 后续影视剧本正文。

**原则：小说正文尽量保持 Gemini 为主要执行写手，避免多个模型频繁混写导致文风漂移。** Gemini 可在 Chapter Brief 允许的范围内自由发挥；不得擅自改变主线、人物重大动机、世界规则、秘密、时间线、重大伏笔或章末目标。

### Production Workflow V2：独立 Continuity / Canon 会话

自 Batch 02 起，连续性复核与 Canon Update 由**第二个、独立上下文的 Gemini 会话**承担。该会话只做 Rewrite Verification、人物/关系/时间线/秘密/伏笔状态维护与 Git 交接，不做文学重写，也不得与 Writer 会话合并。Writer 与 Continuity/Canon 虽使用同一模型家族，必须视为两个职责隔离的 Agent 会话。

## GLM-5.3 Flash

**Role：Project Manager / Continuity Editor / Knowledge Maintainer / Research Agent**

主要负责：

- 维护 `PROJECT_STATUS.md`、`ACTIVE_TASKS.md` 与 `HANDOFF.md`。
- 维护人物状态、时间线、人物关系状态、世界规则、伏笔登记与秘密状态。
- Story Bible 的结构化维护、跨章节连续性检查与 Git 交接。
- Story DNA 研究及机制库维护。

**原则：GLM 检查 Canon 与状态，不做文学重写。** 该角色定义继续适用于既有记录与按需项目管理；自 Batch 02 起，小说日常 Continuity / Canon 生产位依 Workflow V2 转交独立 Gemini 会话。

## GPT-5.6 Terra

**Role：Assistant Editor / Utility Agent**

按需负责：

- 文件整理、Diff、格式检查与普通工程任务。
- 重复表达检测、数据统计与剧本格式整理。

Terra 不属于核心创作链的必需角色，不替代 Sol 的终审、Gemini 的正文执行或 GLM 的连续性职责。

## 正式小说生产链

Workflow V2（自 Batch 02 起）：

`Sol Chapter Planning → Gemini Writer Draft → Continuity Pass → Sol Editorial Review → Gemini Writer Rewrite → Gemini Continuity Rewrite Verification + Canon Update`

普通 Batch 在 Sol 给出 `ACCEPT WITH REVISION` 且未标 `SOL RECHECK REQUIRED` 时，Rewrite 后不默认返回 Sol；KEY、MAJOR REVISION、重大秘密章或出现新的结构/Canon 风险时，才进入 Sol 二次验收。

任何环节发现 Brief 与 Canon 冲突时先暂停该章，由 Sol 裁决；不得由正文写手暗改设定来绕过问题。
