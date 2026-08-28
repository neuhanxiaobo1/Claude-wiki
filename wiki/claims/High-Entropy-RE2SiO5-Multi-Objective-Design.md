---
type: claim
status: active
created: 2026-08-27
updated: 2026-08-27
source_papers:
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: medium-high（热物性数据 strong；负 Grüneisen 机理为推断）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# 高熵 RE2SiO5 元素功能分工多目标设计

## Claim

- 四元高熵 (Ho0.25Lu0.25Yb0.25Eu0.25)2SiO5 通过元素功能分工（Lu/Yb 保 CMAS 抗性与低 TEC、Ho 保力学与隔热、Eu 通过 Eu2+ 引入氧空位）同时实现：热导 1.07–1.47 W/mK（接近 κmin=0.99）、TEC (4.0–5.9)×10⁻⁶/K 匹配 SiC、良好 CMAS 抗性（渗透 125.4 μm，优于 Ho/Eu 单硅酸盐与四元平均）；TEC 降低归因于严重晶格畸变经负 Grüneisen 参数声子的贡献。

## Evidence

- Source paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]" Key Claims 1–3
- Source section/page/table/figure: LFA 热导、DIL 膨胀、XPS（Eu 价态）、α⁻¹-T 拟合、多面体畸变定量
- Evidence summary: 热导 1.07–1.47 W/mK（600 °C 时 1.07，κmin=0.99）；TEC (4.0–5.9)×10⁻⁶/K 匹配 SiC (4.5–5.5)；畸变 [REO7] 3.975‰、[REO6] 4.499‰、[SiO4] 2.531‰ 均系列最高；XPS 证实 Eu3+/Eu2+ 共存；α⁻¹-T 截距 953150（系列第二大，点缺陷浓度高）。
- Evidence strength: strong（性能数据）／ medium（机理：负 Grüneisen 声子、元素功能分工为设计解释）

## Scope

- Applies to: 四元等摩尔高熵 RE2SiO5（X2 相，C2/c）。
- Does not apply to: 其他 RE 组合/比例未验证；1500 °C 行为未知。
- Conditions: 等摩尔设计下 CMAS 抗性未超过 Lu/Yb 单组分——「分工」有效但「最优」未达。

## Supporting Papers

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Evidence: 高熵样品与四种单组分同条件系统对比（热物性 + 腐蚀）。
  - Notes: 渗透深度排序 Lu(40.2) < Yb(75.1) < HE(125.4) < Ho(166.5) < Eu(248.6)，与平均 RE 半径排序一致（支持半径规律，见 "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"）；HE 略优于四元平均（132.6），熵效应贡献有限。

## Challenging or Limiting Evidence

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Challenge: 高熵样品 CMAS 抗性劣于 Lu2SiO5/Yb2SiO5——高熵化未在所有目标上同时达到单组分最优。
  - Evidence: 同条件渗透深度对比。
- Paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Challenge: Lu2SiO5 在 1500 °C 相分解失效；高熵样品高温相稳定性与分解行为未知，元素分工策略的 1500 °C 有效性待验证。
  - Evidence: #16 无 CMAS 对照分解实验（1500 °C）。

## Use in Review Writing

- Possible section: 「EBC 多目标设计策略（高熵 vs 单组分）」段落。
- Possible sentence role: background（高熵设计策略）+ gap（成分优化、1500 °C 验证）
- Citation need: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"

## Related Pages

- Papers: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
- Reviews:

## Uncertainty

- 待确认：元素功能分工的定量归因（各元素对性能的独立贡献未做对照剥离）。
- 待核查：MinerU OCR 数值（畸变值、α⁻¹-T 截距、XPS 峰位）引用前与原文核对。
- AI 推断：RE 比例优化（提高 Lu/Yb 占比）能否逼近 Lu2SiO5 抗性；高熵化的 1500 °C 相稳定性。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
