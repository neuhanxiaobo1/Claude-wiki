---
direction_id: "{{direction_id}}"
type: claim
status: active
review_status: draft
created: 待确认
updated: 待确认
source_papers: []
topics: []
methods: []
datasets: []
metrics: []
tags:
  - claim
---

# {{claim}}

一个 claim 只表达一个可检验判断。实验趋势、机制解释、筛选建议和服役预测通常应拆成不同 claim。删除空栏目，不为填模板增加无证据内容。

## Claim Statement

- Statement:
- Claim type: descriptive result / association / causal mechanism / model prediction / design implication
- Assessment: supported / partially-supported / insufficient-evidence / contested
- Review status: draft / checked / needs-review

`Assessment` 评价当前证据对这一条判断的支持；`Review status` 表示页面是否完成声明范围内的复核。二者不能由论文数量、期刊等级或页面链接数量自动决定。

## Scope and Definitions

- Applies to:
- Conditions:
- Population/material/system:
- Metric and operational definition:
- Does not establish / excluded scope:

没有条件和指标仍能改变含义的 claim 不得标为 supported。机制或因果 claim 必须明确因变量、解释变量及关键控制条件。

## Evidence Ledger

每条证据引用 paper 页面中的 `E#` 或等价的具体原文定位。相同原始数据被多篇论文转引时使用同一 `independence_group`；这只算一个独立数据来源。

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[D/wiki/papers/Paper]]#E1 | support / challenge / limit | direct / calculated / author interpretation / cited prior work | dataset-or-experiment-1 |  |  | checked / partial / pending |

### Evidence Notes

- E#：说明证据为何与 claim 相符或不相符，以及是否存在指标、条件或来源身份问题。
- Independence：不同试样、重复实验或不同论文并不自动独立；按原始数据和实验来源判断。论文转引应回指原始来源，未读原始文献时保留 `pending`。

## Assessment Rationale

- Directly established:
- Partially established:
- Not established:
- Key assumptions / alternative explanations:
- Reason for current assessment:

单篇研究可以充分支持一个限定事实。多篇非独立转引不能提升支持程度；计算和作者解释可以支持相应类型的判断，但不能冒充直接测量。

## Challenging or Limiting Evidence

- Evidence:
- Apparent or directly comparable conflict:
- Difference in conditions/metric/source:
- Effect on claim: none / narrows scope / lowers support / overturns

遇到相反排序时，先检查指标定义、坐标方向、实验条件和数据独立性，再判断是否构成真实冲突。

## Revision History and Downstream Review

- Current revision reason:
- Supersedes or narrows:
- Downstream pages updated:
- Downstream pages needing review: page + affected statement + reason

来源证据变化后，旧 claim 在复核前不得继续作为确定论据。只标记受影响判断，不将整篇论文或整个主题笼统判为无效。

## Use in Synthesis or Review

- Safe wording:
- Required conditions/citation:
- Suitable role: background / comparison / limitation / mechanism / design implication
- Must not be used to claim:

只有 `Assessment: supported` 且 `Review status: checked` 的 claim 才可直接作为确定性综述论据。其他状态可用于描述争议、局限或待验证假设，并明确其状态。

## Related Pages

- Papers:
- Topics:
- Methods:
- Datasets:
- Metrics:
- Gaps:
- Reviews:

## Maintenance

- [ ] Claim contains one testable proposition and explicit scope.
- [ ] Evidence type, support, verification and independence are separated.
- [ ] Every key evidence entry resolves to a paper E# or original locator.
- [ ] Common-source citations are not counted as independent replication.
- [ ] Challenging evidence and comparability were assessed.
- [ ] Downstream impact is recorded when evidence or wording changes.
- [ ] Index/log/tags/aliases were updated only when applicable.


<!-- 方向约定：仅在已选方向D内生成；展开direction_id与D/路径。领域额外栏目只从D/AGENTS.md声明的扩展读取，不加载其他方向模板。 -->
