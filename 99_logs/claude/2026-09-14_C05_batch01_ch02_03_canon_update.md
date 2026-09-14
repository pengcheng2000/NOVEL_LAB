# 2026-09-14 — C05 Batch 01（Ch2–3）Canon Update（GLM 职能）

## 任务

Phase 6 Batch A 第 6 步：将 Ch2/Ch3 Final（Sol 双章 ACCEPT，commit `c1d5d61`）正式 Canon 化。只从 `final/chapter_002_final.md`、`final/chapter_003_final.md` 抽取事实，不使用 Draft/Rewrite。

## 处置的工作区异常

开工时发现两章 Final 有未提交修改——经 diff 核验仅为文件末尾换行（各 +1 空行），无内容变化。未提交、未还原，留给正文负责方处理；本轮提交显式排除这两个文件。

## Canon 更新明细

1. **人物**：PROTAGONIST/TANG_LI/ZHAO_WEIMIN/ZHOU_XU 追加"Chapter 003 结束时"状态；新增 `ZHOU_GUIYING.md`（78 岁小姨妈；只登记正文确认信息，未扩写家暴/法律细节；未接收读衣转述、不知能力存在）。
2. **关系**：Ch2–3 Before/Change/After（谢念×唐荔＝默契配合+信任存疑；×周序＝零信任程序交换；×赵为民＝委托结清、无强制联结）。
3. **时间线**：6/8 九步、6/9 九步事件序列；1988 冬条目按 Final 更新——票为周桂英母女准备（逃离醉酒砸门丈夫）、周桂珍动过念头但折返、请林素云保密；明确登记"无诱饵战术、无目的地、无购票证件设定"（Sol 已删除项不入 Canon）。
4. **规则 Reveal State**：续读旧例全文、折痕消退实证、代价不扩散、转述只对委托人（第三方隔离）、衣内近年重缝藏物（授权拆线）。
5. **Secret Matrix**：六方（Reader/谢念/唐荔/赵为民/周桂英/周序）KNOWS/SUSPECTS/DOES NOT KNOW 快照；周桂英"未接收转述"、周序"不知读衣"均显式锁定。
6. **伏笔**：两张硬座票 → 第一阶段 Payoff 完成（情感余波保留，禁止重复展开）；新登记 5 项（缺页、归还次序七位结构、墨绿灯芯绒疑似样本、9/5+铜檐槽备注、周父巡检表）；校正 Phase 5 表两处过时位置（名单角 Payoff Ch4→Ch3；唐荔碰校服布 Ch2→Ch2 合页/Ch5 蓝布）。
7. **新文件**：`batch_01_ch02_03_canon_summary.md`（12 节 + 7 项物件追踪表）；`CHAPTER_004_005_READINESS.md`（**READY** + 4 条非阻塞备注）。
8. **状态**：PROJECT_STATUS（3 chapters completed，Phase 6 未完成）、ACTIVE_TASKS（NEXT = Gemini Draft Ch4–5 Batch B）、HANDOFF。

## 边界遵守

- 未修改两章 Final 正文；未重新审稿；未写 Ch4；未改 Ch4–6 Brief；未创造新 Canon（赵为民"未理解/未原谅/未释怀"显式登记为不得改写项）。
- commit：`chore: canonize chapters 002 and 003`，push 无 force。
