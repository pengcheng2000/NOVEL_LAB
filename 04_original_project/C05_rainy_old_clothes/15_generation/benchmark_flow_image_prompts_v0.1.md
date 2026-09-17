# 《雨天旧衣店》75 秒 AI Concept Trailer

## BENCHMARK FLOW IMAGE PROMPTS v0.1

Status: DRAFT — PRE-ASSET BENCHMARK PROMPTS

> 本文件在 Google Flow Character / Location / Prop Masters 锁定之前创建，仅作为镜头构图与生成结构草案。正式生产应在资产锁定后生成 v0.2，不应直接作为最终 Production Prompt。

- **Purpose**：Google Flow 第一轮静态关键帧／生图 Benchmark Prompt Pack
- **Scope**：仅覆盖 8 个 Benchmark Image Units；不是 Storyboard、Video Prompt、Production Unit 全量 Prompt 或模型参数文件
- **Primary Delivery Context**：9:16 / 1080×1920 Concept Trailer
- **Prompt Language**：英文主体；中文专名仅作为资产标识或后期文字说明

### Source Files

1. `13_adaptation/concept_trailer_screenplay_v1.0.md`
2. `13_adaptation/concept_trailer_shot_list_v1.1.md`
3. `14_visual_bible/concept_trailer_visual_bible_v1.0.md`
4. `14_visual_bible/asset_specs/ASSET_INDEX.md` — v1.1 / APPROVED
5. `14_visual_bible/asset_specs/CHARACTER_ASSET_SPECS.md` — v1.1 / APPROVED
6. `14_visual_bible/asset_specs/LOCATION_ASSET_SPECS.md` — v1.1 / APPROVED
7. `14_visual_bible/asset_specs/PROP_COSTUME_ASSET_SPECS.md` — v1.1 / APPROVED

事实与执行优先级：

`Final Text > 正式人物档案 / World Bible > APPROVED Screenplay > APPROVED Shot List > APPROVED Asset Specs 内的 Canon / Director / Production 分层`

本文件只把冻结规格组装成测试用静态图 Prompt，不向上游文件增加 Canon。Prompt 中精确骨相、尺寸、色阶、服装微观结构与空间几何均继承 Asset Specs 的 `DIRECTOR VISUAL DECISION — Trailer Lock`；它们只约束当前 Concept Trailer。

---

## 1. Global Prompting Rules

### 1.1 Unified Visual Language

- 整体风格固定为：**realistic Chinese urban drama, restrained magical realism, light mystery**。
- 每张图应像真实剧情片的电影静帧：真实中国城市生活空间、真实成年人、真实皮肤、真实布料重量、真实湿度或寒冷空气。
- “魔幻现实”只通过不合常理但物理可信的环境、衣料、温度和人物反应成立；静态图中不出现可视化魔法机制。
- 现实时空为 2025 年 6 月栖州市回潮里梅雨季：冷青灰、低饱和、湿石板、返潮墙面、苍白日光灯与极少量旧暖光。
- 1988 时空仍是江南城市栖州市回潮里，只发生了罕见冬夜风雪；它不是北方工业城，也不是水乡古镇。

### 1.2 Human Representation

- 所有人物必须是具有真实骨相和皮肤纹理的中国成年人。
- 保留毛孔、细纹、肤色不均、眼下疲惫、劳动痕迹和自然左右不对称。
- 禁止网红脸、韩式偶像妆、幼态大眼、V 型尖下巴、医美窄鼻、玻璃唇、假睫毛、明显眼线、瓷白磨皮与 doll-like CGI skin。
- 谢念和唐荔必须执行各自独立骨相体系；不得因同为年轻中国女性而生成同一张脸。

### 1.3 Material and Environment

- 粗花呢必须显示灰黑白纱线交织、粗颗粒、湿后沉坠和年代磨损。
- 劳保工装必须显示偏黄灰白的粗斜纹、毛边、暗黑氧化拉链和本色蚕丝暗针。
- 梅雨通过水膜、布料重量、玻璃水迹、返潮墙和发丝细微毛躁表现，不使用室内雾。
- 风雪通过残雪、碎煤渣、细硬雪粒、白汽和人物寒冷体态表现，不使用梦境柔焦。

### 1.4 Text Handling

以下中文文字不要求 Flow 正确渲染，必须预留干净承载面，最终建议后期覆盖：

- “寄雨行”
- 门牌“47”
- “承衣簿”
- “存押”
- “孙正”
- 1988 火车票票面文字
- 片名与辅助文案

生成图中若出现乱码，不得视为资产设计；Benchmark 评估重点是承载面的材质、透视、光线与可追踪性。

### 1.5 Global Avoid

- no magic particles
- no glowing clothes
- no blue spiritual energy
- no floating runes
- no ghosts or translucent spirits
- no horror-movie green lighting
- no cyberpunk neon
- no excessive teal-and-orange grading
- no tourist old-town postcard look
- no costume-drama styling
- no Republican-era fashion styling
- no trendy vintage boutique
- no luxury fashion editorial
- no studio beauty lighting
- no plastic CGI skin
- no random extra props that alter the locked location identity

### 1.6 Composition Rule

所有 Prompt 均要求：`vertical composition suitable for a 9:16 crop`。本轮以主体身份、构图关系、材质和连续性正确为先；不要求模型生成片名、字幕、运镜或动画过程。

---

## 2. Benchmark Unit Prompts

---

## BENCH-001

### Unit ID

`BENCH-001`

### Source Mapping

- **Shot ID**：SHOT 001 / 00:00–00:04
- **Source Screenplay Section**：`00:00–00:15｜现实：一件不肯沉默的旧衣`
- **Source Shot List Section**：`SHOT 001 — 第一眼建立《雨天旧衣店》的世界`
- **Asset Dependencies**：
  - Location：`LOC-HCL-2025-EXT-001`
  - Prop：`PROP-GUTTER-001`
  - Character / Costume：无

### Narrative Purpose

用第一帧建立真实、潮湿、经营维艰的回潮里与寄雨行，并把卷帘门和旧铜檐槽作为 IP 的空间识别。

### Must Include

- 2025 年 6 月梅雨黄昏的栖州市回潮里
- 回潮里 47 号寄雨行窄面宽两层砖木混合门面
- 生锈横纹铁皮卷帘门半开，内侧普通玻璃店面
- 褪色风化木招牌，留出“寄雨行”后期覆盖面
- 1960 年代旧铜檐槽：深褐氧化为主、局部暗绿铜锈、一侧接老金属立管
- 湿黑青石板与水泥嵌缝路面、灰绿返潮墙、少量真实市井设施
- 店内苍白日光灯与很弱的旧暖光

### Prompt

```text
A cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, set at rainy dusk in June 2025 in Huichao Lane, an aging mixed residential-and-commercial street in the fictional southern Chinese provincial capital of Qizhou. Show the narrow two-story brick-and-timber storefront of Jiyu Hang at number 47 as an ordinary, weather-worn local old-clothes shop, not a picturesque heritage attraction. The facade is about four meters wide, with patched gray-white plaster, small areas of dark red brick showing through, an old upper wooden window with a plain security grille, black utility wires, and a faded dark wooden signboard above the entrance; keep the signboard surface clean and visually readable for later replacement of the Chinese shop name.

The main entrance is a half-raised horizontal corrugated iron rolling shutter with rust along the lower edge, worn guide rails, small dents, and a shallow threshold worn by decades of shoes. Behind it is an ordinary glass storefront. Under the old tiled eave runs a shallow open copper rain gutter from the 1960s, mostly dark brown oxidized copper with irregular muted green patina around joints and brackets, connected to an old metal downpipe at one side. Fine plum rain beads along the gutter rather than pouring heavily.

Use a vertical medium-wide establishing composition suitable for a 9:16 crop, looking down a narrow lived-in lane with wet black-gray stone slabs and cement joints in the foreground. The uneven water film carries dim reflections, tire marks, shoe marks, and a little dirty water in the seams. Include only restrained everyday street details such as one old electric scooter, a plain plastic stool, a small air-conditioner unit, or a bundled cable, never enough to block the storefront. Cold cyan-gray overcast dusk is the dominant light; inside the shop, a pale fluorescent light and one very weak tungsten-colored work light create a small human presence without making the shop cozy. Realistic moisture, realistic metal and masonry wear, subtle film grain, quiet suspense, no visible supernatural effect, no people, no typography rendered as a final design.
```

### Negative Prompt / Avoid

- no tourist old town
- no water-town postcard
- no white-wall-and-black-tile scenic village
- no lantern street
- no trendy vintage store
- no coffee shop
- no luxury boutique
- no magical shop
- no horror house
- no neon or cyberpunk lighting
- no polished new facade
- no empty film-set street
- no ornate Chinese architecture
- no modern glass curtain wall
- no heavy fog
- no fantasy glow
- no readable AI-generated Chinese signage

### Continuity Notes

- 门面几何、木牌位置、卷帘门、铜槽和立管位置必须可作为 SHOT 018 夜景版本的同一 Location Master。
- 现实入口只能是铁皮卷帘门，不能出现 1988 黑漆木门。
- 铜槽本体是铜，不得生成为 PVC 或镀锌铁。

### Text Handling Notes

木牌上的“寄雨行”和门牌“47”不依赖模型正确生成；保留干净、透视正确、受光合理的文字承载面，后期覆盖。

### Evaluation Focus

- 是否第一眼像真实中国南方老城生活街区，而非古镇景区
- 卷帘门、木牌、铜檐槽和立管的建筑稳定性
- 梅雨湿度、石板水膜和金属氧化是否物理可信
- 店内冷白与极少暖光是否克制
- 9:16 裁切后门面与铜槽是否仍完整可读

---

## BENCH-003

### Unit ID

`BENCH-003`

### Source Mapping

- **Shot ID**：SHOT 003 / 00:08–00:12
- **Source Screenplay Section**：`00:00–00:15｜现实：一件不肯沉默的旧衣`
- **Source Shot List Section**：`SHOT 003 — 第一次建立谢念与委托问题`
- **Asset Dependencies**：
  - Characters：`CHAR-XN-001`, `CHAR-ZWM-001`
  - Location：`LOC-JYX-2025-FRONT-001`
  - Costumes：`COST-XN-BASE-001`, `COST-XN-CARDIGAN-001`, `COST-ZWM-WORK-001`, `COST-ZG-COAT-001`
  - Prop：`PROP-GLOVES-XN-001`

### Narrative Purpose

在同一张静帧中建立谢念的专业观察力、赵为民的疲惫委屈，以及灰呢大衣隐藏针脚所承载的问题。

### Must Include

- 谢念 Costume A：黑色羊毛细针织开衫仍穿在身上，内搭灰蓝棉衫
- 谢念完整 Identity Lock 与白色薄棉线手套
- 谢念翻开灰呢大衣下摆，指腹停在隐蔽人字暗针附近
- 赵为民在柜台另一侧，48 岁、疲惫、普通维修劳动者，不帅化
- 同一件 2025 状态灰色粗花呢大衣
- 寄雨行狭长前店、旧木柜台、纸箱、衣架、冷白日光灯与梅雨窗光

### Prompt

```text
A cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, inside Jiyu Hang, a cramped working old-clothes shop in a humid southern Chinese lane in June 2025. Use a vertical composition suitable for a 9:16 crop, framed as an intimate medium close shot across the worn wooden counter. In the foreground, Xie Nian is inspecting the lower hem of a heavy gray rough-tweed coat; across the counter, Zhao Weimin remains clearly present in the same frame, slightly softer but still recognizable, watching her with exhausted tension.

Xie Nian is a 27-year-old Chinese woman, 165 cm and slim, with a narrow natural long-oval face, a medium-height forehead, lightly high cheekbones without sharp projection, a gently narrowing adult jaw, and a medium narrow rounded chin rather than a pointed V-line. Her eyes are medium-small, horizontally long almond eyes with low narrow natural double-eyelid folds, dark brown irises, no enlarged pupils, and faint blue-gray fatigue beneath them. She has natural straight black eyebrows, a low-to-medium straight nasal bridge with a small-to-medium rounded slightly downward nose tip, medium-width natural nostrils, a moderately wide mouth with a thin upper lip and a medium lower lip, muted gray-pink lip color, visible pores, subtle skin-tone variation, and no makeup styling. Her straight natural-black hair ends around the jaw, parted loosely 6:4 and tucked behind the right ear, with a few humidity-softened flyaways. She wears Costume A: a soft-black, fine-knit, repeatedly washed pure-wool round-neck cardigan with small matte black buttons over a low-saturation gray-blue cotton crew-neck top. Her posture is straight but slightly inward at the shoulders, focused and guarded.

Her hands wear ordinary thin white cotton inspection gloves with fine knit texture. One gloved hand lifts the brittle rayon lining at the coat hem while the other steadies the cloth; her fingertip has just stopped over two extremely fine hidden herringbone hand stitches inside the fold. The coat is a heavy 1980s men's straight-cut double-breasted gray mixed-fleck rough tweed with broad lapels, thick shoulder pads, a locked 3-by-2 six-button arrangement, worn pale collar and cuffs, and a cold, weighty drape. The stitch is subtle and functional, not decorative.

Zhao Weimin is an ordinary Chinese male electric-scooter repair worker around 48, about 170 cm, slightly stooped and leaning forward. He has a broad blunt rectangular face, small narrow tired eyes with heavy bags and realistic red veins, a broad round nose, thin dry lips, rough uneven warm-brown and sallow skin, deep nasolabial folds, short dark stubble, and coarse short black hair with a small amount of gray. His faded dark gray-blue zip-front work jacket and dark heavy work trousers carry only localized oil and wear. His broad hands have large knuckles and black machine-oil residue in the nail grooves. His expression combines suppressed resentment, shame, and four years of caregiving exhaustion; he is not threatening, handsome, heroic, or elderly.

The shop around them is narrow and workmanlike: cold gray-white damp walls, a long old wooden counter with worn edges, three taped cardboard boxes, an iron garment rack, old clothes, a dark heavy curtain at the rear, pale overhead fluorescent light, and cyan-gray rainy daylight from the glass storefront. Keep the visual hierarchy on the gloved hand, hidden stitch, Xie Nian's precise face, then Zhao's exhausted face. Real skin, real textile fibers, subtle film grain, restrained emotion, no visible supernatural effect.
```

### Negative Prompt / Avoid

- no influencer beauty face
- no oversized eyes
- no V-shaped chin
- no porcelain skin
- no glass lips
- no eye makeup or false eyelashes
- no long hair on Xie Nian
- no Tang Li-style square-round face on Xie Nian
- no handsome heroic Zhao Weimin
- no elderly Zhao Weimin
- no clean model hands on Zhao Weimin
- no latex gloves
- no fashionable oversized coat
- no decorative embroidery
- no trendy vintage boutique
- no cozy cafe lighting
- no magic glow
- no horror styling

### Continuity Notes

- 谢念必须保持 Costume A；黑开衫尚未押下。
- 谢念脸型必须是窄长自然椭圆，不能漂移成唐荔的方圆短椭圆脸。
- 赵为民保持宽长方钝脸、微驼体态、维修工手和深灰蓝旧劳保外套。
- 灰呢大衣必须沿用跨 1988/2025 的同一六扣几何母版；本帧为 2025 磨损状态。

### Text Handling Notes

本帧无需依赖关键中文。若背景意外出现店牌、标签或账本文字，均不得视为最终文字资产，后期统一覆盖或清除。

### Evaluation Focus

- 谢念与赵为民是否同时成立且互不抢脸
- 谢念骨相、短发、真实皮肤和白棉线手套是否稳定
- 赵为民是否普通、疲惫、劳动化而非英雄化或老年化
- 粗花呢、人造丝里衬和隐蔽暗针是否具有真实微观材质
- 店铺是否仍是经营中的旧衣工作空间，而非精品古着店

---

## BENCH-009A

### Unit ID

`BENCH-009A`

### Source Mapping

- **Shot ID**：SHOT 009A（SHOT 009 现实段拆分）/ parent time 00:30–00:34
- **Source Screenplay Section**：`00:30–00:52｜记忆：1988 年没有说完的选择` 的现实入口
- **Source Shot List Section**：`SHOT 009 — 现实穿衣 → 风雪 Match Cut`，现实 Production Unit
- **Parent Shot Asset Dependencies**：`CHAR-XN-001`, `LOC-JYX-FIT-001`, `LOC-HCL-1988-EXT-001`, `COST-XN-BASE-001`, `COST-ZG-COAT-001`, `PROP-GLOVES-XN-001`, `PROP-GUTTER-001`
- **Active In-frame Assets**：`CHAR-XN-001`, `LOC-JYX-FIT-001`, `COST-XN-BASE-001`, `COST-ZG-COAT-001`, `PROP-GLOVES-XN-001`

### Narrative Purpose

建立现实端的穿衣瞬间，并为下一张 1988 风雪画面预留可精确匹配的灰呢衣领、纹理方向和画面遮挡关系。

### Must Include

- 不足一平方米的试衣间与带水银斑但未破裂的老穿衣镜
- 谢念 Costume B：黑开衫已留在柜台，只穿固定灰蓝棉质内搭
- 谢念正在套上同一件灰色粗花呢大衣，宽大衣领靠近下颌与镜头
- 白色棉线手套
- 近景／镜中近景、冷暖混合低照度、梅雨现实感
- 衣料在画面一侧或前景占据明确面积，为 009B Match Cut 提供轮廓

### Prompt

```text
A cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, the real-world side of a planned match cut. Inside an extremely narrow fitting cubicle of an old clothes shop in rainy June 2025, frame Xie Nian at close range in front of a tarnished old full-length mirror. The cubicle is less than one square meter, about 0.85 by 1.05 meters, with a dark coarse cotton curtain at the entrance, damp gray-white plaster, a dark brick base, an old cement floor, a blackened plain wooden mirror frame, and irregular silvering loss only around the mirror edges; the mirror is scratched but not cracked. Cold fluorescent spill leaks through the curtain while a weak old wall lamp adds a small, realistic warm tone. The space feels humid and physically cramped, not supernatural.

Xie Nian is a 27-year-old Chinese woman, 165 cm and slim, with a narrow natural long-oval face, lightly high cheekbones, a gently narrowing adult jaw, and a medium narrow rounded chin. She has medium-small horizontal almond eyes with low narrow natural double-eyelid folds, dark brown irises, faint blue-gray fatigue and shallow tear troughs, natural straight black brows, a low-to-medium straight nasal bridge with a rounded slightly downward tip, a thin upper lip and medium lower lip in muted gray-pink, visible pores and subtle skin-tone variation. Her natural-black straight hair ends at the jaw, loosely parted 6:4 and tucked behind the right ear, with a few humidity-softened flyaways. No beauty makeup.

She is in Costume B: the black cardigan has already been removed and must not be on her body. Beneath the borrowed coat she wears the same low-saturation gray-blue cotton crew-neck top; only the upper part is visible. Thin white cotton inspection gloves cover her hands. She is halfway into the same heavy gray mixed-fleck rough-tweed coat used throughout the film, a 1980s men's straight-cut double-breasted garment with broad lapels, thick shoulder pads, two columns of three matte dark buttons, and a heavy cold drape. One sleeve is already on and the broad rough-tweed collar is rising against her lower jaw.

Compose a tight mirror-assisted close-up suitable for a vertical 9:16 crop. Keep Xie Nian's real face and focused reflection readable in the center-left while a large diagonal plane of gray flecked tweed passes very close to the lens along the right side and lower foreground. The coat edge and weave direction must form a strong, simple silhouette that can be matched in BENCH-009B. Her mouth is closed, her gaze concentrated and guarded; the moment is the breath before an impossible transition, but the image itself contains no glow, no distortion, no dream effect, and no visual magic. Real textile weight, real humid skin, subtle film grain, restrained suspense.
```

### Negative Prompt / Avoid

- no black cardigan on Xie Nian
- no long hair
- no influencer beauty
- no oversized eyes
- no pointed V chin
- no porcelain skin
- no fashion makeup
- no modern fitting room
- no LED mirror
- no cracked mirror
- no ghost reflection
- no blood writing
- no green horror light
- no magical portal
- no glowing coat
- no energy particles
- no wide spacious room
- no fashion editorial pose

### Continuity Notes

- 本帧的衣领边线、雪花粗花呢织纹方向、前景遮挡面积和画面侧位必须与 BENCH-009B 对应。
- 灰呢大衣为 2025 状态：领袖磨白、里衬较老；但外部几何、扣位、领型必须与 1988 状态一致。
- 黑开衫不得回到谢念身上；若手入画，必须为谢念白棉线手套。

### Text Handling Notes

本帧无关键中文文字。镜面或背景不得生成可读的随机店铺文字。

### Evaluation Focus

- 谢念 Identity Lock 与 Costume B 是否准确
- 试衣间是否真正逼仄、旧而现实，镜面是否水银斑但不破裂
- 灰呢大衣领口、纹理、厚重感与画面遮挡是否适合 Match Cut
- 静帧是否有“转场前一刻”的张力而没有可视化魔法

---

## BENCH-009B

### Unit ID

`BENCH-009B`

### Source Mapping

- **Shot ID**：SHOT 009B（SHOT 009 的 1988 端拆分）/ parent time 00:30–00:34
- **Source Screenplay Section**：`00:30–00:52｜记忆：1988 年没有说完的选择` 的风雪入口
- **Source Shot List Section**：`SHOT 009 — 现实穿衣 → 风雪 Match Cut`，1988 Production Unit
- **Parent Shot Registry**：SHOT 009 锁定同一灰呢大衣与现实／1988 两端空间
- **Unit-specific Asset Dependencies**：`CHAR-ZG-1988-001`, `LOC-HCL-1988-EXT-001`, `COST-ZG-COAT-001`, `COST-ZG-BASE-1988-001`; `PROP-TICKETS-1988-001` 仅藏于右侧口袋、不要求可见

### Narrative Purpose

用与 009A 对应的灰呢纹理和轮廓，把观众从梅雨现实切入真实发生过的 1988 江南风雪夜。

### Must Include

- 与 009A 同一件、同一扣位和领型的灰色粗花呢大衣，1988 较新状态
- 周桂珍约 49 岁的侧背／半侧轮廓，不锁正脸
- 1988 栖州市回潮里罕见风雪，冷蓝灰真实过去
- 画面前景的灰呢边线和织纹方向与 009A 可匹配
- 无梦境滤镜、无魔法转换、无现代设施

### Prompt

```text
A cinematic still from a realistic Chinese historical memory presented as factual lived reality, not as a dream: winter night, 1988, in Huichao Lane in the southern Chinese city of Qizhou during an unusual heavy snowfall. This is the matching image for a cut from BENCH-009A. Use a vertical composition suitable for a 9:16 crop and preserve the same dominant gray-tweed silhouette: a broad diagonal plane of heavy gray mixed-fleck rough tweed fills the same side and foreground area, with the same weave direction, broad lapel edge, thick shoulder geometry, pocket placement, and 3-by-2 double-breasted construction as the 2025 coat. In 1988 the coat is the exact same physical garment but less worn: its gray, off-white, and sparse black fibers are slightly deeper in tone, the collar and cuffs are less abraded, and the lining is more intact. No recently added 2025 repair stitch should be visible.

The wearer is Zhou Guizhen, a Chinese woman around 49, seen only from a rear three-quarter or very limited side angle, never as a frontal beauty portrait. She is about 158 cm, narrow-framed and thin, with the oversized men's coat hanging heavily from thick shoulder pads. Her posture is hunched against the cold, shoulders raised, torso leaning forward, breath visible. Her black hair contains a modest amount of gray and is gathered simply at the low nape, with a few cold damp strands loose. Only a small portion of a dark brown-gray thin old sweater may show at the neck. Her face remains mostly hidden by the high collar, lowered head, snow, and angle. Her right hand remains buried in the coat's right pocket around two crumpled red hard-seat train tickets, but the tickets are not visible in this frame.

Behind her, reveal just enough of the 1988 Huichao Lane environment to establish the new time: a narrow southern Chinese mixed residential-and-shop street, low brick-and-timber tiled buildings, old gray plaster, dark brick, wooden lattice windows, old cast-iron drainage, black wet stone slabs with thin frozen snow and scattered black coal cinders. Cold blue-gray snow light dominates, with one dirty pale incandescent street lamp in the distance. Snow grains are small and hard, driven sideways; accumulation is uneven and modest, mixed with soot, not a northern blizzard landscape. The past must look physically real, clear, and immediate. No vignette, no sepia, no soft dream haze, no supernatural transformation effect, no modern objects.
```

### Negative Prompt / Avoid

- no frontal face portrait of Zhou Guizhen
- no elderly grandmother styling
- no headscarf or floral padded jacket
- no northern industrial city
- no mining town
- no northeastern courtyard
- no tourist water town
- no Republican-era street
- no modern rolling shutter
- no LED lights
- no air conditioner
- no electric scooter
- no PVC signage
- no dream blur
- no sepia nostalgia filter
- no glowing snow
- no magical transition
- no visible modern train ticket

### Continuity Notes

- 灰呢前景轮廓必须与 BENCH-009A 的衣领／布面遮挡严格对应；大衣是同一件，只改变年代磨损。
- 周桂珍不建立正脸资产；只用侧背、低头、发型、冻寒体态和大衣识别。
- 两张票仍藏在右侧口袋，不得提前露出票面。

### Text Handling Notes

本帧不需要可读文字。任何远处门牌或街牌保持不可读；不要虚构 1988 文字版式。

### Evaluation Focus

- 与 009A 的大衣纹理、边线和画面遮挡是否足以 Match Cut
- 是否清楚进入 1988，同时仍是同一地址的江南老街
- 周桂珍是否靠侧背、体态和衣物成立，而没有生成正脸 Hero Portrait
- 是否避免北方工业城、古镇和梦境化

---

## BENCH-010

### Unit ID

`BENCH-010`

### Source Mapping

- **Shot ID**：SHOT 010 / 00:34–00:38
- **Source Screenplay Section**：`00:30–00:52｜记忆：1988 年没有说完的选择`
- **Source Shot List Section**：`SHOT 010 — 建立 1988 记忆空间`
- **Asset Dependencies**：
  - Character：`CHAR-ZG-1988-001`
  - Location：`LOC-HCL-1988-EXT-001`
  - Costumes：`COST-ZG-COAT-001`, `COST-ZG-BASE-1988-001`
  - Prop：`PROP-TICKETS-1988-001`（藏于右侧大衣口袋）

### Narrative Purpose

完整建立 1988 回潮里风雪旧巷、周桂珍的疲惫侧背与她走向黑漆木门的秘密行动。

### Must Include

- 周桂珍侧背／侧后方，不出现完整正脸
- 同一件 1988 状态灰色粗花呢大衣
- 右手深插大衣右侧口袋，握住两张票但票不必露出
- 残雪、黑色碎煤渣、青石板、低矮砖木瓦房
- 回潮里 47 号斑驳黑漆木门与门闩体系
- 江南城市罕见雪夜，不是北方城市或水乡景区

### Prompt

```text
A cinematic still from a realistic Chinese drama, 1988 winter night in Huichao Lane, Qizhou, a southern Chinese provincial city experiencing an unusual snowstorm. Use a vertical rear three-quarter composition suitable for a 9:16 crop, as if the camera were following several paces behind and slightly to the side of Zhou Guizhen while she crosses the narrow lane toward the black-lacquered wooden door of number 47. The image is a factual past event, not a dream, vision, ghost scene, or nostalgic postcard.

Zhou Guizhen is a Chinese woman around 49, about 158 cm, thin and narrow-framed. Do not show a clear frontal face. Her black hair contains roughly a modest 15 to 20 percent gray and is simply gathered low at the nape, with a few damp loose strands. The cold forces her shoulders upward and her torso forward; her step is hurried but unsteady, with weight pressing into the rear foot as she nears the doorway. She wears the same locked hero coat from the 2025 scenes, here in its less-worn 1988 state: an oversized men's straight-cut heavy gray mixed-fleck rough-tweed overcoat with visible gray, off-white, and sparse black fibers, broad lapels, thick shoulder pads, two columns of three matte dark buttons, side pockets, and no belt. A dark brown-gray thin sweater shows only at the neck; dark cotton trousers and worn black-brown corduroy padded shoes appear below, one shoe showing a small damaged area with a little black filling. Her right hand is buried deep in the coat's right pocket, gripping exactly two crumpled red hard-seat train tickets; keep the tickets concealed or only as a subtle rigid outline, with no readable design.

The lane is about three meters wide, a mixed residential-and-shop old-city street rather than a village: black wet stone paving, frozen gray snow in the joints, scattered crushed black coal cinders, low brick-and-timber buildings, worn gray plaster, dark brick bases, tiled eaves, wooden lattice windows, and old cast-iron drainage. Ahead, number 47 is a plain, weathered black-lacquered wooden door in the same building axis as the later storefront, its paint worn matte and its threshold hollowed by use. Keep the door practical and unornamented, without brass rings or carved panels. Cold blue-gray snow light dominates; a single dirty pale incandescent street lamp farther down the lane gives weak uneven illumination. Small hard snow grains travel sideways, her breath forms white vapor, and the coat hem carries believable weight. Preserve clarity, texture, and restrained dread; subtle film grain, no sepia, no dream haze, no modern infrastructure.
```

### Negative Prompt / Avoid

- no frontal beauty portrait
- no elderly grandmother
- no headscarf
- no floral padded coat
- no northern industrial city
- no mining settlement
- no rural mud village
- no water-town tourism
- no bridges or canals
- no lanterns or archways
- no ornate black door
- no rolling shutter
- no modern aluminum windows
- no LED streetlights
- no electric scooters
- no air conditioners
- no QR codes or CCTV
- no sepia old-photo filter
- no fantasy snow or ghost effect

### Continuity Notes

- 灰呢大衣必须与 BENCH-009A/009B 共用同一六扣、翻领、口袋、长度和织纹母版。
- 周桂珍的右手必须位于右侧口袋；不得镜像为左手／左袋。
- 47 号入口在 1988 固定为黑漆木门，不得出现现实卷帘门。

### Text Handling Notes

门牌“47”建议后期覆盖；本轮只要求门牌承载面和门洞位置正确。票面文字不应出现或可读。

### Evaluation Focus

- 江南城市旧巷与罕见雪夜的历史可信度
- 周桂珍侧背体态、右手口袋动作与不锁正脸策略
- 黑漆木门、青石、残雪和煤渣是否真实且不过度年代戏化
- 大衣跨镜一致性及雪中重量表现

---

## BENCH-017A

### Unit ID

`BENCH-017A`

### Source Mapping

- **Shot ID**：SHOT 017A（SHOT 017 手部 Production Unit）/ parent time 01:04–01:10
- **Source Screenplay Section**：`01:00–01:10｜更大的秘密：店里也藏着她的过去`
- **Source Shot List Section**：`SHOT 017 — 唐荔手部 → 近景 → 谢念反应`，A 单元
- **Parent Shot Asset Dependencies**：`CHAR-TL-001`, `CHAR-XN-001`, `LOC-JYX-2025-CUT-001`, `COST-TL-WORK-001`, `COST-XN-BASE-001`, `COST-SZ-WORKWEAR-001`, `PROP-TAPE-TL-001`, `PROP-GLOVES-XN-001`, `PROP-GUTTER-001`
- **Active In-frame Assets**：`CHAR-TL-001`（hands only）, `LOC-JYX-2025-CUT-001`, `COST-SZ-WORKWEAR-001`; `COST-TL-WORK-001` 仅可在袖口边缘出现

### Narrative Purpose

用裁缝手的触觉识别把普通旧工装转化为私人悬念，并把右腰内侧暗针锁为后续人物反应的共同视觉证据。

### Must Include

- 唐荔裸手：偏宽手掌、相对短而有力的手指、短甲、分布不均老茧和少量针眼
- 绝不能戴谢念的白棉线手套
- 孙正灰工装平铺在店堂正中实木裁床的墨绿厚台布上
- 右腰内侧折边被翻开，露出约三寸本色双股蚕丝人字暗针
- 近距离材质静帧，不需要人物脸

### Prompt

```text
An extreme close-up cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, focused entirely on tactile evidence. On the dark green heavy cloth covering an old solid-wood cutting table in the center of Jiyu Hang's main shop floor, a worn early-2000s Chinese labor jacket lies flat. The jacket is ordinary and inexpensive: straight-cut men's workwear made of coarse gray cotton twill, repeatedly washed and sun-faded into uneven yellow-gray and gray-white, with visible diagonal weave, fine fraying along the lower edge, and a dark oxidized metal zipper partly visible away from the focal area. The inside of the right waist load-bearing fold has been turned open toward the camera.

At the exact center of focus is a repair about three inches long: two strands of natural-colored silk thread bite into the rough twill in a precise hand-sewn herringbone pattern. The stitch is fine, functional, slightly raised, and mostly hidden inside the fold; tiny end knots disappear into the seam. It must not look decorative, oversized, red, gold, embroidered, or supernatural.

Tang Li's bare hand has just made contact with the stitch. Show a broad working hand with relatively short, strong fingers, short unpainted nails trimmed close to the fingertips, slightly rough nail edges, uneven pale calluses at the thumb base, inner index finger, first joint of the middle finger, and outer edge of the palm, plus only a few tiny old needle-prick marks concentrated on the index and middle fingertips. The skin is a real warm medium Chinese skin tone, slightly darker on the hand and forearm, dry in places, with fine scratches and working texture. Her fingertips rest lightly on the silk thread and have paused at the instant of recognition. She wears no glove. A narrow edge of a washed olive-gray rolled work sleeve may enter the top of frame, but no face is shown.

Use shallow but controlled depth of field: the hand, twill weave, fold, and herringbone stitch must all remain readable. The dark green table cloth has small pressure marks and a few thread fibers, never clutter. The background falls into a restrained blur of the damp working shop, with cold overhead fluorescent light, gray rainy daylight, and a neutral-warm task light revealing the thread without turning it into a spotlight. Vertical composition suitable for a 9:16 crop, realistic macro texture, no visible magic, no horror, no fashion styling.
```

### Negative Prompt / Avoid

- no white cotton gloves on Tang Li
- no latex gloves
- no long manicured nails
- no nail polish
- no delicate model hands
- no excessive wounds
- no blood
- no red thread
- no gold thread
- no oversized decorative stitch
- no glowing stitch
- no magical symbols
- no modern fashion jacket
- no blue uniform
- no military jacket
- no cluttered craft table
- no face in frame
- no dramatic spotlight

### Continuity Notes

- 工装右腰暗针的位置、长度、斜纹方向、褪色分布必须与 BENCH-017B/017C 所在场景和后续 Hero Asset 一致。
- 唐荔为裸手；谢念的白手套不得错误转移到此手部。
- 裁床位于主店堂正中，不是后堂密室。

### Text Handling Notes

此构图不需要显示左胸“孙正”。若左胸区域因构图进入边缘，手写文字仍建议后期覆盖，不接受模型乱码。

### Evaluation Focus

- 唐荔手部是否有真实、克制的裁缝劳动痕迹
- 是否明确为裸手且不与谢念的手套混淆
- 灰工装粗斜纹、褪色、右腰折边和双股蚕丝暗针是否物理可信
- 是否把暗针表现为隐藏修补而非装饰或魔法标记

---

## BENCH-017B

### Unit ID

`BENCH-017B`

### Source Mapping

- **Shot ID**：SHOT 017B（SHOT 017 唐荔近景 Production Unit）/ parent time 01:04–01:10
- **Source Screenplay Section**：`01:00–01:10｜更大的秘密：店里也藏着她的过去`
- **Source Shot List Section**：`SHOT 017 — 唐荔手部 → 近景 → 谢念反应`，B 单元
- **Parent Shot Asset Dependencies**：`CHAR-TL-001`, `CHAR-XN-001`, `LOC-JYX-2025-CUT-001`, `COST-TL-WORK-001`, `COST-XN-BASE-001`, `COST-SZ-WORKWEAR-001`, `PROP-TAPE-TL-001`, `PROP-GLOVES-XN-001`, `PROP-GUTTER-001`
- **Active In-frame Assets**：`CHAR-TL-001`, `LOC-JYX-2025-CUT-001`, `COST-TL-WORK-001`, `COST-SZ-WORKWEAR-001`（soft foreground）, `PROP-TAPE-TL-001`

### Narrative Purpose

锁定唐荔从专业针法判断转为私人震动的克制微表情，并建立她与谢念完全不同的正脸身份。

### Must Include

- 唐荔完整 Facial Identity：27 岁、方圆短椭圆脸、宽圆下巴、低内双、轻微上扬外眼角、较宽短直鼻梁与圆厚鼻尖
- 深棕黑中长发低马尾／低束发
- 橄榄灰工作衬衫、袖口挽至小臂，黄色系卷尺挂颈
- 微表情：面色稍退、呼吸变浅、眼神从下方针脚抬向谢念；不尖叫、不后退
- 店堂正中裁床区域连续，灰工装可作为前景证据

### Prompt

```text
A close-up cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, inside the central cutting-table area of Jiyu Hang during a humid, storm-darkened afternoon in 2025. The frame captures Tang Li at the precise moment when professional recognition turns into a private shock. Use a vertical close composition suitable for a 9:16 crop. A soft strip of yellow-gray coarse workwear and the dark green cutting-table cloth may remain low in the foreground as evidence of what she has just touched, while Tang Li's face and upper torso are sharply readable. The old shop behind her is subdued and continuous: cold fluorescent light, damp gray wall, old wood, and the blurred silhouette of a practical sewing station, never a separate back-room mystery chamber.

Tang Li is a 27-year-old Chinese woman with a visibly different facial system from Xie Nian. Her face is medium-wide and square-round to short-oval, with a face-length-to-cheekbone-width ratio around 1.20 to 1.24, a medium-low broad forehead, full temples, rounded medium-height cheekbones, healthy cheek volume with working jaw support, a visibly wider lower jaw, and a short-to-medium broad rounded chin with a nearly horizontal lower curve. Her eyes are medium-sized and relatively flat almond eyes, slightly shorter and rounder than Xie Nian's, with very low inner-double or shallow eyelid folds and outer corners rising only two or three degrees. Her irises are deep brown, with mild work fatigue below the eyes but no beauty-style aegyo-sal. Her brows are medium-thick with natural stray hairs and a low arc. Her nose has a low-to-medium root, a medium-broad short straight bridge, a round slightly thick tip, and naturally broad wings; it must not narrow into a cosmetic small nose. Her mouth is medium-wide with a flatter cupid's bow, a medium-thin upper lip, medium lower lip, warm muted brown-rose natural color, visible fine lip lines, and no gloss. Her real warm medium skin shows pores, slight sun variation, faint under-eye brown-gray fatigue, and a touch of natural redness around the nose.

Her dark brown-black hair is medium-long, slightly coarse and naturally frizzy, gathered in a low ponytail at the back of the head with a plain dark tie. A few practical flyaways sit near the forehead and ears. She wears a washed olive-gray straight cotton work shirt with the sleeves rolled to mid-forearm over a dark oatmeal-gray crew-neck top. A worn yellow-brown measuring tape about two fingers wide hangs around her neck, its old metal end resting below the collarbone.

Her expression remains restrained: her lips are closed but no longer relaxed, one corner tightens, the jaw muscle holds, her breathing has become shallow, and the healthy warmth has slightly drained from her face. Her gaze has just risen from the stitch below frame toward Xie Nian off-camera. Do not make her scream, gasp, cover her mouth, cry theatrically, or step back. The emotional force is in the fixed eyes, tightened outer eyelids, and a small loss of color. Real adult Chinese skin, subtle film grain, grounded working-class environment, no glamor, no visible supernatural effect.
```

### Negative Prompt / Avoid

- no resemblance to Xie Nian's narrow long face
- no jaw-length short hair
- no V-shaped chin
- no narrow cosmetic nose
- no oversized eyes
- no high double eyelids
- no influencer beauty
- no porcelain skin
- no glass lips
- no fashion makeup
- no elderly seamstress
- no gray hair
- no glasses
- no qipao or traditional tailor costume
- no screaming
- no mouth-covering gesture
- no dramatic backward movement
- no fashion studio portrait
- no magical glow

### Continuity Notes

- 唐荔脸型、眼型、鼻型、发长和低马尾必须与 `CHAR-TL-001` 完全一致，不能向谢念靠拢。
- 黄色系卷尺、橄榄灰工作衬衫和挽袖高度与 SHOT 007 资产一致。
- 灰工装若出现在前景，只作为同一裁床上的软焦证据；暗针位置不得被重新设计。

### Text Handling Notes

若灰工装左胸区域进入画面，“孙正”应留作后期覆盖；卷尺刻度无需模型准确渲染。

### Evaluation Focus

- 唐荔是否具有独立、可重复的方圆短椭圆骨相
- 是否明显不同于谢念，却仍是 27 岁现代年轻改衣师
- 低马尾、黄色卷尺、工作服与真实皮肤是否稳定
- 微表情是否从职业判断转成震动，同时保持克制
- 裁床背景是否与 BENCH-017A/017C 连续

---

## BENCH-017C

### Unit ID

`BENCH-017C`

### Source Mapping

- **Shot ID**：SHOT 017C（SHOT 017 谢念反应 Production Unit）/ parent time 01:04–01:10
- **Source Screenplay Section**：`01:00–01:10｜更大的秘密：店里也藏着她的过去`
- **Source Shot List Section**：`SHOT 017 — 唐荔手部 → 近景 → 谢念反应`，C 单元
- **Parent Shot Asset Dependencies**：`CHAR-TL-001`, `CHAR-XN-001`, `LOC-JYX-2025-CUT-001`, `COST-TL-WORK-001`, `COST-XN-BASE-001`, `COST-SZ-WORKWEAR-001`, `PROP-TAPE-TL-001`, `PROP-GLOVES-XN-001`, `PROP-GUTTER-001`
- **Active In-frame Assets**：`CHAR-XN-001`, `LOC-JYX-2025-CUT-001`, `COST-XN-BASE-001`; `COST-SZ-WORKWEAR-001` 可作为软焦前景；`PROP-GLOVES-XN-001` 仅在手进入画面时必须保持

### Narrative Purpose

以谢念第一次明显但仍克制的表情裂缝，把“别人的秘密”反转为她本人失落过去的核心悬念。

### Must Include

- 谢念完整 Identity Lock：窄自然长椭圆脸、中小横长杏仁眼、低位窄双、圆钝鼻尖、淡薄唇、下颌短发夹耳后
- Costume B：只穿低饱和灰蓝棉质内搭，黑开衫绝不回身
- 表情裂缝：眼神焦点停住、上眼睑收紧、下颌短暂僵住、嘴仍闭合
- 裁床区域与 BENCH-017A/017B 连续；灰工装可作为前景或背景证据
- 不使用夸张震惊、哭泣、后退或恐怖光效

### Prompt

```text
A reaction close-up cinematic still from a realistic Chinese urban drama with restrained magical realism and light mystery, in the same central cutting-table area of Jiyu Hang in 2025. Use a vertical composition suitable for a 9:16 crop. Xie Nian is the sharp focal subject, framed from upper chest to head in a restrained reverse angle from Tang Li's position. The yellow-gray work jacket on the dark green cutting-table cloth may form a soft, low foreground edge or a blurred shape behind her, enough to maintain the evidence and spatial continuity without competing with her face. The old shop remains physically continuous with the previous images: damp gray wall, cold fluorescent overhead light, subdued rainy daylight, old wood, and a neutral-warm task-light trace on the table. No dramatic lightning flash and no visible copper gutter inside the room.

Xie Nian is a 27-year-old Chinese woman, 165 cm and slim, with a narrow natural long-oval face, face length around 1.34 to 1.38 times the cheekbone width, a medium forehead slightly narrower than the cheekbones, lightly high but not projecting cheekbones, low cheek fat, a gently narrowing adult jaw, and a medium narrow rounded chin rather than a pointed V-line. Her left jawline is subtly fuller than the right. Her eyes are medium-small, horizontally long almond eyes with low narrow natural double-eyelid folds, nearly level outer corners with the slightest downward tendency, dark brown irises of normal size, straight lower lids, faint blue-gray under-eye fatigue and shallow tear troughs. Her brows are natural black, medium-fine and almost straight. Her nose has a low-to-medium root, a medium-narrow mostly straight bridge with natural bone variation, a small-to-medium rounded slightly downward tip, and natural medium-width wings. Her mouth is moderately wide with a thin upper lip, medium lower lip, muted gray-pink color, fine vertical lip lines, and no gloss. Her light-medium cool-neutral Chinese skin retains pores, mild uneven tone, faint nose-side redness, and real fatigue rather than porcelain smoothness.

Her straight natural-black hair ends at the jaw, loosely parted 6:4, tucked behind the right ear, with a few humidity-softened flyaways and no jewelry. She is in Costume B: only the low-saturation gray-blue cotton crew-neck long-sleeve top is visible. The black wool cardigan was left on the counter in SHOT 007 and must not return. Her posture remains upright with slightly inward shoulders.

This is the first visible crack in her control, but it is very small. Her mouth stays closed. Her lower lip has tightened, her jaw is briefly rigid, her upper eyelids draw slightly inward, and her gaze has stopped on Tang Li just off-camera as if a familiar internal map has failed. She does not widen her eyes dramatically, cry, gasp, recoil, or clutch anything. Her face remains quiet enough that the change is visible only because her baseline is so controlled. If any hand enters the frame, it must wear Xie Nian's thin white cotton inspection glove; otherwise keep hands outside the composition. Real skin, subtle film grain, low-saturation grounded color, emotional precision, no supernatural visual effect.
```

### Negative Prompt / Avoid

- no black cardigan on Xie Nian
- no Tang Li-style square-round face
- no long hair or low ponytail
- no oversized eyes
- no wide-open shocked mouth
- no crying tears
- no screaming
- no dramatic recoil
- no V-shaped chin
- no influencer beauty
- no porcelain skin
- no glass lips
- no eye makeup or false eyelashes
- no jewelry
- no fashion portrait lighting
- no lightning flash
- no gutter inside the shop
- no magic glow
- no horror effect

### Continuity Notes

- 谢念必须与 BENCH-003、BENCH-009A 共用同一脸、发型和皮肤身份；本帧只改变表情和 Costume State。
- Costume B 固定为灰蓝内搭；黑开衫已存押，绝不能重现。
- BENCH-017A/B/C 必须共享裁床、墨绿台布、灰工装色阶和同一雨前光线。
- 若手入画，谢念戴白手套；唐荔的裸手不应出现在本反打中。

### Text Handling Notes

本帧不依赖可读中文。若灰工装“孙正”区域进入背景，应保持不可读并在后期覆盖，不让乱码吸引注意。

### Evaluation Focus

- 谢念 Identity Lock 是否与前序 Benchmark 一致
- 是否准确执行 Costume B，而非把黑开衫穿回去
- 表情是否是“第一次失控的微小裂缝”而非夸张惊恐
- 与 BENCH-017A/B 的裁床、光线和灰工装连续性
- 是否仍保持真实中国成年女性皮肤与克制剧情片质感

---

## 3. Benchmark Review Checklist

每张首轮输出至少按以下项目人工检查：

1. **Source adherence**：是否严格匹配对应 Asset IDs 与 Shot 目的。
2. **Identity stability**：谢念、唐荔、赵为民是否各自遵守骨相；同角色跨 Unit 是否像同一人。
3. **Cross-character separation**：谢念与唐荔是否保持窄长／方圆两套独立系统。
4. **Costume continuity**：谢念 A/B 状态、灰呢大衣跨年代状态、唐荔工作服是否正确。
5. **Material fidelity**：粗花呢、斜纹工装、蚕丝暗针、湿石板、氧化铜是否可信。
6. **Location continuity**：2025 门面／前店／试衣间／裁床与 1988 旧巷是否各自稳定。
7. **Historical integrity**：1988 是否排除现代设施、北方工业城和影视城式年代堆砌。
8. **Expression control**：人物是否用细微肌肉变化表达情绪，而非 AI 常见夸张表演。
9. **Text safety**：中文承载面是否适合后期覆盖；是否有抢眼乱码。
10. **No fantasy leakage**：是否完全没有粒子、发光、符文、鬼魂或梦境形变。
11. **Vertical usability**：9:16 裁切后，脸、手、衣料证据和场景锚点是否仍完整。
12. **Reference suitability**：输出是否足以作为后续 Storyboard / Keyframe 的候选参考，而不是只在单张上“好看”。

---

## 4. Scope Lock

- 本文件只定义上述 8 个静态 Benchmark Image Units。
- 不扩展到 SHOT 001–018 全量 Prompt。
- 不包含视频运动、镜头时长、连续动画或 Image-to-Video 指令。
- 不生成图片，不指定模型参数，不建立 Storyboard。
- 任何 Benchmark 输出均为 Look / Consistency Test；不得反向覆盖 APPROVED Asset Specs 或小说 Canon。
