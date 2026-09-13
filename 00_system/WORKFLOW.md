# WORKFLOW — 工作流程

## 总管线

```
参考小说 → 深度阅读 → 单本 Story DNA → 跨作品比较
→ 提取可复用故事机制 → Story DNA Library
→ 根据机制设计原创故事 → 原创性审查 → 原创小说 → 剧本化 → AI 视频化
```

当前阶段只执行：【参考小说研究 + Story DNA 提取】

## 读取方式：Progressive Compression

**禁止一次性把多部长篇塞进上下文然后粗略总结。**

```
原始章节 → 章节分析 → Arc/卷级分析 → 小说级 DNA → 机制卡 → 跨小说综合
```

- 长篇先建立章节索引（`00_source_index.md`）
- 按合理批次读取（每批 5–15 章，视章节长度）
- 每批结束形成结构化中间状态写入文件
- **不依赖聊天上下文记忆**——所有耐久信息写入文件
- 百万字级作品尤其如此

## 单本标准输出

每本小说建立独立目录（如 `02_analysis/global/it-ends-with-us/`），至少包含：

```
00_source_index.md        章节索引与源文件信息
01_executive_summary.md   执行摘要
02_plot_map.md            情节地图（Arc 结构）
03_character_system.md    人物系统
04_relationship_engine.md 关系引擎
05_hook_and_pacing.md     钩子与节奏
06_reward_engine.md       爽点引擎
07_suspense_information.md 悬疑与信息差
08_emotional_engine.md    情绪引擎
09_style_analysis.md      文风分析
10_reader_addiction.md    读者成瘾循环
11_story_mechanism_cards.md 机制卡（≥10 张）
12_video_adaptation.md    AI 视频适配
13_originality_boundaries.md 原创性边界（GREEN/YELLOW/RED）
NOVEL_DNA.yaml            统一 Schema 结构化输出
```

所有文件遵循 `00_system/ANALYSIS_SCHEMA.md`。缺失机制写 `not_applicable`，不改 Schema。

## 阶段顺序（SINGLE_AGENT_MODE，2026-09-13 起生效）

1. 完成 5 本 GLOBAL → `03_story_dna/global/GLOBAL_SYNTHESIS.md` + `GLOBAL_MECHANISMS.yaml`
2. 完成 5 本 CHINA_PRINT → `03_story_dna/china_print/CHINA_PRINT_SYNTHESIS.md` + `CHINA_PRINT_MECHANISMS.yaml`
3. 完成 5 本 CHINA_WEB → `03_story_dna/china_web/CHINA_WEB_SYNTHESIS.md`（含原 DeepSeek 计划的网文专项综合文件，见 `02_analysis/china_web/STATUS.md`）
4. 全部就绪后做 15 本最终横向分析 → `03_story_dna/master/`

执行顺序内按源文件可得性排序：**FULL_SOURCE > PARTIAL_SOURCE > METADATA_ONLY > MISSING_SOURCE**。无 FULL_SOURCE 时只做 PARTIAL_SOURCE 范围内可可靠完成的分析（开篇 Hook / 开篇人物 / 首章节奏 / 开篇语言），明确标注 PARTIAL ANALYSIS，不声称完成全书级结论（全书人物弧 / 全书 Plot Engine / 最终关系结构 / 完整 Reader Addiction Loop / 全书高潮）。

## 任务分配

| Agent | 区域 | 作品 |
|---|---|---|
| Claude（SINGLE_AGENT_MODE） | GLOBAL | It Ends with Us / The Midnight Library / Lessons in Chemistry / Fourth Wing / The Housemaid |
| Claude（SINGLE_AGENT_MODE） | CHINA_PRINT | 人生海海 / 文城 / 长安的荔枝 / 额尔古纳河右岸 / 繁花 |
| Claude（SINGLE_AGENT_MODE） | CHINA_WEB | 我真没想重生啊 / 大奉打更人 / 我在精神病院学斩神 / 十日终焉 / 都重生了谁谈恋爱啊 |

<details>
<summary>历史存档：原双 Agent 任务分配（仅作记录，不再约束当前工作）</summary>

| Agent | 区域 | 作品 |
|---|---|---|
| Kimi | GLOBAL | It Ends with Us / The Midnight Library / Lessons in Chemistry / Fourth Wing / The Housemaid |
| Kimi | CHINA_PRINT | 人生海海 / 文城 / 长安的荔枝 / 额尔古纳河右岸 / 繁花 |
| DeepSeek | CHINA_WEB | 5 本网文（DeepSeek 侧自定） |
</details>

## 状态管理

- 状态值：`TODO` / `IN_PROGRESS` / `COMPLETED` / `MISSING_SOURCE` / `BLOCKED`
- 源文件状态值：`FULL_SOURCE` / `PARTIAL_SOURCE` / `METADATA_ONLY` / `MISSING_SOURCE`（严禁把 PARTIAL_SOURCE 当作 FULL_SOURCE）
- 持续维护 `00_system/PROJECT_STATUS.md`、`00_system/ACTIVE_TASKS.md`、`99_logs/`（SINGLE_AGENT_MODE 下统一写入 `99_logs/claude/`，历史 kimi/ deepseek/ 目录只读保留）
- 不要求用户重复提供已存在于项目中的信息
- 长任务持续推进，优先留下完整耐久文件状态，而非依赖当前 Session
- 每完成重要阶段更新 PROJECT_STATUS.md / ACTIVE_TASKS.md，必要时更新 HANDOFF_AUDIT.md——任何新 Agent 都应能仅靠项目文件恢复工作
- 第一阶段不自动 git commit
