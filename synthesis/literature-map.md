---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-23
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
claims:
  - "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
tags:
  - synthesis
---

# Literature Map

本页维护跨论文文献地图，由 `agents/synthesis_agent.md` 维护。

## Scope

- Research field: 高温结构陶瓷 CMAS 腐蚀（EBC/TBC 方向）
- Included topics: 稀土单硅酸盐 RE2SiO5、稀土钽酸盐 RETaO4、高熵稀土锆酸盐 (5RE0.2)2Zr2O7 的 CMAS 腐蚀机制与成分调控；高温原位观察与高通量筛选方法。
- Excluded topics: 氯化物熔盐腐蚀（Si3N4 篇已归档）；烧蚀/吸波/透波方向（田老师 collection 内但非本主题）。
- Time range: 2023–2026（已入库 3 篇）；上游热化学依据为 Costa et al. 系列（原始文献待入库）。

## Research Problem Map

| Research problem | Related papers | Methods | Solved parts | Unresolved parts | Evidence strength |
|---|---|---|---|---|---|
| 腐蚀产物形成焓-RE 半径关联是否普适（1300 °C） | #46、#18、#47（1300 °C 对照） | DFT 形成焓、渗透深度/腐蚀层厚度定量、润湿性 | 1300 °C 三体系一致：小半径抗蚀更好 | 1500 °C 规律弱化/反转；X1-RE2SiO5 反向报道待核查 | strong |
| 1500 °C 高温下 RE 效应是否弱化（普适性） | #47（仅单硅酸盐） | 原位观察、FactSage 粘度 | RE2SiO5 体系证实弱化+方向反转 | 钽酸盐/锆酸盐无 1500 °C 数据 | medium |
| 结构类型（烧绿石/缺陷萤石）与 RE 半径对抗蚀性的解耦 | #18 | 高通量 19 成分、Rietveld、腐蚀层测厚 | 缺陷萤石+小半径组合抗蚀最佳 | 二者贡献未解耦，双重机制相对权重未知 | strong |
| 冷却析出产物对涂层热循环完整性影响 | #47 | 原位观察（Movie S2） | 冷却析出机制已揭示 | 对涂层剥落/应力的影响未评估 | strong |
| 高通量方法跨体系推广 | #46、#18、#47 | 层叠法、并行制备、原位观察 | 各方法单体系验证有效 | 三方法未联用、未跨体系 | strong |

## Method Routes

| Route | Core idea | Representative methods | Representative papers | Strength | Limitation |
|---|---|---|---|---|---|
| 高温原位观察 | 相机记录 CMAS 熔化-铺展-产物析出全过程，区分高温生长与冷却析出 | 高温接触角仪、超深场显微镜、FactSage 粘度 | "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]" | 直接捕捉动态过程，时间/温度分辨 | 单样品表面，通量低 |
| 层叠法高通量筛选 | 多种成分压制于同一块体，统一条件一次腐蚀、截面直接对比 | 层叠压制烧结、截面渗透深度、TEM/EPMA、DFT | "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]" | 消除样品间误差，高效获得成分依赖规律 | 层间致密度差异；防层间扩散 |
| 高通量并行制备 | 多成分并行制样 + 热物性/腐蚀联合表征 | 高通量球磨/压片、Rietveld、LFA、DIL、腐蚀层测厚 | "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]" | 大样本成分-结构-性能关联 | 腐蚀条件单一（1300 °C/5 h） |

## Claims Map

- Claim: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"（形成焓-RE 半径关联）
  - Supports: #46（DFT+渗透深度+润湿性）、#18（腐蚀层厚度）、#47（1300 °C 对照）
  - Challenges: #47（1500 °C 方向反转）；X1-RE2SiO5 文献反向报道（待核查）
  - Source papers: 三篇已入库论文
  - Evidence strength: strong（1300 °C）／待扩展（1500 °C）

- Claim: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"（1500 °C 粘度剧降）
  - Supports: #47 主实验
  - Challenges: 无直接反驳；仅单体系覆盖
  - Source papers: #47
  - Evidence strength: medium

- Claim: "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"（钽酸盐产物澄清）
  - Supports: #46 TEM+EPMA 证据链
  - Challenges: 文献旧报道（Ca2Ta2O7/磷灰石）已被澄清
  - Source papers: #46
  - Evidence strength: strong

- Claim: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"（缺陷萤石双重机制）
  - Supports: #18 19 成分系统数据
  - Challenges: 结构与半径共线、未解耦（#18 自述）
  - Source papers: #18
  - Evidence strength: strong

## Gap Map

- Gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（1500 °C 数据缺失）
  - Related direction: 温度效应普适性验证
  - Supporting evidence: #46/#18 实验设计仅 1300 °C；#47 仅单硅酸盐
  - Related open question: 主题 Main Question 2；"[[synthesis/open-questions]]" Q1

- Gap: "[[wiki/gaps/Structure-Radius-Decoupling]]"（结构-半径解耦）
  - Related direction: 高熵 TBC 成分设计准则
  - Supporting evidence: #18 结构-半径共线
  - Related open question: 主题 Main Question 3；"[[synthesis/open-questions]]" Q2

- Gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"（冷却析出影响）
  - Related direction: 热循环损伤评估
  - Supporting evidence: #47 原位观察冷却析出
  - Related open question: 主题 Main Question 4；"[[synthesis/open-questions]]" Q3

- Gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"（高通量方法推广）
  - Related direction: 方法学组合与跨体系应用
  - Supporting evidence: 三篇论文方法各自单体系验证
  - Related open question: "[[synthesis/open-questions]]" Q4

## Maintenance Checklist

- [x] Updated after major paper ingestion.
- [x] Important new topics/methods/claims/gaps linked.
- [x] Evidence strength marked for major synthesis claims.
- [x] Important additions reflected in `index.md`.
- [x] Operation recorded in `log.md`.
