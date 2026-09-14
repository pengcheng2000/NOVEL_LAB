# NOVEL_LAB — 故事机制研究实验室

长期 AI 小说研究与原创 IP 项目。目标：把市场验证过的热门小说拆解为可复用的 Story DNA / 故事机制，为原创小说与 AI 视频 IP 建立研究基础。

## 当前阶段

第一部原创 IP 已确认：C05《雨天旧衣店》。**Phase 6A 小说生产前置阶段已完成；Chapter 001 正文尚未开始。**正式项目目录为 `04_original_project/C05_rainy_old_clothes/`。

## 目录结构

```
00_system/           系统文件（Schema、规则、状态）—— 全部 Agent 共享读取
01_reference/        参考小说源文件（受版权保护，git 忽略）
  ├── global/        全球大众小说
  ├── china_print/   中国传统出版小说
  └── china_web/     中国网文
02_analysis/         单本深度分析
03_story_dna/        跨作品综合 + 机制库
04_original_project/ 未来原创项目
05_originality_review/ 原创性审查
99_logs/             工作日志
```

## 协作规则（2026-09-14 起：GitHub 多 Agent / 多设备协作）

> **GitHub 仓库 `https://github.com/pengcheng2000/NOVEL_LAB.git` 是项目中央真源。**
> 协作方式见 `00_system/AGENT_PROTOCOL.md`（开始前 git pull + 必读文件序列；完成后更新状态并 push；严禁 force push），
> 模型分工见 `00_system/MODEL_ROLES.md`（GPT-5.6 Sol/Codex=总编辑/故事架构/终审；Gemini 3.8 Flash=小说正文主写；GLM-5.3 Flash=管理/连续性/知识维护；GPT-5.6 Terra=助理编辑/工具任务）。
> 规则：不无理由覆盖其他 Agent 已完成的输出；如需重新分析，先书面说明旧结果不足的原因。
> （2026-09-13 的 SINGLE_AGENT_MODE 已随跨设备迁移存档，见 `00_system/HANDOFF_AUDIT.md` §10。）

<details>
<summary>历史存档：原双 Agent 分区规则（2026-09-13 之前，仅作记录，不再约束当前工作）</summary>

本 Agent（Kimi）可写：
- `00_system/`（初始化及 Schema 统一维护）
- `02_analysis/global/`、`02_analysis/china_print/`
- `03_story_dna/global/`、`03_story_dna/china_print/`、`03_story_dna/master/`
- `99_logs/kimi/`

DeepSeek 专属（未经明确要求不修改）：
- `02_analysis/china_web/`
- `03_story_dna/china_web/`
- `99_logs/deepseek/`
</details>

## 核心原则

1. **提取抽象机制，不复制具体表达。** 人物姓名、独特世界观名词、经典台词、高度独创设定、标志性剧情链不得进入未来原创作品。
2. **分析文件禁止大段复制原文。** 证据用章节号/标题/剧情位置/简短概述，引用仅限极短片段。
3. **不下载盗版源文件。** 缺失源文件标记 `MISSING_SOURCE`，不伪装已读全文。
4. **Progressive Compression：** 章节分析 → 卷级分析 → 小说级 DNA → 机制卡 → 跨小说综合。不依赖聊天上下文，一切耐久信息写入文件。
5. **结论必须可回溯到剧情结构。** 禁止"人物丰满/剧情紧凑"类套话；必须回答为什么、通过什么机制、在哪个阶段、制造什么预期、多久兑现、能否迁移。

## 关键系统文件

- `00_system/ANALYSIS_SCHEMA.md` — 统一分析 Schema（A–Q 全维度），所有 Agent 必须使用同一 Schema
- `00_system/COPYRIGHT_RULES.md` — 版权与原创性边界规则
- `00_system/WORKFLOW.md` — 工作流程与读取方式
- `00_system/AGENT_PROTOCOL.md` — 多 Agent / 多设备协作协议（新 Agent 必读）
- `00_system/MODEL_ROLES.md` — 各模型职责分工
- `00_system/HANDOFF.md` — Agent 交接板（每次重要工作结束时更新）
- `00_system/PROJECT_STATUS.md` — 项目状态总表
- `00_system/ACTIVE_TASKS.md` — 当前活动任务

## 项目专属 Skill

- `novel-dna-analyzer` — 单本系统化分析
- `cross-novel-synthesis` — 多本横向比较与机制卡提取
- `originality-reviewer` — 原创故事风险筛查

## Git

GitHub（`https://github.com/pengcheng2000/NOVEL_LAB.git`）为中央真源：开始工作前 `git pull`；完成重要工作后更新状态文件、写日志、commit 并 push（详见 `00_system/AGENT_PROTOCOL.md`）。**严禁 `git push --force`**（除非用户明确要求）。版权源文本不进入公开仓库（见 `.gitignore` 与 `01_reference/README.md`）。
