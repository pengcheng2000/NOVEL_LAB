# MODEL_ROLES — 模型职责分工

> 2026-09-14 起，项目在三个模型/工具链之间协同。职责是"主责"，不是"垄断"——任何 Agent 都可对其他领域提出意见，但最终产出由主责 Agent 审定。当前项目阶段（见 PROJECT_STATUS.md）决定谁的职责最重。

| 模型 / 工具链 | 角色 | 主要职责 |
|---|---|---|
| **GLM-5.3 Flash**（Claude Code） | **Project Manager / Research / Continuity** | 项目状态维护（PROJECT_STATUS / ACTIVE_TASKS / HANDOFF）；Story DNA 研究与机制库维护；人物状态、时间线、伏笔登记；Story Bible 维护；跨章节一致性检查；阶段交接与日志。 |
| **GPT-5.6 Sol / Codex**（VS Code） | **Story Lead / Main Writer / Story Architect** | 原创 IP 设计；人物与故事结构；大纲；小说正文；重要情节创作；逻辑审查；主要创作工作。 |
| **Gemini / Antigravity**（VS Code） | **Screenwriter / Visual Adaptation** | 小说转剧本；分集设计；场景化；视觉叙事；AI 视频前期设计（分镜、视觉风格、生成管线方案）。 |

## 协作边界举例

- 写小说正文/改大纲 → GPT-5.6（Codex）主责；GLM 负责动笔前的一致性检查与动笔后的状态登记。
- 新章节涉及旧伏笔/旧人物状态 → GLM 先出一致性核查结论，GPT-5.6 再动笔。
- 正文完成后要转短剧/AI 视频 → Gemini 主责分集与视觉化；GLM 维护"小说 → 剧本"的对应状态表。
- 研究类任务（拆解参考书、机制库更新）→ GLM 主责。
