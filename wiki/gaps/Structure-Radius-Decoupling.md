---
type: gap
status: open
created: 2026-08-23
updated: 2026-08-23
priority: high
evidence_strength: strong
papers:
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
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

## Why It Matters

- 若结构贡献占主导，成分设计应优先「选结构」（无序化）；若半径贡献占主导，则应优先「选小半径」。二者给出不同的高熵成分筛选准则，直接影响 TBC 高熵化设计路线（也与主题页争议「RE 半径影响方向因体系而异」相关——该争议可能实质是结构效应混杂）。

## Supporting Evidence

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: S1–S12 全为烧绿石、S13–S19 全为缺陷萤石——结构与平均半径完全共线（#18 自述未设计解耦实验）；作者以「动力学+热力学双重机制」定性解释，未定量拆分。
  - Source section/page/table/figure: §3.3、Potential Gaps 3
  - Evidence strength: strong

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

- Papers: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Claims: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"、"[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
- Reviews:

## Uncertainty

- 待确认：无
- 待核查：无
- AI 推断：解耦实验的具体成分设计可行性。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Evidence strength marked.
- [x] Related open question updated if needed.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
