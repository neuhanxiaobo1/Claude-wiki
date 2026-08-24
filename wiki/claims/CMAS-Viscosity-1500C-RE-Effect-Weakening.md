---
type: claim
status: active
created: 2026-08-23
updated: 2026-08-23
source_papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: medium（单篇、单体系覆盖）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# 1500 °C CMAS 粘度剧降致 RE 效应弱化

## Claim

- 1500 °C 时 CMAS 粘度降至 1300 °C 的 1/4 以下，传质与腐蚀反应加速，使 RE 种类对 CMAS 抗蚀性的影响弱化；且 RE2SiO5 的渗透深度-RE³⁺ 半径关系在 1500 °C 出现方向反转（大 RE 阳离子抗性更好），区别于 1300 °C 的小半径优势。

## Evidence

- Source paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]" Key Claims 3–4
- Source section/page/table/figure: 图 16（FactSage 粘度）、图 18(a)（渗透深度对比）
- Evidence summary: FactSage 计算 1300 °C 粘度 >4 倍于 1500 °C；1300 °C 渗透深度随 RE³⁺ 半径减小近线性减小，1500 °C 时仅随半径减小缓慢增加、数据分散度小；大阳离子（Tb、Dy、Ho、Y、Er）体系形成致密产物层、界面平滑（图 18(b)）。
- Evidence strength: strong（对 #47 内部结论）／ medium（跨体系普适性）

## Scope

- Applies to: 1500 °C 级 CMAS 腐蚀（已证实：RE2SiO5 体系）。
- Does not apply to: 1300 °C（规律相反，见 "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"）。
- Conditions: 结论基于渗透深度判据 + FactSage 计算粘度（非实测）。

## Supporting Papers

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: 7 种 RE2SiO5 × 5/20/50 h 系统数据 + 原位观察 + FactSage 粘度。
  - Notes: 原位观察（Er2SiO5）显示 1500 °C 保温约 1 h 产物才缓慢析出，1300 °C 对照 2.5 h 无产物——反应速率差异的直接证据。

## Challenging or Limiting Evidence

- 无直接反驳证据；主要限制是覆盖范围：
  - 仅 RE2SiO5 单体系有 1500 °C 数据；钽酸盐、锆酸盐均为 1300 °C 数据（"[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"）。
  - 粘度来自 FactSage 计算而非实测；REO1.5 在 CMAS 中的溶解度差异为定性推断（#47 Limitations）。

## Use in Review Writing

- Possible section: 「温度对 RE 成分调控规律的影响」段落。
- Possible sentence role: contrast（与 1300 °C 规律对比）+ limitation（高温数据稀缺）
- Citation need: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"

## Related Pages

- Papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
- Reviews:

## Uncertainty

- 待确认：该规律在钽酸盐、锆酸盐体系中是否成立（主题 Main Question 2）。
- 待核查：MinerU OCR 粘度数值（1/4 以下）与原文核对。
- AI 推断：1500 °C 方向反转的机理（粘度-溶解度-反应动力学耦合）为定性推断。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
