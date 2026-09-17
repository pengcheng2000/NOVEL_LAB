# 《雨天旧衣店》75 秒 AI Concept Trailer

## GOOGLE FLOW ASSET GENERATION PROMPTS v0.1

Status: DRAFT — FLOW ASSET GENERATION PROMPTS

- **Purpose**：依据 APPROVED Asset Specs v1.1 生成第一批 Google Flow Character / Location / Prop Masters 候选
- **Workflow Position**：`Asset Specs v1.1 → Flow Asset Candidates → Accepted Masters → Benchmark Keyframes → Video`
- **Scope**：9 Character Master Prompts、3 Character Detail Prompts、6 Location Master Prompts、6 Hero Prop / Costume Master Prompts
- **Not Included**：图片生成结果、Storyboard、Benchmark v0.2、视频 Prompt、模型参数、完整 Production Unit Prompt

### Source Files

1. `13_adaptation/concept_trailer_shot_list_v1.1.md`
2. `14_visual_bible/concept_trailer_visual_bible_v1.0.md`
3. `14_visual_bible/asset_specs/ASSET_INDEX.md` — v1.1 / APPROVED
4. `14_visual_bible/asset_specs/CHARACTER_ASSET_SPECS.md` — v1.1 / APPROVED
5. `14_visual_bible/asset_specs/LOCATION_ASSET_SPECS.md` — v1.1 / APPROVED
6. `14_visual_bible/asset_specs/PROP_COSTUME_ASSET_SPECS.md` — v1.1 / APPROVED

本文只从正式文字 Source of Truth 抽取视觉资产身份。此前 Look Development 图片不得补充、替换或覆盖本文件中的任何身份信息。

---

## 1. Production Rules

### 1.1 Master Candidate Principle

- 每个生成单元只产出一个人物、一个场景或一个独立道具资产；不做拼版、对照表、contact sheet、turnaround sheet 或多视图合成。
- Prompt 生成的是 **MASTER CANDIDATE**。只有通过本文件 Acceptance Checklist 的单张结果，才可重命名为 `MASTER`。
- 失败结果仅属于 `LOOK_DEV`，不得进入 Benchmark Keyframe、Storyboard 或 Shot Prompt。
- 本批图像用于稳定身份和空间，不承担剧情表演、镜头运动或连续动作。

### 1.2 Character Master Rules

- FACE MASTER：单人头肩／胸像，正面或轻微 3/4，中性背景，均匀柔和自然光，无文字、无道具遮脸、无剧情表演。
- BODY / COSTUME MASTER：单人 3/4 身或全身，正常站姿，中性背景，同一 Facial Identity，完整显示发型、体型、服装色阶、版型和鞋。
- 真实中国成年人；保留毛孔、肤色不均、细纹、疲惫与劳动痕迹。禁止网红化、偶像化、磨皮、娃娃脸和商业影棚时尚感。
- 谢念与唐荔必须严格执行两套独立骨相；任何撞脸结果直接判定失败。

### 1.3 Location Master Rules

- 场景 Master 尽量无人；可有弱化的匿名远景生活痕迹，但不得出现任何核心人物或形成剧情动作。
- 目的仅是锁定空间几何、入口、门窗、柜台／裁床／镜子／布帘位置、材质、磨损、物件密度、光线、色彩和年代。
- 中文店招、门牌和标签只需正确承载面，最终统一后期覆盖。

### 1.4 Prop / Costume Master Rules

- 单件物体或一个不可拆分的道具组合，简洁中性背景，高材质可读性，无人物、无手持者、无拼版。
- 锁定比例、形态、颜色、材料、磨损和连续性锚点；不拍剧情动作。
- “孙正”“承衣簿”“存押”等中文不依赖模型直出。
- `PROP-TICKETS-1988-001` 仍处于 Historical Research Gate，本文件不为其创建 Prompt。

### 1.5 Global Visual Quality

统一采用：realistic Chinese drama, grounded material realism, neutral cinematic photography, accurate adult anatomy, real skin texture, restrained color, soft natural or practical light. 禁止魔法粒子、发光衣物、蓝色灵力、鬼片效果、古镇宣传片、古装化、民国化、赛博霓虹和过度青橙调色。

---

## 2. Character Masters

### FLOW-CHAR-XN-FACE-001

**Asset ID**：`CHAR-XN-001`
**Master Purpose**：锁定谢念正脸、骨相、皮肤、短发与中性表情。

#### Prompt

```text
Single-person neutral face identity master portrait of Xie Nian, a real 27-year-old Chinese woman. Head-and-shoulders framing, front-facing with only a very slight three-quarter turn, plain warm-gray matte background, soft even natural window light, no dramatic shadow, no story action, no props, no text, no collage. She is slim and looks 27 to 29, alert and precise with mild fatigue, not fragile and not glamorous.

Her face is a narrow natural long oval, face length about 1.34 to 1.38 times cheekbone width, medium forehead slightly narrower than the cheekbones, subtly inward temples, lightly high cheekbones without sharp projection, low cheek fat, an adult jaw that narrows gently, and a medium-length narrow chin with a rounded blunt end, never a V point. Her left jawline is subtly fuller than the right. Medium-small horizontally long almond eyes, low narrow natural double-eyelid folds, nearly level outer corners with the slightest downward tendency, dark brown irises of normal size, straight lower lids, faint blue-gray under-eye fatigue and shallow tear troughs. Natural black medium-fine almost-straight brows with a low peak. Low-to-medium nasal root, medium-narrow mostly straight bridge with slight natural bone variation, small-to-medium rounded slightly downward nose tip, natural medium-width wings. Moderately wide closed mouth, thin upper lip, medium lower lip, muted gray-pink color, fine vertical lip lines, right mouth corner very slightly lower. Light-medium cool-neutral Chinese skin with visible pores, mild uneven tone, subtle nose-side redness, no smoothing.

Natural-black straight hair ending at the jaw, loose 6:4 side part, tucked behind the right ear, light inward bend at the ends, a few humidity-softened flyaways. No jewelry. Plain low-saturation gray-blue crew-neck cotton top only as a neutral neckline. Calm closed mouth, stable direct gaze, no smile and no heightened emotion. Realistic cinema portrait, identity documentation quality rather than fashion photography.
```

#### Negative / Avoid

- influencer face
- Korean idol makeup
- oversized eyes or enlarging contact lenses
- high European double eyelids
- V-shaped pointed chin
- cosmetic tiny upturned nose
- glossy full lips
- porcelain skin or beauty retouching
- long hair, waves, or blunt bangs
- jewelry
- smile or dramatic sadness
- fashion editorial lighting
- doll-like CGI face
- mixed-ethnicity facial drift

#### Continuity Anchors

- 窄长自然椭圆脸；中小横长眼；低位窄双；圆钝鼻尖；偏薄淡唇。
- 下颌长度自然黑短发，右侧夹耳后。
- 真实毛孔、眼下青灰疲惫与轻微左右不对称必须保留。

---

### FLOW-CHAR-XN-COST-A-001

**Asset ID**：`CHAR-XN-001` + `COST-XN-CARDIGAN-001` + `COST-XN-BASE-001`
**Master Purpose**：锁定谢念 Costume A 的全身比例、体态与黑开衫状态。

#### Prompt

```text
Single-person full-body costume identity master of the exact same Xie Nian facial identity: a 27-year-old Chinese woman, 165 cm, slim with narrow shoulders, a thin chest and back, long lean limbs, straight posture and slightly inward shoulders. Plain neutral gray studio wall and matte floor, soft even natural light, normal relaxed standing pose, arms resting naturally, no story action, no props, no text, no collage. Preserve her narrow long-oval face, medium-small horizontal almond eyes with low narrow double folds, low-to-medium straight nose with rounded tip, thin muted lips, real cool-neutral skin texture, and jaw-length natural-black hair tucked behind the right ear.

Show Costume A clearly: a soft-black pure-wool fine-knit round-neck cardigan, lightweight and light-absorbing, repeatedly washed, gently fitted but not tight, six small matte black buttons, sleeves to the wrists, hem reaching the upper hip with slight looseness and a faint washed waviness. Under it, a low-saturation gray-blue cotton crew-neck long-sleeve top. Deep charcoal straight washed-cotton trousers, hems lightly touching dark gray-black matte low-cut practical shoes with low heels and no branding. No accessories, no jewelry, no bag. The silhouette is practical, quiet and slightly guarded, never fashionable or styled. Realistic Chinese adult anatomy and textile behavior.
```

#### Negative / Avoid

- different face from FLOW-CHAR-XN-FACE-001
- oversized fashion cardigan
- navy or gray cardigan
- mohair, chunky knit, or fleece
- short skirt or tight trousers
- heels
- jewelry or handbag
- model pose
- luxury styling
- beauty retouching
- long hair
- logo clothing

#### Continuity Anchors

- Costume A 只用于 SHOT 007 脱衣前；黑开衫为纯软黑细针织，非藏青。
- 165cm 偏瘦、肩颈直且微内收；内搭、裤、鞋与 Costume B 完全相同。

---

### FLOW-CHAR-XN-COST-B-001

**Asset ID**：`CHAR-XN-001` + `COST-XN-BASE-001`
**Master Purpose**：锁定黑开衫离身后的谢念固定内搭与单薄轮廓。

#### Prompt

```text
Single-person full-body costume identity master of the exact same Xie Nian from the approved face master: 27-year-old Chinese woman, 165 cm, slim, narrow shoulders, lean limbs, straight posture with slightly inward shoulders, jaw-length natural-black hair tucked behind the right ear, narrow long-oval face, medium-small horizontal almond eyes, rounded nose tip, muted thin lips and real lightly fatigued skin. Plain neutral gray background and matte floor, soft even natural light, ordinary balanced standing pose, no dramatic action, no props, no text, no collage.

Show Costume B only. The black wool cardigan has been removed and must not appear anywhere. She wears a low-saturation gray-blue cotton crew-neck long-sleeve top, straight and fitted without clinging, hem ending at the hip, sleeves reaching the wrist, lightly softened by normal washing with small natural folds at the elbows. Deep charcoal straight washed-cotton trousers and the exact same dark gray-black matte low-cut practical shoes used in Costume A. No jewelry, watch, belt decoration, scarf, bag, print or logo. The reduced layer should make her look slightly more exposed and physically thin, but not fragile or sexualized. Accurate real fabric and adult body proportions.
```

#### Negative / Avoid

- black cardigan anywhere in frame
- different face or hairstyle
- white shirt
- fitted fashion knit
- transparent fabric
- logo T-shirt
- skirt or heels
- jewelry
- model pose
- glamour styling
- porcelain skin
- oversized eyes

#### Continuity Anchors

- Costume B 与 A 共用同一灰蓝内搭、深炭裤和实用鞋；唯一变化是黑开衫离身。
- SHOT 007 后所有谢念资产不得把黑开衫穿回身上。

---

### FLOW-CHAR-TL-FACE-001

**Asset ID**：`CHAR-TL-001`
**Master Purpose**：锁定唐荔独立于谢念的方圆骨相、低马尾和真实劳动女性面孔。

#### Prompt

```text
Single-person neutral face identity master portrait of Tang Li, a real 27-year-old Chinese woman and working alterations tailor. Head-and-shoulders framing, front-facing with a slight three-quarter turn, plain warm-neutral matte background, soft even natural light, no scene, no props, no text, no collage, no dramatic expression. She looks 27 to 30, grounded, capable and physically real, not sweetly styled and not elderly.

Her facial structure must be clearly different from Xie Nian: medium-wide square-round to short-oval face, face length about 1.20 to 1.24 times cheekbone width, medium-low broad forehead, full temples, rounded medium-height cheekbones, healthy cheek volume with working jaw support, visibly wider lower jaw, and a short-to-medium broad rounded chin with a nearly horizontal lower curve. Left cheek subtly fuller than the right. Medium-sized relatively flat almond eyes, slightly shorter and rounder, very low inner-double or shallow eyelid folds, outer corners rising only two or three degrees, deep brown irises, mild work fatigue below the eyes. Medium-thick natural brows with stray hairs and a low arc. Low-to-medium nasal root, medium-broad short straight bridge, round slightly thick nose tip, naturally broad wings. Medium-wide mouth, flatter cupid's bow, medium-thin upper lip, medium lower lip, warm muted brown-rose color and fine dry lip lines. Warm medium Chinese skin with visible pores, subtle sun variation, faint brown-gray under-eye fatigue and natural redness around the nose.

Dark brown-black medium-long hair, slightly coarse and naturally frizzy, gathered in a low ponytail with a plain dark tie; irregular center-right part and a few practical flyaways. Only a simple dark oatmeal-gray crew-neck neckline is visible. Neutral closed mouth, direct calm gaze, no smile. Identity-documentation realism, no beauty campaign styling.
```

#### Negative / Avoid

- Xie Nian's narrow long face
- jaw-length short hair
- V-shaped chin
- narrow cosmetic nose
- oversized eyes
- high double eyelids
- influencer beauty
- porcelain skin
- glossy lips
- elderly seamstress
- gray hair or glasses
- qipao or traditional costume
- sweet smile
- fashion editorial lighting

#### Continuity Anchors

- 方圆短椭圆脸、宽圆下巴、低内双、微上扬外眼角、较宽短直鼻梁与圆厚鼻尖。
- 深棕黑中长发必须低束；真实暖中等肤色，不得与谢念撞脸。

---

### FLOW-CHAR-TL-COST-001

**Asset ID**：`CHAR-TL-001` + `COST-TL-WORK-001` + `PROP-TAPE-TL-001`
**Master Purpose**：锁定唐荔结实体型、低马尾、工作服和黄色系卷尺。

#### Prompt

```text
Single-person full-body costume master of the exact same Tang Li facial identity: 27-year-old Chinese woman, about 162 cm, medium sturdy build, shoulders slightly wider than Xie Nian's, normal body fat, lightly developed forearm muscles from years of cutting and sewing, broad square-round short-oval face, low inner-double eyes, broad short nose with rounded tip, warm medium real skin, dark brown-black medium-long hair tied in a low ponytail. Plain neutral gray background and matte floor, soft even natural light, normal relaxed standing pose with weight slightly favoring one leg, no story action, no text, no collage.

She wears a washed olive-gray straight cotton work shirt, practical and not waist-fitted, sleeves rolled evenly to mid-forearm, over a dark oatmeal-gray crew-neck cotton top. Deep brown-gray straight work trousers and black-brown soft-soled practical work shoes. Around her neck hangs a worn yellow-brown soft measuring tape about two fingers wide, both sides falling naturally toward the lower chest, with an old metal end near the collarbone. No apron in this first master, no jewelry, no glasses. Clothing shows light real wear at elbows, cuffs and pocket edges, plus a few tiny thread fibers, but remains clean and usable. Grounded contemporary Chinese alterations worker, not a traditional tailor stereotype or fashion designer.
```

#### Negative / Avoid

- different face from FLOW-CHAR-TL-FACE-001
- slim fashion-model body
- elderly tailor
- qipao, long gown, sleeve guards, or hair net
- bright fashion apron
- black designer outfit
- neon plastic measuring tape
- waist-worn tape
- heels
- jewelry or glasses
- exaggerated muscular body
- influencer styling

#### Continuity Anchors

- 低马尾高度、橄榄灰上衣、挽袖高度、深褐灰裤与黄色系卷尺必须稳定。
- 唐荔是 27 岁现代改衣师，体型结实但不过度健身。

---

### FLOW-CHAR-ZWM-FACE-001

**Asset ID**：`CHAR-ZWM-001`
**Master Purpose**：锁定赵为民普通、疲惫、劳动化而不英雄化的中年面孔。

#### Prompt

```text
Single-person neutral face identity master portrait of Zhao Weimin, a real Chinese male electric-scooter repair worker around 48. Head-and-shoulders, front-facing with a slight three-quarter turn, plain neutral gray-brown background, soft even natural light, no tools, no scene, no text, no collage, no dramatic story acting. He should look 48 to 52 because of labor, caregiving and poor sleep, but not elderly, handsome, heroic, villainous or destitute-caricatured.

Broad blunt rectangular face, face length about 1.23 to 1.27 times cheekbone width, medium broad forehead with mild recession at both sides, slightly hollow temples, medium-high cheekbones softened by rough tissue, reduced cheek fat, broad jaw angles, a medium-wide square-rounded chin with slight recession, right mouth corner subtly lower, left eye bag heavier. Medium-small narrow eyes with thick mildly drooping upper lids, unstable narrow inner-double folds, slightly downward outer corners, deep brown irises, visible but restrained red veins, heavy lower-eye bags and brown-gray fatigue. Medium-thick irregular brows, dense at the inner ends and sparse at the tails. Low-to-medium root, medium-high broad straight nose bridge, broad round slightly downward nose tip, thick natural wings. Medium-wide mouth, thin dry lips, downward resting corners, deep lip lines. Uneven warm-brown and sallow Chinese skin with coarse pores, sun variation, forehead lines, eye-corner lines, deep nasolabial folds, small age spots and one-day dark stubble.

Coarse short black crew cut with moderate density, slight natural recession and only 10 to 15 percent scattered gray at temples and crown, no styling product. A faded dark gray-blue work-jacket collar and old gray-white undershirt neckline may appear. Closed mouth, tired guarded gaze, no smile.
```

#### Negative / Avoid

- handsome rugged hero
- fitness-model middle-aged man
- elderly man in his sixties or seventies
- full white hair
- villain face
- drunken red skin
- homeless caricature
- narrow sharp nose
- European deep-set eyes
- sculpted beard
- smooth beauty skin
- fashion haircut
- dramatic anger
- commercial actor retouching

#### Continuity Anchors

- 宽长方钝脸、小窄疲惫眼、重眼袋、宽圆鼻尖、薄干嘴、黑黄粗糙皮肤与短胡茬。
- 粗硬短平头仅少量灰发；视觉年龄约 48，不可老年化。

---

### FLOW-CHAR-ZWM-COST-001

**Asset ID**：`CHAR-ZWM-001` + `COST-ZWM-WORK-001`
**Master Purpose**：锁定赵为民微驼体态、维修工服装与左胸内袋位置。

#### Prompt

```text
Single-person full-body costume master of the exact same Zhao Weimin facial identity: Chinese male repair worker around 48, about 170 cm, medium sturdy frame made slightly lean by exhaustion, shoulders mildly stooped, torso habitually leaning forward, neck slightly withdrawn, labor-developed forearms and broad hands, no athletic hero silhouette. Plain neutral gray background and matte floor, soft even natural light, ordinary standing posture, both arms relaxed so the clothing is readable, no dramatic gesture, no tools, no text, no collage.

He wears a faded dark gray-blue zip-front cotton-blend labor jacket with a clear left chest inner-pocket structure, an old gray-white undershirt, dark gray heavy-cloth work trousers, and dark rubber-soled work shoes. The jacket and trousers show localized machine-oil marks, dust, faded cuffs, knee wear and normal creases, never uniform grime. The left chest fabric should be able to form a subtle concealed hard-object outline in later shots, but no object is visible in this neutral master. His hands are broad with large knuckles and short uneven nails; machine-oil residue remains in nail grooves and finger creases. Coarse short black hair with a small amount of gray, real rough skin, practical ordinary Chinese worker clothing, no branding.
```

#### Negative / Avoid

- heroic pose
- right chest pocket emphasis
- visible hidden object
- leather jacket
- racing uniform
- military clothing
- safety helmet
- tool-belt overload
- clean fashion workwear
- brand logos
- full-body grime
- bodybuilding physique

#### Continuity Anchors

- 左胸内袋位置、深灰蓝外套、旧汗衫、深灰工装裤和局部油污固定。
- 身体微驼前倾；后续 SHOT 006 为右手按左胸内袋，不得镜像。

---

### FLOW-CHAR-LSY1988-FACE-001

**Asset ID**：`CHAR-LSY-1988-001`
**Master Purpose**：锁定 1988 年约 39 岁年轻林素云的成熟正脸，防止老年化或民国化。

#### Prompt

```text
Single-person neutral face identity master portrait of Lin Suyun in 1988, a mature Chinese woman around 39, not an elderly grandmother and not a young idol. Head-and-shoulders, front-facing with a slight three-quarter turn, plain muted warm-gray background, soft even natural light, no historical room, no props, no text, no collage, no story performance. She is a working tailor and shopkeeper: composed, observant and physically grounded.

Balanced medium oval face tending slightly soft-square, face length about 1.27 to 1.31 times cheekbone width, medium open forehead nearly as wide as the cheekbones, full temples, medium-height stable cheekbones without projection, moderate-low cheek fat, gently defined jaw width, medium-length medium-width chin with a rounded flat end, right cheekbone subtly higher and left mouth corner subtly lower. Medium horizontal almond eyes, ratio about 2.6 to 2.8, natural inner corners, nearly level outer corners, medium-low natural double-eyelid folds, slight mature lower-lid softness, deep brown irises, stable assessing gaze. Medium natural brows with a gentle low arc and open brow-eye spacing. Low-to-medium nasal root, medium-height medium-width straight bridge, rounded slightly downward tip, natural wings. Medium-width mouth, soft cupid's bow, medium-thin upper lip, medium lower lip, natural warm gray-red tone, real lip lines. Warm-neutral medium Chinese skin with visible pores, fine lines at eye corners and early nasolabial lines, slight pigment variation, healthy working texture.

Natural black hair, medium density and coarse-straight texture, parted slightly left of center and smoothly gathered into a simple low round bun above the nape, fixed only with a dark tie and discreet dark pins. No decorative hairpiece. A plain low-saturation deep-blue cotton work-smock neckline is visible. Closed mouth, steady calm eyes, no smile.
```

#### Negative / Avoid

- elderly grandmother
- white hair or dense age spots
- twenty-year-old idol
- oversized eyes
- porcelain skin
- bright lipstick
- qipao
- Republican-era styling
- wooden hairpin or silver pin
- hair net
- sleeve guards
- mystical shopkeeper
- kindly grandmother smile
- dramatic fear

#### Continuity Anchors

- 视觉年龄 38–42；平衡椭圆偏软方脸；中等杏仁眼；开阔额头；圆平下巴。
- 黑发整齐低挽无装饰圆髻；深蓝罩衫只作为朴素领口出现。

---

### FLOW-CHAR-LSY1988-COST-001

**Asset ID**：`CHAR-LSY-1988-001` + `COST-LSY-1988-001`
**Master Purpose**：锁定年轻林素云 1988 工作服、体态、低髻和成熟轮廓。

#### Prompt

```text
Single-person three-quarter to full-body costume master of the exact same 1988 Lin Suyun facial identity: Chinese woman around 39, about 160 cm, medium-slim with a stable frame, medium shoulders, straight back, lightly strengthened forearms and wrists from tailoring work, composed balanced stance. Plain neutral gray background and matte floor, soft even natural light, normal standing posture, no action, no props, no text, no collage.

Her natural-black hair remains neatly gathered into the same simple unadorned low round bun. She wears a low-saturation deep-blue cotton straight work smock reaching the upper thigh, practical and clean, with a simple front construction, no bright modern zipper, no decorative frog closures, no embroidery, no apron, no sleeve guards. Under it is a dark gray-blue cotton top, with dark straight cotton trousers and black soft-soled cloth shoes. The smock shows realistic repeated-washing fade and slight elbow wear but remains orderly and usable. Preserve her mature oval-soft-square face, stable almond eyes, real 39-year-old skin and calm expression. She should look like a practical 1988 urban Chinese tailor, not a costume-drama artisan.
```

#### Negative / Avoid

- different face or older age
- qipao or long traditional gown
- ornate frog closures
- apron
- sleeve guards
- wooden hairpin or hair net
- costume-drama styling
- rural folk costume
- modern uniform
- heels
- jewelry
- dramatic pose

#### Continuity Anchors

- 深蓝低饱和棉布罩衫、暗灰蓝内搭、深色直筒棉裤、黑布鞋固定。
- 无木簪、发网、围裙、套袖；低髻高度和正脸身份与 Face Master 一致。

---

## 3. Character Detail Masters

### FLOW-CHAR-XN-HAND-001

**Asset ID**：`CHAR-XN-HAND-001` / detail of `CHAR-XN-001`
**Master Purpose**：锁定谢念右虎口一寸浅白旧疤与精准、偏窄的手型。

#### Prompt

```text
Single isolated anatomical detail master of Xie Nian's bare right hand, one real 27-year-old Chinese woman's hand only, resting naturally on a plain neutral medium-gray matte surface under soft even natural light. No face, no body, no second hand, no object, no text, no collage. The palm is turned partly toward camera so the web between thumb and index finger is clearly visible. The hand is narrow with medium-long fingers, defined but not coarse joints, short clean unpainted nails and slight dry textile-work lines on the fingertips. A healed one-inch pale-white shallow diagonal scar runs through the right thumb-index web: thin, slightly raised, old, not red, not inflamed, not fresh, not dramatic. Real skin pores, fine creases and subtle cool-neutral Chinese skin variation. Clinical clarity without looking medical or staged as an injury photograph.
```

#### Negative / Avoid

- left hand
- fresh wound
- blood or scab
- thick keloid
- tattoo
- manicure or nail polish
- jewelry
- latex glove
- multiple hands
- collage
- beauty-retouched skin
- distorted fingers

#### Continuity Anchors

- 疤痕固定在右掌虎口，斜向、一寸、浅白、已愈合。
- 手掌偏窄、手指中长、短甲；不得与唐荔宽手或赵为民粗手混淆。

---

### FLOW-CHAR-TL-HAND-001

**Asset ID**：`CHAR-TL-HAND-001` / detail of `CHAR-TL-001`
**Master Purpose**：锁定唐荔短甲、老茧与少量针眼的裁缝手。

#### Prompt

```text
Single isolated anatomical detail master of Tang Li's bare working hand, one real 27-year-old Chinese woman's tailor hand only, relaxed on a plain neutral warm-gray matte surface in soft even natural light. No face, no body, no tools, no cloth, no text, no collage. Show a relatively broad palm with short strong fingers, practical joints, short unpainted nails cut close to the fingertips with slightly rough edges. Uneven pale calluses appear at the thumb base, inner index finger, first joint of the middle finger and outer palm edge. Only a few tiny old needle-prick marks are visible on the index and middle fingertips; they are subtle healed points, not open wounds or a dense pattern. Warm medium Chinese skin, slightly darker on the back of the hand, natural pores, dry areas, fine scratches and real working texture. Accurate anatomy and restrained documentary realism.
```

#### Negative / Avoid

- delicate model hand
- long fingers
- long nails
- nail polish
- jewelry
- gloves
- blood or open punctures
- dense horror wounds
- smooth porcelain skin
- sewing tools
- multiple hands
- collage

#### Continuity Anchors

- 宽手掌、较短有力手指、短甲、分布不均浅黄老茧、少量旧针眼。
- SHOT 017 使用裸手；不得生成谢念白棉线手套。

---

### FLOW-CHAR-ZWM-HAND-001

**Asset ID**：`CHAR-ZWM-HAND-001` / detail of `CHAR-ZWM-001`
**Master Purpose**：锁定赵为民粗大骨节、工具老茧与甲沟机油黑边。

#### Prompt

```text
Single isolated anatomical detail master of Zhao Weimin's bare repair-worker hand, one real Chinese man's right hand around age 48 only, resting naturally on a plain neutral gray-brown matte surface under soft even natural light. No face, no body, no tools, no text, no collage. The palm is broad and thick, fingers relatively short, knuckles large and prominent, palm lines deep, with friction calluses at the thumb web and inner index finger. Nails are short, uneven and practical; dark machine-oil residue is embedded specifically in the nail grooves, cuticle edges, joint creases and a few deep skin lines, while the rest of the hand remains visibly human skin rather than being painted black. Warm-brown and sallow Chinese skin, rough pores, dry cracked areas around nails, minor old abrasions, no fresh injury. Accurate adult male anatomy, ordinary labor realism, not heroic advertising imagery.
```

#### Negative / Avoid

- clean model hand
- long elegant fingers
- manicure
- full hand painted black
- excessive grease dripping
- gloves
- tools in frame
- blood or fresh cuts
- jewelry
- bodybuilder hand
- multiple hands
- collage

#### Continuity Anchors

- 手掌宽厚、指节粗大、短而不齐的指甲、机油只集中在甲沟和纹路。
- 该资产服务后续右手动作；不得镜像替代为左手 Master。

---

## 4. Location Masters

### FLOW-LOC-HCL-2025-EXT-001

**Asset ID**：`LOC-HCL-2025-EXT-001`
**Master Purpose**：锁定 2025 回潮里 47 号寄雨行门面几何、卷帘门、木牌、铜檐槽和梅雨材质。

#### Prompt

```text
Empty location master, no identifiable people, of Jiyu Hang at number 47 in Huichao Lane, June 2025, in a fictional southern Chinese provincial capital. A narrow-front two-story brick-and-timber mixed-use old building, storefront width about four meters, patched gray-white plaster with small areas of dark red brick, an old upper wooden window with a plain security grille, black utility wires and lived-in municipal clutter. The ground-floor entrance is a half-raised horizontal corrugated iron rolling shutter with rust, worn guide rails, dents and a shoe-worn shallow threshold; an ordinary glass storefront sits just behind it. Above is a faded dark weathered wooden signboard with a clean blank area for later Chinese text. Under the old tiled eave runs the same shallow open 1960s copper gutter, mostly dark brown oxidized copper with irregular muted green patina, simple brackets and one old metal downpipe at the side.

Rainy late afternoon, cold cyan-gray overcast light, wet black-gray stone slabs mixed with cement joints, uneven water film, shoe and tire traces, gray-green damp marks near the wall base. Medium everyday object density: one old electric scooter, a plain plastic stool, a small air-conditioning unit or cable bundle, all secondary and never blocking the facade. Pale fluorescent light and one weak warm work light visible inside. Neutral cinematic location photography, vertical composition suitable for 9:16 reference use, architectural clarity, realistic wear, no story action.
```

#### Negative / Avoid

- core characters or posed people
- tourist old town
- water-town postcard
- lantern street
- cafe or trendy vintage boutique
- magical shop or horror house
- ornate traditional architecture
- polished new facade
- cyberpunk neon
- heavy fog
- readable AI Chinese text

#### Continuity Anchors

- 门面宽度、二楼窗位、一楼门洞、木牌、卷帘门、铜槽与立管位置固定。
- 现实入口只能是卷帘门；SHOT 018 夜景必须复用同一建筑 Master。

#### Text Handling

“寄雨行”与门牌“47”保留干净承载面，后期覆盖；不接受乱码作为 Master 内容。

---

### FLOW-LOC-JYX-FRONT-001

**Asset ID**：`LOC-JYX-2025-FRONT-001`
**Master Purpose**：锁定寄雨行一楼前店平面、柜台、衣架、纸箱、樟木箱、布帘与现实照明。

#### Prompt

```text
Empty interior location master of the 2025 front shop of Jiyu Hang, no core characters, no story action. A narrow rectangular working old-clothes shop about four meters wide and roughly eight meters deep, inside a brick-and-timber old building. View from near the street entrance along the depth so the floor plan is readable. On the right, a long worn solid-wood counter begins about 1.2 meters inside the glass storefront, with a one-person working passage behind it; its edge is rounded by use, scratched and repaired, with a dull aged aluminum pressure strip. On the left, one or two old iron-pipe garment racks hold practical low-saturation used clothes. Three thick taped cardboard boxes sit consistently behind the counter or against the wall, the top box showing translucent polyester dust bags. Near the rear wall stands an old camphorwood chest. A heavy dark coarse-cloth curtain hangs near the back-center, leading toward the fitting cubicle and rear work area.

Patched gray-white damp plaster, small exposed old-brick areas, visible timber beams and later electrical conduit, worn cement floor with a brighter footpath and plum-rain shoe marks. Cold-white double-tube fluorescent fixtures are the main light; cyan-gray rainy daylight enters through the ordinary glass storefront, with only one low warm work lamp at the counter. Medium-high but organized working density, leaving a clear counter surface for clothing inspection. Real old Chinese neighborhood shop, not curated retro decor. Vertical composition suitable for 9:16, material and spatial documentation quality.
```

#### Negative / Avoid

- core characters
- modern fashion store
- vintage boutique
- cafe
- antique collection room
- pharmacy or pawn shop
- magic shop
- Chinese zen interior
- red lanterns or carved screens
- empty studio set
- luxury high ceiling
- warm cozy overall lighting

#### Continuity Anchors

- 街侧卷帘门／玻璃面、右侧柜台、左侧衣架、三只纸箱、后部樟木箱和深色布帘相对位置固定。
- 空间约三十余平方米、狭长、拥挤但可工作；不得随机扩成大店。

#### Text Handling

任何账本、标签、招牌或包装文字均不要求正确；Master 以结构和材质为准，文字后期处理。

---

### FLOW-LOC-JYX-FIT-001

**Asset ID**：`LOC-JYX-FIT-001`
**Master Purpose**：锁定不足一平方米试衣间的比例、布帘、老镜和冷暖漏光。

#### Prompt

```text
Empty location master of the tiny fitting cubicle inside Jiyu Hang, no person, no clothing, no story action. The space is physically less than one square meter, approximately 0.85 meters wide by 1.05 meters deep and 2.4 meters high, only large enough for one adult to raise both arms. A dark coarse-cotton curtain fills the entrance; its lower right edge is visibly shorter, with a very faint old lake-blue remnant along the worn binding. Opposite or slightly left of the entrance stands one old full-length mirror in a plain blackened wooden frame. The mirror has irregular silvering loss around the edges and fine scratches, but the central reflection area remains usable and the glass is not cracked.

Old gray-white damp plaster, a dark brick base, worn cement floor, simple old curtain rod and a small practical wall-lamp fitting. Cold fluorescent spill enters around the curtain edge while a weak low-watt warm wall lamp adds a small secondary tone. The cubicle is oppressive because of scale, not because of clutter; no chair, decoration, merchandise or ritual object. Neutral vertical architectural reference, realistic damp aging, clear geometry, no horror atmosphere.
```

#### Negative / Avoid

- people
- modern mall fitting room
- LED mirror
- cracked mirror
- ghost reflection
- blood writing
- horror green light
- ritual room
- candles or symbols
- wide spacious room
- decorative furniture
- clothing display

#### Continuity Anchors

- 0.85×1.05 米逼仄比例、深色粗布帘、右下短缺湖蓝滚边、发黑木镜框和边缘水银斑固定。
- 中央镜面可用且绝不破裂；空间内只能容纳一人。

#### Text Handling

该场景无关键文字；镜面中不得出现随机文字或标志。

---

### FLOW-LOC-HCL-1988-EXT-001

**Asset ID**：`LOC-HCL-1988-EXT-001`
**Master Purpose**：锁定 1988 同址旧巷、黑漆木门、残雪煤渣与历史排除项。

#### Prompt

```text
Empty historical location master of Huichao Lane at number 47 in winter 1988, in the same southern Chinese city and same building axis as the 2025 storefront. No core characters, no story action. A narrow urban mixed residential-and-shop lane about three meters wide, low brick-and-timber tiled buildings, worn gray plaster, dark brick bases, wooden lattice windows, old cast-iron drainage and wet black stone paving. Thin frozen gray snow lies unevenly in the paving joints and mixes with scattered crushed black coal cinders; this is an unusual southern snowfall, not deep northern accumulation.

At number 47, the later rolling-shutter opening is represented by a narrower plain weathered black-lacquered wooden door with a practical internal bolt system, matte worn paint, exposed wood at edges and a deeply worn threshold. No brass rings, carving or grand-house decoration. Cold blue-gray snow-night light dominates; one dirty pale or yellowish incandescent street lamp farther down the lane gives weak uneven illumination. Small hard snow grains move sideways, but the scene stays clear and factual, with no dream blur. Preserve recognizable roofline, doorway axis and street scale for historical continuity. Vertical composition suitable for 9:16 location reference, restrained film grain, historically spare production design.
```

#### Negative / Avoid

- people
- northern industrial city
- mining town
- northeastern courtyard
- rural mud village
- water-town tourism
- bridge or canal postcard
- Republican-era film street
- lanterns or archways
- rolling shutter
- LED lights
- air conditioners or electric scooters
- aluminum windows or PVC signs
- sepia filter
- dream haze

#### Continuity Anchors

- 与 2025 保持同一门洞轴线、巷宽和屋檐 DNA，但入口固定为斑驳黑漆木门。
- 青石、残雪、黑煤渣、低砖木瓦房和巷口白炽灯固定；不得北方化或古镇化。

#### Text Handling

门牌“47”后期覆盖；不要生成可读街牌、现代标语或虚构历史字体。

---

### FLOW-LOC-JYX-1988-INT-001

**Asset ID**：`LOC-JYX-1988-INT-001`
**Master Purpose**：锁定黑漆木门内 1988 工作／起居空间、煤炉、水壶及冷暖边界。

#### Prompt

```text
Empty interior location master of the front working-and-living area inside Jiyu Hang in 1988, no people, no story action. Show only the approximately three-by-four-meter zone just inside the weathered black-lacquered wooden door. The door and practical bolt occupy one side of frame; a dark used coal stove stands about 1.5 to 2 meters inside without blocking passage, with a black-gray cast-iron kettle on top releasing ordinary white steam. Old gray plaster, dark brick at the wall base, simple timber framing, worn cement floor, a plain low-watt incandescent bulb or simple shade, and one restrained wooden utility shelf. The coal stove shows real soot, heat marks and ash; the kettle has normal scale and heat wear, not decorative nostalgia.

Lighting locks the space: low orange incandescent ambience and dark red coal glow inside, with cold blue snow light cutting through the partly open door. The warm and cold zones remain physically plausible; steam catches light but does not glow. Low-to-medium object density, leaving clear space for two people and the future ticket exchange. Practical 1988 urban Chinese interior, not a kitchen tableau, not a film-set collection of vintage props. Vertical composition suitable for 9:16 location reference, realistic materials and restrained color.
```

#### Negative / Avoid

- people
- cozy nostalgic kitchen
- family dinner scene
- Republican-era tailor shop
- qipao studio
- rural earthen stove room
- northern kang room
- modern gas stove
- LED lighting
- plastic electric kettle
- aluminum windows
- stacked vintage prop collection
- glowing steam
- ritual or magic space

#### Continuity Anchors

- 黑漆门、门闩、煤炉距门位置、生铁水壶、水泥地与灰泥／青砖墙固定。
- 低瓦橘黄灯和暗红炉火对抗门外冷蓝雪光；物件密度保持低到中。

#### Text Handling

本场景无关键文字；任何墙面纸张或容器标签保持空白／不可读。

---

### FLOW-LOC-JYX-CUT-001

**Asset ID**：`LOC-JYX-2025-CUT-001`
**Master Purpose**：锁定主店堂正中裁床、墨绿台布、周边走动空间和弱化工作背景。

#### Prompt

```text
Empty location master of the central cutting-table work zone inside Jiyu Hang in 2025, no core characters, no garment laid on the table, no story action. This is part of the main shop floor, not a rear secret room. A large old solid-wood cutting table about 1.8 meters long, 1.0 meter wide and 0.82 meters high stands in the middle of the shop with its long axis following the shop depth. Leave at least 0.75 meters of walking space around it. Cover the top with one heavy dark-green cotton or wool work cloth, lightly pressure-marked with a few small thread fibers, clean enough for inspection.

Continue the same old-shop architecture: damp gray plaster, worn cement floor, timber elements, cold-white fluorescent overhead light and storm-dark rainy daylight. A normal work lamp gives a modest neutral-warm pool over the table without becoming a spotlight. In the subdued background, show only one or two soft elements such as a practical metal sewing machine, simple thread stand, dark curtain or iron clothing rack; keep them dim and secondary. The table edge is rounded and polished by fabric friction, with shallow scissor marks and small impact wear. Neutral vertical composition suitable for 9:16, spatially clear, realistic working environment, low object density on the main table.
```

#### Negative / Avoid

- people
- garment or story prop on table
- back-room secret chamber
- basement workshop
- modern fashion atelier
- white sterile design studio
- antique sewing museum
- trendy craft livestream set
- cluttered scissors and thread display
- dramatic interrogation spotlight
- altar or magical workbench
- glowing thread

#### Continuity Anchors

- 裁床位于主店堂正中，1.8×1.0 米左右，墨绿厚台布、四周可站人。
- 背景只弱化显示工作环境；不得移动到后堂或独立密室。

#### Text Handling

该场景 Master 不需要文字；缝纫机商标、包装和墙面标签保持不可读。

---

## 5. Hero Prop / Costume Masters

### FLOW-PROP-COAT-001

**Asset ID**：`COST-ZG-COAT-001`
**Master Purpose**：锁定灰色粗花呢大衣外部几何、六扣、织纹、比例和 2025 磨损状态。

#### Prompt

```text
Single isolated hero garment master, one heavy 1980s men's overcoat only, suspended naturally from a plain sturdy wooden hanger against a simple neutral medium-gray matte background, soft even studio-natural light, no person, no mannequin body visible, no text, no collage, no multiple views. Full-length front three-quarter view with the entire silhouette and hem visible.

The coat is a straight-cut double-breasted heavy gray mixed-fleck rough-tweed garment, approximately 108 cm long, shoulder width around 50 cm, chest around 114 cm, with thick shoulder pads, broad classic lapels, no waist shaping, no belt and two practical side pockets. Lock the director reference arrangement: exactly six matte dark charcoal round buttons in two columns of three, evenly spaced, no emblems or metallic trim. The textile is coarse and tactile, tightly woven from medium-deep gray, off-white and sparse black fibers forming an irregular snow-fleck pattern, never a smooth uniform gray. The 2025 state shows worn pale collar and cuffs, slight oily sheen at the collar, softened edges, localized abrasion at front and hem, and believable heavy drape. The rayon lining may be visible only as a small natural opening at the lower edge, brittle with fine creases; hidden stitches must not become decorative exterior embroidery. Real garment weight, ordinary old clothing, high material readability.
```

#### Negative / Avoid

- person or visible mannequin
- multiple coats or contact sheet
- women's fitted coat
- fashion oversized coat
- trench coat or military coat
- single-breasted front
- four or eight buttons
- metal military buttons
- belt
- blue, black, camel, plaid or houndstooth fabric
- smooth cashmere
- glowing fabric or visible magic

#### Continuity Anchors

- 男款直筒、厚垫肩、大翻领、两列三扣、两侧口袋、108cm 视觉长度。
- 此 Master 是 2025 状态；1988 只允许磨损减轻，几何和织纹不变。

#### Text Handling

无文字需求；不得生成品牌标签或可读商标。

---

### FLOW-PROP-WORKWEAR-001

**Asset ID**：`COST-SZ-WORKWEAR-001`
**Master Purpose**：锁定“孙正”灰工装的直身版型、斜纹、左胸袋、氧化拉链与右腰暗针。

#### Prompt

```text
Single isolated hero garment master of one early-2000s Chinese men's labor jacket, laid flat on a plain dark muted-green textile surface against a simple neutral background, soft even overhead light, no person, no hands, no text rendered as final, no collage, no multiple views. Show the entire front silhouette while gently turning open only the inside right waist fold so both the left chest area and hidden repair structure remain readable in one coherent object view.

The jacket is ordinary straight-cut long-sleeve workwear in coarse gray cotton twill, roughly men's L proportions, about 71 cm long and 48 cm across the shoulders. Low practical work collar, center metal zipper oxidized almost black, one left chest patch pocket with a flap, no reflective strips, no branding. Repeated washing and strong sunlight have faded the gray unevenly into yellow-gray and gray-white, while shadowed folds retain medium gray. Fine abrasion and fraying appear at the collar, elbows, cuffs and hem; wear is irregular and real, without large theatrical stains. Reserve a clean cloth area on the left chest pocket flap for later placement of the handwritten Chinese name.

Inside the opened right waist load-bearing fold, show one approximately three-inch repair in two strands of natural-colored silk thread, a fine functional herringbone hand stitch with tiny end knots hidden into the fold. The repair is subtle, slightly raised and internal, never decorative. High textile readability, ordinary inexpensive labor garment, grounded evidence-object photography.
```

#### Negative / Avoid

- person or hands
- multiple garments
- modern fashion work jacket
- streetwear or flight jacket
- military uniform
- blue work uniform
- reflective stripes
- logo or embroidered name patch
- readable AI Chinese text
- new clean fabric
- uniform artificial distressing
- red, gold or glowing stitch
- oversized decorative herringbone seam

#### Continuity Anchors

- 左胸单个带盖贴袋、暗黑金属拉链、偏黄灰白粗斜纹、右腰内侧三寸本色双股蚕丝暗针。
- 左胸和右腰相对位置、褪色分布与斜纹方向锁定，用于 SHOT 016–017。

#### Text Handling

“孙正”必须后期覆盖为旧深色手写墨迹并贴合纤维晕染；Flow 只生成干净、透视正确的袋盖承载面。

---

### FLOW-PROP-LEDGER-001

**Asset ID**：`PROP-LEDGER-001`
**Master Purpose**：锁定《承衣簿》暗红生丝硬封面、厚度、旧纸与现实账簿质感。

#### Prompt

```text
Single isolated hero prop master of one large old Chinese working ledger only, resting closed at a slight three-quarter angle on a plain neutral dark wood or matte gray surface, soft even natural light, no hands, no person, no text rendered as final, no collage, no multiple books. The ledger is approximately 30 cm high, 22 cm wide and 4.5 to 5 cm thick, visibly heavy, with a rigid flat cover wrapped in deeply worn dark red raw silk. The silk has faded unevenly into dark crimson and brown-red, with frayed pale corners, fine spine cracks, hand-polished darker areas and a small amount of hard board visible at worn edges. Leave a clean quiet title area in the upper-middle cover for later Chinese typography.

At the fore edge, many old rough-edged pages are visible: aged warm off-white to yellow-gray paper, slightly brittle, softly uneven and locally curled, but not rotten, mold-eaten or perforated. Binding is substantial and practical without metal lock, chain, gems, embossing, gold trim or religious ornament. The object must read as a real family business ledger used for decades, not a magical book, antique treasure or modern leather notebook. Accurate silk, paper and weight, restrained documentary product photography.
```

#### Negative / Avoid

- multiple books
- hands or person
- magical book
- glowing text
- runes or talismans
- metal lock or chain
- gold trim
- dragon or cloud motifs
- bright red satin
- European antique book
- modern business notebook
- rotten archaeological manuscript
- readable AI Chinese title

#### Continuity Anchors

- 30×22×约5cm 大型厚账簿、暗深红磨损生丝、旧米黄毛边纸和沉重现实感固定。
- 不得变成皮革本、线装古籍或魔法道具。

#### Text Handling

封面“承衣簿”及未来内页文字统一后期覆盖；Master 只锁定书名字区材质、透视与受光。

---

### FLOW-PROP-STAMPSET-001

**Asset ID**：`PROP-STAMPSET-001`
**Master Purpose**：锁定铜章与朱砂色印泥盒作为一个不可拆分道具组合的比例和材料。

#### Prompt

```text
Single isolated hero prop set consisting only of one old hand stamp and its one matching small ink-paste box, arranged simply on a plain neutral warm-gray matte surface under soft even natural light. No hands, no person, no paper, no printed characters, no collage, no extra seals. The stamp has a short upright hard-wood handle, around 75 to 85 mm total height, with an oval-to-rounded-square grip polished darker by years of hand use, fine scratches and no ornament. At the bottom is a roughly 30-by-30-mm square copper stamp head, dark brown with natural oxidation and slightly brighter worn edges. No animal knob, carving, tassel or gemstone.

Beside it sits one low round or softly rounded metal ink-paste box about 60 to 65 mm wide and 18 mm high. The lid is open and placed close by, showing dense restrained dark vermilion-red paste that is matte and cohesive, never liquid, glossy like blood, smoking or glowing. The box has tiny dents, dull age and a little red staining at the rim. Grounded practical shop tool, accurate wood, copper and paste materials, clear scale relationship.
```

#### Negative / Avoid

- official imperial seal
- jade seal
- dragon knob or animal ornament
- religious talisman stamp
- plastic office stamp
- oversized seal
- blood-like liquid
- glowing vermilion
- smoke or particles
- hands or person
- paper with text
- multiple seal sets
- readable characters

#### Continuity Anchors

- 30mm 方铜章头、短旧木柄、低矮印泥盒、暗朱红致密印泥比例固定。
- 这是现实工作工具，不是官印、法器或古董展品。

#### Text Handling

印面与“存押”方印不在 Master 中依赖模型生成；印文后期制作。

---

### FLOW-PROP-GUTTER-001

**Asset ID**：`PROP-GUTTER-001`
**Master Purpose**：锁定旧铜檐槽截面、氧化分布、固定件与立管连接。

#### Prompt

```text
Single isolated architectural hero-asset master of one representative section of the 1960s copper rain gutter used on Jiyu Hang, shown against a simple neutral gray backdrop with a short plain dark eave-edge support for scale, no full building, no people, no text, no collage. The gutter is a shallow open U-shaped to semicircular copper channel, about 11 to 13 cm across and 7 to 9 cm deep, thin but structurally sound, with a modest irregular edge, simple aged metal brackets and one short connection toward an 8 to 10 cm old metal downpipe. Include a restrained historical repair weld and one small dent, but no major break or leak.

Surface color is mostly deep brown oxidized copper, with irregular muted dark-green patina only around joints, old water lines, brackets and seams; it must not be uniformly bright green or polished gold. Rain-washed channels create darker streaks and subtle metal variation. The object is functional, plain and municipal, without ornament. Soft raking natural light should reveal metal thickness, oxidation, bracket geometry and water-wear texture. No water magic, no glow, no decorative architecture.
```

#### Negative / Avoid

- PVC gutter
- galvanized iron gutter
- bamboo or stone channel
- modern rain chain
- polished gold copper
- uniformly green sculpture
- palace ornament
- beast-head spout
- carved brackets
- glowing water
- runes or energy waves
- people or full storefront
- multiple gutter designs

#### Continuity Anchors

- 浅 U 形开放槽、深褐铜为主、局部暗绿铜锈、朴素卡箍和一侧立管连接固定。
- SHOT 001/004/018 只改变雨水强度，不改变材质与几何。

#### Text Handling

无文字需求；固定件不得出现品牌标记。

---

### FLOW-PROP-TAPE-001

**Asset ID**：`PROP-TAPE-TL-001`
**Master Purpose**：锁定唐荔黄色系卷尺的宽度、色阶、柔软垂感和金属端扣。

#### Prompt

```text
Single isolated hero accessory master of one worn yellow-brown tailor's measuring tape only, hanging in a relaxed U shape from a simple neutral peg against a plain warm-gray matte background, soft even natural light, no person, no hands, no text rendered clearly, no collage, no extra tools. The tape is soft and flexible, visually about two fingers wide, approximately 3 to 3.5 cm, long enough for both sides to fall naturally toward chest level when worn. Its color is muted yellow to worn ochre-brown, not bright fluorescent plastic. The surface shows gentle repeated bending, softened edges, small handling darkening and practical age without tears. One old dull metal end fitting or clip sits near one end, lightly scratched and not decorative. Any measurement markings remain faint and non-readable; prioritize material, width, drape and metal detail. Ordinary working tailor's object, realistic and unstyled.
```

#### Negative / Avoid

- person or hands
- multiple measuring tapes
- bright neon yellow plastic
- rigid ruler
- modern digital tool
- decorative necklace
- scarf
- waist belt
- scissors or sewing kit
- readable random numbers
- pristine new product
- collage

#### Continuity Anchors

- 微磨损黄褐色、两指宽、柔软垂落、旧金属端扣固定。
- 后续人物 Master 中挂颈，两侧垂长接近，不变成腰带或项链。

#### Text Handling

刻度和数字不依赖模型正确生成；后续若需要近景，统一以受控纹理或后期覆盖处理。

---

## 6. Flow Asset Naming Convention

### 6.1 Generation Unit ID

每次 Flow 任务使用本文唯一 Unit ID，不另起聊天式名称。例如：

- `FLOW-CHAR-XN-FACE-001`
- `FLOW-LOC-JYX-FRONT-001`
- `FLOW-PROP-COAT-001`

### 6.2 Candidate Filename

生成结果在验收前统一命名：

`{FLOW_UNIT_ID}__CANDIDATE__v{NNN}.{ext}`

示例：

`FLOW-CHAR-XN-FACE-001__CANDIDATE__v003.png`

### 6.3 Failed / Look Dev Filename

未通过任一硬锁的结果统一降级：

`{FLOW_UNIT_ID}__LOOK_DEV__REJECTED__v{NNN}.{ext}`

失败图不得使用 `MASTER` 字样，不得进入 Shot Prompt 引用链。

### 6.4 Accepted Master Filename

只有通过 Acceptance Checklist 后，复制／导出为：

`{ASSET_ID}__MASTER__v1.{ext}`

人物服装状态须保留状态后缀：

- `CHAR-XN-001__FACE_MASTER__v1.png`
- `CHAR-XN-001__COST_A_MASTER__v1.png`
- `CHAR-XN-001__COST_B_MASTER__v1.png`

### 6.5 Version Discipline

- 新图不得覆盖旧 Master；变更必须递增版本。
- 单张 Master 只证明它对应的资产层级，不得反向扩展 Canon。
- Master 文件名、生成日期、Flow 任务 ID、使用 Prompt 版本和验收结论应在后续资产日志登记。

---

## 7. Asset Acceptance Checklist

### 7.1 Character Face Master

- [ ] 视觉年龄与角色年龄范围一致。
- [ ] Face Shape、下颌、下巴比例符合对应 Facial Identity Spec。
- [ ] 眼型、眼距、眼睑褶、鼻梁／鼻尖／鼻翼、嘴宽与唇厚正确。
- [ ] 真实中国成年人皮肤：毛孔、轻微不均与疲惫存在，无磨皮或 doll-like 质感。
- [ ] 发长、分缝、束发位置和碎发正确。
- [ ] 无网红化、偶像化、医美小鼻、过大眼睛、V 型尖下巴或玻璃唇。
- [ ] 与其他角色不存在撞脸；尤其谢念与唐荔骨相明确分离。
- [ ] 单人、无文字、无拼版、背景中性、无剧情表演。

### 7.2 Character Body / Costume Master

- [ ] 与通过的 Face Master 为同一 Facial Identity。
- [ ] 身高感、肩宽、体型、重心和职业体态正确。
- [ ] 发型轮廓与 Face Master 一致。
- [ ] 服装颜色、材质、版型、层次、旧化和鞋型符合对应 Costume State。
- [ ] 谢念 Costume A / B 唯一差异是黑开衫是否离身；内搭、裤、鞋一致。
- [ ] 唐荔卷尺、赵为民左胸内袋、林素云低髻与深蓝罩衫位置正确。
- [ ] 无剧情动作、无时尚模特姿势、无多余首饰、Logo 或道具。

### 7.3 Character Detail Master

- [ ] 手的左右侧正确，解剖结构与指头数量正确。
- [ ] 谢念右虎口浅白旧疤位置、长度、方向与愈合状态正确。
- [ ] 唐荔短甲、老茧分布和少量针眼真实克制。
- [ ] 赵为民粗大骨节、短甲与甲沟／纹路机油黑边正确，未把整手涂黑。
- [ ] 无美甲、首饰、手套误配、血伤或拼版。

### 7.4 Location Master

- [ ] 空间尺寸感、长宽关系和纵深符合 Location Spec。
- [ ] 入口、门窗、柜台、衣架、纸箱、樟木箱、布帘、镜子或裁床位置正确。
- [ ] 建筑时代、墙地顶材料、木／砖／铁／铜材质正确。
- [ ] 使用磨损、返潮、铁锈、铜锈、地面水迹真实而非美术化做旧。
- [ ] 主光源、色温和雨／雪环境符合对应年代。
- [ ] 物件密度正确，不因随机生成改变店铺结构。
- [ ] 1988 场景没有 LED、空调、电动车、PVC 招牌、铝合金窗、二维码或现代包装。
- [ ] 未误生成旅游古镇、咖啡馆、精品古着店、魔法商店、恐怖鬼屋或影视城年代街。
- [ ] 无核心人物和剧情动作；中文承载面适合后期覆盖。

### 7.5 Hero Prop / Costume Master

- [ ] 单件资产或规定的一组不可拆分道具，无遮人、无拼版。
- [ ] 比例、形态、颜色和材料符合对应 Asset Spec。
- [ ] 磨损位置与程度真实、非均匀滤镜化。
- [ ] 数量与组件正确：大衣六扣 3×2；印章一枚加印泥盒一只；卷尺一条。
- [ ] 灰呢大衣的领型、扣位、口袋、织纹与长度可作为跨年代同一物 Master。
- [ ] 灰工装左胸袋、氧化拉链、斜纹、右腰暗针位置可读。
- [ ] 《承衣簿》不是魔法书；铜槽不是 PVC／铁槽；卷尺不是荧光塑料。
- [ ] 中文文字留有合成面，不把乱码当成资产设计。

### 7.6 MASTER Gate

只有满足以下全部条件的结果才可命名为 `MASTER`：

1. 通过对应类别的全部硬锁；
2. 与 Asset Specs v1.1 无冲突；
3. 不从生成结果引入新的 Canon；
4. 能在至少两个后续 Shot / Unit 中稳定复用，或作为该唯一资产的可靠材质基准；
5. 人工验收记录明确写出 `ACCEPTED AS MASTER`。

任何失败结果只属于 Look Development，即使“更漂亮”或“更有氛围”，也不得进入 Benchmark Keyframe 或正式 Shot Prompt。

---

## 8. Scope Lock

- 本文件只创建第一批 Flow 资产生成 Prompt，不生成图片。
- 不创建周桂珍完整 Character Master。
- 不创建 `PROP-TICKETS-1988-001` Prompt；其 Historical Research Gate 继续有效。
- 不修改 Screenplay、Shot List、Visual Bible 或 Asset Specs v1.1。
- 不创建 Benchmark v0.2，不包含视频 Prompt 或 Storyboard。
