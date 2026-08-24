---
type: claim
status: active
created: 2026-08-23
updated: 2026-08-23
source_papers:
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: high（19 成分系统数据）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
---

# 缺陷萤石结构 CMAS 抗蚀双重机制

## Claim

- 小平均半径的缺陷萤石结构高熵稀土锆酸盐 CMAS 抗蚀最佳（腐蚀层 20–70 μm，远薄于 YSZ 150–200 μm 与 Gd2Zr2O7 80–120 μm），源于双重机制：动力学上无序结构缺乏低能扩散通道、抑制离子输运；热力学上小 RE 半径使磷灰石 Ca2RE8(SiO4)6O2 形成焓升高、析出不利。

## Evidence

- Source paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]" Key Claims 4–5
- Source section/page/table/figure: 图 11（截面腐蚀层对比）、图 13（厚度-平均半径关联）
- Evidence summary: 19 种 (5RE0.2)2Zr2O7 中 S13–S19 缺陷萤石（Fm3m）腐蚀层显著薄于 S1–S12 烧绿石；腐蚀层厚度与 RE 平均离子半径正相关；棒状磷灰石主要分布于残余 CMAS、球形 ZrO2 富集于反应前沿；热力学论证引 Costa et al. 磷灰石热化学数据。
- Evidence strength: strong

## Scope

- Applies to: 1300 °C/5 h 单一腐蚀条件；(5RE0.2)2Zr2O7 五元等摩尔高熵锆酸盐。
- Does not apply to: 时间演化与更高温度行为未验证（"[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"）；结构与半径效应未解耦（"[[wiki/gaps/Structure-Radius-Decoupling]]"）。
- Conditions: 结构判据为 Subramanian 半径比（1.46–1.78 烧绿石，<1.46 缺陷萤石）。

## Supporting Papers

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: 19 成分系统腐蚀层数据 + 结构与半径定量关联。
  - Notes: 烧绿石反应剧烈（表面颗粒状产物多）、缺陷萤石温和（棒状产物少）——形貌证据与双重机制一致。

## Challenging or Limiting Evidence

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Challenge: 本文中结构类型与 RE 半径高度相关（小半径 → 缺陷萤石），无法区分「结构贡献」与「半径贡献」；作者的双重机制解释未设计解耦实验。
  - Evidence: #18 自身 Potential Gaps 3；S1–S12 全为烧绿石、S13–S19 全为缺陷萤石。

## Use in Review Writing

- Possible section: 高熵 TBC 的 CMAS 抗性设计原则；「选结构」vs「选半径」权衡。
- Possible sentence role: background + gap 引出（解耦实验缺失）
- Citation need: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"

## Related Pages

- Papers: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/Structure-Radius-Decoupling]]"
- Reviews:

## Uncertainty

- 待确认：动力学（无序抑制输运）与热力学（形成焓）两机制各自的相对贡献未定量。
- 待核查：ZrO2 球形颗粒的形成机制（#18 未深入讨论，AI 推断）。
- AI 推断：双重机制的相对权重。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
