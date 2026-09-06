---
type: memory
status: active
created: YYYY-MM-DD
updated: 2026-09-06
---

# Tag Taxonomy

本页定义 ResearchWiki 的统一标签体系。新增标签前，先检查是否已有同义标签。领域专属标签应根据 `memory/project_profile.md` 逐步添加。

## Naming Rules

- frontmatter tags 默认使用英文小写短语，单词用连字符连接。
- 同一概念只保留一个主标签。
- 中文术语可以写在正文和标题中，但 tags 尽量统一。
- 不确定是否应新增标签时，先写到 `inbox.md` 的“待整理标签”，并标注为“待确认”。
- 领域标签一旦确定，应在本页登记，不要只散落在页面 frontmatter 中。
- 本页是当前词表，不是示例模板；created 的历史日期未确定，不补造。示例、代码块中的标签不作为已登记标签。
- 标签服务检索，不决定证据评价或核查状态。新增标签先判断是否有独立检索用途；同义映射仅在含义相同时应用，不批量替换语义不同的标签。

## General Tags

- `paper`
- `author`
- `topic`
- `method`
- `dataset`
- `metric`
- `claim`
- `gap`
- `review`
- `synthesis`
- `context`
- `style`
- `positioning`
- `open-question`
- `zotero`
- `zotero-import`
- `ingestion`
- `import-plan`
- `possible-duplicate`
- `needs-check`
- `needs-review`
- `needs-metadata`
- `ai-inference`

## Paper Processing Status Tags

- `unread`
- `reading`
- `processed`

以上是处理状态标签，不是证据等级。已有 status 字段无需再机械复制成同名标签；若两者都有则须一致。review_status 使用 draft / checked / needs-review，与处理状态分开；needs-review 标签只能辅助检索，不能替代具体待复核论断及原因。needs-check 用于一般待核对项，不能与 needs-review 无条件合并；ai-inference 标记推断性质，不表示证据强弱。

## Domain Tags

2026-08-20 用户确认研究领域为陶瓷-腐蚀，新增：

- `ceramics`
- `corrosion`

2026-08-23 入库 CMAS/EBC 方向论文（#47、#46、#18），新增：

- `cmas`
- `ebc`

2026-08-27 入库 TBC 方向论文（#29 Hf6Ta2O17-Al2O3），新增：

- `tbc`

新增领域标签按实际语料与检索需要登记；不自动加入占位示例标签。

## Duplicate Tag Policy

| Not Recommended | Recommended | Note |
|---|---|---|
| `lit-review`, `survey` | `review` | 统一指综述类输出 |
| `research-gap`, `gap-analysis` | `gap` | 统一指研究空白 |
| `uncertain`, `to-check` | `needs-check` | 统一指需要进一步核对 |

上述映射仅针对标签用途；例如原文中的 survey 或不确定性含义不得据此改写。旧页面先记录漂移位置，在获授权的维护范围内逐项修正，不为统一标签扩大为整库重写。
