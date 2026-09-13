# SCHEMA_PILOT_REVIEW — Schema 健康检查（基于 IEWU 第 1 章试跑）

日期：2026-09-13
依据：`02_analysis/global/it-ends-with-us/PILOT_ANALYSIS.md`（试跑实测）
性质：**仅建议，不重写 ANALYSIS_SCHEMA.md**。任何采纳都应走版本化修订（v1.1），并保留 v1.0 存档。

---

## 字段分层建议

### CORE（以后每本必须分析）

| 来源分节/字段 | 理由 |
|---|---|
| B `premise` / `core_fantasy` / `reader_promise` | 定位北极星；开篇即可锁定 |
| C `starting_status` / `contradiction` / `relatability` / `wish_fulfillment` / `desire` / `fear` | 人物引擎三轴，开篇高可靠 |
| D `first_page_hook` / `first_chapter_hook` / `first_irreversible_event` / `next_chapter_reason` | 开篇生死线；PARTIAL 阶段主产出 |
| J（信息控制，开篇范围） | 单章强项，试跑验证 |
| L（单章/单 Arc 情绪曲线） | 可靠且高价值 |
| M（文风主字段：pov / tense / narrative_distance / humor_mechanism / internal_monologue） | 开篇即可下结论 |
| N（循环识别，标注"候选"） | 成瘾循环是研究核心目标 |
| O（机制卡，数量按覆盖量弹性） | 唯一"输入即资产"的维度 |
| Q（GREEN/YELLOW/RED，按已读范围分档） | 版权边界不可后置 |
| H（锚点清单 + 评分；评分可降级为软指标） | 开篇观测窗口最佳 |

### SECONDARY（有价值，不过度深入）

A（基础信息）；C 其余（`information_advantage` / `social_status`）；D `lock_in_point`；E `inciting_incident` / `core_conflict`；G（关系引擎，按重要关系取舍）；K `scene_length` / `chapter_ending_hooks`；M 其余子字段；F 的 reward 类型识别（不逐项枚举 not_applicable）。

### OPTIONAL（特定类型才需要）

I（世界观——SFF/无限流必做，现实题材 not_applicable 是常态而非异常）；`sexual_tension` / `face_slapping` 等类型特定 reward 项；G 的 `mentor` / `rivalry` 等低频关系类型。

### FULL_TEXT_ONLY（没有完整小说时禁止分析）

`character_arc`；E 的 `escalation_method` / `obstacle_generation` / `arc_loop` / `conflict_refresh_method` / `midpoint_function` / `climax_pattern`；F 的全部量化字段（`reward_frequency` / `buildup_length` / `payoff_strength` / `delayed_payoff` / `reward_escalation`）；K 的 `climax_interval` / `volume_structure`；N 的主/次循环终判；O 的 ≥10 张规模要求；P 全部；Q 的完整 RED 清单；B 的 `central_question` 终版。

> 禁止方式：这些字段在 PARTIAL 材料下**不得填 not_applicable（那是谎称确认了不存在），应填 `deferred_full_source`**——区分"确认不适用"与"尚未可分析"两种空值，是防止 PARTIAL 伪装 FULL 的关键。

## 结构性建议（流程层）

1. **证据门控（最高优先级）**：为每个分析文件建立强制头部 `SOURCE_SCOPE / COVERAGE / LIMITATION`（即本次试跑的标记格式），Schema 化而非依赖自觉。
2. **空值二分**：`not_applicable`（确认不适用）vs `deferred_full_source`（待全文）。当前 Schema 只有前者，会诱导把"没读到"伪装成"确认没有"。
3. **文件结构弹性**：16 文件标准输出仅适用于 FULL_SOURCE；PARTIAL 阶段允许合并文件（试跑用单文件承载 8 维度，质量更高）。
4. **机制卡数量弹性**：≥10 张改为按覆盖量（建议：每 ~10 章覆盖量 2–4 张，全书 10–20 张）。硬数量必被稀释。
5. **复述税削减**：D/K、F/N、L/N、C/G 四组重叠分节在写作指令中明确"只写一次，交叉引用"。
6. **新增 3 个流程字段**：`source_scope`（文件级）、`evidence_scope`（机制卡级）、`confidence: textual|inferred|external`（结论级）。
7. **评分降级**：H 的 groundedness_score 与 P 的全部 1–10 评分降为软指标（可写可不写）；P 节整体移入"创作阶段工具"定位，研究阶段仅保留 `iconic_scenes` / `visual_hook` / `recurring_character_potential`。

## 核心检查："为了填表而分析"的风险判定

**存在，且已被试跑证实。** 风险链条：完整性强制（覆盖 A–Q）→ 证据不足 → not_applicable/套话填充 → 分析文件看起来完成而机制洞察为零。

试跑中亲自遇到的三个实例：
- F 节 11 个 reward 子项，第 1 章材料下 9 项只能占位——占位本身零信息；
- 机制卡数量压力（见上）；
- 16 文件拆分迫使同一证据多处复述。

**但同样要记录反面**：Schema 的"结论必须回溯剧情结构"与反套话条款在试跑中**确实起效**——本次产出中没有任何一个结论无法指出证据位置。问题不在分析标准，在**完整性标准与分析标准的混淆**：让"填满表格"当上了"发现机制"的裁判。

修正方向一句话：**Schema 从"完整性清单"转型为"证据分级许可"——分析者被允许写多少，由证据等级决定，而不是由表格格数决定。**
