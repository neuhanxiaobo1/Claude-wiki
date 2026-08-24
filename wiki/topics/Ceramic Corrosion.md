---
type: topic
status: active
created: 2026-08-23
updated: 2026-08-23
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
methods:
datasets:
metrics:
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
- Boundary notes: 当前以 CMAS 腐蚀为主线（3 篇已入库论文均属此体系）；氯化物熔盐体系（Si3N4 篇）已归档至 raw/notes/ 备用。

## Why It Matters

- 用户博士课题核心方向（高温结构陶瓷环境障涂层/CMAS 腐蚀）；CMAS 侵蚀是燃气涡轮热端部件 EBC/TBC 服役温度继续提升的关键瓶颈。

## Main Questions

- Question: 腐蚀产物形成焓随 RE 离子半径的变化（大半径更放热、更易形成）是否是 CMAS 腐蚀的普适热力学规律？在不同体系（硅酸盐/钽酸盐/锆酸盐）与不同温度下是否一致？
  - Related papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Status: open（1300 °C 三体系一致；1500 °C 仅硅酸盐有数据且 RE 效应弱化）

- Question: 1500 °C 级高温下，低粘度 CMAS 导致的快速传质、RE 种类影响弱化、润湿流失与冷却析出是否在钽酸盐、锆酸盐体系中同样成立？
  - Related papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Status: open（仅 #47 覆盖 1500 °C 且只限 RE2SiO5；#46、#18 均为 1300 °C，尚不能判断高温规律是否跨体系）

- Question: 结构类型（有序烧绿石 vs 无序缺陷萤石）与 RE 平均半径对 CMAS 抗性的贡献如何解耦？
  - Related papers: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Status: open（#18 中二者高度相关，未设计解耦实验）

- Question: 冷却过程析出的腐蚀产物（短水平 Ca2RE8(SiO4)6O2 晶粒）对涂层完整性与热循环寿命的影响？
  - Related papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Status: open

## Representative Papers

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Contribution: 首次系统研究 7 种 RE2SiO5 在 1500 °C 的 CMAS 腐蚀；高温原位观察揭示 Ca2RE8(SiO4)6O2 的「高温生长 + 冷却析出」双机制；发现 1500 °C 下 RE 种类影响弱化、大 RE 阳离子抗性更好。
  - Evidence: XRD/SEM-EDS + 原位观察（Movie S1–S3）+ FactSage 粘度计算。

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Contribution: 层叠法高通量筛选 8 种 RETaO4 的 CMAS 抗性；澄清腐蚀产物之争（主产物为 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体+少量磷灰石）；确认晶界腐蚀普遍性；渗透深度随 RE 半径增大而增加。
  - Evidence: TEM/EPMA 精确定量 + DFT 形成焓 + 高温润湿性实验。

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Contribution: 高通量制备 19 种五元高熵锆酸盐，建立 RE 平均半径/半径分散度/结构类型与热物性、CMAS 抗性的系统关联；小平均半径缺陷萤石结构抗蚀最佳（动力学+热力学双重机制）。
  - Evidence: 19 成分系统热物性数据 + 腐蚀层厚度定量对比（20–70 μm vs YSZ 150–200 μm）。

## Method Routes

- Route: 高温原位观察（相机记录 CMAS 熔化-铺展-产物析出全过程，区分高温生长与冷却析出）
  - Methods: 高温原位观察、FactSage 粘度计算、接触角测量、XRD/SEM-EDS
  - Strengths: 直接捕捉动态过程，揭示时间/温度分辨机制
  - Limitations: 仅适用于单一样品表面，通量低

- Route: 层叠法高通量筛选（多种成分压制于同一块体，统一条件一次腐蚀、截面直接对比）
  - Methods: 层叠压制烧结、截面渗透深度测量、TEM/EPMA 产物定量、DFT 形成焓
  - Strengths: 消除样品间实验误差，高效获得成分依赖规律
  - Limitations: 各层致密度可能存在差异；单一样品内需防层间扩散

- Route: 高通量固相反应制备 + 热物性/腐蚀联合表征（19 成分并行制样）
  - Methods: 高通量球磨/压片、Rietveld 精修、LFA 热导、DIL 膨胀、CMAS 腐蚀层测厚
  - Strengths: 建立成分-结构-性能大样本关联，支撑设计准则
  - Limitations: 腐蚀条件单一（1300 °C/5 h），无动力学数据

## Current Consensus

- Consensus: CMAS 腐蚀产物的形成焓随 RE 离子半径增大而更放热（更易形成），因此 1300 °C 级温度下小 RE 半径成分的 CMAS 抗性更好。
  - Supporting claims: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"（#46 Key Claims 1–3、#18 Key Claims 3–4、#47 1300 °C 对照数据）
  - Evidence strength: strong（三篇独立证据链：DFT + EPMA + 渗透深度/腐蚀层厚度）

- Consensus: 1500 °C 时 CMAS 粘度剧降（1300 °C 的 1/4 以下），传质与反应加速，RE 种类对抗蚀性的影响弱化；但 #47 同时显示大 RE 阳离子样品更易被 CMAS 润湿并发生熔体流失，冷却阶段还会诱发短 Ca2RE8(SiO4)6O2 晶粒二次析出，因此高温抗蚀排序不能简单外推自 1300 °C 的形成焓-半径规律。
  - Supporting claims: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"（#47 Key Claims 3–4）
  - Evidence strength: medium（仅单篇、单体系覆盖 1500 °C，待钽酸盐/锆酸盐高温数据交叉验证）

## Disagreements and Controversies

- 争议: 1300 °C 下 RE 半径对 CMAS 抗蚀性的影响方向因体系而异——RETaO4 与高熵锆酸盐中渗透深度/腐蚀层随 RE 半径增大而增加（小半径抗蚀好）；而文献报道 X1-RE2SiO5 反应区宽度随 RE³⁺ 半径减小而增加（#47 引言引述）。
  - Related pages: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Status: open（需按晶型/结构类型统一梳理）

- 争议: RETaO4 CMAS 腐蚀产物在文献中长期存在矛盾结论（Ca2Ta2O7 vs 磷灰石 vs 固溶体），#46 以 TEM+EPMA 精确定量澄清为 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体。
  - Related pages: "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - Status: 已澄清（#46 证据链完整）

## Related Gaps

- Gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（钽酸盐、锆酸盐体系 1500 °C 级 CMAS 腐蚀数据缺失；来源 #46 Potential Gaps 1、#18 Potential Gaps 1）。
  - Why relevant: 验证「高温 RE 效应弱化」的普适性（主题 Main Question 2）。

- Gap: "[[wiki/gaps/Structure-Radius-Decoupling]]"（结构类型与 RE 半径对抗蚀性的解耦；来源 #18 Potential Gaps 3）。
  - Why relevant: 决定设计准则中「选结构」还是「选半径」的优先级。

- Gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"（冷却析出产物对涂层热循环完整性的影响；来源 #47 Potential Gaps 2）。
  - Why relevant: 实际服役含热循环，冷却析出不可忽视。

- Gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"（高通量方法向其他 EBC/TBC 体系推广；来源 #46 Potential Gaps 2、#47 Potential Gaps 3）。
  - Why relevant: 加速成分筛选是用户课题的方法学机会。

## Linked Pages

- Papers: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
- Methods:
- Datasets:
- Metrics:
- Claims: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"、"[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"、"[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"、"[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"、"[[wiki/gaps/Structure-Radius-Decoupling]]"、"[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"、"[[wiki/gaps/High-Throughput-Screening-Transfer]]"
- Reviews:

## Uncertainty

- 待确认：CMAS 腐蚀与氯化物熔盐腐蚀是否拆分主题（当前 CMAS 为绝对主线，熔盐体系仅 1 篇归档备用）。
- 待核查：X1-RE2SiO5 反应区宽度与 RE 半径关系的原始文献（#47 引言引述，未读原文）。
- AI 推断：无

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
