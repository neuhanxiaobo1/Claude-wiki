---
type: gap
status: narrowed
review_status: checked
gap_type: candidate-question
novelty_status: not-assessed
created: 2026-08-23
updated: 2026-09-07
priority: pending
papers:
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
---

# 层叠筛选结果的独立试样可复现性与迁移边界

## Gap Statement

在已研究 RETaO₄ 层叠 CMAS 筛选条件下，层间接触和跨 RE 产物组成是否改变成分排序与产物归属，相对独立试样的偏差能否被量化？跨体系推广须以此类验证为依据。

- Current classification: candidate-question
- 边界：仅复用七篇复核源页与八项新版 claim；本轮未做领域新颖性检索。review_status: checked 指前提、分类和使用边界已核查，不表示问题已解答或实验可行性已确认。

## Origin and Preconditions

evidence boundary + AI inference。新版 RETaO₄ claim 支持产物类别，明确不支持层间完全化学独立。问题是测量/比较有效性，不是把层叠、并行制备与原位观察组合本身称为创新。

## Existing Coverage

| Work/evidence | What is already addressed / conditions | What remains | Independence / review status |
|---|---|---|---|
| [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E1]]；[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]] | 八 RE 十层试样已有同炉暴露与跨 RE 点成分 | Nd/Er 区域见其他 RE，影响来源和大小未被独立分离 | 本文实验；checked |
| [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]]；[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E5]] | 已报告深度及产物组成 | 误差棒不是仪器精度；阳离子归一化不是完全计量证明 | 本文实验；checked |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E1]]；[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]] | 19 组成并行制备/表征 | 不是层叠；样品映射问题影响回归，不能当作迁移验证 | checked；映射未决 |
| [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E3]]；[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E4]] | 高温原位观察提供时序信息 | 与批量筛选任务不同，不自动验证高通量或跨体系精度 | checked；视频未读 |

## Why It Matters

AI 推断：若层叠排序对邻层或位置敏感，后续选材可能误将实验配置差异当成材料差异。若独立复现成立，则可明确方法在所测边界内的用途；并不自动意味着其他材料体系适用或用户已选择方法开发。

## Novelty Assessment

- Novelty status: not-assessed。
- 本轮没有执行领域检索，不能声称“尚无人研究”“首次”或“领域普遍缺失”；旧 high/medium 和 strong 不能作为新颖性或选题优先级。
- 已有最接近工作及限制见上表。外部工作可能已解决问题，后续若要认定 scoped-field-gap，必须记录日期、检索源/检索式、纳排范围、最接近工作及反例。

## Research Question and Required Evidence

- 可检验问题（AI 推断）：保持相同名义烧结/腐蚀条件时，独立 RETaO₄ 试样与不同层序/邻层的层叠试样，是否给出一致的深度分布和产物类别？
- 所需证据与比较：需独立样品、层序/位置变换、腐蚀前后跨 RE 元素分布、微结构及相同测厚定义；记录重复数、样品间变异和预先确定的实用等效界限。不以差异不显著等同方法等效，也不把多个层片当独立重复。
- 回答或削弱前提的结果：若改变邻层/位置导致超出重复变异的系统变化，应限制原筛选排序并检查来源；若独立样品在预设等效界限内复现，则在所测条件下支持有效性，该候选问题可收窄或解决。

## Feasibility and Research Path

AI 推断：优先验证现有体系，再决定跨体系；需要可控层序制样、元素/相分布和重复暴露，不默认任意体系层间扩散程度。资源、成本和可实现对照尚待确认，可行性 pending。

## Risks, Alternative Explanations and Counter-Evidence

跨 RE 成分不能单独证明污染来源或已改变排序；几何、烧结历史与局部 CMAS 供给也可能造成差异。旧页 #36 实为已入库 2019 单硅酸盐，#48 亦已入库，撤回错误身份/待入库叙述。旧记录中的未复核跨体系候选（如 #59）仅是待查线索，不能据其肯定或否定领域新颖性。

## Status and Revision History

- 2026-09-07：status 改为 narrowed；用复核后的证据替换旧“真实 gap”及确定性机制前提，保留原路径。priority: pending 表示未完成研究价值、资源和新颖性排序。
- 本轮完成五项 gap 的前提与分类修订，并同步 index、计划和维护记录；未改原始资料或重新复核外部文献。
- 下游待复核：[[synthesis/open-questions]] 应替换旧问题前提与评级；[[synthesis/research-positioning]] 应撤回依赖旧 gap 的确定方向；[[synthesis/review-outline]]、[[synthesis/core-argument-map]] 和 [[synthesis/literature-map]] 应依据当前边界重组，不将候选当作已证领域结论。
- 相关主题正文仍待同步：[[wiki/topics/Ceramic Corrosion]]。源页/claim 历史 gap 待办由本轮修订接续；具体原文未决仍有效。

## Use in Positioning or Review

- Safe wording: 层叠筛选已产生可用的条件内结果，但跨 RE 组成使其与独立试样的一致性值得核验；跨体系迁移目前是候选验证方向，不能称尚无人实施的方法空白。
- 更强使用前提：先解决会改变论断的原始证据疑点，再按用户研究范围评估已有研究、可行性与新颖性；本页不是用户已确认的选题。
