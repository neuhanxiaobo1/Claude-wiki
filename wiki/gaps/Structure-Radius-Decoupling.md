---
type: gap
status: open
created: 2026-08-23
updated: 2026-08-28
priority: high
evidence_strength: strong
papers:
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
---

# 结构类型与 RE 半径对 CMAS 抗性的解耦

## Gap Description

- 高熵锆酸盐中「缺陷萤石优于烧绿石」的 CMAS 抗蚀结论与「小平均半径更优」的规律高度共线（小半径 → 缺陷萤石），结构类型与 RE 半径对 CMAS 抗性的贡献尚未解耦，双重机制（动力学无序输运抑制 vs 热力学形成焓）的相对权重未知。
- 同一问题在 RE2SiO5 单硅酸盐体系以另一种形式存在：1300 °C 半径规律出现晶型依赖的翻转——X1 大半径系列（La/Nd/Sm/Eu/Gd）内部反应区宽度随 RE³⁺ 半径减小而增加（#47 引言引文 [18] = Tian et al., JECS 2019，未入库），而 X2 段（Tb–Lu，含 #36 的 8 组分系统数据）衰退层厚度随半径减小而变薄。同是「结构（晶型）与半径」，X1/X2 翻转的证据使该解耦问题的范围从锆酸盐（烧绿石/缺陷萤石）扩展到硅酸盐（X1/X2）。

## Why It Matters

- 若结构贡献占主导，成分设计应优先「选结构」（无序化/晶型）；若半径贡献占主导，则应优先「选小半径」。二者给出不同的成分筛选准则，直接影响 TBC 高熵化与 EBC 单硅酸盐成分设计路线（也与主题页争议「RE 半径影响方向因体系而异」直接相关——该争议可能实质是结构效应混杂）。

## Supporting Evidence

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: S1–S12 全为烧绿石、S13–S19 全为缺陷萤石——结构与平均半径完全共线（#18 自述未设计解耦实验）；作者以「动力学+热力学双重机制」定性解释，未定量拆分。
  - Source section/page/table/figure: §3.3、Potential Gaps 3
  - Evidence strength: strong

- Paper: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"（X1/X2 翻转的 X2 侧证据）
  - Evidence: 8 种 RE2SiO5（Tb–Lu，X2 段为主）衰退层厚度随半径减小近似线性变薄（Fig. 11）；#47 引言引文 [18]（Tian et al., JECS 2019, DOI 10.1016/j.jeurceramsoc.2018.12.015，X1 系列 La/Nd/Sm/Eu/Gd）报道 X1 内部反应区宽度随半径减小而增加——同一 1300 °C、同一研究组，方向随晶型翻转。#36 大半径组（Tb/Dy/Ho）晶型归属未在原文明确（待核查），若为 X1 则 X1/X2 边界处趋势衔接需澄清。
  - Source section/page/table/figure: #36 Fig. 11；#47 引言（引文 [18]/[25]）
  - Evidence strength: strong（翻转现象有独立文献佐证，晶型归属细节待核查）

## Cross-Page Basis

- Page: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - What it shows: 缺陷萤石抗蚀最佳的双重机制解释。
  - Why it supports this gap: 该 claim 的 Challenging Evidence 明确指出结构与半径未解耦——claim 成立的前提正是本 gap 的求解。

## Gap Type

- Type: 真实 gap
- Reason: #18 作者自认未解耦；三篇入库论文中无一包含解耦设计。

## How Existing Work Handles It

- Existing approach:
  - Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Remaining limitation: 19 成分中结构与半径天然共线；无同半径异结构或同结构异半径对照组。

## What Remains Unsolved

- Unsolved part: 同平均半径下缺陷萤石 vs 烧绿石的 CMAS 抗性差异；同结构下半径变化的独立效应。
- Why unresolved: 高熵体系成分自由度大，设计正交对照组需精细的成分-结构相图知识；高通量方法尚未覆盖结构-半径正交设计。

## Possible Research Questions

- Question: 固定 RE 平均半径、通过成分组合改变有序度（或反之），CMAS 抗蚀性如何变化？
  - Feasibility: medium（依赖相图知识设计正交成分，实验可行）
  - Evidence needed: 正交设计成分组 + 腐蚀层厚度数据。

## Possible Research Paths

- Path: 利用「同半径异结构」组合（如调整 RE 池组成使 r(RE³⁺)/r(Zr⁴⁺) 跨越 1.46 临界但平均半径接近）。
  - Required method/data: 高通量制备 + XRD/Raman 定结构 + CMAS 腐蚀截面定量。
  - Risk: 可设计的成分组数量有限，正交性难以完全保证。

## Risks and Counter-Evidence

- Risk: 解耦后发现结构效应远小于半径效应，gap 的优先级下降。
  - Evidence: #46 钽酸盐体系（无烧绿石/萤石之分）同样呈现半径依赖，暗示半径效应本身独立存在——但钽酸盐与锆酸盐不可直接类比。
  - How to check: 优先做小规模正交预实验。

## Related Pages

- Papers: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"、"[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Claims: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"、"[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
- Reviews:

## Uncertainty

- 待确认：无
- 待核查：#36 大半径组（Tb/Dy/Ho）晶型归属；#21（Tian et al., JECS 2019，X1 系列）原文数值（未入库）。
- AI 推断：解耦实验的具体成分设计可行性。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Evidence strength marked.
- [x] Related open question updated if needed.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
