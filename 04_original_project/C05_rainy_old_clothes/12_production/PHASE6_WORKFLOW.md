# Phase 6 Novel Production Workflow

> 状态：Phase 6A 定稿；自 Batch 02 起采用 Production Workflow V2。适用于《雨天旧衣店》每一章/批次从规划到 Canon 回写的完整生产链。

## 1. 生产原则

1. **先决定章节功能，再生产文字。** 每章必须有独立 Goal、Conflict、Change、Reward 与 Ending Hook；“气氛好”不能替代功能。
2. **正文统一由 Gemini 3.8 Flash 执行。** Sol 控制结构与上限，不通过整章代写夺走 Main Writer 的文风连续性。
3. **记忆段不是结案。** 读衣通常处于单元中点，真正结案来自现实核验、关系选择和不可逆后果。
4. **Canon 优先。** Brief 或草稿与硬规则、时间线、秘密释放层级冲突时，暂停生产，由 Sol 裁决；不得在正文中暗改。
5. **一批一关。** 未完成获批 Rewrite 的独立 Continuity Verification 与 Canon Update，不进入下一生产批次。

### Production Workflow V2（自 Batch 02 起）

- Sol 与 Gemini Writer 默认使用 MEDIUM 推理强度。
- Writer 与 Continuity / Canon 必须是两个独立 Gemini 会话，不共享未落盘判断。
- 普通 Batch 经 Sol `ACCEPT WITH REVISION` 且未标 `SOL RECHECK REQUIRED` 后：Gemini Writer Rewrite → 独立 Gemini Continuity 完成 Rewrite Verification + Canon Update；不默认返回 Sol 做第二次 Final Verification。
- KEY、`MAJOR REVISION`、重大秘密章，或 Rewrite 新增重大 Canon / 越过秘密边界 / 出现结构失败时，必须返回 Sol 二次验收。
- Continuity / Canon 会话只检查和维护 Canon，不做文学重写，不替 Writer 偷改正文。

## 2. Canon 优先级

发生冲突时按以下顺序处理：

1. `00_story_bible/CORE_IDENTITY.md`。
2. `03_world/OLD_CLOTHES_RULES.md`、`05_timeline/MASTER_TIMELINE.md`、`06_secrets/SECRET_MATRIX.md`。
3. 人物、关系、Story Engine 与伏笔文件。
4. `08_outline/` 中最新定稿结构。
5. 本目录中的已批准 Chapter Brief。
6. 草稿中的临场创造。

低优先级内容若产生更好方案，只能以 `WRITER_NOTE` 或 Editorial Review 建议上报；在 Sol 明确批准并回写 Canon 前，不得视为生效。

## 3. 文件位置与命名

| 产物 | 位置 | 文件名 |
|---|---|---|
| Chapter Brief | `12_production/chapter_briefs/` | `chapter_XXX_brief.md` |
| Gemini 初稿 | `09_manuscript/drafts/` | `chapter_XXX_draft.md` |
| Continuity 报告 | `12_production/editorial/` | `chapter_XXX_continuity.md` 或 Batch 对应文件名 |
| Sol 编辑审查 | `12_production/editorial/` | `chapter_XXX_editorial_review.md` |
| Gemini 重写定稿 | `09_manuscript/final/` | `chapter_XXX_final.md` |
| 生产日志 | `12_production/production_logs/` | `chapter_XXX_log.md` |

`XXX` 固定为三位数字。Draft 与 Final 文件只放正文及必要元数据；分析、审稿意见和状态变更不得混进正文。

## 4. 标准生产链

### STEP 1 — Sol / Chapter Planning

Sol 必须读取：

- Story Bible 与当前卷纲。
- `FIRST_20_CHAPTERS.md` 或当前阶段结构表。
- 最新人物状态、关系状态、时间线、伏笔与秘密登记。
- 最近 2–5 章正文；Chapter 001 无此前正文。
- 上一章 Continuity / Editorial / Production Log。

输出 `chapter_XXX_brief.md`。Brief 必须锁定章节目的、场景变化、信息权限、伏笔、Ending Hook 和 Gemini 的自由边界，使 Writer 无需重新设计剧情即可落笔。

### STEP 2 — Gemini / Draft

Gemini 必须读取：

- 当前 Chapter Brief。
- `PROSE_STYLE_GUIDE.md` 与 `GEMINI_WRITER_INSTRUCTIONS.md`。
- Brief 指定的必要 Story Bible 文件。
- 最近 2–5 章已批准正文。

输出 `chapter_XXX_draft.md`。

Gemini 可以自由处理场景细节、动作、对白、生活质感、局部幽默和情绪表现；不得擅改核心剧情、人物重大动机、世界规则、秘密层级、时间线、重大伏笔及章末目标。认为 Brief 有严重问题时照可执行部分完成，并在正文后附 `WRITER_NOTE`，不得偷偷另写一套剧情。

### STEP 3 — Independent Continuity Session / Continuity Pass

独立 Continuity 会话对照 Brief、Canon 与最近章节，只检查：

- 时间、日期、天气、地点、年龄。
- 人物在场条件与知识状态。
- 人物关系和承诺状态。
- 衣物、账本、票据、道具位置与所有权。
- 世界规则、旧衣规则、代价与触发条件。
- 伏笔、秘密释放层级与既有 Canon 冲突。

输出 `chapter_XXX_continuity.md` 或 Batch 对应报告，按 `BLOCKER / ERROR / QUERY / PASS` 标注。该会话不做文学评价或文学重写。Batch 02 的初稿 Continuity 已按旧安排由 GLM 完成；从本批 Rewrite Verification 起及后续 Batch，依 Workflow V2 由第二个 Gemini 会话承担。

### STEP 4 — Sol / Editorial Review

Sol 读取 Brief、Draft 与 Continuity Review，输出 `chapter_XXX_editorial_review.md`：

- **MUST FIX**：Canon 冲突、章节功能失败、人物行为不成立、信息泄露、无 Ending Hook、明显 AI 套话等，不修不能批准。
- **SHOULD FIX**：节奏、情绪、对话、视角距离、重复、Reward 强度等显著影响质量的问题。
- **OPTIONAL**：不改变结构的局部提升建议。

审查重点：故事功能、人物主动性、关系权力变化、节奏、情绪、对白、信息释放、伏笔、Hook、重复和文风。Sol 优先说明问题、原因、位置与修改方向；必要示范通常控制在 300–800 字，不默认重写整章。

### STEP 5 — Gemini / Rewrite

Gemini 根据 Editorial Review 与 Continuity Pass 重写，输出 `chapter_XXX_final.md`。所有 `MUST FIX` 必须逐项落实；若某项无法落实，在文末列出未解决项，不得静默忽略。

正文最终文字继续由 Gemini Writer 统一生成。KEY、`MAJOR REVISION`、重大秘密章或 Sol 明标 `SOL RECHECK REQUIRED` 时，Rewrite 必须返回 Sol；普通 Batch 则直接进入独立 Continuity Verification。

### STEP 6 — Independent Continuity Session / Rewrite Verification + Canon Update

确认 Rewrite 已逐项落实 `MUST FIX` 且无新冲突后，独立 Continuity / Canon 会话：

- 更新人物状态、关系状态、时间线、道具/衣物去向。
- 更新伏笔 Setup / Reminder / Payoff 状态与秘密披露状态。
- 记录本章实际发生而 Brief 未预见、且已获 Sol 批准的新 Canon。
- 更新 `PROJECT_STATUS.md`、`ACTIVE_TASKS.md`、`HANDOFF.md` 与章节生产日志。

Canon Update 完成并提交后，下一生产批次方可进入 STEP 1。Batch 01 及更早由 GLM 承担；从 Batch 02 起依 Workflow V2 由第二个 Gemini 会话承担。

## 5. 章节状态

`PLANNED → DRAFTED → CONTINUITY_CHECKED → EDITED → REWRITTEN → APPROVED → CANON_UPDATED`

只有 `CANON_UPDATED` 视为章节完成。文件存在不等于通过；任何退回都保持在当前章，不能用下一章弥补当前章缺陷。

## 6. 三项生产监控

1. **单元语法重复率**：滚动检查最近四个单元，至少覆盖三种语法；连续两个单元不得用同一种情绪结案，更不得都以哭泣、拥抱或道歉收束。
2. **主谜场景占比**：按场景与有效篇幅双重估算，全书滚动窗口原则上不超过 45%。每四章至少有一场无魔法的经营或关系日常，避免事故调查吞掉生活质感。
3. **谢念主动行动占比**：每章至少一次由谢念主动提出、拒绝、调查、交易或承担后果的有效动作；滚动五章内至少三次由她的决定改变局面。被动看到记忆不计主动行动。

## 7. 停线条件

出现以下任一项，当前章停止向后生产：

- Brief 与硬 Canon 冲突。
- 需要新增能力规则才能完成情节。
- 必须让人物知道其尚不该知道的信息才能推进。
- 单元拿掉后，对人物、关系或主线没有影响。
- 章末只能靠隐瞒视点人物明确知道的信息制造悬念。
- 草稿违反 `CHAPTER_ACCEPTANCE_STANDARD.md` 的强制退回条件。
