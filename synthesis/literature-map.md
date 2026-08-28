---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-27
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
  - "[[wiki/topics/Thermal Barrier Coatings]]"
methods:
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
claims:
  - "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
  - "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
tags:
  - synthesis
---

# Literature Map

本页维护跨论文文献地图，由 `agents/synthesis_agent.md` 维护。

## Scope

- Research field: 高温结构陶瓷 CMAS 腐蚀（EBC/TBC 方向）
- Included topics: 稀土单硅酸盐 RE2SiO5（含高熵 (Ho0.25Lu0.25Yb0.25Eu0.25)2SiO5）、稀土钽酸盐 RETaO4、高熵稀土锆酸盐 (5RE0.2)2Zr2O7 的 CMAS 腐蚀机制与成分调控；TBC 候选材料 Hf6Ta2O17 与 TGO 的热化学相容性；高温原位观察与高通量筛选方法。
- Excluded topics: 氯化物熔盐腐蚀（Si3N4 篇已归档）；烧蚀/吸波/透波方向（田老师 collection 内但非本主题）。
- Time range: 2022–2026（已入库 6 篇）；上游热化学依据为 Costa et al. 系列（原始文献待入库）。

## Research Problem Map

| Research problem | Related papers | Methods | Solved parts | Unresolved parts | Evidence strength |
|---|---|---|---|---|---|
| 腐蚀产物形成焓-RE 半径关联是否普适（1300 °C） | #46、#18、#47（1300 °C 对照）、#48、#16（1300 °C 对照） | DFT 形成焓、渗透深度/腐蚀层厚度定量、润湿性 | 1300 °C 三体系一致：小半径抗蚀更好；#48 证明规律在固溶体/高熵体系成立（排序与平均半径完全对应） | 1500 °C 规律弱化/反转；X1-RE2SiO5 反向报道待核查 | strong |
| 1500 °C 高温下温度效应是否跨体系普适 | #47、#16（均限 RE2SiO5） | 原位观察、FactSage 粘度、接触角/润湿观察、无 CMAS 对照 | RE2SiO5 体系两篇证实低粘度促进传质、RE 效应弱化（Lu2SiO5 1300 °C 最优 → 1500 °C 219 μm）；同时观察到大 RE 样品润湿流失、冷却析出与相分解 | 钽酸盐/锆酸盐/高熵硅酸盐无 1500 °C 数据；高温排序受粘度、润湿、流失、冷却过程与相稳定性共同影响 | medium-high |
| 1500 °C 相分解（2Lu2SiO5 = Lu2Si2O7 + Lu2O3）的普适性与高熵抑制 | #16、#48（无高温数据） | 无 CMAS 对照、TEM 晶界表征 | Lu2SiO5 分解证实并定位为晶间渗透通道 | 其他 RE2SiO5 与高熵样品是否分解未知；熵稳定效应待验证 | strong（单体系）/ weak（普适性） |
| 结构类型（烧绿石/缺陷萤石）与 RE 半径对抗蚀性的解耦 | #18 | 高通量 19 成分、Rietveld、腐蚀层测厚 | 缺陷萤石+小半径组合抗蚀最佳 | 二者贡献未解耦，双重机制相对权重未知 | strong |
| 冷却析出产物对涂层热循环完整性影响 | #47、#16 | 原位观察（Movie S1–S3 / Movie 1–2） | 冷却析出机制两篇独立证实（#16：1500 °C 保温无反应、冷却起始析出） | 对涂层剥落/应力的影响未评估 | strong |
| 高通量方法跨体系推广 | #46、#18、#47、#48 | 层叠法、并行制备、原位观察、高熵对照设计 | 各方法单体系验证有效 | 四方法未联用、未跨体系 | strong |
| TBC-TGO 热化学相容性（>1400 °C） | #29 | 粉末反应、扩散偶、CTE/E 实测、应力估算 | Hf6Ta2O17-Al2O3 不相容已证实（AlHf3TaO10 生成 + 热应力超 YSZ 许用） | 其他候选材料无数据；扩散障方案未验证；真实涂层未闭环 | strong（单体系） |

## Method Routes

| Route | Core idea | Representative methods | Representative papers | Strength | Limitation |
|---|---|---|---|---|---|
| 高温原位观察 | 相机记录 CMAS 熔化-铺展-产物析出全过程，区分高温生长与冷却析出；无 CMAS 对照分离基体失稳与熔体反应 | 高温接触角仪、超深场显微镜、FactSage 粘度、无 CMAS 退火对照、TEM 晶界表征 | "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]" | 直接捕捉动态过程，时间/温度分辨；#16 用对照实验揭示相分解机制 | 单样品表面，通量低 |
| 层叠法高通量筛选 | 多种成分压制于同一块体，统一条件一次腐蚀、截面直接对比 | 层叠压制烧结、截面渗透深度、TEM/EPMA、DFT | "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]" | 消除样品间误差，高效获得成分依赖规律 | 层间致密度差异；防层间扩散 |
| 高通量并行制备 | 多成分并行制样 + 热物性/腐蚀联合表征 | 高通量球磨/压片、Rietveld、LFA、DIL、腐蚀层测厚 | "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]" | 大样本成分-结构-性能关联 | 腐蚀条件单一（1300 °C/5 h） |
| 高熵多组分对照设计 | 元素功能分工 + 高熵样品与单组分同条件对照，多目标（热导/TEC/CMAS）协同评估 | 高熵固溶体制备、晶格畸变定量、XPS、LFA/DIL、纳米压痕、EPMA 产物定量 | "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]" | 「选成分」升级为「多目标设计」；对照使元素贡献可归因 | 单腐蚀条件；等摩尔单成分点 |
| 粉末反应 + 扩散偶联用（TBC-TGO 相容性） | 混合粉末定反应阈值与产物相，扩散偶定动力学与扩散方向 | 混合粉末退火、Rietveld、SEM-EDS 梯度、Kirkendall 空洞、CTE/E、应力估算 | "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]" | 低成本定相容性阈值；直接反映界面反应动力学 | 块体几何 ≠ 涂层 TGO 薄层；需真实涂层闭环 |

## Claims Map

- Claim: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"（形成焓-RE 半径关联）
  - Supports: #46（DFT+渗透深度+润湿性）、#18（腐蚀层厚度）、#47（1300 °C 对照）
  - Challenges: #47（1500 °C 方向反转）；X1-RE2SiO5 文献反向报道（待核查）
  - Source papers: 三篇已入库论文
  - Evidence strength: strong（1300 °C）／待扩展（1500 °C）

- Claim: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"（1500 °C 粘度剧降与 RE 效应弱化）
  - Supports: #47 主实验
  - Challenges: 无直接反驳；但 #47 还显示润湿流失和冷却析出会改变高温腐蚀表观结果，仅单体系覆盖
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

- Claim: "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"（相分解诱导晶间渗透）
  - Supports: #16 无 CMAS 对照 + TEM + 渗透深度
  - Challenges: 无直接反驳；#47 未观察到/未核查分解，机制相对权重（粘度 vs 相分解）未定量
  - Source papers: #16
  - Evidence strength: strong（Lu2SiO5 单体系）

- Claim: "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"（石榴石型腐蚀产物）
  - Supports: #48 EPMA 定量 + 反应式
  - Challenges: #47/#16 未报道石榴石——单组分体系是否存在待核查
  - Source papers: #48
  - Evidence strength: strong（高熵体系单篇）

- Claim: "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"（高熵元素功能分工）
  - Supports: #48 四单组分同条件对照
  - Challenges: CMAS 抗性未超过 Lu/Yb 单组分；1500 °C 相稳定性未知（#16 提示单硅酸盐高温分解风险）
  - Source papers: #48
  - Evidence strength: strong（性能数据）/ medium（机理）

- Claim: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"（TBC-TGO 不相容）
  - Supports: #29 粉末反应 + 扩散偶 + 热物性三重证据
  - Challenges: Li et al.（2011）旧结论已被修正；真实涂层体系未闭环
  - Source papers: #29
  - Evidence strength: strong（单体系）

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
  - Supporting evidence: 五篇 CMAS 论文方法各自单体系验证
  - Related open question: "[[synthesis/open-questions]]" Q4

- Gap: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"（TBC-TGO 相容性数据缺失）
  - Related direction: TBC 选材判据扩展与界面工程
  - Supporting evidence: #29 单体系系统研究；其他候选材料空白
  - Related open question: "[[synthesis/open-questions]]" Q7

## Maintenance Checklist

- [x] Updated after major paper ingestion.
- [x] Important new topics/methods/claims/gaps linked.
- [x] Evidence strength marked for major synthesis claims.
- [x] Important additions reflected in `index.md`.
- [x] Operation recorded in `log.md`.
