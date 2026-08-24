---
type: claim
status: active
created: 2026-08-23
updated: 2026-08-23
source_papers:
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: high（证据链完整，澄清文献之争）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
---

# RETaO4 CMAS 腐蚀产物澄清：主产物为固溶体

## Claim

- RETaO4 与 CMAS 在 1300 °C 反应的主产物是 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 面心立方固溶体（而非简单的 Ca2Ta2O7 或硅酸盐相），另有少量 Ca2RE8(SiO4)6O2 磷灰石；两种产物同时出现在反应层与晶界，且晶界腐蚀在所有 RETaO4 中普遍存在（此前仅在 YTaO4 中报道）。

## Evidence

- Source paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]" Key Claims 1、4
- Source section/page/table/figure: 图 9–12（TEM/SAED/EPMA）、表 1、图 8（晶界腐蚀）
- Evidence summary: TEM-SAED 确认面心立方结构（(2̄22) 面间距 2.807 Å）；EPMA-WDS 定量 Ca+RE 与 Mg+Al+Ta 各约 50%，与固溶体模型一致；磷灰石 (033̄0) 面间距 2.720 Å；8 种 RETaO4 反应前沿均观察到晶界腐蚀产物。
- Evidence strength: strong

## Scope

- Applies to: 1300 °C、33CaO-9MgO-13AlO1.5-45SiO2 CMAS；8 种 RETaO4（RE = Nd, Sm, Eu, Gd, Dy, Ho, Y, Er）。
- Does not apply to: 更高温度（1500 °C）行为未验证（"[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"）。
- Conditions: 产物成分由 EPMA 平均组成定量；固溶体成分存在波动（Ca 0.65–1.11、RE 0.89–1.35）。

## Supporting Papers

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Evidence: TEM + EPMA 精确定量 + 反应式推演（(2-x)CaO + yMgO + z/2Al2O3 + xRETaO4 + (2-x-y-z)/2Ta2O5 → 固溶体）。
  - Notes: 层叠法在统一条件下同时验证 8 种成分，结论不受样品间差异影响。

## Challenging or Limiting Evidence

- Paper: 文献中早前报道（#46 引言引述）
  - Challenge: 文献对 YTaO4/RETaO4 CMAS 腐蚀产物长期存在矛盾结论（Ca2Ta2O7 vs 磷灰石 vs 固溶体）。
  - Evidence: #46 以 TEM+EPMA 精确定量澄清；主题页已标记该争议为「已澄清」。

## Use in Review Writing

- Possible section: RETaO4 TBC 的 CMAS 腐蚀机制；晶界腐蚀普遍性。
- Possible sentence role: background（争议回顾）+ 定论性陈述（#46 澄清）
- Citation need: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"

## Related Pages

- Papers: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps:
- Reviews:

## Uncertainty

- 待确认：固溶体产物形成的动力学路径（反应层与晶界产物是否同源）未深入讨论。
- 待核查：MinerU OCR 中固溶体化学式上下标与原文核对。
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
