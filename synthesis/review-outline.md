---
type: synthesis
status: active
created: 2026-08-28
updated: 2026-08-28
reviews:
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
  - "[[wiki/topics/Thermal Barrier Coatings]]"
papers:
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
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
  - review
---

# Review Outline

本页是文献综述大纲与写作控制台，由 `agents/review_agent.md` 维护（2026-08-28 基于 6 篇语料首次激活，同日补入 #36 奠基性工作）。

## Review Goal

- Topic: 高温结构陶瓷（EBC/TBC）的 CMAS 腐蚀机制与抗蚀成分设计——稀土单硅酸盐 RE2SiO5（含高熵）、稀土钽酸盐 RETaO4、高熵稀土锆酸盐；姊妹方向 TBC-TGO 热化学相容性。
- Target reader: 待确认（博士文献综述用途，读者层级待用户填写）
- Scope: 2019–2026，田志林组 7 篇主线（6 篇 CMAS + 1 篇 TBC-TGO）；上游热化学依据 Costa et al. / Risbud et al. 系列待入库；Excluded 范围待用户填写 `memory/project_profile.md`。
- Output type: thesis section（博士文献综述）／待确认

## Core Thesis

- 论题 1（1300 °C 公理）: 腐蚀产物形成焓随 RE 半径增大更放热，1300 °C 下小半径成分抗蚀更好——三体系（RE2SiO5 / RETaO4 / 高熵锆酸盐）一致（#36 奠基单组分 8 组分衰退层-半径线性规律与光学碱度 ΔΛ 判据），且在固溶体/高熵体系中按平均半径成立。→ "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
- 论题 2（1500 °C 失效边界）: 1500 °C 时 CMAS 粘度剧降（传质与反应加速）使 RE 效应弱化，叠加相分解诱导晶间渗透——高温抗蚀排序不能外推自 1300 °C 的形成焓-半径规律。→ "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"、"[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
- 论题 3（判据缺口）: 高温选材缺两个判据——基体相稳定性（1500 °C 分解风险）与 TGO 热化学相容性（>1400 °C 界面反应）——选材流程需按服役温度分级并补维度。→ "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"、"[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"

## Outline

### 1. Background and problem

- 燃气涡轮热端服役温度提升；EBC/TBC 体系的 CMAS 侵蚀瓶颈（外来熔体 vs 内生界面反应两种失效源）。
- 候选材料谱：RE2SiO5、RETaO4、高熵锆酸盐（缺陷萤石/烧绿石）、Hf6Ta2O17（α-PbO2 型）。
- 关键科学问题：抗蚀性是否存在可外推的成分规律？规律在温度升档后是否失效？
- 证据来源：各论文页 Introduction；"[[wiki/topics/Ceramic Corrosion]]" Definition/Why It Matters。

### 2. Main research routes

- 高温原位观察路线（#47/#16）：熔化-铺展-析出全过程、冷却析出与高温生长分离、无 CMAS 对照。
- 层叠法高通量（#46）：统一条件一次腐蚀、截面直接对比。
- 高通量并行制备 + 联合表征（#18）：19 成分大样本。
- 高熵多组分对照设计（#48）：元素功能分工 + 单组分同条件对照。
- 粉末反应 + 扩散偶联用（#29）：TBC-TGO 相容性阈值与动力学。
- 证据来源："[[wiki/topics/Ceramic Corrosion]]" Method Routes、"[[wiki/topics/Thermal Barrier Coatings]]"、"[[synthesis/literature-map]]" Method Routes。

### 3. Method comparison

- 通量 vs 深度：层叠法/并行制备（高通量、条件单一）vs 原位观察（低通量、时间/温度分辨、可分离冷却环节）。
- 原位 vs 事后：原位捕捉动态（冷却析出、相分解）是 #16 发现新机制的关键；事后截面只给最终态。
- 单条件 vs 多条件：所有路线腐蚀条件均单一（1300 °C 或 1500 °C 单点）——跨温度规律需要多条件设计。
- 对照设计价值：#16 无 CMAS 对照分离基体失稳与熔体反应；#48 单组分对照使元素贡献可归因。
- 证据来源：literature-map Method Routes 表（Strength/Limitation 列）。

### 4. Evidence from results

- 形成焓-半径规律证据链（1300 °C）：#36 单组分 8 组分衰退层-半径线性规律 + Risbud 量热 + ΔΛ 判据（奠基）、#46 DFT+渗透深度+润湿性、#18 腐蚀层厚度、#47 1300 °C 对照、#48 渗透排序与平均半径对应、#16 1300 °C Lu 最优（约 50 μm 与 #36 定量吻合）。
- 1500 °C 温度效应双证据：#47 七体系（RE 效应弱化、润湿流失、冷却析出）+ #16 Lu2SiO5（保温无反应、冷却起始析出、219 μm vs 50 μm）。
- 相分解机制：#16 Eq (1) 2Lu2SiO5 = Lu2Si2O7 + Lu2O3 + TEM 晶界通道。
- 产物谱澄清：钽酸盐固溶体（#46）、磷灰石（#36/#47/#16）、硅酸盐石榴石（#48 首次）、铝酸盐石榴石 RE3Al5O12 与钙长石（#36 小/大半径组分别检出）。
- TBC-TGO：#29 反应阈值 1400 °C、AlHf3TaO10 生成、热应力 880–1031 MPa 超 YSZ 许用。
- 证据来源：各 claim 页 Supporting Evidence。

### 5. Limitations and gaps

- "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"：三体系高温数据缺失 + 相分解普适性未知（Q1/Q6）。
- "[[wiki/gaps/Structure-Radius-Decoupling]]"：结构-半径共线未解耦（Q2）+ X1/X2 晶型翻转（#36/#21）。
- "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"：冷却析出/冷却热应力后果未评估（Q3；#36 剥落观察最早）。
- "[[wiki/gaps/High-Throughput-Screening-Transfer]]"：方法未跨体系联用（Q4）。
- "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"：相容性判据未推广（Q7）。
- 另：单篇论文页内未建页的小 gap（见 open-questions Not Yet True Gaps）。

### 6. Future directions

- 1500 °C 跨体系抗性地图（Q1/Q6 → Positioning 1）。
- 相稳定性优先设计（Q6 → Positioning 2）。
- 结构-半径正交解耦实验（Q2）。
- 热循环完整性评估（Q3）。
- 方法学组合与推广（Q4）。
- TBC-TGO 判据与扩散障（Q7 → Positioning 3）。
- 证据来源："[[synthesis/research-positioning]]"、"[[synthesis/open-questions]]"。

## Reusable Claims

- Claim: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - Source page: #36/#46/#18/#47/#48/#16
  - Suggested section: 4（证据）为主、1（背景）引出（#36 作叙事起点）
  - Citation need: #36、#46、#18、#47、#48、#16 题名+DOI

- Claim: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - Source page: #47/#16
  - Suggested section: 4（证据）+ 5（局限）
  - Citation need: #47、#16 题名+DOI

- Claim: "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - Source page: #16
  - Suggested section: 4（证据）+ 6（相稳定性方向）
  - Citation need: #16 题名+DOI

- Claim: "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - Source page: #46
  - Suggested section: 4（证据）
  - Citation need: #46 题名+DOI

- Claim: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - Source page: #18
  - Suggested section: 4（证据）+ 5（结构-半径共线局限）
  - Citation need: #18 题名+DOI

- Claim: "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - Source page: #48（#36 铝酸盐石榴石作对照区分）
  - Suggested section: 4（证据，产物谱）
  - Citation need: #48、#36 题名+DOI

- Claim: "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
  - Source page: #48
  - Suggested section: 2（高熵设计路线）+ 4（证据）
  - Citation need: #48 题名+DOI

- Claim: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
  - Source page: #29
  - Suggested section: 4（证据，TBC 姊妹方向）+ 6（判据推广）
  - Citation need: #29 题名+DOI

## Evidence Gaps

- Missing evidence: 钽酸盐/锆酸盐/高熵硅酸盐 1500 °C 腐蚀数据
  - Why needed: 论题 2 目前仅 RE2SiO5 双证据，跨体系普适性决定综述结论强度。
  - Possible source: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（#36/#23/#52 候选入库）

- Missing evidence: X1-RE2SiO5 反应区宽度-半径反向报道的原文数值
  - Why needed: 「1300 °C 半径规律」争议段（Ceramic Corrosion 主题 Disagreements）需要原文数值核实（2026-08-28 已溯源至 #21 Tian et al., JECS 2019, DOI 10.1016/j.jeurceramsoc.2018.12.015；#36 原文已核实为 X2 段递减）。
  - Possible source: #21（未入库）；#47 引言引文 [18]

- Missing evidence: 冷却析出对涂层剥落/开裂的因果证据
  - Why needed: 论题 2 的冷却环节后果目前为 AI 推断（#36 剥落观察为最早定性证据）。
  - Possible source: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"

- Missing evidence: Costa et al. / Risbud et al. 热化学上游原始文献
  - Why needed: 论题 1 的热力学解释链溯源。
  - Possible source: #16 引文 [22]、#36 引文 [15]；待入库

## Draft Paragraphs

### Paragraph 1（核心论题段草稿）

- Function: 综述核心论题——1300 °C 公理与 1500 °C 失效边界。
- Draft: 稀土硅酸盐与稀土氧化物涂层体系的 CMAS 抗性在 1300 °C 下呈现一致的成分规律：腐蚀产物形成焓随 RE 离子半径增大而更放热，小半径成分（如 Lu、Yb）抗蚀更好。这一规律最早由 8 种 RE2SiO5（Tb–Lu）的系统研究确立——衰退层厚度随 RE 离子半径减小而近线性变薄，并给出光学碱度差筛选判据；随后在 RETaO4 钽酸盐（层叠法高通量，渗透深度随 RE 半径增大而增加）、高熵锆酸盐（19 成分，腐蚀层厚度 20–70 μm 对 YSZ 150–200 μm）中分别得到验证，并进一步在 (Ho0.25Lu0.25Yb0.25Eu0.25)2SiO5 高熵固溶体中成立——渗透深度排序 Lu < Yb < 高熵 < Ho < Eu 与平均 RE 半径完全对应。然而当服役温度升至 1500 °C，CMAS 粘度降至 1300 °C 的 1/4 以下，传质与反应显著加速：七种 RE2SiO5 的原位观察显示 RE 种类影响弱化，而 1300 °C 下抗蚀最优的 Lu2SiO5 在 1500 °C/50 h 渗透达 219 μm（1300 °C 的 4 倍以上），其失效还叠加了相分解（2Lu2SiO5 = Lu2Si2O7 + Lu2O3）诱导的晶间渗透通道。因此，高温抗蚀排序不能简单外推自 1300 °C 的形成焓-半径规律，成分设计准则需要按服役温度分级，并将基体相稳定性纳入判据。
- Evidence: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"、"[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"、"[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"；#36/#46/#18/#47/#48/#16。
- Missing evidence: 1500 °C 数据目前仅 RE2SiO5 体系——「跨体系高温失效」表述需限制范围或待补证据。

## Maintenance Checklist

- [x] Important papers included.
- [x] Claims have evidence.
- [x] Gaps are linked.
- [x] Draft text does not overclaim.
- [x] Operation recorded in `log.md`.
