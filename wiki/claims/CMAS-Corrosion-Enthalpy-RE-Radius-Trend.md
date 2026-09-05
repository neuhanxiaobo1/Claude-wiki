---
type: claim
status: active
created: 2026-08-23
updated: 2026-08-28
source_papers:
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: high（1300 °C 三体系一致 + #36 奠基性单组分 8 组分数据，六篇独立支持）
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

- Source paper: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]" Key Claims 1–2
- Source section/page/table/figure: Fig. 11（衰退层厚度-RE 半径关系）、Table 2（光学碱度计算）、Risbud et al. 量热数据（ref [15]）
- Evidence summary: 8 种 RE2SiO5（Tb, Dy, Ho, Er, Y, Tm, Yb, Lu）在 1300 °C/50 h 的衰退层厚度随 RE 离子半径（CN=6）减小而近似线性变薄（Lu2SiO5 约 50 μm/50 h → 约 79 μm/100 h）；机制归因于 Ca2RE8(SiO4)6O2 磷灰石形成焓随半径减小更吸热，光学碱度差 ΔΛ(RE2SiO5−CMAS) 从 Tb 0.134 线性降至 Lu 0.094。
- Evidence strength: strong（本 claim 的奠基性系统数据）

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

- Applies to: 1300 °C 级温度；钽酸盐 RETaO4（渗透深度）、高熵稀土锆酸盐（腐蚀层厚度）、RE2SiO5 单硅酸盐（渗透深度；#36 以衰退层厚度为指标）。
- Does not apply to: 1500 °C 级 RE2SiO5（该温度下规律弱化甚至方向反转，见 "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"）。
- Conditions: 判据为渗透深度或腐蚀层厚度；形成焓数据来自 DFT 简化成分模型或 Costa et al. 磷灰石热化学数据。

## Supporting Papers

- Paper: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - Evidence: 8 种 RE2SiO5 衰退层厚度-RE 半径近似线性关系（Fig. 11）+ Risbud 形成焓 + 光学碱度判据三重证据。
  - Notes: 单组分单硅酸盐体系的奠基数据；三组分类（剧烈/中等/缓和）与 100 h 延长验证；大半径组（Tb/Dy/Ho）晶型归属待核查（见本页 Uncertainty）。

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Evidence: 渗透深度-RE 半径单调正相关（4 个时长）+ DFT 形成焓 + 润湿性实验三重证据。
  - Notes: 润湿性证据方向与渗透深度一致（大半径端 CMAS 完全反应、接触角极小）。

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: 腐蚀层厚度-RE 平均半径正相关（19 成分大样本）。
  - Notes: 结构类型与半径高度相关，无法单独归因于半径（见 "[[wiki/gaps/Structure-Radius-Decoupling]]"）。

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: 1300 °C 对照渗透深度-半径关联。
  - Notes: 该论文主实验在 1500 °C，1300 °C 数据为对照。

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Evidence: 1300 °C/20 h 渗透深度排序 Lu(40.2) < Yb(75.1) < 高熵(125.4) < Ho(166.5) < Eu(248.6)，与 RE³⁺ 平均半径排序完全一致。
  - Notes: 高熵样品按平均半径（0.894 Å）恰好落在 Yb（0.868）与 Ho（0.901）之间——半径规律在固溶体/高熵体系同样成立；同时给出固溶体半径调控的设计含义。

- Paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Evidence: 1300 °C 下 Lu2SiO5（最小半径）抗蚀最优（渗透约 50 μm），作者直接引用 Costa et al. 形成焓数据解释。
  - Notes: 该论文主实验在 1500 °C（Lu2SiO5 失效，见 "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"）；1300 °C 数据为对照且与本 claim 一致。

## Challenging or Limiting Evidence

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Challenge: 1500 °C 下 RE2SiO5 渗透深度随 RE³⁺ 半径减小仅缓慢增加——方向与 1300 °C 相反，规律弱化。
  - Evidence: 图 18(a)；FactSage 粘度计算（图 16）。

- Paper: #47 引言引述文献 [18]（已锁定为 Tian et al., J. Eur. Ceram. Soc. 39 (2019) 1463–1476, DOI 10.1016/j.jeurceramsoc.2018.12.015，X1 系列 La/Nd/Sm/Eu/Gd，未入库）
  - Challenge: 文献报道 X1-RE2SiO5 的反应区宽度随 RE³⁺ 半径减小而增加（即小半径反应更剧烈），与本 claim 方向相反。
  - Evidence: #47 引言原文（引文 [18]）；2026-08-28 经 #47 MinerU 缓存核对锁定来源。注意：该反向趋势仅限 X1 大半径系列内部；#36（Tian et al., Corros. Sci. 2019，引文 [25]）覆盖 Tb–Lu 段为递减趋势——1300 °C 半径规律存在晶型依赖的翻转（见 "[[wiki/gaps/Structure-Radius-Decoupling]]"）。

- Paper: #59（Zheng, Ming, Tian et al., Extreme Materials 2025, 1(4): 27–32, DOI: 10.1016/j.exm.2025.10.001，已核实未入库，MinerU 缓存 10185）
  - Challenge: 层叠法统一条件下 1300 °C/20 h 的 CMAS 渗透深度排序非单调：Er2SiO5 最浅，Tm 次之，Y/Lu/Yb 相当且深于 Er，Tb/Dy 最深。产物量仍随 RE 半径减小而减少（与形成焓规律一致），但以「渗透深度」为指标时小半径端（Lu）并非最优。
  - Evidence: #59 Fig. 7 + 残余 CMAS 成分（Table S1）；作者解释为溶解-析出协同（小半径 RE 溶解强、析出弱，残余熔体中 RE 含量高）——「抗蚀评价需综合产物形成能力、基体溶解与 CMAS 渗透三因素」。

## Use in Review Writing

- Possible section: 综述中「RE 成分对 CMAS 抗蚀性的调控规律」核心段落。
- Possible sentence role: background（1300 °C 规律）+ contrast（1500 °C 反转）
- Citation need: 六篇已入库 CMAS 论文 + Costa et al. / Risbud et al. 热化学原始文献

## Related Pages

- Papers: 六篇已入库 CMAS 论文（#36、#47、#46、#18、#16、#48）
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"、"[[wiki/gaps/Structure-Radius-Decoupling]]"
- Reviews:

## Uncertainty

- 待确认：该规律是否为 CMAS 腐蚀的普适热力学规律（主题 Main Question 1）。
- 待核查：X1-RE2SiO5 反应区宽度-RE 半径关系原始文献的原文数值（已锁定来源：Tian et al., JECS 2019, DOI 10.1016/j.jeurceramsoc.2018.12.015，未入库）；#36 大半径组（Tb/Dy/Ho）的晶型归属（X1 或 X1/X2 混合）——若为 X1，则 #36 内部的 Tb→Ho 递减趋势与 X1 系列（La→Gd）的递增趋势之间如何衔接需澄清。
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
