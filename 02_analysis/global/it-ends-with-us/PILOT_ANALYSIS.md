# PILOT_ANALYSIS — 流水线试跑评估报告

> 评估对象：`00_system/ANALYSIS_SCHEMA.md`（A–Q v1.0）+ `novel-dna-analyzer` Skill + `WORKFLOW.md` 标准输出流程
> 试跑材料：It Ends with Us 官方试读（第 1 章，约 9,000 词）
> 试跑产出：`00_source_index.md` / `01_opening_analysis.md`（8 维度 + 12 专项问题）/ `11_opening_mechanism_cards.md`（4 张）
> 日期：2026-09-13
> 本文件评估的是**分析系统**，不是这本小说。

---

## 1. 当前 ANALYSIS_SCHEMA 是否过重？

**过重，且过重的方向明确：它是一本"全书分析 Schema"被直接用作"任何阶段分析 Schema"。**

实测第 1 章（约 9,000 词，信息密度已属上乘）能可靠填充的字段约占 A–Q 全部字段的 **35–40%**。E/F/I/L/P 的主体字段（escalation_method / midpoint_function / climax_pattern / reward_frequency / emotional_curve 全曲线 / production_difficulty）在只有开篇材料时**原则上不可分析**——不是"难分析"，是任何声称分析的输出都必然是编造。

结论：Schema 字段设计本身质量高（字段粒度、反套话条款、机制卡结构都经过深思），问题在于它没有**分阶段许可层**——缺一个"当前证据等级允许碰哪些字段"的守门机制。

## 2. 第一章能够可靠填多少字段？

| Schema 分节 | 可靠填充度 | 说明 |
|---|---|---|
| A 基础信息 | ~90% | popularity_context / adaptation_status 需外部资料（登记为 EXTERNAL_CONTEXT 即可） |
| B 一句话核心 | ~75% | premise / reader_promise 可靠；core_fantasy 勉强；central_question 只能写假设版 |
| C 主角系统 | ~60% | starting_status / desire / fear / weakness / contradiction / relatability / wish_fulfillment 高质量可填；character_arc / social_status 变动轨迹不可填 |
| D 开篇 Hook | ~70% | first_page_hook / first_chapter_hook / first_irreversible_event / lock_in_point(部分) / next_chapter_reason 可填；first_3_chapters / first_10_chapters 需更多章节 |
| E Plot Engine | ~15% | inciting_incident 算命中；其余全部不可靠 |
| F Reward Engine | ~10% | 仅能识别本章已出现的 reward 类型，量化维度（频率/升级）全部失效 |
| G 关系引擎 | ~40% | 单一关系可深度分析（首遇机制），但 relationship 的全书走向不可判断 |
| H Groundedness | ~85% | 意外发现：**开篇是 groundedness 的最佳观测窗口**（金钱/职业/阶层/居住标记在开篇密度最高），评分可给但有标注义务 |
| I 世界观 | ~10% | 现实题材开篇世界观即日常世界，基本 not_applicable |
| J 悬疑信息差 | ~60% | 开篇信息控制（见 01_opening_analysis.md G 节）是单章强项 |
| K 节奏 | ~35% | scene_length / chapter_ending_hooks 可统计样本=1；tension_curve 全书版不可 |
| L 情绪曲线 | ~50% | 单章曲线完整可得；全书曲线不可 |
| M 文风 | ~90% | 文风是开篇即可下结论的维度（本次试跑产出最完整的维度） |
| N Addiction Loop | ~25% | 可识别候选循环，**主/次循环的判定需要全书** |
| O 机制卡 | 开篇 4 张（诚实上限） | "≥10 张"在第 1 章材料下不可达——见第 10 节 |
| P 视频适配 | ~5% | 不可分析 |
| Q 原创性分层 | ~30% | 开篇元素的 GREEN/RED 可分档；全书 RED 清单不可 |

## 3. 哪些字段只有全文才能分析？

character_arc；E 全部结构字段（obstacle_generation / arc_loop / midpoint / climax）；F 全部量化字段（reward_frequency / buildup_length / payoff_strength / delayed_payoff / reward_escalation）；I 的完整判定；K 的 climax_interval / volume_structure；L 全书曲线；N 的主循环判定；O 的 10 张规模；P 全部；Q 的完整 RED 清单；B 的 central_question 终版。

## 4. 哪些字段存在明显重复？

1. **D × K**：first_3_chapters / first_10_chapters 本质是 pacing 字段，放在 Hook 分节造成两个分节都要谈章节推进。
2. **E × K**：conflict_refresh_method 与 tension_curve / climax_interval 描述同一现象的两个侧面。
3. **F × N**：reward_loop 是 reward_engine 的循环化重述，分析时会写出同一段证据两次。
4. **L × N**：emotional_loop 与 emotional_curve 高度重叠；"情绪债务如何欠下/偿还"在两节都成立。
5. **C × G**：relatability / wish_fulfillment 与 relationship 的 attraction 分析在浪漫题材中必然互相渗透。

重复不致命（多视角有益），但**同一证据被要求在多个文件复述**才是流程层浪费的来源——见第 10 节。

## 5. 哪些指标主观性过强？

- `groundedness_score`（1–10）：本次实测发现评分依赖"哪些锚点算数"的口径，不先定义锚点清单就直接打分必然漂移。建议：锚点清单是硬的，分数是软的（分数可删）。
- P 节全部 1–10 评分（vfx_difficulty / production_difficulty 等）：对不制作视频的分析者是想象题。
- F 节 buildup_length / payoff_strength：没有量化定义（多少章算长铺垫？多强算强兑现？），不同分析者不可比。建议改为相对刻度（本书内对比）而非绝对刻度。

## 6. 哪些字段对未来原创小说最有价值？

排序（基于本次试跑的体感）：
1. **O 机制卡**——本次试跑直接产出了 4 张可迁移的机制卡，是全流程唯一"输入即产出"的资产。
2. **N Addiction Loop**——回答"读者为什么翻页"，是原创设计的北极星。
3. **B core_fantasy / reader_promise**——试跑证明这两个字段在第 1 章就能锁定，而它们决定原创书的定位。
4. **D 开篇字段**——开篇决定生死，且是 PARTIAL_SOURCE 阶段唯一稳定可得的深度维度。
5. **C contradiction / relatability / wish_fulfillment**——人物引擎的三根轴。

## 7. 哪些字段对 AI 视频最有价值？

P 节中真正有用的只有：`iconic_scenes`（名场面清单，本质是 O 的子集）、`visual_hook`、`recurring_character_potential`（角色复用性=IP 化潜力）。其余（vfx_difficulty / cast_complexity / production_difficulty）在研究阶段是伪需求——应降级为创作阶段工具。

## 8. 哪些字段应该优先级降低？

`adaptation_status`（一行外部信息，不是分析）；P 节的制片难度三件套；F 节的逐项枚举（11 个 reward 类型逐项写 not_applicable 是流程税）；M 节部分子字段（description_density / scene_vs_summary 在短章样本下不可靠）。

## 9. 是否需要增加新字段？

**建议增加 3 个（均为流程性字段，不动分析框架）：**
1. `source_scope`（每个分析文件的强制头部声明：FULL / PARTIAL+覆盖范围 / METADATA）——本次试跑靠自觉执行，应 Schema 化。用户任务书的 PARTIAL 标记条款应固化进 Schema。
2. 机制卡 `evidence_scope` 字段——本次卡片格式中已实测（每张卡标注证据范围），Schema O 节当前没有此字段，建议加入。
3. `confidence`（结论置信：textual / inferred / external）——把本次 TEXTUAL_EVIDENCE vs EXTERNAL_CONTEXT 的分离制度化。

**建议不增加**分析维度字段——A–Q 的覆盖面已足够，再加会加重第 1 节的过重问题。

## 10. 当前 novel-dna-analyzer 是否容易产生套话？

**Skill 的反套话条款（禁止"人物丰满/剧情紧凑"）是有效的——但它是消极防御。真正的套话风险来自三个结构性压力：**

1. **"覆盖 A–Q 全部维度"的完整性强制**：当证据不足时，分析者面临"写 not_applicable"与"硬写一段"的选择，后者在表格压力下是默认诱惑。**建议改为证据门控：没有证据的字段直接不设节，而非 not_applicable 占位。**
2. **16 文件标准输出 × 5 个分节重叠**：同一证据（如 confession 游戏）按现在的文件划分要写进 03（人物）/04（关系）/05（钩子节奏）/10（成瘾循环）四处。复述是套话的温床。**建议允许 PARTIAL 阶段合并文件**（本次试跑实际用一个 01_opening_analysis.md 承载 8 个维度，效果优于拆分）。
3. **"机制卡 ≥10 张"的硬数量**：本次诚实产出是 4 张。第 5–10 张只能靠稀释（把一个机制拆成三个名字）。**建议改为"每 10 章覆盖量产出 2–4 张"或按材料量弹性**——数量指标永远会被古德哈特定律攻击。

## 11. 流水线可行性总评

- **单章→开篇分析**：流程完全可行，本次试跑即完整走过一遍（源索引 → 全文阅读 → 8 维度分析 → 机制卡）。产出质量达到研究标准。
- **PARTIAL_SOURCE 的正确策略**（试跑验证）：不补全书、不预测剧情、把开篇可测维度做深。四个维度（D/J/L单章/M）+ H 意外高价值，足以支撑有意义的 PARTIAL 产出。
- **批量运行判定：尚未就绪。** 两个前置条件：(a) Schema 需要按 `SCHEMA_PILOT_REVIEW.md` 的建议增加证据门控层（本次以纪律代替，规模化后纪律必然衰减）；(b) 至少需要一本 FULL_SOURCE 验证全书流程（分批阅读 → Arc 综合 → NOVEL_DNA.yaml）——该路径至今零次实测。
