# Part II Opening Arc Canon Recovery Audit

> 审计角色：GPT-5.6 Sol / Editor-in-Chief / Head Writer / Canon Recovery Authority
>
> 问题 Commit：`0596eeb canon: finalize part two opening arc chapters 021 to 023`
>
> 权威顺序：① Ch21–23 Accepted Final prose（以 `322157a` Rewrite 为内容基准）→ ② `b7e7a9b` Sol Final Acceptance → ③ Part I Final / Canon → ④ Part II Architecture / Brief → ⑤旧 Draft / Reports。Finalization Agent 自然语言总结无权覆盖前四层。

## Audit Verdict

**CANON REPAIR REQUIRED**

- Ch21–23 Accepted prose：安全，不需要重写或编辑。
- Final 文件：正文字符完全一致，但不满足严格 binary match；三份 Final 各比 accepted Rewrite 多 1 个末尾 LF。
- Canon / Character / Relationship / Rule / Status：存在定点污染与过度抽取，需要按本 Manifest 修复。
- `EXPANSION GATE = PASS SUSPENDED / TEMP HOLD`。
- Ch24–29：`NOT AUTHORIZED YET`。

本轮不回滚 `0596eeb`，不修改 Final，不直接修 Canon；由 Continuity 按事实级 Manifest 定点修复。

## Final Text Binary Verification

| Chapter | Accepted Rewrite blob (`322157a`) | Generated Final blob (`0596eeb`) | Bytes | Binary Match | Complete Difference |
|---|---|---|---:|---|---|
| Ch21 | `e9b102ad3c3b1bfe2cedcdfe919044adbfa5680f` | `26b5ed388ffeed0edc04ba77011097eafb7bfb69` | 14,375 → 14,376 | **NO** | Final 末尾新增 1 个 LF / 空行 |
| Ch22 | `aa06f31e1146fd551c023fc96b98c484ae0e7a4d` | `b18a35352224e57b3b4c28756dd61242155db5e9` | 14,716 → 14,717 | **NO** | Final 末尾新增 1 个 LF / 空行 |
| Ch23 | `26e9e7ebc7e23813da8ef8d068b3ed095f1c42fc` | `57680b0a2f1cc00036212344a3765a570a3bc05c` | 14,553 → 14,554 | **NO** | Final 末尾新增 1 个 LF / 空行 |

**BINARY HARD CONFLICT FOUND — NON-SUBSTANTIVE TRAILING-LF ONLY。**三份 diff 除文件末尾空行外无任何正文字符、标点、段落或事实差异。

因此：

- `BINARY IDENTITY = FAIL`
- `FINAL PROSE CONTENT = SAFE`
- `FINAL TEXT CONTAMINATION = 0`
- Canon Repair **禁止触碰** `chapter_021_final.md`、`chapter_022_final.md`、`chapter_023_final.md`。末尾 LF 不影响正文效力，不为追求 blob 相等再次改 Final。

## Canon Contamination Summary

实际仓库未出现用户警报中的大部分“报告幻觉”，但 `0596eeb` 确有 Canon 污染：

- **18 个不受支持的事实 / 知识 / 政策抽取簇**；
- **4 个系统或文档结构状态缺陷**；
- **12 个文件需要定点 Patch**；
- 3 份 Final 内容安全，不在 Patch 清单。

十八个污染簇编号：

1. Canon Summary 把 `c69f530` 误写为 Finalization commit；
2. 梁女士夹克被改写为“1990年代薄棉/混纺防雨绸/插肩袖/暗门襟”；
3. 梁女士委托被改写为“翻新内衬防风层/更换抽绳”；
4. Version 1 第一栏被扩写出“受赠/代办”等 Final 未列选项；
5. Version 1 第二栏被扩写出“不可逆重制/清洗/暂缓”等固定菜单；
6. Public Policy 三体系被写入 `OLD_CLOTHES_RULES` 并命名为“铁律”；
7. 本案暂停被泛化为普遍的“可信争议暂停原则”，并擅写“可逆普通做工维持挂单暂存”；
8. Canon Summary 错写唐荔“知晓七格”；
9. `SECRET_MATRIX` 错写唐荔不知道超自然读衣能力；
10. 唐荔当前权限状态被过度绝对化为永久“不干涉/不触碰后堂、钥匙绝不交涉”；
11. `RELATIONSHIP_ENGINE` 把谢念/唐荔有摩擦的合作写成“无缝配合”；
12. `RELATIONSHIP_ENGINE` 错写秦沛已明确接受唐荔工位限制；
13. Canon Summary 错写周序对“孙正”完全不知道，抹去 Part I 已知的仓库/候选灰工装现实链；
14. Canon Summary / `SECRET_MATRIX` 错写余禾协助归还梁女士夹克；实际递还者是谢念；
15. `SECRET_MATRIX` 把余禾“不知后堂秘密”写成“不知道后堂大锁”这一过度物理化状态；
16. Finalization 工作日志凭空写入 `¥120 counter fee`；
17. Finalization 工作日志凭空写入 `¥20,000 intact`，制造与历史 2 万元及无定额预付款混线风险；
18. Finalization 工作日志把“梁女士取回暗绿夹克”写成“grey work jacket returned to Liang”，混淆暗绿夹克与第一格候选灰工装。

四个系统 / 结构缺陷：

1. PROJECT_STATUS / ACTIVE_TASKS / HANDOFF 把 Gate 标为 ACTIVE 并授权 Ch24–29，当前须转为 TEMP HOLD；
2. ACTIVE_TASKS 待办队列错误回退到已完成的 Part-I Finalization；
3. HANDOFF 的 IN_PROGRESS / NEXT_TASK 同样回退到 Part-I Finalization，并丢失正确 Canon Repair 接力；
4. FORESHADOWING_PLAN 重复插入旧第一格条目及 Ch14/Ch17/Ch20 多个“章末待兑付状态”标题，破坏当前状态结构。

## Confirmed Safe Facts

- 梁女士在普通公开二手市集付款购买暗绿棉夹克，持普通收据与支付记录；只证明交易发生及当时没有明显理由预见争议。
- 沈女士为 `LOCAL ONLY`，不锁完整姓名；照片与肘部普通修补细节形成 `CREDIBLE CLAIM / UNDER VERIFICATION`。
- 沈女士关于母亲仍在世、在家生活、神志清楚的说法是 `REPORTED CLAIM`，未独立核验；无疾病背景。
- 暗绿夹克订单挂起、裁剪暂停、拍摄停止，由梁女士取回自行保管；Case 未结。
- 回潮桥货运仓库—调剂社—第三方仓储现实底座恢复；经手环节全部为调查假设。
- 周序本弧只处理施工通道、占道、沉降监测和街区安全。
- 秦沛不知道第一格、七格、《承衣簿》与读衣机制；只知道候选灰工装及“孙正”现实标记。
- 余禾实际在本弧返场并承担普通前台来源说明、拍摄同意、排期与客户沟通。
- `2016 NEW FACTS = 0`；红外套仅作方法参照。
- `READ COUNT = 0 / QUASI-READ = 0 / PLEDGE = 0 / NEW RULES = 0 / Memory Segment = NONE`。

## Unsupported Facts

经 `0596eeb` 实际文件搜索，下列警报项**没有进入任何核心 Canon 文件**：

- “梁巡”完整姓名；
- 1993 年“红光调剂社”、历史发票或旧年代买卖记录；
- 120 元柜台初查费（仅 Finalization 工作日志误述）；
- 秦沛首期 2 万元业务款 / 2 万元预付款；
- 铁皮盒；
- 工作证复印件；
- 工装失窃报警记录；
- 沈母腿脚不便；
- 唐荔住进东厢房；
- 周序查访调剂社档案；
- 周序 × 秦沛互通调剂社档案或仓储链；
- “旧物代寻”正式经营范围；
- “不读、不揽、不留”新口号 / 新政策；
- “高端心理抚慰店”；
- 周国梁成为货运仓库历史人物；
- 孙正被直接写成真实原主 / 衣主。

上述内容不得在 Repair 中“顺手补写”；其中 Finalization 工作日志的 120 元与 ¥20,000 误述必须删除。

## Direct Canon Conflicts

1. **唐荔知识双向冲突**：Canon Summary 写“知晓七格”，`SECRET_MATRIX` 又写“不知道超自然读衣异能”。正确状态是：她知道读衣能力存在、亲见过流程并知道代价及《承衣簿》特殊用途；不知道第一格具体文字与七格完整结构，Opening Arc 无新增特殊知识。
2. **周序知识冲突**：Canon Summary 写他对“孙正”完全不知道；Part I 已确认他知道孙正临时用工、仓库清退链和带“孙正”标记的候选灰工装。其未知项是第一格、七格、《承衣簿》和能力。
3. **灰工装/夹克物件混淆**：Finalization 日志写“grey work jacket returned to Liang”；实际梁女士取回暗绿棉夹克，候选灰工装始终在秦沛第三方仓储链。
4. **规则预算自相矛盾**：`OLD_CLOTHES_RULES` 一面写 `NEW RULES = 0`，一面新增三条“铁律/原则”。这些是证据方法或 Public Policy，不是超自然规则。

## Liang Case Recovery

正确 Opening Case：

- 人物只称梁女士；无“梁巡”；
- 衣物为暗绿色厚实斜纹水洗棉夹克，阔版落肩、暗哑工装排扣；只需 Canonize 对情节有用的“暗绿棉夹克、袖长待改、左肘磨损/白色垫布修补”；
- 委托是改短袖长、修补左肘磨损，并同意拍摄普通修补过程；
- 市集收据与支付记录只证明普通交易发生；
- 无 1993 红光调剂社、历史发票、120 元初查费、工作证、报警记录或盗窃案；
- Case 结尾衣物由梁女士带走，双方继续核验。

## Public Policy Recovery

Version 1 必须严格恢复 Accepted Final：

1. **物品来源说明**：个人自有、二手购买、代人送修；二手转让或代人送修时主动提供购买凭证或相关交接说明；客户填写只是自述声明。
2. **普通处理与修补授权范围**：记录具体处理部位、工序及是否涉及不可逆裁剪。
3. **拍摄、公开与隐私同意**：普通修补与公开展示分开；出现可信第三方持现实关联材料异议时，相关公开内容暂停核验。

三栏是 `Public Business Policy V1`，不是法律制度、万能筛选器或 `OLD_CLOTHES_RULES`。本案处理不能抽成“所有可信异议都自动暂停所有可逆做工”的新硬政策。

## Yu He Recovery

- Opening Arc 实际返场，状态为 `ACTIVE FRONT-DESK OPERATIONS`。
- 功能：来源说明、拍摄同意、普通排期、客户沟通与联系内容组。
- 暗绿夹克由谢念递还梁女士，不是余禾。
- 余禾可知道后堂作为物理空间存在；其知识边界应写为不知道后堂特殊物、账簿内容、第一格/七格及读衣机制，而非“不知道后堂大锁”。

## Zhou Xu Recovery

- 本弧新增动作只限施工通道、客流占道、沉降监测点和街区安全。
- 不调查梁/沈交易、家事、市集或授权；不查调剂社档案，不与秦沛交换仓储链信息。
- 累计知识必须保留 Part I：知道孙正为仓库临时工、仓库—调剂社现实流转、候选灰工装存在并带“孙正”标记。
- 继续不知道《承衣簿》、第一格、七格和读衣机制。
- 关系状态：`BOUNDED REAL-WORLD ALLIANCE + MUNICIPAL / CONSTRUCTION FUNCTION ONLY IN THIS ARC`。

## Qin Pei Recovery

- 知道暗绿夹克内容撤停、梁/沈异议、普通合作与候选灰工装“孙正”标记。
- 可提出公开寻找线索的商业建议；不因此知道第一格。
- 不知道《承衣簿》、七格、第一格结构和读取机制；只怀疑寄雨行有未公开处理方式。
- 没有 2 万元业务预付款；首期普通协作预付款金额继续未锁。
- 没有“高端心理抚慰店”定位。

## Tang Li Recovery

- 工作功能保持：普通经营责任 + 工位/排期/劳动成本主导权；不是洒扫与基础缝补杂工。
- 本弧与谢念先有真实职业摩擦，后共同形成 Version 1；不得写成“无缝配合”。
- 特殊权限未恢复，本弧未参与后堂特殊事务；不得升级为“永远不触碰后堂门/钥匙永久不得讨论”的世界规则。
- 没有住进东厢房。
- 知识恢复为：知道能力存在、流程与代价、《承衣簿》特殊用途；不知道第一格具体文字、七格完整结构及谢念 Ch23 私有方法修正。

## First-Slot Recovery

- 状态：`CANDIDATE LOCATED / ELIGIBILITY UNRESOLVED / UNREAD`。
- “孙正”只证明衣物某阶段与名字发生联系；不证明原主、衣主、穿衣人或最终持有人。
- 允许调查发放、领取、代领、临时借用/实际使用、回收、遗留、清退等经手链；全部为 `INVESTIGATION HYPOTHESES`。
- 不 Canonize 班组制度、工装登记册、固定仓管员、防汛调拨或具体经手人。
- 周国梁维持市政排水维护线，不进入货运仓库人员链。

## Financial / 20k Recovery

- 秦沛首期普通协作预付款：金额未锁。
- 历史第一笔 2 万元：`2023-04-12` 栖州旧物调剂服务社收到林素云交付 2 万元；用途、品名及与灰工装因果继续 UNKNOWN。
- Finalization 日志中的 `¥20,000 intact` 删除；禁止把它解释成秦沛业务款。
- Finalization 日志中的 `¥120 counter fee` 删除；不存在柜台初查收费制度。
- 不存在铁皮盒 Object State。

## Object State Recovery

| Object | Correct State |
|---|---|
| 暗绿棉夹克 | `ORDER SUSPENDED / CUTTING PAUSED / FILMING CEASED / RETURNED TO CLIENT FOR CUSTODY`；梁女士持有 |
| 候选灰工装 | 秦沛控制的第三方仓储链；`CANDIDATE LOCATED / ELIGIBILITY UNRESOLVED / UNREAD` |
| 三栏表 | 前台 Version 1 工作表；非法律/超自然规则 |
| 120 元 / 铁皮盒 | 不存在，不得登记为财务或物件 |

## Knowledge-State Recovery

| 角色 | Correct Cumulative State After Ch23 |
|---|---|
| 谢念 | 知第一格与能力；建立三栏并修正经手链方法；不知孙正生死/灰工装真实衣主与穿者 |
| 唐荔 | 知能力存在、流程/代价与账簿特殊用途；不知第一格具体文字、七格完整结构、谢念私有方法修正 |
| 周序 | 知孙正临时用工、仓库/调剂社现实链、候选灰工装及标记；不知第一格/七格/账簿/能力 |
| 秦沛 | 知候选灰工装及标记、普通合作和内容撤停；不知第一格/七格/账簿/机制 |
| 余禾 | 负责前台分流；不知后堂特殊物、账簿内容、第一格/七格/机制 |

## Files Requiring Patch

共 **12 个**：

1. `00_system/PROJECT_STATUS.md`
2. `00_system/ACTIVE_TASKS.md`
3. `00_system/HANDOFF.md`
4. `01_characters/PROTAGONIST.md`
5. `01_characters/TANG_LI.md`
6. `02_relationships/RELATIONSHIP_ENGINE.md`
7. `03_world/OLD_CLOTHES_RULES.md`
8. `05_timeline/MASTER_TIMELINE.md`
9. `06_secrets/SECRET_MATRIX.md`
10. `07_foreshadowing/FORESHADOWING_PLAN.md`
11. `09_manuscript/canon/part_02_opening_arc_ch21_23_canon_summary.md`
12. `99_logs/gemini/2026-09-15_C05_part02_opening_arc_finalization.md`

明确 **不需 Patch**：`01_characters/ZHOU_XU.md`、`01_characters/QIN_PEI.md` 及三份 Ch21–23 Final。前两者的本次新增内容没有用户所警报的查档/合作/金额污染；累计知识修复集中在 Canon Summary / Secret Matrix。

## Canon Repair Manifest

| FILE | WRONG CURRENT FACT | CORRECT FACT | SOURCE OF AUTHORITY | PATCH TYPE |
|---|---|---|---|---|
| `00_system/PROJECT_STATUS.md` | Ch21–23 Canon 已可靠、Gate ACTIVE、可立即规划 Ch24–29；混入重复历史 last-update 行 | Ch21–23 Final prose accepted；Canonization under repair；Gate TEMP HOLD；Part I 仍 COMPLETE；删本次混入的重复状态噪声 | 本 Audit + `b7e7a9b` | STATUS PATCH |
| `00_system/ACTIVE_TASKS.md` | NEXT Ch24–29；队列又回退到 Part-I Finalization | NEXT Continuity Apply Canon Repair Manifest；Ch24–29 NOT AUTHORIZED；保留 Ch21–23 Final Text accepted | 本 Audit | STATUS PATCH |
| `00_system/HANDOFF.md` | NEXT Ch24–29；IN_PROGRESS/NEXT_TASK 回退 Part-I Finalization；Gate ACTIVE | NEXT Continuity Canon Repair；Canonization under repair；Gate TEMP HOLD；修复重复编号/交接噪声 | 本 Audit | STATUS PATCH |
| `01_characters/PROTAGONIST.md` | 三栏压缩为“来源 / 普通处理授权 / 拍摄与隐私” | 使用 Final 精确结构：“物品来源说明 / 普通处理与修补授权范围 / 拍摄、公开与隐私同意” | Ch23 Final + `b7e7a9b` | FACT WORDING PATCH |
| `01_characters/TANG_LI.md` | “严格不干涉/不打探/不替开门”被写成长期绝对状态 | 特殊权限未恢复；本弧未参与后堂特殊事务；无钥匙交换；不新增永久禁触规则 | Part I Canon + Ch21–23 Final | SCOPE DOWNGRADE |
| `02_relationships/RELATIONSHIP_ENGINE.md` | 谢念/唐荔“无缝配合”；钥匙与权限“绝不交涉”；秦沛已接受唐荔工位限制 | 有摩擦后形成工作分流；特殊权限未恢复/本弧无钥匙事件；秦沛只接受撤停并要求替代素材，唐荔自行确立排期权 | Ch21–23 Final | RELATIONSHIP PATCH |
| `03_world/OLD_CLOTHES_RULES.md` | 将三体系、名字标记方法、可信争议暂停写为三条“铁律/原则”，并写可逆做工挂单 | 保留 Ch21–23 Read=0/New Rules=0；明确 Version 1 是 Public Policy，不改变/新增旧衣规则；删除三条规则化抽取 | `b7e7a9b` + Ch23 Final | RULE DECONTAMINATION |
| `05_timeline/MASTER_TIMELINE.md` | 三栏名称被压缩改写 | 恢复 Final 的三栏全称；其余 6/23 顺序保留 | Ch23 Final | TIMELINE WORDING PATCH |
| `06_secrets/SECRET_MATRIX.md` | 三栏改写；唐荔错误“不知异能”；余禾错误参与归还并“不知后堂大锁”；累计知识省略 | 恢复精确三栏；唐荔知能力/流程/代价但不知第一格/七格完整结构；谢念归还夹克；余禾只不知特殊内容；保留周序/秦沛累计知识边界 | Part I Canon + Ch21–23 Final + `b7e7a9b` | KNOWLEDGE PATCH |
| `07_foreshadowing/FORESHADOWING_PLAN.md` | 重复第一格行和旧章末标题；“暗绿薄棉夹克”；“四大假设” | 去重；统一“暗绿棉夹克”；写“货运仓库经手链假设”；只保留当前 Ch23 状态标题 | Ch21–23 Final | STRUCTURE + FACT PATCH |
| `09_manuscript/canon/part_02_opening_arc_ch21_23_canon_summary.md` | Finalization commit 错；夹克材质/款式/委托错；三栏选项扩写；Tang/Zhou/Yu He 知识动作错；班组/规则泛化 | 按本报告 Liang/Public Policy/Knowledge/Object/First-Slot 各节逐项恢复；Finalization commit 改 `0596eeb`，同时标 Canon repaired pending verification | Ch21–23 Final + `b7e7a9b` + Part I Canon | CANON SUMMARY REWRITE-IN-PLACE |
| `99_logs/gemini/2026-09-15_C05_part02_opening_arc_finalization.md` | “exact binary copy”错误；路径写 `manuscript/rewrite`；灰工装归梁；¥120 fee；¥20,000 intact | 记录三份仅多末尾 LF；正确目录 `09_manuscript/drafts/`；梁女士取回暗绿夹克；删除两项金额；注明本次 Canon Audit / Repair | Blob audit + Ch21–23 Final + Part I Finance Canon | REPORT CORRECTION |

Repair 必须逐项完成，不得整文件回滚；不得借修复新增 Ch24 规划、角色、机构、金额或规则。

## Expansion Gate State

`EXPANSION GATE = PASS SUSPENDED / TEMP HOLD`

结构 Gate 在 `b7e7a9b` 已通过，但实际 Canon 可靠性未通过本轮审计，因此暂停生效。Ch24–29 仍禁止规划，Writer 仍冻结。

恢复流程：

1. Gemini Continuity MEDIUM 按 Manifest 定点修复；
2. Continuity 执行 Canon Integrity Verification；
3. GPT-5.6 Sol QUICK / MEDIUM Final Gate Recheck；
4. 只有 Canon 干净后，Gate 才转为 `PASS / ACTIVE`，随后才允许 Sol 规划 Ch24–29。

## Final Recommendation

下一位：**Gemini Continuity & Canon Agent（MEDIUM）**。

任务：**APPLY CANON REPAIR MANIFEST**。保护三份 Final，不重写正文；修复上述 12 文件并出具逐项 Integrity Verification。当前不规划 Ch24–29，不写 Chapter 024。
