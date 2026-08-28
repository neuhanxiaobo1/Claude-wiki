---
type: topic
status: active
created: 2026-08-27
updated: 2026-08-27
papers:
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
methods:
datasets:
metrics:
claims:
  - "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
gaps:
  - "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
tags:
  - topic
  - ceramics
  - corrosion
  - tbc
---

# Thermal Barrier Coatings

## Definition

- 热障涂层（TBC）：沉积于燃气涡轮热端金属部件表面的陶瓷隔热层，典型体系为 YSZ + MCrAlY/Pt-Al 粘结层；服役中粘结层氧化生成 TGO（α-Al2O3），TBC/TGO 界面是失效高发区。本主题聚焦 TBC 候选材料的选材判据与高温退化机制，与 CMAS 腐蚀主题（"[[wiki/topics/Ceramic Corrosion]]"）并列。

## Scope

- Included: TBC 候选材料（Hf6Ta2O17 等 1600 °C 级高熔点氧化物）与 TGO 的热化学相容性、界面反应产物与扩散机制（Kirkendall 效应）、界面热应力评估、选材判据扩展。
- Excluded: CMAS 外来熔盐侵蚀行为（归 "[[wiki/topics/Ceramic Corrosion]]"）；粘结层合金设计与氧化动力学（暂无论文入库）。
- Boundary notes: 本主题与 Ceramic Corrosion 存在交集（CMAS 同样侵蚀 TBC），当前按「失效源」划分：CMAS 外来侵蚀 → Ceramic Corrosion；TGO 内生界面反应 → 本主题。

## Why It Matters

- TBC 使涡轮前温提升数百摄氏度，是航空发动机核心使能技术；1600 °C 级候选材料能否工程化取决于本体性能与界面相容性的双重达标。与用户博士课题（EBC/CMAS 腐蚀）同属高温结构陶瓷涂层方向的姊妹主题。

## Main Questions

- Question: TBC-TGO 热化学相容性是否应成为 TBC 选材的强制性判据？如何低成本、高通量评估？
  - Related papers: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Status: open（#29 示范了粉末+扩散偶评估框架，但数据仅单体系）

- Question: Hf6Ta2O17 基 TBC 的 TGO 不相容问题能否通过扩散障或改性粘结层解决？
  - Related papers: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Status: open（论文仅提出方向，无实验）

## Representative Papers

- Paper: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Contribution: 首次系统研究 Hf6Ta2O17 与 Al2O3 的高温热化学相容性；发现 >1400 °C 反应生成 AlHf3TaO10（约 9.2% 体积膨胀）并定量界面热应力（880–1031 MPa，超 YSZ 许用），修正 Li et al.（2011）结论。
  - Evidence: 混合粉末反应 + 扩散偶 + CTE/E 实测 + Bramfitt 错配度 + 应力估算。

## Method Routes

- Route: 粉末固相反应 + 扩散偶联用（混合粉末定反应阈值与产物相，扩散偶定动力学与扩散方向）
  - Methods: 混合粉末 1300–1600 °C 退火、XRD/Rietveld 精修、SEM-EDS 成分梯度、Kirkendall 空洞分析、CTE/弹性模量实测
  - Strengths: 低成本定相容性阈值；扩散偶直接反映界面反应动力学与扩散机制
  - Limitations: 块体几何与真实涂层 TGO 薄层不同；需真实涂层循环氧化实验闭环

## Current Consensus

- Consensus: TBC 选材须同时评估本体性能（热导、相稳定性、CMAS 抗性）与界面相容性（TGO 反应）——#29 表明 Hf6Ta2O17 本体性能占优但 TGO 相容性存在短板。
  - Supporting claims: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
  - Evidence strength: strong（单体系证据；判据普适性为方法学推论）

## Disagreements and Controversies

- 争议: Hf6Ta2O17 与 Al2O3 是否反应——Li et al.（2011, Key Eng. Mater.）报道无反应，#29 系统实验证实 >1400 °C 反应生成 AlHf3TaO10。
  - Related pages: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
  - Status: 已澄清（#29 证据链完整；Li et al. 原文实验条件待核查）

## Related Gaps

- Gap: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"（候选材料-TGO 相容性数据普遍缺失；来源 #29 Potential Gaps）。
  - Why relevant: 主题 Main Question 1 直接对应。

## Linked Pages

- Papers: "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
- Methods:
- Datasets:
- Metrics:
- Claims: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
- Gaps: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
- Reviews:

## Uncertainty

- 待确认：TBC 主题是否并入用户课题综述主线（或作为姊妹方向独立维护）。
- 待核查：Li et al.（2011）原文实验条件（是否温度未达反应阈值）。
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.