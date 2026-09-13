# HANDOFF — Agent 交接板

> 每次重要工作结束时更新本文件；每次开始工作前先读本文件（完整协议见 `00_system/AGENT_PROTOCOL.md`）。

LAST_AGENT: Claude Code
LAST_MODEL: GLM-5.3 Flash
LAST_DEVICE: Mac mini
LAST_COMMIT: chore: make NOVEL_LAB portable and multi-agent ready（2026-09-14，首次推送）

COMPLETED:
- GitHub 跨设备迁移完成：全部项目文件首次推送到 github.com/pengcheng2000/NOVEL_LAB（main 分支）
- 建立多 Agent 协作基础设施：00_system/AGENT_PROTOCOL.md + MODEL_ROLES.md + HANDOFF.md
- 消除全项目唯一一处设备绝对路径（00_system/HANDOFF_AUDIT.md → `<PROJECT_ROOT>`）
- .gitignore 重构：99_logs/ 自本次迁移起纳入版本控制；01_reference/ 版权源文本保持排除（本地保留）
- 安全检查：无 API Key/Token/密码/凭证；无 .env；无 >1MB 文件

IN_PROGRESS:
- 无（等待用户在任一设备启动下一阶段任务）

NEXT_TASK:
- Phase 6：Novel Production——按 `04_original_project/C05_rainy_old_clothes/` Story Bible 开始小说生产（等待用户明确启动；主责：GPT-5.6/Codex）
- 历史遗留待办见 00_system/ACTIVE_TASKS.md 队列（ORIGINAL_PROJECT_DISCOVERY 反向入库等）

FILES_CHANGED:
- 新增：00_system/AGENT_PROTOCOL.md、00_system/MODEL_ROLES.md、00_system/HANDOFF.md、.gitattributes、01_reference/README.md
- 修改：.gitignore、CLAUDE.md、AGENTS.md、00_system/HANDOFF_AUDIT.md（路径消除）、00_system/PROJECT_STATUS.md、00_system/ACTIVE_TASKS.md
- 首次入库：00_system/、02_analysis/、03_story_dna/、04_original_project/（含 C05_rainy_old_clothes Story Bible）、05_originality_review/、99_logs/、.claude/skills/ 全部内容

FILES_TO_READ_NEXT:
- 新 Agent 标准启动序列：CLAUDE.md → 00_system/AGENT_PROTOCOL.md → MODEL_ROLES.md → PROJECT_STATUS.md → ACTIVE_TASKS.md → HANDOFF.md
- 当前开发项目：04_original_project/C05_rainy_old_clothes/（00–08 设计文档 + 11_reviews）

IMPORTANT_DECISIONS:
- GitHub = 项目中央真源；所有本地磁盘只是工作副本
- 三模型分工确立：GLM=管理/研究/一致性；GPT-5.6=主创作；Gemini=剧本/视觉（详见 MODEL_ROLES.md）
- 01_reference/ 下的版权源文本（官方试读摘录 .txt 等）永久排除在公开仓库之外，本地保留不删除
- 99_logs/ 自本次迁移起进入版本控制（跨设备可见）

KNOWN_RISKS:
- 仓库为 PUBLIC：已核查无凭证/密钥/完整版权正文；分析文件对参考书仅做机制级抽象描述，后续贡献者须持续遵守 00_system/COPYRIGHT_RULES.md
- 跨设备换行差异：.gitattributes 已统一（仓库内 LF）
- 多 Agent 并发编辑冲突：依赖 AGENT_PROTOCOL 的 pull-first 与 IN_PROGRESS 登记纪律
