---
direction_id: "{{direction_id}}"
type: paper
title: 待确认
year: 待确认
authors: 待确认
venue: 待确认
status: processed
review_status: draft
created: 待确认
updated: 待确认
source: 待确认
source_version: 待确认
zotero_collection: 待确认
zotero_item_key: 待确认
zotero_attachment_key: 待确认
pdf_attachment_name: 待确认
doi: 待确认
topics: []
methods: []
datasets: []
metrics: []
claims: []
gaps: []
tags:
  - paper
---

# {{title}}

保留来源、阅读覆盖、关键证据、限定结论及未决影响；栏目合并不减少原文阅读或必要细节。删去不适用的空项，已在元数据/E#记录的信息引用即可，不另写第二份摘要。新建页用本模板；旧页局部修订保留原结构、标题与证据ID。页面状态含义见hard_memory。

## Metadata and Sources

元数据中的题名、作者、年份、标识等不在正文逐项重抄；这里补充可追溯的来源映射：
- Primary source and version: 实际路径/标识；正式版、预印本或解析缓存的对应关系
- Other materials: PDF / MinerU / translation / supplement / video（仅列实际使用或影响结论的材料）
- Source limitations: 缺失来源及其影响；非Zotero来源省略不适用的Zotero字段

## Reading and Verification Status

- Processing mode: new-ingestion / full-review / local-revision
- Sections read:
- Figures/tables/formulas rechecked:
- Supplement/video status:
- Missing material and affected conclusions: 可引用下方具体E#/未决项
- Scope covered by `review_status`: 局部已核不能推定整页checked

## Research Problem and Contribution

- Research problem and significance:
- Author-stated contribution / contribution supported by this reading: 分开表述
- Novelty status: author claim only / not assessed / confirmed within stated search scope（确认时附实际检索范围）

## Study Design

| Element | Details | Source |
|---|---|---|
| Objects/materials/data | | |
| Conditions and actual coverage | | |
| Controls/baselines | | |
| Metrics and operational definitions | | |
| Measurement/model and assumptions | | |
| Uncertainty/repeats/statistics | | |

记录理解主要判断所需的设计；未报告写“原文未报告”。领域扩展的必需记录在此或E#补充，不因模板简化省略；多个E#共用设计时引用本节，差异条件在各E#说明。

## Key Evidence

### E1

Evidence label: {{short evidence label}}

- Evidence type: direct observation/measurement / calculation/model / author interpretation / cited prior work / AI inference
- Object and conditions: 共用设计可引用上节，列出本条差异
- Metric and result: 定义、数值、单位、误差/近似性；注明实测、计算、图上估读或转引
- Source locator: section / figure / table / equation / PDF page（区分页序与印刷页码）
- Original data source / independence: 本文数据或共同转引来源；未知则注明
- Supports:
- Does not establish / alternative explanation:
- Verification status: 实际核查材料与范围；未决及其影响

按需追加E2、E3；已分配ID按根AGENTS第6节保持稳定。原始结果只在此记录一次，解释与限定结论在下节引用。单条核查范围不能代替页面review_status。

## Conclusions for Reuse

### Finding 1

- Finding / safe wording: 可直接复用的限定结论
- Evidence: E#（旧页可用已有等价定位）
- Support: sufficient / partial / insufficient — reason
- Applies to / exceptions: 必要对象、条件和边界
- Author interpretation:
- This reading's assessment: 与作者解释分开；AI推断明确标记
- Decision: retain / narrow / withdraw / pending — reason

每条重要结论在此评价一次，按需增加Finding；不把转引写成本文数据。摘要性文字最后写，如确有总览用途可加一至三句并回指Finding/E#，不要求另设Takeaway。当前任务涉及写作时，在对应Finding补用途/章节和使用前缺失证据，不再重抄同一结论。

## Limitations and Open Questions

- Author-stated limitation:
- Evidence-boundary limitation (`AI 推断`):
- Corpus gap / candidate question / field-gap search scope: 仅在有依据且与任务相关时记录

与E#/Finding相同的限制直接引用；主要局限必须保留，不强制生成gap。未做领域检索不能宣称领域空白；缺失材料造成的具体影响可统一记录在下节并回指相应证据。

## Downstream Review

- Updated within this task: 页面及改动关系；无则省略
- Needs review: 具体页面/论断、原因、来源及处置状态
- Unaffected after check: 仅记录实际已查范围；无相关下游时简短说明

只更新本轮范围内的直接依赖；未处理的已知错误不得继续当确定依据。方向借鉴保留原条件与接收评价。若没有下游问题，仍须在相应E#/Finding保留源证据本身的未决，不能将“无下游”当成“无未决”。

<!-- 可选扩展：确有比较/写作/详细精读需要时增加关系分析、推导或段落笔记；不限制必要细节。相关页优先在论述处链接或现有frontmatter中登记，不机械复制Linked Pages清单。完成核对使用templates/pdf_ingestion_template.md，收尾按根AGENTS第7节；不生成Maintenance勾选副本。 -->
