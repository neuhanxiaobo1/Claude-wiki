---
type: topic
status: active
created: 2026-08-23
updated: 2026-08-28
papers:
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
methods:
datasets:
metrics:
claims:
  - "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
tags:
  - topic
  - corrosion
  - ceramics
  - cmas
  - ebc
---

# Ceramic Corrosion

## Definition

- 陶瓷材料在高温、腐蚀性介质（CMAS 熔盐、氯化物熔盐、水蒸气/水氧等）作用下的退化行为与机制研究。用户研究领域主术语（2026-08-20 确认，见 `memory/term_aliases.md`）。

## Scope

- Included: 高温结构陶瓷/涂层（EBC、TBC）的 CMAS 腐蚀机制、腐蚀产物形成热力学（形成焓-RE 半径关联）、腐蚀动力学（渗透深度/反应层厚度）、RE 成分与结构类型（单斜/烧绿石/缺陷萤石）对抗蚀性的调控、高通量与原位观察方法。
- Excluded: 金属腐蚀电化学（除非与陶瓷涂层体系直接相关，待确认）。
- Boundary notes: 当前以 CMAS 腐蚀为主线（已入库 5 篇 CMAS 论文）；氯化物熔盐体系（Si3N4 篇）已归档至 raw/notes/ 备用；TBC-TGO 内生界面反应已拆分至 "[[wiki/topics/Thermal Barrier Coatings]]"（按失效源划分：CMAS 外来侵蚀归本主题）。

## Why It Matters

- 用户博士课题核心方向（高温结构陶瓷环境障涂层/CMAS 腐蚀）；CMAS 侵蚀是燃气涡轮热端部件 EBC/TBC 服役温度继续提升的关键瓶颈。

## Main Questions

- Question: 腐蚀产物形成焓随 RE 离子半径的变化（大半径更放热、更易形成）是否是 CMAS 腐蚀的普适热力学规律？在不同体系（硅酸盐/钽酸盐/锆酸盐）与不同温度下是否一致？
  - Related papers: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"、"[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"、"[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"、"[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Status: open（1300 °C 三体系一致——#36 给出单组分 8 组分奠基数据，且 #48 证明规律在固溶体/高熵体系同样成立——渗透排序与平均半径完全对应；1500 °C 仅硅酸盐有数据且 RE 效应弱化）

- Question: 1500 °C 级高温下，低粘度 CMAS 导致的快速传质、RE 种类影响弱化、润湿流失、冷却析出与基体相分解是否在钽酸盐、锆酸盐体系中同样成立？
  - Related papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Status: open（两篇论文覆盖 1500 °C 但均限 RE2SiO5；#16 新增「相分解诱导晶间渗透」机制；#46、#18、#48 均为 1300 °C，尚不能判断高温规律是否跨体系）

- Question: 结构类型（有序烧绿石 vs 无序缺陷萤石）与 RE 平均半径对 CMAS 抗性的贡献如何解耦？
  - Related papers: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Status: open（#18 中二者高度相关，未设计解耦实验）

- Question: 冷却过程析出的腐蚀产物（Ca2RE8(SiO4)6O2 晶粒）对涂层完整性与热循环寿命的影响？
  - Related papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Status: open（#47 与 #16 两篇原位证据均证实冷却析出，且 #16 显示 1500 °C 保温阶段无反应、产物集中于冷却起始析出；对涂层损伤的因果链未评估）

- Question: 1500 °C 下 Lu2SiO5 的相分解（2Lu2SiO5 = Lu2Si2O7 + Lu2O3）是否普适于其他 RE2SiO5？高熵化（熵稳定效应）能否抑制分解？
  - Related papers: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"、"[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Status: open（仅 Lu2SiO5 有分解证据；#47 未做 TEM/无 CMAS 对照；#48 高熵样品无 1500 °C 数据）

## Representative Papers

- Paper: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - Contribution: 「1300 °C 小半径 RE 抗蚀更好」主线的奠基工作：8 种 RE2SiO5 衰退层厚度-RE 半径近似线性规律（三组分类），首次以磷灰石形成焓 + 光学碱度差 ΔΛ 给出机制与筛选判据；最早观察腐蚀后冷却热应力剥落。
  - Evidence: Fig. 11 系统衰退层数据 + Risbud 量热 + OB 计算 + 100 h 延长验证。

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Contribution: 首次系统研究 7 种 RE2SiO5 在 1500 °C 的 CMAS 腐蚀；高温原位观察揭示 Ca2RE8(SiO4)6O2 的「高温生长 + 冷却析出」双机制；发现 1500 °C 下 RE 种类影响弱化、大 RE 阳离子抗性更好。
  - Evidence: XRD/SEM-EDS + 原位观察（Movie S1–S3）+ FactSage 粘度计算。

- Paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Contribution: 单体系深度研究 Lu2SiO5 的 1500 °C CMAS 腐蚀；原位观察发现「保温无反应 + 冷却起始析出」；首次提出相分解诱导晶间渗透机制（2Lu2SiO5 = Lu2Si2O7 + Lu2O3），证实 1300 °C 最优的 Lu2SiO5 在 1500 °C 渗透 219 μm（>4 倍）而失效。
  - Evidence: 原位观察（Movie 1/2）+ 无 CMAS 分解对照 + TEM 晶界表征 + 渗透深度定量。

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Contribution: 首次制备四元高熵 RE2SiO5 EBC，以元素功能分工策略同时实现低热导（接近 κmin）、TEC 匹配 SiC 与良好 CMAS 抗性；在 RE2SiO5-CMAS 体系首次鉴定石榴石型产物 (CaxRE3-x)(MgyAlzSi5-y-z)O12；渗透排序与平均 RE 半径完全对应，为半径规律提供固溶体证据。
  - Evidence: LFA/DIL/XPS/纳米压痕 + 五样品同条件 CMAS 腐蚀 + EPMA 产物定量。

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Contribution: 层叠法高通量筛选 8 种 RETaO4 的 CMAS 抗性；澄清腐蚀产物之争（主产物为 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体+少量磷灰石）；确认晶界腐蚀普遍性；渗透深度随 RE 半径增大而增加。
  - Evidence: TEM/EPMA 精确定量 + DFT 形成焓 + 高温润湿性实验。

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Contribution: 高通量制备 19 种五元高熵锆酸盐，建立 RE 平均半径/半径分散度/结构类型与热物性、CMAS 抗性的系统关联；小平均半径缺陷萤石结构抗蚀最佳（动力学+热力学双重机制）。
  - Evidence: 19 成分系统热物性数据 + 腐蚀层厚度定量对比（20–70 μm vs YSZ 150–200 μm）。

## Method Routes

- Route: 高温原位观察（相机记录 CMAS 熔化-铺展-产物析出全过程，区分高温生长与冷却析出）
  - Methods: 高温原位观察、FactSage 粘度计算、接触角测量、XRD/SEM-EDS、无 CMAS 相稳定性对照、TEM 晶界表征
  - Strengths: 直接捕捉动态过程，揭示时间/温度分辨机制；#16 用无 CMAS 对照 + TEM 把「基体相分解」与「CMAS 反应」分离
  - Limitations: 仅适用于单一样品表面，通量低

- Route: 层叠法高通量筛选（多种成分压制于同一块体，统一条件一次腐蚀、截面直接对比）
  - Methods: 层叠压制烧结、截面渗透深度测量、TEM/EPMA 产物定量、DFT 形成焓
  - Strengths: 消除样品间实验误差，高效获得成分依赖规律
  - Limitations: 各层致密度可能存在差异；单一样品内需防层间扩散

- Route: 高通量固相反应制备 + 热物性/腐蚀联合表征（19 成分并行制样）
  - Methods: 高通量球磨/压片、Rietveld 精修、LFA 热导、DIL 膨胀、CMAS 腐蚀层测厚
  - Strengths: 建立成分-结构-性能大样本关联，支撑设计准则
  - Limitations: 腐蚀条件单一（1300 °C/5 h），无动力学数据

- Route: 高熵多组分设计 + 热物性/腐蚀联合表征（元素功能分工策略，高熵样品与单组分同条件对照）
  - Methods: 高熵固溶体制备、多面体晶格畸变定量、XPS 价态分析、LFA/DIL、纳米压痕、CMAS 腐蚀 + EPMA 产物定量
  - Strengths: 把「成分选择」升级为「多目标协同设计」；对照设计使各元素贡献可归因
  - Limitations: 单腐蚀条件（1300 °C/20 h）；等摩尔单成分点，无比例优化

## Current Consensus

- Consensus: CMAS 腐蚀产物的形成焓随 RE 离子半径增大而更放热（更易形成），因此 1300 °C 级温度下小 RE 半径成分的 CMAS 抗性更好。
  - Supporting claims: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"（#36 Key Claims 1–2 奠基 8 组分数据 + 光学碱度判据、#46 Key Claims 1–3、#18 Key Claims 3–4、#47 1300 °C 对照数据、#48 渗透排序（Lu<Yb<HE<Ho<Eu，与平均半径完全对应）、#16 1300 °C 对照（Lu 最优，约 50 μm 与 #36 定量吻合））
  - Evidence strength: strong（六篇独立证据链：DFT + EPMA + 量热 + 渗透深度/衰退层厚度，覆盖单组分与固溶体/高熵体系）

- Consensus: 1500 °C 时 CMAS 粘度剧降（1300 °C 的 1/4 以下），传质与反应加速，RE 种类对抗蚀性的影响弱化——#16 证实 1300 °C 抗蚀最优的 Lu2SiO5 在 1500 °C/50 h 渗透达 219 μm（>4 倍）；同时 #47 显示大 RE 阳离子样品更易被润湿并熔体流失、冷却阶段诱发短 Ca2RE8(SiO4)6O2 晶粒二次析出，#16 进一步揭示 Lu2SiO5 相分解（2Lu2SiO5 = Lu2Si2O7 + Lu2O3）诱导的晶间渗透——高温抗蚀排序不能简单外推自 1300 °C 的形成焓-半径规律。
  - Supporting claims: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"（#47 Key Claims 3–4、#16 Key Claims 2）、“[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]”
  - Evidence strength: medium-high（两篇论文、仅 RE2SiO5 体系覆盖 1500 °C；待钽酸盐/锆酸盐高温数据交叉验证）

## Disagreements and Controversies

- 争议: 1300 °C 下 RE 半径对 CMAS 抗蚀性的影响方向因体系而异——RETaO4 与高熵锆酸盐中渗透深度/腐蚀层随 RE 半径增大而增加（小半径抗蚀好）；而文献报道 X1-RE2SiO5 反应区宽度随 RE³⁺ 半径减小而增加（#47 引言引述 [18] = Tian et al., JECS 2019，未入库）。
  - Related pages: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"、"[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/gaps/Structure-Radius-Decoupling]]"
  - Status: open（2026-08-28 #36 原文核实：Tb–Lu 段（X2 为主）衰退层厚度随半径减小而变薄、与主线一致；反向趋势确为 X1 大半径系列（La/Nd/Sm/Eu/Gd）内部现象，源头 #21 Tian et al., JECS 2019 未入库——1300 °C 半径规律存在晶型依赖翻转，归入 Structure-Radius-Decoupling gap；#36 大半径组 Tb/Dy/Ho 晶型归属待核查）

- 争议: RETaO4 CMAS 腐蚀产物在文献中长期存在矛盾结论（Ca2Ta2O7 vs 磷灰石 vs 固溶体），#46 以 TEM+EPMA 精确定量澄清为 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体。
  - Related pages: "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - Status: 已澄清（#46 证据链完整）

- 争议: 1300 °C 单硅酸盐「最优 RE 成分」因评价指标而异——#36 以衰退层厚度为指标得 Lu 最薄（近似线性规律），#59 层叠法以渗透深度为指标得 Er 最浅（非单调：Er < Tm < Y/Lu/Yb < Tb/Dy）；#59 明确批评单一指标（产物量/反应层厚度）无法准确评价抗蚀性，主张综合「产物形成能力 + 基体溶解 + CMAS 渗透」三因素。
  - Related pages: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"、#59（Extreme Materials 2025，已核实未入库）
  - Status: open（评价指标统一是 1500 °C 跨体系比较的方法学前提；#59 缓存 10185 已就绪，是否入库待用户决策）

- 争议: RE2SiO5-CMAS 腐蚀产物谱——此前报道以磷灰石 Ca2RE8(SiO4)6O2 为主（#47/#16），#48 首次在高熵体系鉴定硅酸盐石榴石 (CaxRE3-x)(MgyAlzSi5-y-z)O12；石榴石是仅高熵体系特有还是普遍存在但被忽略，尚无定论。
  - Related pages: "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - Status: open（#36 原文核实：单组分小半径组（Er/Tm/Yb/Lu）早已检出铝酸盐石榴石 RE3Al5O12——与 #48 硅酸盐石榴石物相不同；石榴石型产物在单组分体系并非完全空白，但两类石榴石的生成条件分界未澄清）

## Related Gaps

- Gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（钽酸盐、锆酸盐、高熵硅酸盐体系 1500 °C 级 CMAS 腐蚀数据缺失；来源 #46 Potential Gaps 1、#18 Potential Gaps 1、#48 Potential Gaps 2；RE2SiO5 已有 #47/#16 两篇但相分解普适性未知）。
  - Why relevant: 验证「高温 RE 效应弱化」与「相分解」的跨体系普适性（主题 Main Question 2/5）。

- Gap: "[[wiki/gaps/Structure-Radius-Decoupling]]"（结构类型与 RE 半径对抗蚀性的解耦；来源 #18 Potential Gaps 3 + #36/#21 的 X1/X2 晶型翻转）。
  - Why relevant: 决定设计准则中「选结构」还是「选半径」的优先级；X1/X2 翻转表明晶型效应可能大到反转半径规律。

- Gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"（冷却析出产物/冷却热应力对涂层热循环完整性的影响；来源 #36 剥落观察、#47 Potential Gaps 2、#16 Potential Gaps 2）。
  - Why relevant: 实际服役含热循环，冷却析出与冷却热应力不可忽视（三篇证据）。

- Gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"（高通量方法向其他 EBC/TBC 体系推广；来源 #46 Potential Gaps 2、#47 Potential Gaps 3）。
  - Why relevant: 加速成分筛选是用户课题的方法学机会。

## Linked Pages

- Papers: "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"、"[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"、"[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"、"[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
- Methods:
- Datasets:
- Metrics:
- Claims: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"、"[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"、"[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"、"[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"、"[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"、"[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"、"[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"、"[[wiki/gaps/Structure-Radius-Decoupling]]"、"[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"、"[[wiki/gaps/High-Throughput-Screening-Transfer]]"
- Reviews:

## Uncertainty

- 待确认：CMAS 腐蚀与氯化物熔盐腐蚀是否拆分主题（当前 CMAS 为绝对主线，熔盐体系仅 1 篇归档备用）。
- 待核查：X1-RE2SiO5 反应区宽度与 RE 半径关系的原始文献原文数值——2026-08-28 #36 原文核实后确认：反向趋势为 X1 大半径系列（La/Nd/Sm/Eu/Gd）内部现象，源头 #21（Tian et al., JECS 2019, DOI: 10.1016/j.jeurceramsoc.2018.12.015）未入库；#36 大半径组（Tb/Dy/Ho）晶型归属待核查。
- 待核查：#47（Er2SiO5 保温约 1 h 缓慢析出）与 #16（Lu2SiO5 保温无可见析出）的原位行为差异来源（RE 种类差异 vs 观察分辨率）。
- AI 推断：高熵 RE2SiO5（#48）的 1500 °C 相分解行为（熵稳定效应是否抑制分解）。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
