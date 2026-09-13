# ANALYSIS_SCHEMA — 统一分析 Schema（v1.0）

所有 Agent（Kimi / DeepSeek）分析任何小说时必须使用完全相同的 Schema。
本 Schema 同时是 Markdown 分析文件的结构规范，以及 `NOVEL_DNA.yaml` 的字段规范。

## 使用规则

- **不存在的机制写 `not_applicable`**，不得删除字段、不得改 Schema。
- 每个重要结论必须回溯到剧情结构（章节号 / 章节标题 / 剧情位置 / 简短概述）。
- 禁止无分析价值的套话（"人物丰满""剧情紧凑""引人入胜""情感细腻"）。
- 分析文件禁止大段复制原文；确有必要时仅引用极短片段（单处 ≤ 1 句）。
- 机制卡必须抽象到未来可重新原创的程度。

---

## A. 基础信息 (Basic Info)

| 字段 | 说明 |
|---|---|
| `title` | 书名 |
| `author` | 作者 |
| `original_language` | 原始语言 |
| `genre` | 类型 |
| `publication_period` | 出版时期 |
| `target_readers` | 目标读者 |
| `popularity_context` | 爆红背景（榜单、销量、社交媒体传播路径） |
| `adaptation_status` | 影视/其他改编状态（如已知） |

## B. 一句话核心 (One-Line Core)

| 字段 | 说明 |
|---|---|
| `premise` | 前提设定（一两句话讲清故事） |
| `core_fantasy` | 核心幻想（读者借这个故事满足什么愿望） |
| `central_question` | 中心问题（驱动全书的问题） |
| `reader_promise` | 读者承诺（翻开书时被默认许诺的东西） |

## C. 主角系统 (Protagonist System)

`starting_status`（开局状态，越具体越好：收入/职位/人际关系/心理状态）
`external_goal`（外在目标）
`internal_need`（内在需求，主角自己未必知道）
`desire` / `fear` / `weakness` / `contradiction`（核心矛盾：人物内在不可调和的两面）
`special_advantage`（特殊优势：能力/资源/体质等）
`information_advantage`（信息优势：主角知道而别人不知道的）
`social_status`（社会地位及其变动轨迹）
`character_arc`（成长弧线，分阶段描述）
`relatability`（代入感来源：为什么目标读者会在主角身上看到自己）
`wish_fulfillment`（愿望满足：读者通过主角 vicariously 得到什么）

## D. 开篇 Hook (Opening Hook)

- `first_page_hook`：第一页发生了什么、制造了什么问题
- `first_chapter_hook`
- `first_3_chapters`：前三章各自的功能
- `first_10_chapters`：前十章建立了什么（世界观/人物/承诺兑现）
- `first_irreversible_event`：第一个重大不可逆事件出现在哪、是什么
- `lock_in_point`：读者何时真正被锁住（无法弃书的时刻）
- `next_chapter_reason`：开篇阶段读者为什么愿意点下一章

## E. 情节发动机 (Plot Engine)

`inciting_incident` / `core_conflict` / `escalation_method`（升级方式）
`obstacle_generation`（障碍如何持续产生：是世界内在的、反派驱动的、还是主角性格导致的）
`revelation_pattern`（揭示模式）/ `reversal_pattern`（反转模式）
`arc_loop`（单元循环：一个典型剧情单元的形状）
`conflict_refresh_method`（冲突如何刷新、防止疲劳）
`midpoint_function`（中点发生了什么、功能是什么）
`climax_pattern`（高潮的形状与位置）

## F. 爽点 / Reward Engine

逐项分析（不存在写 `not_applicable`）：
`power_reward` / `status_reward` / `money_reward` / `romance_reward` / `sexual_tension`
`social_recognition` / `face_slapping`（打脸）/ `revenge` / `mystery_payoff`
`competence_fantasy`（能力幻想）/ `emotional_payoff`

量化维度：
- `reward_frequency`：多久一次
- `buildup_length`：铺垫多长
- `payoff_strength`：兑现强度
- `delayed_payoff`：延迟兑现机制（哪些爽点故意压着不放）
- `reward_escalation`：兑现如何升级

## G. 人际关系 (Relationship Engine)

覆盖：`romance` / `friendship` / `rivalry` / `mentor` / `family` / `enemy` / `workplace_class_relations`

对每条重要关系分析：`attraction`（为何互相吸引）、`dependency`、`conflict`、`status_gap`、`secrecy`、`jealousy`、`betrayal`、`reconciliation`。

**核心问题不是"有几个美女帅哥"，而是：**
- 为什么人物有吸引力？
- 为什么读者想看这两个人继续互动？
- 这段关系怎样制造剧情（而不只是装饰）？

## H. 接地气程度 (Groundedness)

逐项分析：`ordinary_life_entry_point` / `money` / `job` / `school` / `family` / `housing` / `class` / `consumption` / `dating` / `social_status` / `embarrassment` / `peer_comparison` / `ambition` / `everyday_humor`

输出 `groundedness_score`（1–10），**必须解释评分依据**（哪些具体日常锚点存在/缺失）。

## I. 世界观 (Worldbuilding)

`world_rules` / `hierarchy` / `scarcity` / `power_structure` / `institution` / `social_order` / `constraints`

核心判断：**世界观是否服务剧情**（每个设定是否制造了冲突/欲望/障碍），而不是单纯复杂。逐条检验：如果删掉这个设定，故事会不会塌？

## J. 悬疑与信息差 (Suspense & Information Gap)

`audience_knows_character_doesnt` / `character_knows_audience_doesnt`
`hidden_identity` / `secret` / `false_answer`（假答案）/ `red_herring`（误导线索）
`delayed_revelation` / `twist` / `mystery_ladder`（悬念阶梯：小谜→中谜→大谜的结构）

## K. 节奏 (Pacing)

`scene_length` / `chapter_length` / `action_dialogue_exposition_balance`
`tension_curve` / `low_intensity_scenes`（低强度场景的功能）
`climax_interval`（高潮间隔）/ `arc_length` / `volume_structure` / `chapter_ending_hooks`（章末钩子类型统计）

## L. 情绪曲线 (Emotional Curve)

识别作品中出现的：`desire` / `anticipation` / `humiliation` / `frustration` / `hope` / `attraction` / `fear` / `triumph` / `grief` / `catharsis`

**重点：作者如何制造情绪债务，然后如何兑现。**（先让读者欠下什么情绪，再在什么节点偿还）

## M. 文风与叙述 (Style & Narration)

只做抽象分析，不模仿具体作者。
`pov` / `tense` / `narrative_distance` / `sentence_rhythm` / `dialogue_density` / `humor_mechanism` / `description_density` / `exposition_method` / `internal_monologue` / `scene_vs_summary`

## N. Reader Addiction Loop（最重要）

必须回答：**"为什么读者看完这一章还想点下一章？"**

逐项分析：
- `curiosity_loop`（好奇循环）
- `reward_loop`（奖励循环）
- `relationship_loop`（关系循环：想看两人关系下一步）
- `progression_loop`（成长/进度循环）
- `mystery_loop`（谜题循环）
- `status_loop`（地位变化循环）
- `emotional_loop`（情绪循环）

并明确指出该书**主要的 addiction loop 是哪一个、次要的是哪几个**。

## O. Story Mechanism Cards（每本 ≥ 10 张）

```yaml
- mechanism_name:
  problem_solved:      # 这个机制解决什么叙事问题
  trigger:             # 何时触发
  setup:               # 如何铺垫
  escalation:          # 如何升级
  payoff:              # 如何兑现
  why_it_works:        # 底层心理/结构原因
  genres_applicable:   # 可迁移到哪些题材
  risk_of_cliche:      # 变俗的风险
  how_to_transform:    # 如何变形以保持新鲜
  protected_elements:  # 该作品中不可复用的具体表达（RED 项）
```

机制卡必须抽象到未来可以重新原创。

## P. AI 视频适配价值 (AI Video Adaptation)

`visual_hook` / `strong_locations` / `iconic_scenes` / `cast_complexity` / `vfx_difficulty` / `dialogue_dependence` / `episode_segmentation` / `short_video_hook_potential` / `recurring_character_potential` / `production_difficulty`

各维度 1–10 评分 + 总分，解释依据。

## Q. 原创借鉴安全层级 (Originality Safety Tiers)

- **GREEN**：高度抽象、可直接学习的机制。
- **YELLOW**：组合方式具有识别度，使用时需进一步变形。
- **RED**：高度独创的人物、设定、剧情组合、台词或标志性表达，**不应直接复用**。

对本书所有重要元素分档，并列出 RED 清单。

---

## NOVEL_DNA.yaml 规范

每本小说的分析目录下必须输出 `NOVEL_DNA.yaml`：
- 顶层键使用本 Schema 的 A–Q 分节命名（`basic_info` / `one_line_core` / `protagonist_system` / `opening_hook` / `plot_engine` / `reward_engine` / `relationship_engine` / `groundedness` / `worldbuilding` / `suspense_information` / `pacing` / `emotional_curve` / `style_narration` / `reader_addiction_loop` / `mechanism_cards` / `video_adaptation` / `originality_tiers`）。
- 缺失机制一律 `not_applicable`。
- 附 `source_meta`（源文件路径、版本、章节覆盖范围、分析日期）。
