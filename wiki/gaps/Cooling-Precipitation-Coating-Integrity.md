---
type: gap
status: open
created: 2026-08-23
updated: 2026-08-23
priority: medium
evidence_strength: strong
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# 冷却析出产物对涂层热循环完整性的影响

## Gap Description

- #47 原位观察揭示冷却过程（约 1400 °C）加速短而水平分布 Ca2RE8(SiO4)6O2 晶粒的析出，与高温阶段沿 [001] 生长的长晶粒属不同形成机制；但该冷却析出相对涂层完整性（剥落、开裂、残余应力）的影响未评估。

## Why It Matters

- 实际服役含热循环（起停循环），每次冷却都是一次额外析出事件；若冷却析出相在涂层/反应层界面富集并引入应力，将成为热循环寿命的关键损伤源——目前 CMAS 腐蚀研究普遍只做等温腐蚀，系统性低估了热循环损伤。

## Supporting Evidence

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: Er2SiO5 原位观察（Movie S2、图 15）：降温至 1400 °C 大量 50–100 μm 短水平晶粒从残余熔体析出；作者明确指出 REO1.5 溶解度随温度降低而下降是该析出的驱动力，但未评估对涂层的影响（#47 Potential Gaps 2）。
  - Source section/page/table/figure: §4.1、图 15、Movie S2
  - Evidence strength: strong

## Cross-Page Basis

- Page: "[[wiki/topics/Ceramic Corrosion]]"
  - What it shows: 主题页 Related Gaps 已列出本条（来源 #47 Potential Gaps 2）。
  - Why it supports this gap: 主题页 Main Question 4 直接对应本条（open 状态）。

## Gap Type

- Type: 真实 gap
- Reason: 析出事件本身已被原位实验证实（strong 证据），缺的是「析出 → 涂层损伤」的因果链评估。

## How Existing Work Handles It

- Existing approach:
  - Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Remaining limitation: 实验为等温腐蚀 + 冷却观察，块体样品无涂层体系；未做热循环实验。

## What Remains Unsolved

- Unsolved part: 冷却析出相的空间分布（界面富集？）、对界面结合强度与残余应力的影响、多循环累积效应。
- Why unresolved: 需要涂层体系（基体+粘结层+EBC）热循环实验，成本高于块体等温腐蚀；原位观察冷却析出与力学测试联用尚无现成方法。

## Possible Research Questions

- Question: CMAS 腐蚀后的 EBC 在热循环中，冷却析出 Ca2RE8(SiO4)6O2 如何影响涂层剥落寿命？
  - Feasibility: medium（等离子喷涂涂层 + 腐蚀 + 热循环炉实验成熟）
  - Evidence needed: 热循环后截面形貌/裂纹统计 + 界面结合强度对比（有/无 CMAS 腐蚀）。

## Possible Research Paths

- Path: 块体层腐蚀 → 冷却 → 循环热震，统计裂纹萌生位置与析出相分布的相关性。
  - Required method/data: 热震/热循环装置、截面 SEM、微区应力测量（如 Raman 光谱）。
  - Risk: 块体与涂层体系应力状态不同，结论外推需谨慎。

## Risks and Counter-Evidence

- Risk: 冷却析出相可能反而致密化反应层、阻碍进一步腐蚀（正向作用），gap 的实际重要性下降。
  - Evidence: #47 界面形貌显示大 RE 体系致密产物层确实抑制溶解——冷却析出可能参与该致密化。
  - How to check: 先做冷却速率对比实验（快冷/慢冷）观察析出量对渗透深度的影响。

## Related Pages

- Papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Claims:
- Reviews:

## Uncertainty

- 待确认：冷却析出对涂层完整性是损伤作用还是保护作用（或兼有）。
- 待核查：无
- AI 推断：析出相界面富集导致应力集中的具体机制。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Evidence strength marked.
- [x] Related open question updated if needed.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
