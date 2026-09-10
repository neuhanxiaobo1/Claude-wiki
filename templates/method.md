---
direction_id: "{{direction_id}}"
type: method
status: active
review_status: draft
created: 待确认
updated: 待确认
papers: []
topics: []
datasets: []
metrics: []
claims: []
gaps: []
tags:
  - method
---

# {{method}}

Method 页面描述可重复使用的实验、计算、数据处理或综合方法。材料体系、物理机制、观察结果和评价指标本身不应仅因在方法段出现就建成 method 页面。

## Method Identity

- Canonical name:
- Aliases:
- Method type: experiment / characterization / calculation / data analysis / synthesis protocol
- Purpose and output:
- Unit of analysis/sample:
- Distinguishing features from related methods:

## Procedure and Inputs

| Step/component | Input or setting | Output | Source |
|---|---|---|---|
|  |  |  |  |

- Required equipment/software/data:
- Calibration/reference:
- Key parameters that affect interpretation:
- Reported but unverified procedural details:

只保存理解复现性和结果解释所需的信息。若不同论文使用同名但操作定义不同，应记录变体，不静默合并。

## Assumptions and Measurement Model

- Assumption:
  - Role:
  - Evidence/source:
  - Failure risk:
- Operational definition:
- Detection/resolution boundary:
- Calculated or inferred quantities and model assumptions:

计算结果、拟合参数和代理指标须说明如何从输入得到，不能当作直接测量。

## Variants

| Variant | Difference | Compatible outputs | Papers | Merge/comparison note |
|---|---|---|---|---|
|  |  |  |  |  |

## Validated Uses

| Use case | Evidence | Conditions/sample | What was established | Verification |
|---|---|---|---|---|
|  | [[D/wiki/papers/Paper]]#E1 |  |  | checked / partial / pending |

“被论文使用”不等于“方法有效”。Validated Uses 应链接具体证据，说明方法在什么条件下回答了什么问题。

## Strengths and Limitations

### Strengths

- Strength:
  - Evidence:
  - Applies under:

### Limitations

- Limitation:
  - Evidence or methodological reason:
  - Affected output/claim:
  - Mitigation:

不得把作者未讨论的优势写成事实；由本次分析提出时标 `AI 推断`。未检出、局部采样和分辨率限制应与相应结果相连。

## Comparison With Other Methods

| Method | Same problem/output? | Comparable conditions? | Difference | Supported advantage/tradeoff | Evidence |
|---|---|---|---|---|---|
|  | yes / partial / no | direct / qualitative / not comparable |  |  |  |

只有目标、输出定义和条件足够一致时才能声称精度、速度或效果更好；其余写适用场景差异。

## Misuse Boundaries

- This method can establish:
- This method alone cannot establish:
- Common interpretation error:
- Required complementary evidence:

## Downstream Review

- Updated claims/pages:
- Needs review: page + affected statement + reason
- Method variants or aliases needing resolution:

## Related Pages

- Topics:
- Papers:
- Datasets:
- Metrics:
- Claims:
- Gaps:
- Reviews:

## Maintenance

- [ ] Page represents a reusable method rather than a result, mechanism or metric.
- [ ] Procedure, inputs, outputs, assumptions and operational definitions are explicit.
- [ ] Validated uses link to specific paper evidence.
- [ ] Same-name variants and comparison eligibility were checked.
- [ ] Calculated/inferred outputs are separated from direct measurements.
- [ ] Limitations connect to affected claims and detection boundaries.
- [ ] Index/log/tags/aliases were updated only when applicable.


<!-- 方向约定：仅在已选方向D内生成；展开direction_id与D/路径。领域额外栏目只从D/AGENTS.md声明的扩展读取，不加载其他方向模板。 -->
