---
type: claim
status: active
created: 2026-08-27
updated: 2026-08-27
source_papers:
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
topics:
  - "[[wiki/topics/Thermal Barrier Coatings]]"
methods:
datasets:
metrics:
confidence: strong（粉末反应 + 扩散偶 + 热物性三重证据链，单篇）
tags:
  - claim
  - ceramics
  - corrosion
  - tbc
---

# Hf6Ta2O17 与 TGO（Al2O3）的高温热化学不相容

## Claim

- >1400 °C 时 Hf6Ta2O17 与 Al2O3（粘结层 TGO 主相）发生固相反应生成 AlHf3TaO10（Pbcn，与 HfTiO4 同构，约 9.2% 体积膨胀）；反应由 Al 单向扩散驱动（Al2O3 侧形成 Kirkendall 空洞），AlHf3TaO10 低 CTE（4.31×10⁻⁶/K）导致界面热应力达 880–1031 MPa、超出 YSZ 许用范围（330–862 MPa）——Hf6Ta2O17 基 TBC 存在 TGO 相容性短板，修正 Li et al.（2011）「无反应」结论。

## Evidence

- Source paper: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]" Key Claims 1–4
- Source section/page/table/figure: 粉末反应 XRD（1300–1600 °C/10 h）、Rietveld 精修、扩散偶层厚（2.93–4.61 μm）、EDS 成分梯度、CTE/E 实测、应力估算、Bramfitt 错配度
- Evidence summary: 1300 °C 无反应；>1400 °C 生成 AlHf3TaO10（Eq 2）；扩散偶 1400 °C/10–50 h 层厚递增；Al 含量跨界面 90.0→16.6 at%；界面热应力 Al2O3/AlHf3TaO10 880.6 MPa、Hf6Ta2O17/AlHf3TaO10 1030.8 MPa（Al2O3/Hf6Ta2O17 直接界面仅 272.6 MPa）；Bramfitt ε=27.5%（>15% 非共格）。
- Evidence strength: strong

## Scope

- Applies to: Hf6Ta2O17-Al2O3 体系，>1400 °C（粉末实验 1300–1600 °C；扩散偶 1400 °C）。
- Does not apply to: ≤1300 °C（无反应）；其他 TBC 候选材料-TGO 组合未覆盖。
- Conditions: 块体扩散偶几何；热应力为简化一维弹性估算（未考虑蠕变松弛与成分梯度）。

## Supporting Papers

- Paper: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Evidence: 粉末反应 + 扩散偶 + 热物性三重证据。
  - Notes: 论文给出失效机制示意（Fig 12）：反应层形成 → 体积膨胀 + 热失配应力 → 界面开裂/剥落风险。

## Challenging or Limiting Evidence

- Paper: Li et al.（2011, Key Eng. Mater.，未入库）
  - Challenge: 曾报道 Hf6Ta2O17 与 Al2O3 无反应。
  - Evidence: 被本文系统实验修正（可能因其温度未达反应阈值或表征不充分，原文实验条件待核查）。
- 限制：扩散偶为块体-块体，真实涂层中 TGO 为 μm 级薄层，反应动力学与应力状态可能不同；无涂层体系循环氧化验证。

## Use in Review Writing

- Possible section: 「TBC 选材判据与 TGO 相容性」段落。
- Possible sentence role: background（相容性判据）+ gap（扩散障/改性粘结层）
- Citation need: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"

## Related Pages

- Papers: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
- Topics: "[[wiki/topics/Thermal Barrier Coatings]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
- Reviews:

## Uncertainty

- 待确认：反应层对真实 TBC 体系（TGO 薄层、涂层应力状态）的定量影响。
- 待核查：Li et al.（2011）原文实验条件；MinerU OCR 中晶格参数与应力数值引用前核对。
- AI 推断：扩散障层（如 HfO2 基）缓解不相容的可行性。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
