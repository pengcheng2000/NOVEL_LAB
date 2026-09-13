# PHASE4_RULES — 原创 IP 孵化阶段设计原则

> Phase 4 · 2026-09-13 起 · 项目从 RESEARCH 切换到 ORIGINAL CREATION DESIGN

## 0. 阶段边界（铁律）

- **只完成**：8 个候选 → 机制设计 → 原创性审查 → 商业/接地气/AI 视频分析 → Top 3。
- **禁止**：写正文、写第一章、生成几十万字大纲、进入正式章节生产、替用户决定唯一冠军。
- 完成后停止，等待用户选择最终方向，不自动进入 Phase 5。

## 1. 证据边界（继承 Phase 3）

15 本参考作品 FULL_SOURCE = 0。MASTER Story DNA 是**创作研究库**，不是经全文验证的绝对规律：
- 用作 CREATIVE HYPOTHESES / STORY PATTERNS / DESIGN TOOLS ✅
- 当作不可违背的事实 ❌
- 跨作品抽象后的机制可用于原创设计；单书低置信度结论（如执行细节）不得当作事实引用。

## 2. 创作方法（反拼盘）

```
作品 → Story DNA → 抽象机制 → 重新组合 → 新人物 → 新世界 → 新因果链 → 新剧情 → 新表达
```

**禁止**：复用原作人物/独特世界观/经典场景/改名换皮/连续剧情链/模仿作者文风/多作品拼接。
**允许学习**：身份反转、信息差、情绪债务、延迟兑现、爱情拉扯、阶层欲望、不可能任务、秘密、双时间线、封闭规则、成长、竞争、资源、悬疑、关系升级、章节钩子、长篇更新机制。

## 3. 基因数量限制

- 每候选 PRIMARY STORY GENES ≤7（推荐 4–7），必须来自 MASTER_MECHANISM_LIBRARY（MM 编号）或标记 ORIGINAL_PROJECT_DISCOVERY（NEW_GENE，可反向入库）。
- 每个基因写明：Gene / Function（在本故事中的功能）/ **Transformation**（进入本故事后发生的原创化变化）。
- SECONDARY TECHNIQUES 可并存，但不得取代核心故事。

## 4. 反拼盘感标准

删掉 Story DNA 来源说明后，故事必须仍然像"一个完整世界自然长出来的故事"。每个候选：
- Original Additions ≥5（新职业/新制度/新关系/新社会背景/新核心秘密/新规则/新视角——非机制库来源）；
- 因果完整性：主角为何行动/反派为何行动/爱情为何发生/冲突为何升级/秘密为何不能立即公布/人物为何不离开/故事为何不能第三章就结束——全部要有因果基础，不能只因为"这个桥段很爽"。

## 5. 人物与欲望标准（接地气的真正定义）

不要求现实主义。要求读者快速理解：这个人想要什么？为什么在乎？失败会失去什么？我为什么继续看？
允许并欢迎：美女/帅哥/爱情/暧昧/性张力/财富/阶层/身份/欲望/嫉妒/竞争/面子/消费/成功/失败。爱情线必须服务至少一种：成长/关系悬念/冲突/身份差/价值观差/秘密/资源冲突/情绪奖励/剧情推进。禁止"漂亮角色数量堆积"。

## 6. 评分模型（统一，总分 100）

| 维度 | 权重 |
|---|---|
| Reader Addiction | 20 |
| Character/Relationship | 15 |
| Originality | 15 |
| Groundedness | 10 |
| Emotional Potential | 10 |
| Long-Form Sustainability | 10 |
| Commercial Potential | 10 |
| AI Video Potential | 10 |

额外记录 Production Difficulty（1–10，10=极难）与 CONFIDENCE，不计入 100 分。

## 7. 原创性审查

- 按 `.claude/skills/originality-reviewer/SKILL.md` 七项清单执行（一一对应人物/独特世界设定/连续剧情节点/标志性场景/改名换皮/组合指向性/可抽象空间）。
- 输出评级 LOW / MEDIUM（CAUTION，给出变形方向）/ HIGH（FAIL，必须重构：改变因果关系/人物关系/核心目标/世界规则/冲突来源/剧情顺序中至少两项）。
- 存放位置：按 Phase 4 指令置于 `04_original_project/01_candidates/CXX/ORIGINALITY_REVIEW.md`（Skill 默认的 05_originality_review/ 目录以索引文件形式指向，兼顾两者）。

## 8. 候选分布要求

8 个候选须有明显差异，覆盖：≥2 纯现实/都市，≥2 都市+高概念，≥1 强悬疑，≥1 爱情/关系驱动，≥1 长篇网文向，≥1 AI 视频特别适配。同一候选可满足多类。

## 9. 研究库不是天花板

允许创造 NEW_GENE（标记 ORIGINAL_PROJECT_DISCOVERY）。若新机制明显更好，以新机制优先——MASTER 库是起点，不是上限。
