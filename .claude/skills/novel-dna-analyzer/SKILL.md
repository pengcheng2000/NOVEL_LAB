---
name: novel-dna-analyzer
description: 对单本参考小说执行系统化 Story DNA 分析。当需要深度分析一本小说（建立章节索引、按维度拆解、输出机制卡与 NOVEL_DNA.yaml）时使用。必须遵循 00_system/ANALYSIS_SCHEMA.md 的统一 Schema。
---

# novel-dna-analyzer — 单本小说系统化分析

## 职责

针对单本小说执行系统化分析，输出统一格式的 Story DNA。

## 前置条件（必须先做）

1. 读取 `00_system/ANALYSIS_SCHEMA.md`（统一 Schema）。
2. 读取 `00_system/COPYRIGHT_RULES.md`（版权规则）。
3. 读取 `00_system/WORKFLOW.md`（读取方式与输出规范）。
4. 确认源文件存在于 `01_reference/<region>/` 且状态非 `MISSING_SOURCE`。
5. 确认目标目录（SINGLE_AGENT_MODE，全部可写）：
   - GLOBAL → `02_analysis/global/`
   - CHINA_PRINT → `02_analysis/china_print/`
   - CHINA_WEB → `02_analysis/china_web/`

## 执行流程（Progressive Compression）

### 第一步：建立章节索引

在分析目录创建 `00_source_index.md`：
- 源文件路径、格式、总章节数、总字数估计
- 章节列表（编号、标题、长度）
- 分批读取计划（Arc 划分）

### 第二步：分批阅读

- 每批 5–15 章（视章节长度），禁止一次性全文塞入上下文粗略总结。
- 每批结束将结构化中间状态写入文件（笔记按 Arc 归档，可存放于分析目录内 `notes/` 子目录）。
- 中间笔记必须包含：剧情节点、人物状态变化、钩子、爽点兑现点、信息差变化、章末悬念类型。

### 第三步：Arc 级综合

按卷/Arc 汇总中间笔记，形成 Arc 结构描述。

### 第四步：小说级分析文件

输出标准文件集（见 WORKFLOW.md）：
`00_source_index.md` 至 `13_originality_boundaries.md` + `NOVEL_DNA.yaml`。

## 分析要求

- 覆盖 Schema A–Q 全部维度，缺失写 `not_applicable`，不改 Schema。
- 每个重要结论回溯到剧情结构（章节号/标题/位置/简短概述）。
- 禁止套话（"人物丰满""剧情紧凑"等）；必须回答：为什么、什么机制、哪个阶段、什么预期、多久兑现、删掉会怎样、能否迁移。
- 机制卡 ≥ 10 张，抽象到可重新原创的程度，并标注 protected_elements（RED 项）。
- 禁止大段复制原文；引用单处 ≤ 1 句并注明出处。

## 完成后

更新 `00_system/PROJECT_STATUS.md` 与 `00_system/ACTIVE_TASKS.md`，并在 `99_logs/claude/` 留下本作分析日志（覆盖范围、批次、发现要点）。
