---
type: gap
status: open
created: 2026-08-23
updated: 2026-08-27
priority: high
evidence_strength: strong
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
  - "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# 钽酸盐/锆酸盐体系 1500 °C 级 CMAS 腐蚀数据缺失

## Gap Description

- 1500 °C 下 CMAS 粘度剧降导致「RE 种类影响弱化」的现象目前在 RE2SiO5 体系已获两篇论文证实（#47 七体系 + #16 Lu2SiO5 单体系深度机制），且 #16 进一步揭示 1500 °C 相分解诱导晶间渗透的新失效机制；但 RETaO4（#46）、高熵锆酸盐（#18）、高熵 RE2SiO5（#48）的 CMAS 腐蚀数据均为 1300 °C 单一温度，无法验证「高温 RE 效应弱化」与「相分解」的跨体系普适性。

## Why It Matters

- 第三代 EBC/TBC 的服役温度正推向 1500 °C（HfO2–Si 粘结层使 EBC 使用温度升至 1482 °C 以上）；若「高温 RE 效应弱化」或「相分解诱导渗透」普适成立，则成分设计准则需按服役温度分级，1300 °C 下的小半径优选策略可能在高温失效。

## Supporting Evidence

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Evidence: 实验设计仅 1300 °C（§5），无温度梯度；作者未声明更高温度计划。
  - Source section/page/table/figure: §5、全文
  - Evidence strength: strong

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: CMAS 腐蚀为单一条件 1300 °C/5 h，无时间梯度与更高温度数据。
  - Source section/page/table/figure: §2.3
  - Evidence strength: strong

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: 该论文 1500 °C 数据（7 种 RE2SiO5）证实规律弱化/反转，但仅覆盖单硅酸盐一体系。
  - Source section/page/table/figure: 图 18(a)
  - Evidence strength: strong

- Paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Evidence: 1500 °C 下 Lu2SiO5 渗透 219 μm（1300 °C 的 >4 倍）且发生相分解——RE2SiO5 体系 1500 °C 数据已补强至「双论文 + 机制层面」，但该体系内其他成分的分解行为仍未知。
  - Source section/page/table/figure: 图 9、图 6/7
  - Evidence strength: strong

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Evidence: 高熵 RE2SiO5 仅 1300 °C/20 h 单条件腐蚀，无 1500 °C 数据；高熵样品的高温相稳定性（结合 #16 的分解发现）未知。
  - Source section/page/table/figure: §2 实验设计
  - Evidence strength: strong

## Cross-Page Basis

- Page: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - What it shows: 1500 °C 下 RE 效应弱化且方向反转，但证据强度仅 medium（单体系）。
  - Why it supports this gap: 该 claim 的普适性恰恰受本 gap 限制——二者互为表里。

## Gap Type

- Type: 真实 gap
- Reason: 三篇论文的实验设计明确缺失该数据（非推断）；1500 °C 实验存在客观难度（CMAS 流失、设备），但并非不可行（#47 已实现）。

## How Existing Work Handles It

- Existing approach:
  - Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Remaining limitation: 仅单硅酸盐；大 RE 阳离子体系（Tb/Dy/Ho）因 CMAS 润湿流失缺失 50 h 数据。

## What Remains Unsolved

- Unsolved part: 1500 °C 下钽酸盐、锆酸盐、高熵硅酸盐的腐蚀产物类型、渗透动力学、RE 半径依赖方向与相分解行为。
- Why unresolved: 现有高通量工作（#46、#18）与高熵设计工作（#48）均以 1300 °C 为腐蚀温度；高温高通量腐蚀装置与方法尚缺。

## Possible Research Questions

- Question: 1500 °C 下 RETaO4 与高熵锆酸盐的 CMAS 腐蚀行为是否符合「粘度剧降-RE 效应弱化」规律？
  - Feasibility: medium（高温实验可实现，但高通量高温装置需自行搭建）
  - Evidence needed: 1500 °C 腐蚀截面数据（渗透深度/腐蚀层厚度）至少 3–5 种 RE 成分 × 2 体系。

## Possible Research Paths

- Path: 将层叠法高通量筛选（#46）推广至 1500 °C 腐蚀条件。
  - Required method/data: 高温（≥1500 °C）腐蚀炉 + 层叠块体制备 + 截面定量表征。
  - Risk: CMAS 在 1500 °C 粘度极低、流失严重（#47 已观察到），需解决熔体保持问题。

## Risks and Counter-Evidence

- Risk: 该 gap 可能因「1500 °C 下成分选择不再重要」而失去工程意义（若 RE 效应确实完全弱化）。
  - Evidence: #47 显示 1500 °C 仍存在方向反转（大 RE 抗性更好），说明成分效应未消失，只是规律改变。
  - How to check: 补充钽酸盐/锆酸盐 1500 °C 数据后判断。

## Related Pages

- Papers: 五篇已入库 CMAS 论文（#47、#46、#18、#16、#48）
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Claims: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"、"[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
- Reviews:

## Uncertainty

- 待确认：无
- 待核查：无
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Evidence strength marked.
- [x] Related open question updated if needed.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
