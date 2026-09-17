# 《雨天旧衣店》75 秒 Concept Trailer — Asset Registry

## ASSET INDEX v1.0

Status: SPECIFIED — TEXTUAL SOURCE OF TRUTH

- **用途**：为 `concept_trailer_screenplay_v1.0.md` 与 `concept_trailer_shot_list_v1.1.md` 提供可复用、可组合、与单张生成图解耦的稳定资产身份。
- **范围**：当前 75 秒 Concept Trailer；不自动扩展为小说全局视觉 Canon。
- **生产原则**：文字规格先于 Look Development 图片。既有图片仅为实验参考，除非本文或 APPROVED Visual Bible 明确锁定，不得成为资产事实来源。
- **非本文件职责**：不包含 Flow Prompt、图像 Prompt、视频 Prompt、Storyboard、模型参数或镜头生成指令。

---

## 1. Source Hierarchy 与标签

事实优先级：

`Final Text > 正式人物档案 / World Bible > APPROVED Screenplay > APPROVED Shot List > Visual Bible Director Decision`

所有规格使用三类标签：

- **CANON FACT**：来自 Final Text、正式人物档案、World Bible 或被更高层来源确认的事实。
- **DIRECTOR VISUAL DECISION**：为本 Trailer 建立的视觉锁；在本项目生产期内固定，但不得反写为小说 Canon。
- **PRODUCTION CONSTRAINT**：为一致性、后期合成和生成稳定性建立的工程约束，不改变故事事实。

当三类内容并列时，资产生成必须先满足 CANON FACT，再满足 DIRECTOR VISUAL DECISION，最后应用 PRODUCTION CONSTRAINT。

---

## 2. Character Registry

| Asset ID | Asset Type | Asset Name | Priority | Required Shots | Identity Lock Level | Spec File | Status |
|---|---|---|---|---|---|---|---|
| CHAR-XN-001 | Character | 谢念（2025） | A | 003–009, 014–017 | HIGH — FACE / BODY / HAND | `CHARACTER_ASSET_SPECS.md` | SPECIFIED |
| CHAR-TL-001 | Character | 唐荔（2025） | A | 007, 017 | HIGH — FACE / HAND | `CHARACTER_ASSET_SPECS.md` | SPECIFIED |
| CHAR-ZWM-001 | Character | 赵为民（2025） | A | 002, 003, 005, 006, 014 | HIGH — FACE / HAND / POSTURE | `CHARACTER_ASSET_SPECS.md` | SPECIFIED |
| CHAR-LSY-1988-001 | Character | 年轻林素云（1988） | A | 011–013 | HIGH — FACE / HAIR / COSTUME | `CHARACTER_ASSET_SPECS.md` | SPECIFIED |
| CHAR-ZG-1988-001 | Character | 周桂珍（1988） | B | 010–013 | MEDIUM — SILHOUETTE / HAND / GAIT | `CHARACTER_ASSET_SPECS.md` | SPECIFIED |

说明：SHOT 015 中年迈林素云仅以手部与面碗记忆碎片出现，不建立第六套正脸身份资产；其局部表现并入 `PROP-MEMORY-MEAL-001`，不得由此推导老年林素云完整视觉 Canon。

---

## 3. Location Registry

| Asset ID | Asset Type | Asset Name | Priority | Required Shots | Identity Lock Level | Spec File | Status |
|---|---|---|---|---|---|---|---|
| LOC-HCL-2025-EXT-001 | Location | 2025 回潮里／寄雨行外景 | A | 001, 018 | HIGH — ARCHITECTURE / FACADE | `LOCATION_ASSET_SPECS.md` | SPECIFIED |
| LOC-JYX-2025-FRONT-001 | Location | 2025 寄雨行前店 | A | 002–008, 014–015 | HIGH — FLOOR PLAN / COUNTER / LIGHTING | `LOCATION_ASSET_SPECS.md` | SPECIFIED |
| LOC-JYX-FIT-001 | Location | 寄雨行试衣间 | B | 008–009, 014 | HIGH — MIRROR / CURTAIN / SCALE | `LOCATION_ASSET_SPECS.md` | SPECIFIED |
| LOC-HCL-1988-EXT-001 | Location | 1988 回潮里旧巷 | A | 009–011 | HIGH — ERA / DOOR / STREET DNA | `LOCATION_ASSET_SPECS.md` | SPECIFIED |
| LOC-JYX-1988-INT-001 | Location | 1988 寄雨行室内 | A | 011–013 | HIGH — ERA / STOVE / THRESHOLD | `LOCATION_ASSET_SPECS.md` | SPECIFIED |
| LOC-JYX-2025-CUT-001 | Location | 2025 店堂正中裁床区域 | A | 016–017 | HIGH — TABLE / WORK ZONE | `LOCATION_ASSET_SPECS.md` | SPECIFIED |

---

## 4. Costume Registry

| Asset ID | Asset Type | Asset Name | Priority | Required Shots | Identity Lock Level | Spec File | Status |
|---|---|---|---|---|---|---|---|
| COST-ZG-COAT-001 | Costume / Hero Garment | 周桂珍灰色粗花呢大衣 | A | 002–004, 008–014 | HIGH — SAME GARMENT ACROSS ERAS | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-XN-CARDIGAN-001 | Costume / Hero Garment | 谢念黑色羊毛针织开衫 | A | 003–008, 015 | HIGH — COSTUME STATE TRANSITION | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-SZ-WORKWEAR-001 | Costume / Hero Garment | “孙正”灰色劳保工装 | A | 016–017 | HIGH — TEXTILE / MARK / STITCH | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-XN-BASE-001 | Costume | 谢念固定内搭与下装 | A | 003–009, 014–017 | HIGH — DO NOT CHANGE BETWEEN SHOTS | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-TL-WORK-001 | Costume | 唐荔改衣师工作服 | A | 007, 017 | HIGH — SILHOUETTE / COLOR | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-ZWM-WORK-001 | Costume | 赵为民维修工工作服 | A | 002, 003, 005, 006, 014 | HIGH — LEFT CHEST POCKET / WEAR | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-LSY-1988-001 | Costume | 年轻林素云深蓝工作罩衫 | A | 011–013 | HIGH — ERA / COLOR / SHAPE | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| COST-ZG-BASE-1988-001 | Costume | 周桂珍大衣下可见内层与棉鞋 | B | 010–013 | MEDIUM — PARTIAL VISIBILITY | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |

---

## 5. Prop Registry

| Asset ID | Asset Type | Asset Name | Priority | Required Shots | Identity Lock Level | Spec File | Status |
|---|---|---|---|---|---|---|---|
| PROP-LEDGER-001 | Prop / Hero | 《承衣簿》 | A | 005, 007, 008 | HIGH — COVER / SCALE / PAPER | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| PROP-STAMPSET-001 | Prop / Hero | 铜章与朱砂色印泥 | A | 008 | HIGH — SHAPE / MATERIAL | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| PROP-TICKETS-1988-001 | Prop / Hero | 两张 1988 红色硬座票 | A — RESEARCH HOLD | 010–013 | HIGH — COUNT / COLOR / CONDITION; FORMAT PENDING | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED WITH RESEARCH HOLD |
| PROP-GUTTER-001 | Prop / Architectural Hero | 1960 年代旧铜檐槽 | A | 001, 004, 009, 017, 018 | HIGH — MATERIAL / POSITION / SOUND SOURCE | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| PROP-GLOVES-XN-001 | Prop / Costume Accessory | 谢念白色棉线手套 | B | 003–009, 014, 016–017 | HIGH WHEN HANDS VISIBLE | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| PROP-TAPE-TL-001 | Prop / Character Anchor | 唐荔黄色系卷尺 | A | 007, 017 | HIGH — COLOR / NECK POSITION | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |
| PROP-MEMORY-MEAL-001 | Prop / Memory Fragment | 阳春面、碗、蒸汽、年迈手部碎片 | B | 015 | MEDIUM — EMOTIONAL INSERT | `PROP_COSTUME_ASSET_SPECS.md` | SPECIFIED |

SHOT 006 左胸内袋内的硬质塑料旧物保持 **UNKNOWN**：只生成隔布轮廓，不建立独立资产，不显示具体形状、用途、文字或照片。

---

## 6. Shot → Asset Dependency Matrix

| Shot | Time | Characters | Location | Costume Assets | Prop Assets | Critical Continuity |
|---|---|---|---|---|---|---|
| 001 | 00:00–00:04 | — | LOC-HCL-2025-EXT-001 | — | PROP-GUTTER-001 | 梅雨黄昏；卷帘门半开；寄雨行木牌文字后期覆盖 |
| 002 | 00:04–00:08 | CHAR-ZWM-001 | LOC-JYX-2025-FRONT-001 | COST-ZWM-WORK-001; COST-ZG-COAT-001 | — | 赵抱同一灰呢大衣；卷帘门体系；湿衣沉重 |
| 003 | 00:08–00:12 | CHAR-XN-001; CHAR-ZWM-001 | LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-XN-CARDIGAN-001; COST-ZWM-WORK-001; COST-ZG-COAT-001 | PROP-GLOVES-XN-001 | 谢念 Costume A；白手套；赵维修工手与疲惫脸 |
| 004 | 00:12–00:15 | CHAR-XN-001 | LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-XN-CARDIGAN-001; COST-ZG-COAT-001 | PROP-GLOVES-XN-001; PROP-GUTTER-001 | 无光效；靠雨、铜鸣、内衬冷湿启动 |
| 005 | 00:15–00:19 | CHAR-XN-001; CHAR-ZWM-001 | LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-XN-CARDIGAN-001; COST-ZWM-WORK-001 | PROP-LEDGER-001; PROP-GLOVES-XN-001 | 账簿暗红生丝；文字后期覆盖 |
| 006 | 00:19–00:23 | CHAR-ZWM-001 | LOC-JYX-2025-FRONT-001 | COST-ZWM-WORK-001 | — | **右手按左胸内袋**；硬质物仅隔布轮廓，不具象化 |
| 007 | 00:23–00:27 | CHAR-XN-001; CHAR-TL-001 | LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-XN-CARDIGAN-001; COST-TL-WORK-001 | PROP-LEDGER-001; PROP-GLOVES-XN-001; PROP-TAPE-TL-001 | A→B 转换；黑开衫脱下后不得回到谢念身上 |
| 008 | 00:27–00:30 | CHAR-XN-001 | LOC-JYX-2025-FRONT-001; LOC-JYX-FIT-001 | COST-XN-BASE-001; COST-ZG-COAT-001 | PROP-LEDGER-001; PROP-STAMPSET-001; PROP-GLOVES-XN-001 | 开衫留柜台；“存押”后期合成；谢念进入试衣间 |
| 009 | 00:30–00:34 | CHAR-XN-001 | LOC-JYX-FIT-001; LOC-HCL-1988-EXT-001 | COST-XN-BASE-001; COST-ZG-COAT-001 | PROP-GLOVES-XN-001; PROP-GUTTER-001 | 同一大衣完成 Match Cut；现实/1988 不做形变魔法 |
| 010 | 00:34–00:38 | CHAR-ZG-1988-001 | LOC-HCL-1988-EXT-001 | COST-ZG-COAT-001; COST-ZG-BASE-1988-001 | PROP-TICKETS-1988-001 | 侧背与手；票仍在右侧大衣口袋；黑漆木门 |
| 011 | 00:38–00:42 | CHAR-ZG-1988-001; CHAR-LSY-1988-001 | LOC-HCL-1988-EXT-001; LOC-JYX-1988-INT-001 | COST-ZG-COAT-001; COST-ZG-BASE-1988-001; COST-LSY-1988-001 | PROP-TICKETS-1988-001 | 林素云成熟非老年；黑漆门内外冷暖边界 |
| 012 | 00:42–00:48 | CHAR-ZG-1988-001; CHAR-LSY-1988-001 | LOC-JYX-1988-INT-001 | COST-ZG-COAT-001; COST-ZG-BASE-1988-001; COST-LSY-1988-001 | PROP-TICKETS-1988-001 | 两张票，不能增减；周桂珍不锁正脸 |
| 013 | 00:48–00:52 | CHAR-ZG-1988-001; CHAR-LSY-1988-001 | LOC-JYX-1988-INT-001 | COST-ZG-COAT-001; COST-LSY-1988-001 | PROP-TICKETS-1988-001 | 票未落入掌心即中断；极近手部，不增加答案 |
| 014 | 00:52–00:55.5 | CHAR-XN-001; CHAR-ZWM-001 | LOC-JYX-FIT-001; LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-ZG-COAT-001; COST-ZWM-WORK-001 | PROP-GLOVES-XN-001 | 谢念 Costume B 外套灰呢大衣；雨骤停 |
| 015 | 00:55.5–01:00 | CHAR-XN-001 | LOC-JYX-2025-FRONT-001 | COST-XN-BASE-001; COST-XN-CARDIGAN-001 | PROP-MEMORY-MEAL-001 | 黑开衫只在柜台；老年林素云不出完整正脸 |
| 016 | 01:00–01:04 | CHAR-XN-001（手部可见） | LOC-JYX-2025-CUT-001 | COST-XN-BASE-001; COST-SZ-WORKWEAR-001 | PROP-GLOVES-XN-001 | 裁床在店堂正中；“孙正”文字后期覆盖 |
| 017 | 01:04–01:10 | CHAR-TL-001; CHAR-XN-001 | LOC-JYX-2025-CUT-001 | COST-TL-WORK-001; COST-XN-BASE-001; COST-SZ-WORKWEAR-001 | PROP-TAPE-TL-001; PROP-GLOVES-XN-001; PROP-GUTTER-001 | 唐荔为裸手，谢念仍戴白手套；暗针→唐荔→谢念反应 |
| 018 | 01:10–01:15 | — | LOC-HCL-2025-EXT-001 | — | PROP-GUTTER-001 | 复用 001 建筑身份；夜雨；卷帘门半卷；标题后期合成 |

---

## 7. Extraction-ready Assembly Rule（非 Prompt）

未来每个 Shot 的生成描述必须从本 Registry 读取对应资产 ID，并按以下顺序拼装信息：

`SHOT SPEC + CHARACTER IDENTITY + COSTUME STATE + LOCATION IDENTITY + PROP IDENTITY + CAMERA / ACTION`

这里的“拼装”是文档依赖关系，不是现成 Prompt。任何工具侧改写不得删除资产 ID，也不得用单张生成图反向覆盖文字锁。

---

## 8. Canon Audit / Source Tensions

### 新发现并已在本规格中裁定的冲突

1. **裁床位置**：Chapter 019 Final 明确为“店堂正中的实木裁床”；Visual Bible Location 06 写“寄雨行深处”。本 Registry 与 Location Spec 依优先级锁定为**主店堂中部／店堂正中**。镜头可通过构图压暗或弱化背景，但不得把裁床移动到后堂或独立密室。

### 已知旧冲突，不计为本轮新增

- Part I Canon Summary 曾将赵母衣物与谢念押物颜色／归属写反；APPROVED Screenplay 已按 Chapter 001 Final 裁定为：赵母遗物＝灰色粗花呢大衣，谢念押物＝黑色羊毛针织开衫。

### 非冲突但必须标注的层级差异

- 谢念人物档案中的深蓝工作罩衫属于小说日常服装事实；本 Trailer 以 Chapter 001 Final 的黑开衫为场景事实，并以 APPROVED Visual Bible 的固定灰蓝／冷白内搭作为导演锁，不改写小说长期衣橱。
- 灰呢大衣双排六扣（3×2）是 `DIRECTOR VISUAL DECISION — Trailer Reference Lock`，不是小说 Canon。
- 火车票的数量、红色、硬座、1988、揉皱为锁定信息；具体票制、尺寸、纸张、字体与版式在史料核验前保持未定。
- SHOT 017 唐荔触衣时必须裸手；白手套只属于谢念，不能转移到唐荔。
