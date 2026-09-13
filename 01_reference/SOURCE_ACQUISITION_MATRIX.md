# SOURCE_ACQUISITION_MATRIX — 15 本小说来源获取矩阵

最后更新：2026-09-13
核验方式：后台研究 Agent 对官方平台逐一实证核验（Amazon 商品页 / iTunes Search API / Google Play / Kobo Wayback 存档 / 微信读书搜索 API / 豆瓣阅读 / QQ阅读 / 起点 m.qidian.com / 番茄 fanqienovel.com），共 211 次工具调用。无法核验项标注 UNVERIFIED。
状态值：`FULL_SOURCE` / `PARTIAL_SOURCE` / `METADATA_ONLY` / `MISSING_SOURCE`（严禁自行升级）。
优先级：`P0`（快速可得完整合法文本或最适合流水线测试）/ `P1`（价值高但获取成本稍高）/ `P2`（后续处理）。

---

## 总览

| # | 作品 | 类别 | 当前状态 | 优先级 | 一句话判定 |
|---|---|---|---|---|---|
| 1 | It Ends with Us | GLOBAL | PARTIAL_SOURCE | P1 | KU 可订阅阅读；已有第 1 章 PARTIAL 分析可延展 |
| 2 | The Midnight Library | GLOBAL | PARTIAL_SOURCE（极浅） | P2 | 无 KU，需购买；中文试读仅 1.5 页 |
| 3 | Lessons in Chemistry | GLOBAL | PARTIAL_SOURCE | P2 | 无 KU，需购买；试读覆盖 1.5 章 |
| 4 | Fourth Wing | GLOBAL | PARTIAL_SOURCE | P1 | KU 可订阅；试读约 2 章 |
| 5 | The Housemaid | GLOBAL | METADATA_ONLY | P2 | 英文电子书仅 Amazon 渠道（含 KU），其他平台无 |
| 6 | 人生海海 | CHINA_PRINT | MISSING_SOURCE | P2 | 仅微信读书单渠道（付费 ¥33） |
| 7 | 文城 | CHINA_PRINT | MISSING_SOURCE | P2 | 仅微信读书单渠道（付费 ¥39.5） |
| 8 | 长安的荔枝 | CHINA_PRINT | MISSING_SOURCE | **P0** | 全 15 本中最短（约 7 万字）完整长篇；三平台上架，最适合作为第一本 FULL_SOURCE |
| 9 | 额尔古纳河右岸 | CHINA_PRINT | MISSING_SOURCE | P2 | 微信读书 price=0（疑似会员畅读/限免，机制 UNVERIFIED） |
| 10 | 繁花 | CHINA_PRINT | MISSING_SOURCE | P2 | 微信读书 + 豆瓣阅读双渠道，约 19.6 万字 |
| 11 | 我真没想重生啊 | CHINA_WEB | MISSING_SOURCE | **P0** | 起点全书 1101 章**免费**；313 万字；多平台分发 |
| 12 | 大奉打更人 | CHINA_WEB | MISSING_SOURCE | P1 | 起点全书 952 章**免费**；380 万字 |
| 13 | 我在精神病院学斩神 | CHINA_WEB | MISSING_SOURCE | P1 | 番茄**全书免费**；426 万字；有解码工具链支持 |
| 14 | 十日终焉 | CHINA_WEB | MISSING_SOURCE | **P0** | 番茄**全书免费**；320 万字；2024 番茄年度榜 TOP1；有解码工具链支持 |
| 15 | 都重生了谁谈恋爱啊 | CHINA_WEB | MISSING_SOURCE | P2 | 起点仅前约 104 章免费，其余 VIP 付费 |

**免费全书合法可读：4 本**（大奉打更人、我真没想重生啊—起点免费模式；十日终焉、斩神—番茄免费+广告模式），合计约 1440 万字零成本。
**付费即可得完整合法文本：10 本**（4 本全球多平台 + Housemaid Amazon 独占 + 5 本中文出版以微信读书为主渠道）。
**电子书广覆盖最佳：长安的荔枝**（微信读书 + 豆瓣阅读 + QQ阅读三平台）。

---

## 逐本明细

### 1. It Ends with Us — Colleen Hoover（GLOBAL）

- **current_source_status**: PARTIAL_SOURCE
- **current_files**: `01_reference/global/it-ends-with-us/official_excerpt_simon_schuster.txt`（37,372 字节）
- **current_coverage**: 官方试读，Chapter 1 全章（屋顶场景）
- **legal_full_text_available**: YES——付费购买或 KU 订阅
- **publisher**: Atria Books（Simon & Schuster），2016，376 页
- **official_platforms**: Simon & Schuster 官网（已有官方试读）
- **ebook_platforms**: Amazon Kindle（KU 有，"Read for Free" 已验证；购买约 $11.99）/ Kobo US（EPUB）/ Google Play / Apple Books——四大平台全有
- **downloadable_format**: EPUB（Kobo/Google/Apple）、AZW/KFX（Kindle）
- **drm_status_if_known**: Kindle KFX DRM；Kobo EPUB 带 Adobe DRM（除非 DRM-free 标记）；Apple FairPlay
- **local_file_readability**: 需购买后解 DRM 或用无 DRM 渠道；有声书朗读者 Olivia Song
- **recommended_acquisition_method**: 用户开通 Kindle Unlimited（月费最低覆盖多本目标书）或购买后提供 EPUB 副本
- **estimated_priority**: **P1**——已有 PARTIAL 分析基础，FULL_SOURCE 到位后可直接进入全书分析，边际成本最低
- **notes**: 续作 It Starts with Us 同在 KU。核验来源：amazon.com/dp/B0176M3U10 + Kobo Wayback 2025-10 存档 + iTunes Search API

### 2. The Midnight Library — Matt Haig（GLOBAL）

- **current_source_status**: PARTIAL_SOURCE（深度受限）
- **current_files**: `douban_trial_opening.txt`（2,385 字节，中文试读）+ `toc_and_metadata.md`（完整目录）
- **current_coverage**: 引言 + 第 1 章开头约 1.5 页 + 全书 72 条目录
- **legal_full_text_available**: YES——付费购买（无 KU，PRH 不入 KU 已验证）
- **publisher**: Canongate（英）/ Viking（美），2020，288 页
- **official_platforms**: Canongate/PRH 官网；豆瓣阅读官方中文试读
- **ebook_platforms**: Kindle（约 $10.99）/ Kobo / Google Play / Apple Books
- **downloadable_format**: EPUB / AZW
- **drm_status_if_known**: 同业标准 DRM
- **local_file_readability**: 需购买
- **recommended_acquisition_method**: 用户购买英文 EPUB（分析以英文原文为准，避免译文折损——现有试读为中文译文，文风维度已降级）
- **estimated_priority**: P2——无 KU、试读极浅、研究优先级让位于更快可得书目
- **notes**: 有声书 Carey Mulligan 朗读。来源：amazon.com/dp/B085BVSXS9 + Kobo Wayback 存档

### 3. Lessons in Chemistry — Bonnie Garmus（GLOBAL）

- **current_source_status**: PARTIAL_SOURCE
- **current_files**: `official_extract_penguin_au.txt`（11,642 字节）
- **current_coverage**: 第 1 章中段（午餐盒场景）至第 2 章末
- **legal_full_text_available**: YES——付费购买（无 KU 已验证）
- **publisher**: Doubleday（Penguin Random House US），2022
- **official_platforms**: Penguin 官网系试读（已有）
- **ebook_platforms**: Kindle（约 $13.99，Sold by Random House LLC）/ Kobo / Google Play / Apple Books
- **downloadable_format**: EPUB / AZW
- **drm_status_if_known**: 同业标准 DRM
- **local_file_readability**: 需购买
- **recommended_acquisition_method**: 用户购买英文 EPUB
- **estimated_priority**: P2
- **notes**: 有声书 Miranda Raison。页数：Wikipedia 信息框 560 页（零售常见约 390 页，UNVERIFIED）。来源：amazon.com/dp/B098PW8NP8 等

### 4. Fourth Wing — Rebecca Yarros（GLOBAL）

- **current_source_status**: PARTIAL_SOURCE
- **current_files**: `official_peek_inside_entangled.txt`（46,440 字节）
- **current_coverage**: 官方 Peek Inside，约前 2 章
- **legal_full_text_available**: YES——KU 订阅（"Read for Free" 已验证）或购买 $14.99
- **publisher**: Red Tower Books（Entangled Publishing），2023，512 页
- **official_platforms**: Entangled 官网（已有官方试读）
- **ebook_platforms**: Kindle（KU 有）/ Kobo / Google Play / Apple Books
- **downloadable_format**: EPUB / AZW
- **drm_status_if_known**: 同业标准 DRM
- **local_file_readability**: 需 KU 订阅或购买
- **recommended_acquisition_method**: KU 订阅（与 IEWU、Housemaid 一号覆盖三本）
- **estimated_priority**: **P1**——KU 覆盖 + 现象级新类型（romantasy）样本，类型代表性强
- **notes**: 有声书 Rebecca Soler & Teddy Hamilton；Empyrean 系列第 1 卷。来源：amazon.com/dp/B0BGDM197Q + Kobo Wayback 2026-07 存档

### 5. The Housemaid — Freida McFadden（GLOBAL）

- **current_source_status**: METADATA_ONLY
- **current_files**: `metadata.md`（Bookouture 官方文案）
- **current_coverage**: 无正文
- **legal_full_text_available**: YES——但**英文电子书仅 Amazon 渠道**（Google Play US 仅有声书与译本，Apple Books US/UK 均未检出官方英文电子书——已逐一验证）
- **publisher**: Bookouture（电子书，Hachette UK 旗下）；平装 Grand Central Publishing
- **official_platforms**: Bookouture 官网（无试读，已验证）；微信读书中文版《女仆》需登录
- **ebook_platforms**: Amazon Kindle（KU 有，$5.99 或 KU）；Kobo UNVERIFIED（Cloudflare 拦截且无存档产品页）
- **downloadable_format**: AZW/KFX（Kindle）
- **drm_status_if_known**: Kindle DRM
- **local_file_readability**: 需 KU 订阅或 Kindle 购买
- **recommended_acquisition_method**: KU 订阅
- **estimated_priority**: P2——获取渠道最窄的英文书；平装页数 UNVERIFIED
- **notes**: 2025 电影改编（Sydney Sweeney）。来源：amazon.com/dp/B09TWSRMCB + play.google.com + iTunes Search API 核验

### 6. 《人生海海》麦家（CHINA_PRINT）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **current_coverage**: 无
- **legal_full_text_available**: YES——微信读书付费（标价 33 书币档，可购买/会员）
- **publisher**: 北京十月文艺出版社
- **official_platforms**: 出版社纸质书
- **ebook_platforms**: 微信读书（上架，评分 874/1000，约 11 万人评价）；豆瓣阅读**未检出**；QQ阅读**未检出**（麦家其他作品在架，本书无）；掌阅 UNVERIFIED
- **downloadable_format**: 无标准下载格式（微信读书为 App 内阅读）
- **drm_status_if_known**: 微信读书无导出（平台 DRM）
- **local_file_readability**: 需用户在微信读书购买后提供合法副本，或提供纸质书 OCR/自录文本
- **recommended_acquisition_method**: 用户微信读书购买 + 提供文本副本；或购纸质书
- **estimated_priority**: P2
- **notes**: 平台覆盖单一。来源：weread.qq.com 搜索 API + douban read + QQ阅读三重核验（2026-09-13）

### 7. 《文城》余华（CHINA_PRINT）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **legal_full_text_available**: YES——微信读书付费（标价 39.5）
- **publisher**: 北京十月文艺出版社（北京出版集团）
- **ebook_platforms**: 微信读书（上架）；豆瓣阅读**未检出**（余华其他作品在架）；QQ阅读**未检出**；掌阅 UNVERIFIED
- **downloadable_format**: 无标准下载格式
- **drm_status_if_known**: 微信读书平台 DRM
- **local_file_readability**: 同上
- **recommended_acquisition_method**: 用户微信读书购买 + 提供文本副本
- **estimated_priority**: P2
- **notes**: 授权分散（余华作品分散于多平台，本书单册仅微信读书检出）

### 8. 《长安的荔枝》马伯庸（CHINA_PRINT）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **current_coverage**: 无
- **legal_full_text_available**: YES——**三平台上架**，覆盖全 15 本最佳
- **publisher**: 湖南文艺出版社（博集天卷）
- **ebook_platforms**: 微信读书（标价 21.6）+ 豆瓣阅读（ebook/421999317，会员可读）+ QQ阅读（影视原著版）
- **downloadable_format**: 无标准下载格式（平台阅读制）
- **drm_status_if_known**: 各平台 DRM
- **local_file_readability**: 需购买后提供副本
- **recommended_acquisition_method**: **首选购买对象**：约 7 万字 = 15 本中体量最小的完整长篇；用户购任一平台电子书并提供文本副本，即可成为项目第一本 FULL_SOURCE
- **estimated_priority**: **P0**——字数少（分析成本最低）+ 三渠道可得 + 马伯庸"历史可能性小说"机制密度高 + 影视化验证过的商业叙事。最适合流水线第一次全书实测
- **notes**: 体量据豆瓣阅读书评"短短七万字"。来源：weread + read.douban.com/ebook/421999317 + book.qq.com

### 9. 《额尔古纳河右岸》迟子建（CHINA_PRINT）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **legal_full_text_available**: YES——微信读书上架且搜索接口显示 **price=0**（免费或会员畅读；精确机制 UNVERIFIED）
- **publisher**: 人民文学出版社（茅盾文学奖获奖作品全集版）
- **ebook_platforms**: 微信读书；豆瓣阅读**未检出**；QQ阅读**未检出**（"迟子建"零结果）；掌阅 UNVERIFIED
- **recommended_acquisition_method**: 若微信读书确为免费/会员畅读，获取成本趋近于零——建议优先实测确认
- **estimated_priority**: P2（若 price=0 属实则可升 P1）
- **notes**: 茅奖作品。来源：weread 搜索 API bookId 3004054407

### 10. 《繁花》金宇澄（CHINA_PRINT）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **legal_full_text_available**: YES——微信读书（标价 30.7）+ 豆瓣阅读（￥14.90，会员免费读）
- **publisher**: 上海文艺出版社
- **ebook_platforms**: 微信读书 + 豆瓣阅读（另含经典插图版）；QQ阅读**未检出**；掌阅 UNVERIFIED
- **word_count**: 约 19.6 万字（豆瓣阅读版标注"约 196,000 字"）
- **recommended_acquisition_method**: 豆瓣阅读购买（￥14.90，15 本中文书中标价最低）
- **estimated_priority**: P2
- **notes**: 茅奖作品，剧版带动插图版上架。方言文体的文风分析价值高但迁移价值有限（王导剧版已验证改编路径）

### 11. 《我真没想重生啊》柳岸花又明（CHINA_WEB）

- **current_source_status**: MISSING_SOURCE
- **current_files**: 无
- **legal_full_text_available**: YES——**起点全书 1101 章免费**（起点免费阅读模式，目录逐章"免费"标记已验证）
- **publisher / 首发**: 起点中文网（book ID 1015648531）
- **ebook_platforms**: 起点 + 微信读书（付费条目）+ 书旗/阿里文学 + 红袖读书——多平台分发，非独家
- **word_count**: **313.07 万字，1101 章**，完本（2021-12-03）
- **downloadable_format**: 网页/App 在线阅读；起点网页版可逐章访问
- **drm_status_if_known**: 网页端无文件级 DRM，但平台条款不允许批量抓取
- **local_file_readability**: 按 WORKFLOW 网文研究只需前 30–50 章 + 关键卷抽样 + 结局，起点网页版即可覆盖
- **recommended_acquisition_method**: 起点网页版官方免费阅读，按 WORKFLOW 抽样范围做研究性摘录（`00_source_index.md` 如实登记覆盖范围）
- **estimated_priority**: **P0**——零成本 + 都市重生日常流代表 + 已完本
- **notes**: 主角陈汉升/萧容鱼；起点男生月票榜历史 No.197。来源：book.qidian.com/info/1015648531 + m.qidian.com 目录页

### 12. 《大奉打更人》卖报小郎君（CHINA_WEB）

- **current_source_status**: MISSING_SOURCE
- **legal_full_text_available**: YES——**起点全书 952 章免费**（已验证）
- **publisher / 首发**: 起点中文网（book ID 1019664125，首章 2020-03-14）
- **ebook_platforms**: 起点 + QQ阅读（29664125）+ 微信读书——阅文系内分发；番茄**未检出**
- **word_count**: **380.1 万字，952 章**，完本（2022-01-05；起点官方口径，网传更高数字含番外口径不一）
- **recommended_acquisition_method**: 同上——起点免费阅读 + 抽样研究
- **estimated_priority**: P1——免费可得但体量大；玄幻探案流代表；影视/出版多形态开发验证过的 IP
- **notes**: 完本卷名：京察风云/国士无双/楚江暝宿/逐鹿中原/绝世武神。来源：m.qidian.com/book/1019664125/catalog/

### 13. 《我在精神病院学斩神》三九音域（CHINA_WEB）

- **current_source_status**: MISSING_SOURCE
- **legal_full_text_available**: YES——**番茄小说网页版全书免费**（免费+广告模式，"完整版在线免费阅读"已验证）
- **publisher / 首发**: 番茄小说（page ID 6982529841564224526）
- **ebook_platforms**: 番茄 + 微信读书授权条目（price=0）；起点/QQ阅读**无原著**（注意：存在大量同名仿冒书）
- **word_count**: **426.4 万字，2033 章**，已完结（2024-07-31）
- **drm_status_if_known**: 番茄网页端使用 webfont PUA 字符混淆（`99_logs/deepseek/tools/` 解码工具链已就绪，mapping.json 362 码位已建，7 个冲突待复核）
- **local_file_readability**: 网页可读；文本恢复需解码工具（已备）
- **recommended_acquisition_method**: 番茄官方免费阅读 + 既有解码管线做研究性抽样提取（工具注释已限定"仅研究抽样，不批量重建"）
- **estimated_priority**: P1——免费 + 都市超能力流代表 + 动画化验证；但 426 万字为 15 本之最
- **notes**: 主角林七夜；动画《斩神之凡尘神域》原著。来源：fanqienovel.com/page/6982529841564224526

### 14. 《十日终焉》杀虫队队员（CHINA_WEB）

- **current_source_status**: MISSING_SOURCE
- **legal_full_text_available**: YES——**番茄小说网页版全书免费**（已验证）
- **publisher / 首发**: 番茄小说（page ID 7143038691944959011）
- **ebook_platforms**: 番茄 + 微信读书（"十日终焉·囚笼"，price=0）；QQ阅读**未检出**
- **word_count**: **320.1 万字，1496 章**，已完结（2025-10-31）
- **drm_status_if_known**: 同番茄 webfont 混淆；解码工具链就绪
- **recommended_acquisition_method**: 同上——番茄免费 + 解码管线抽样
- **estimated_priority**: **P0**——免费 + **2024 番茄年度巅峰榜 TOP1 / 中国网络文学影响力榜 / 实体销量 200 万册**（15 本中商业验证最新最强）+ 无限流悬疑类型代表 + 完结不满一年
- **notes**: 来源：fanqienovel.com/page/7143038691944959011

### 15. 《都重生了谁谈恋爱啊》错哪儿了（CHINA_WEB）

- **current_source_status**: MISSING_SOURCE
- **legal_full_text_available**: 部分——起点仅**前约 104 章免费**，其余 VIP 付费章节（订阅制；与前两本起点全免费书不同，已验证）
- **publisher / 首发**: 起点中文网（book ID 1037068783）
- **ebook_platforms**: 起点 + QQ阅读 + 微信读书；番茄**未检出**
- **word_count**: **234.09 万字，774 章**，已完结（2025-09-30）
- **recommended_acquisition_method**: 前 104 免费章可支持开篇研究（恰好覆盖 WORKFLOW 的前 30–50 章开篇窗口）；全书需订阅或用户付费
- **estimated_priority**: P2——开篇研究免费可得，全书研究需付费；体量相对最小（234 万字）是加分项
- **notes**: 主角江勤；QQ阅读评分 9.2（女生网分类）。来源：m.qidian.com/book/1037068783/catalog/

---

## 获取策略总结

1. **零成本全书合法可读 4 本**（#11/12/13/14，约 1440 万字）——网文研究按 WORKFLOW 抽样制（前 30–50 章 + 关键卷 + 结局），实际处理量约 15–25 万字/本。
2. **一个 KU 账号覆盖 3 本英文**（#1/4/5）。
3. **第一本 FULL_SOURCE 出版物首选《长安的荔枝》**：7 万字、三渠道、¥21.6 以内。
4. **需要用户行动的**：全部英文书（KU/购买）与 5 本中文出版书（微信读书/豆瓣阅读购买）；网文 4 本无需用户支出。
5. UNVERIFIED 项：掌阅全部（无网页书城可核验）、Housemaid 的 Kobo 与平装页数、各英文书官方试读精确规模、《额尔古纳河右岸》微信读书 price=0 的确切机制。
