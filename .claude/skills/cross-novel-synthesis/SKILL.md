---
name: cross-novel-synthesis
description: 对多本已完成分析的小说进行横向比较，提取跨作品可复用故事机制，形成机制卡库与综合报告。当需要生成 GLOBAL_SYNTHESIS / CHINA_PRINT_SYNTHESIS / MASTER 级综合文件时使用。
---

# cross-novel-synthesis — 跨小说综合

## 职责

对多本小说（已有 `NOVEL_DNA.yaml` 与机制卡）进行横向比较，输出跨作品综合与可复用机制库。

## 前置条件

1. 读取 `00_system/ANALYSIS_SCHEMA.md` 与 `00_system/COPYRIGHT_RULES.md`。
2. 确认参与综合的每本小说已完成分析（存在 `NOVEL_DNA.yaml`）。
3. 读取所有参与作品的 `NOVEL_DNA.yaml` + `11_story_mechanism_cards.md`，必要时回查具体分析文件。

## 禁止事项

- **禁止简单罗列共同点。**"这几本都有悬念"没有价值；要说清悬念在不同作品中以什么不同结构实现、共同的心理底层是什么。

## 必须寻找的维度

1. **重复出现的读者吸引机制**——跨作品、跨题材反复出现的是什么
2. **类型差异**——同一机制在不同类型中如何变形
3. **文化差异**——哪些机制是文化特定的，哪些是普世的
4. **人物欲望结构**——主角的 desire/fear/need 模式比较
5. **情绪兑现结构**——情绪债务如何欠下、多久偿还
6. **爽点结构**——reward 类型、频率、延迟策略比较
7. **悬疑结构**——mystery ladder 与信息差模式比较
8. **爱情机制**——关系推进与张力维持方式比较
9. **阶层与财富机制**——class/money 如何驱动故事
10. **章节推进机制**——章末钩子与成瘾循环比较
11. **长篇维持机制**——长篇如何防止疲劳（conflict refresh）
12. **影视化潜力**——AI 视频适配维度比较

## 输出格式

### 综合报告（如 GLOBAL_SYNTHESIS.md）

- 现象级爆红的共同结构性原因（可回溯到各作品证据）
- 跨题材重复机制清单（附出现作品与实现差异）
- 文化特定 vs 普世机制的判定与依据
- 对 AI 视频创作的启示
- 综合层结论的 GREEN/YELLOW/RED 分档

### 机制库（如 GLOBAL_MECHANISMS.yaml）

每张机制卡：
```yaml
- mechanism_name:
  observed_in:          # 出现于哪些作品
  variants:             # 各作品中的不同实现
  psychological_foundation:  # 底层心理机制
  genres_applicable:
  risk_of_cliche:
  how_to_transform:
  protected_elements:   # 各作品中不可复用的具体表达
```

## 完成后

更新 `00_system/PROJECT_STATUS.md`，并在 `99_logs/claude/` 留下综合日志。
