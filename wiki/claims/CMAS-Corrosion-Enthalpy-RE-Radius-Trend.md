---
type: claim
status: active
created: 2026-08-23
updated: 2026-08-23
source_papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: high（1300 °C 三体系一致）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
---

# CMAS 腐蚀产物形成焓与 RE 半径关联

## Claim

- CMAS 腐蚀产物的形成焓随 RE 离子半径增大而更负（更放热、更易形成），因此在 1300 °C 级温度下，小 RE 半径成分的 CMAS 抗蚀性更好（渗透深度/腐蚀层厚度更小）。

## Evidence

- Source paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]" Key Claims 2–3
- Source section/page/table/figure: 图 7（渗透深度）、图 15（DFT 形成焓）
- Evidence summary: 100 h 时 NdTaO4 渗透 196.4 μm vs ErTaO4 89.4 μm；DFT 显示 (Ca0.5RE0.5)2(Ta0.75Mg0.125Al0.125)2O7 固溶体形成焓随 RE 半径增大更负。
- Evidence strength: strong

- Source paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]" Key Claim 4
- Source section/page/table/figure: 图 13（腐蚀层厚度-平均半径关联）
- Evidence summary: 19 种 (5RE0.2)2Zr2O7 腐蚀层厚度与 RE 平均离子半径正相关；结合 Costa et al. 磷灰石热化学数据论证小半径磷灰石形成焓升高。
- Evidence strength: strong

- Source paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"（1300 °C 对照数据）
- Source section/page/table/figure: 图 18(a)
- Evidence summary: 1300 °C 下 RE2SiO5 渗透深度随 RE³⁺ 半径减小近线性减小，作者将其与 Ca2RE8(SiO4)6O2 形成焓关联（引 Costa et al.）。
- Evidence strength: strong

## Scope

- Applies to: 1300 °C 级温度；钽酸盐 RETaO4（渗透深度）、高熵稀土锆酸盐（腐蚀层厚度）、RE2SiO5 单硅酸盐（渗透深度）。
- Does not apply to: 1500 °C 级 RE2SiO5（该温度下规律弱化甚至方向反转，见 "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"）。
- Conditions: 判据为渗透深度或腐蚀层厚度；形成焓数据来自 DFT 简化成分模型或 Costa et al. 磷灰石热化学数据。

## Supporting Papers

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Evidence: 渗透深度-RE 半径单调正相关（4 个时长）+ DFT 形成焓 + 润湿性实验三重证据。
  - Notes: 润湿性证据方向与渗透深度一致（大半径端 CMAS 完全反应、接触角极小）。

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: 腐蚀层厚度-RE 平均半径正相关（19 成分大样本）。
  - Notes: 结构类型与半径高度相关，无法单独归因于半径（见 "[[wiki/gaps/Structure-Radius-Decoupling]]"）。

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: 1300 °C 对照渗透深度-半径关联。
  - Notes: 该论文主实验在 1500 °C，1300 °C 数据为对照。

## Challenging or Limiting Evidence

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Challenge: 1500 °C 下 RE2SiO5 渗透深度随 RE³⁺ 半径减小仅缓慢增加——方向与 1300 °C 相反，规律弱化。
  - Evidence: 图 18(a)；FactSage 粘度计算（图 16）。

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]" 引言引述文献
  - Challenge: 文献报道 X1-RE2SiO5 的反应区宽度随 RE³⁺ 半径减小而增加（即小半径反应更剧烈），与本 claim 方向相反。
  - Evidence: #47 引言（原始文献未读，待核查）。

## Use in Review Writing

- Possible section: 综述中「RE 成分对 CMAS 抗蚀性的调控规律」核心段落。
- Possible sentence role: background（1300 °C 规律）+ contrast（1500 °C 反转）
- Citation need: 三篇论文 + Costa et al. 热化学原始文献

## Related Pages

- Papers: 三篇已入库 CMAS 论文
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"、"[[wiki/gaps/Structure-Radius-Decoupling]]"
- Reviews:

## Uncertainty

- 待确认：该规律是否为 CMAS 腐蚀的普适热力学规律（主题 Main Question 1）。
- 待核查：X1-RE2SiO5 反应区宽度-RE 半径关系的原始文献。
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
