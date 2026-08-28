---
type: gap
status: open
created: 2026-08-27
updated: 2026-08-27
priority: high
evidence_strength: strong
papers:
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
topics:
  - "[[wiki/topics/Thermal Barrier Coatings]]"
methods:
claims:
  - "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
tags:
  - gap
  - ceramics
  - corrosion
  - tbc
---

# TBC-TGO 高温热化学相容性数据缺失

## Gap Description

- 1600 °C 级 TBC 候选材料（Hf6Ta2O17 等新型高熔点氧化物）与粘结层氧化产物 TGO（α-Al2O3）的高温热化学相容性数据普遍缺乏；现有选材几乎只评估热导、相稳定性与 CMAS 抗性，TGO 界面反应这一失效维度被系统性忽略（#29 为体系内首篇系统研究，即发现 >1400 °C 不相容）。

## Why It Matters

- TBC 服役中 TGO 在粘结层表面必然形成；若 TBC 材料与 TGO 反应生成低 CTE 中间相，界面热应力可达 GPa 级（#29 中 880–1031 MPa，超 YSZ 许用范围），直接威胁涂层寿命——候选材料可能因 TGO 相容性被一票否决，必须在选材阶段提前排除。

## Supporting Evidence

- Paper: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Evidence: Hf6Ta2O17-Al2O3 在 >1400 °C 反应生成 AlHf3TaO10，界面热应力 880–1031 MPa 超 YSZ 许用；作者指出该维度此前未被澄清。
  - Source section/page/table/figure: 全文、Fig 12（机制示意）
  - Evidence strength: strong

## Cross-Page Basis

- Page: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
  - What it shows: 单体系不相容已证实（三重证据链）。
  - Why it supports this gap: 单体系证据凸显「其他候选材料普遍缺乏此类数据」的方法学空白。

## Gap Type

- Type: 真实 gap
- Reason: 粉末 + 扩散偶方法成熟（#29 已示范），但 1600 °C 级候选材料库中仅此一例系统研究；方法可推广而数据未积累。

## How Existing Work Handles It

- Existing approach:
  - Paper: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Remaining limitation: 仅 Hf6Ta2O17 单体系；扩散偶动力学仅 1400 °C；块体几何而非真实涂层。

## What Remains Unsolved

- Unsolved part: 各候选材料（稀土钽酸盐、高熵锆酸盐、稀土硅酸盐等）与 Al2O3 的反应阈值温度、产物相、扩散动力学。
- Why unresolved: TBC 选材流程未纳入该判据；高通量粉末反应筛选未建立。

## Possible Research Questions

- Question: 如何建立 TBC-TGO 相容性高通量筛选方法并将其纳入选材判据？
  - Feasibility: high（粉末混合退火 + 自动 XRD 判相可实现）
  - Evidence needed: 候选材料 × Al2O3 粉末对在 1300–1600 °C 的反应矩阵。

## Possible Research Paths

- Path: 高通量粉末反应筛选（多成分平行制样 + 分段退火 + XRD 自动判相）。
  - Required method/data: 高通量制样平台、高温退火炉、自动 XRD 分析流程。
  - Risk: 粉末反应与涂层界面反应的热力学阈值可能不一致（界面应变能贡献），需扩散偶复核。

## Risks and Counter-Evidence

- Risk: 该 gap 可能随「无粘结层新型 TBC 体系（直接沉积）」出现而重要性下降。
  - Evidence: 当前主流 TBC 仍依赖 MCrAlY/Pt-Al 粘结层，TGO 不可避免。
  - How to check: 跟踪无粘结层涂层技术成熟度。

## Related Pages

- Papers: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
- Topics: "[[wiki/topics/Thermal Barrier Coatings]]"
- Methods:
- Claims: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
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
