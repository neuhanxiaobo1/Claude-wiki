---
type: memory
status: active
created: YYYY-MM-DD
updated: 2026-09-06
---

# Term Aliases

本页维护 ResearchWiki 的术语同义词映射，防止重复建页。领域术语应根据 `memory/project_profile.md` 逐步补充。

只有含义相同的写法列入 Aliases；相关概念不作合并依据。Recommended page 可以是现有导航页或目录，必须注明关系，不代表术语相同或要求立即建页。未知历史创建日期保留未定；示例不参与实际词表与链接统计。

## Record Format

```markdown
## Main Term

- Aliases:
- Recommended page:
- Recommended tag:
- Note:
- Status: active / 待确认
```

## General Terms

### Literature Review

- Aliases: 文献综述、literature review
- Recommended page: `wiki/reviews/`（目录导航，尚不指定同名页面）
- Recommended tag: `review`
- Note: survey、review paper 可能指文章类型，related work 常指论文小节；按上下文关联，不据此自动合并页面。
- Status: active

### Research Gap

- Aliases: research gap、研究空白
- Recommended page: `[[synthesis/open-questions]]`
- Recommended tag: `gap`
- Note: 研究不足、open problem、open question 为相关概念，不自动等同领域空白。open-questions 是汇总入口；是否创建具体 gap 及其分类按 gap 规则判断。
- Status: active

### Claim

- Aliases: 论断、关键判断
- Recommended page: `wiki/claims/`
- Recommended tag: `claim`
- Note: finding 是相关的结果概念，不必每项独立建 claim；claim 一词本身不保证判断已有证据支持。
- Status: active

## Domain Terms

### Ceramic Corrosion

- Aliases: 陶瓷腐蚀、陶瓷材料腐蚀、corrosion of ceramics、ceramic corrosion
- Recommended page: `[[wiki/topics/Ceramic Corrosion]]`
- Recommended tag: `corrosion`
- Note: 用户研究领域主术语（2026-08-20 确认）。
- Status: active

### CMAS

- Aliases: 钙镁铝硅酸盐、钙-镁-铝-硅酸盐、calcium-magnesium-aluminosilicate
- Recommended page: `[[wiki/topics/Ceramic Corrosion]]`
- Recommended tag: `cmas`
- Note: 当前语料中的腐蚀介质术语；推荐页是相关主题入口。CMAS melts 明确含熔融状态，不能在省略状态后视为条件相同；不同配方也不能仅凭同名合并数据。
- Status: active

### EBC

- Aliases: 环境障涂层、environmental barrier coating、环境屏障涂层
- Recommended page: `[[wiki/topics/Ceramic Corrosion]]`
- Recommended tag: `ebc`
- Note: 当前语料涉及的材料应用术语；推荐页是相关主题入口，不表示 EBC 与陶瓷腐蚀同义，也不据此认定用户已确认研究主线（目标以 project_profile 为准）。
- Status: active

### TBC

- Aliases: 热障涂层、thermal barrier coating、热障涂层材料
- Recommended page: `[[wiki/topics/Thermal Barrier Coatings]]`
- Recommended tag: `tbc`
- Note: 推荐页是已有 TBC 主题入口；同一论文可以同时涉及 TBC 与 CMAS 腐蚀，按实际关系链接，不以别名表预设失效分类或排他归属。
- Status: active

## 示例（不属于当前词表）

```markdown
### Example Method

- Aliases: example approach, demo method
- Recommended page: `[[wiki/methods/Example Method]]`
- Recommended tag: `example-method`
- Note: 这是虚构示例，不对应真实论文。
- Status: Example only
```
