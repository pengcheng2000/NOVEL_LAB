# AGENT_PROTOCOL — 多 Agent / 多设备协作协议

> 适用范围：所有在此仓库工作的 AI Agent（Claude Code + GLM / VS Code + Codex / VS Code + Antigravity / Gemini）与所有设备（Mac mini / Windows 工作电脑）。
> **GitHub 仓库是项目的中央真源（single source of truth），不是任何一台本地机器。**

## 开始工作前（必做，顺序不可省）

1. `git pull`（先同步，再动笔）
2. 依序阅读：
   1. `CLAUDE.md` —— 项目总纲与核心原则
   2. `00_system/AGENT_PROTOCOL.md` —— 本文件
   3. `00_system/MODEL_ROLES.md` —— 各模型职责分工
   4. `00_system/PROJECT_STATUS.md` —— 阶段状态总表
   5. `00_system/ACTIVE_TASKS.md` —— 活动任务与待办队列
   6. `00_system/HANDOFF.md` —— 上一位 Agent 的交接记录
3. **不依赖旧聊天上下文**——一切长期状态以 Git 内的文件为准；聊天记录只是会话内的短期记忆。

## 工作中

- 不同 Agent 尽量不要同时编辑同一个文件；各自产出优先写入职责对应的目录（见 MODEL_ROLES.md）。
- 共享状态文件（PROJECT_STATUS.md / ACTIVE_TASKS.md / HANDOFF.md）：只更新/追加自己负责的字段，**不重写他人的记录**。
- 开始一项会持续较长时间的任务前，先在 `HANDOFF.md` 的 IN_PROGRESS 登记，push 一次，再动笔——让其他设备能看见。
- 若发现另一 Agent 正在处理同一任务：**避免覆盖**，改为接续、等待或在 HANDOFF.md 中留言协调。
- 他人已完成的产出不无理由覆盖；确需重做，先书面说明旧结果为何不足。

## 完成重要工作后（必做）

1. 更新 `00_system/PROJECT_STATUS.md`、`00_system/ACTIVE_TASKS.md`、`00_system/HANDOFF.md`（LAST_AGENT / LAST_COMMIT / COMPLETED / NEXT_TASK 等字段）
2. 写工作日志到 `99_logs/<agent>/YYYY-MM-DD_*.md`
3. `git add` → `git commit`（imperative scoped subject，如 `analysis: add C06 stress-test evidence`）→ `git push`
4. **严禁 `git push --force`**（除非用户明确要求）；远程有新提交时用 pull / merge / rebase 正常解决。

## 路径纪律

- 项目文件内禁止写死任何设备的绝对路径；需要指代项目根目录时用 `<PROJECT_ROOT>`，或直接用相对路径（如 `00_system/`、`04_original_project/`）。
- 脚本定位项目根目录一律用 Git repository root（`git rev-parse --show-toplevel`）或相对自身路径推导，不写死。
