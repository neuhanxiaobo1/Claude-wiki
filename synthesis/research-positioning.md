---
type: synthesis
status: active
created: 2026-08-28
updated: 2026-08-28
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
  - "[[wiki/topics/Thermal Barrier Coatings]]"
methods:
claims:
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
tags:
  - synthesis
  - positioning
---

# Research Positioning

本页沉淀研究定位：已入库 7 篇论文覆盖了什么，哪些问题仍然开放，潜在工作如何形成差异化。由 `agents/synthesis_agent.md` 与 `agents/gap_agent.md` 维护（2026-08-28 基于 6 篇语料首次激活，同日补入 #36 奠基性工作）。

## Current Research Mainline

- 已覆盖主线（田志林组 2019–2026，7 篇）：CMAS 腐蚀产物形成焓随 RE 半径增大更放热 → 1300 °C 小半径成分抗蚀更好（三体系 + 固溶体/高熵证据链，[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]；#36 给出单组分 8 组分衰退层-半径线性规律与光学碱度 ΔΛ 筛选判据，为 1300 °C 规律的奠基工作）；1500 °C 下 CMAS 粘度剧降使 RE 效应弱化（[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]），且 Lu2SiO5 相分解诱导晶间渗透（[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]）——1300 °C 半径规律不能外推到 1500 °C。
- 姊妹方向：TBC 候选材料与 TGO 的热化学相容性（[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]），选材流程缺此判据。
- 综述可用公理（1300 °C）+ 失效边界（1500 °C）+ 缺失判据（相稳定性、TGO 相容性）三层结构已成形。

## Methods You Can Inherit

| Method | Reusable idea | Suitable use | Main risk |
|---|---|---|---|
| 高温原位观察（#47/#16） | 相机记录熔化-铺展-析出全过程，区分高温生长与冷却析出；无 CMAS 对照分离基体失稳与熔体反应 | 1500 °C 级腐蚀机制研究、冷却环节权重评估 | 单样品表面，通量低 |
| 层叠法高通量筛选（#46） | 多种成分压同一块体、一次腐蚀截面直接对比 | 成分依赖规律的快速获取 | 层间致密度差异、层间扩散 |
| 高通量并行制备（#18） | 多成分并行制样 + 热物性/腐蚀联合表征 | 成分-结构-性能大样本关联 | 腐蚀条件单一 |
| 高熵多组分对照设计（#48） | 元素功能分工 + 高熵与单组分同条件对照 | 多目标（热导/TEC/CMAS）协同评估 | 单条件、等摩尔单点 |
| 粉末反应 + 扩散偶联用（#29） | 混合粉末定反应阈值与产物，扩散偶定动力学与方向 | TBC-TGO 相容性低成本评估 | 块体几何 ≠ 涂层薄层 |

## Crowded Directions

- Direction: 1300 °C 级 CMAS 抗性成分筛选（RE2SiO5 / RETaO4 / 高熵锆酸盐三体系）
  - Why crowded: 田志林组已三体系系统覆盖并建立热化学解释框架（#36 单组分奠基/#46/#18/#47 1300 °C 对照/#48/#16 对照），Costa et al. / Risbud et al. 上游热化学依据已成熟。
  - Evidence: "[[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"（strong）；#36 8 组分 + #18 19 成分大样本。

- Direction: 高熵 EBC/TBC 多目标设计（低热导 + TEC 匹配 + CMAS 抗性）
  - Why crowded: #48 元素功能分工与 #18 高熵设计准则已形成范式，单点创新空间收窄。
  - Evidence: "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"、"[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"。

- Direction: 单组分腐蚀产物鉴定（磷灰石 / 固溶体 / 石榴石）
  - Why crowded: 钽酸盐产物之争已由 #46 澄清；硅酸盐产物谱已由 #47/#16（磷灰石）、#36（磷灰石 + 铝酸盐石榴石 + 钙长石）与 #48（硅酸盐石榴石）覆盖。
  - Evidence: "[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"（strong）、"[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"。

## Open Entry Spaces

- Opportunity: 1500 °C 服役窗口的跨体系 CMAS 抗性地图（钽酸盐/锆酸盐/高熵硅酸盐高温数据）
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - Why still open: #46/#18/#48 实验设计仅 1300 °C；#47/#16 高温证据仅限 RE2SiO5；高温规律（弱化/相分解）跨体系普适性未知。
  - Supporting evidence: "[[synthesis/open-questions]]" Q1/Q6；#16 219 μm vs 50 μm。
  - Evidence strength: strong（空白是事实）

- Opportunity: 相稳定性（分解/熵稳定）作为高温抗蚀第一判据
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（相分解维度）
  - Why still open: #16 证实 Lu2SiO5 1500 °C 分解并定位为渗透通道，但其他 RE2SiO5 与高熵样品是否分解未知；高熵熵稳定效应在 1500 °C 无数据。
  - Supporting evidence: "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"（single-system strong）。
  - Evidence strength: strong（单体系）/ weak（普适性，AI 推断）

- Opportunity: 结构类型与 RE 半径对抗蚀贡献的解耦
  - Related gap: "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - Why still open: #18 中烧绿石/缺陷萤石与平均半径共线，双重机制相对权重未知；单硅酸盐侧 #36（X2 段递减）与 #21（X1 系列内部反向，未入库）构成晶型依赖翻转——结构效应可能大到反转半径规律，但两文未做解耦设计。
  - Supporting evidence: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"（strong）、#36 Fig. 11 + #47 引言引文 [18]。
  - Evidence strength: strong（共线/翻转为事实）

- Opportunity: 冷却析出产物与热循环完整性的因果链
  - Related gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - Why still open: #47/#16 两篇独立原位证据证实冷却析出，但剥落/开裂后果未评估；#16 显示 1500 °C 保温无反应、析出集中于冷却起始，冷却环节权重上升；#36 已在 1300 °C 观察到衰退层 E/TEC 失配的冷却热应力剥落——「冷却损伤」证据链从 2019 年延续至今仍未闭环。
  - Supporting evidence: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]" 冷却析出部分、#36 Key Claim 3。
  - Evidence strength: strong（析出事件 ×2 + 剥落观察 ×1）/ weak（后果为 AI 推断）

- Opportunity: 高通量方法跨体系推广与组合（层叠法 + 原位观察 + 并行制备 + 高熵设计）
  - Related gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - Why still open: 四方法各自单体系验证，未联用、未跨体系；该组工作节奏快，窗口期有限。
  - Supporting evidence: "[[synthesis/open-questions]]" Q4。
  - Evidence strength: strong（作者自述可推广）

- Opportunity: TBC-TGO 热化学相容性判据与扩散障方案（姊妹方向）
  - Related gap: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
  - Why still open: #29 单体系证实 Hf6Ta2O17 不相容，其他候选材料无数据；扩散障未验证；真实涂层未闭环。
  - Supporting evidence: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"（strong，单体系）。
  - Evidence strength: strong（单体系）/ weak（判据普适性）

## Possible Positioning Statements

### Positioning 1：1500 °C 服役窗口的跨体系 CMAS 抗性地图

- Core idea: 把钽酸盐/锆酸盐/高熵硅酸盐纳入统一 1500 °C 框架（层叠法 + 原位观察联用），检验「高温 RE 效应弱化」与「相分解」的跨体系普适性，建立按服役温度分级的成分设计准则。
- Supporting literature: #47/#16（1500 °C 原位方法学 + 双证据）、#36/#46/#18/#48（三体系 1300 °C 基线成分组，可直接复用）。
- Feasibility: 高——方法（原位观察/层叠法）均已在该组验证；材料基线已由 #36/#46/#18/#48 建立；仅需扩展到 1500 °C 实验条件。
- Risks: 该组节奏快，窗口期可能被抢占（Q4 提示检索 2026 新工作）；层叠法在 1500 °C 的层间扩散/致密度控制更苛刻。2026-08-28 检索发现该组已发表 RE2SiO5 层叠法筛选（Extreme Materials 2025，1(4): 27–32）——已核实仅 1300 °C/20 h 单温度，RE2SiO5 高温部分窗口未收窄；但该文引入新变数：按渗透深度排序 Er2SiO5 最优（非 Lu），「最优成分」本身存在指标依赖争议（衰退层厚度 vs 渗透深度），1500 °C 地图需先行统一评价指标。钽酸盐/锆酸盐 1500 °C 数据仍完全开放。
- Literature needed: #21（X1 系列，JECS 2019）原文数值（X1 反向趋势已锁定来源，未入库）；#59 是否正式入库由用户决策（缓存 10185 已就绪）。
- Status: promising（RE2SiO5 高温窗口未收窄；新增指标统一这一方法学前提）

### Positioning 2：相稳定性优先的高温抗蚀设计（相分解普适性 + 熵稳定验证）

- Core idea: 从 #16 相分解机制出发，系统检验 RE2SiO5 全系与高熵样品的 1500 °C 相稳定性（无 CMAS 对照 + TEM 晶界表征），回答「高熵化是解药（熵稳定）还是未知数」，把高温选材从「选成分」升级为「保相稳定」。
- Supporting literature: "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"（#16）、#47（1500 °C 七体系但未做 TEM/对照）、#48（高熵样品无高温数据）。
- Feasibility: 中高——#16 的对照实验设计（无 CMAS 退火 + TEM）可直接复制；需多成分样品与高温长时退火资源。
- Risks: 分解是否普适尚属未知（若仅 Lu 体系特有，问题降级为单体系机制细节）；相分解与 CMAS 腐蚀的耦合定量难度大。
- Literature needed: 其他 RE2SiO5 的 1500 °C 相图/分解文献；高熵陶瓷熵稳定效应的上游证据；第三方佐证——Li et al.（Ceram. Int. 2025）高熵单硅酸盐 1500 °C 层厚随平均半径单调递减（与 #47 高温反转方向一致，待核查原文）。
- Status: draft（依赖相分解普适性未知）

### Positioning 3：TBC 选材的 TGO 相容性强制判据与低成本评估（姊妹方向）

- Core idea: 把「TGO 热化学相容性」推广为 TBC 候选材料选材流程的强制判据，建立候选材料 × Al2O3 反应矩阵（粉末法低成本筛查），并验证扩散障方案。
- Supporting literature: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"（#29）；Li et al.（2011）旧结论已被修正。
- Feasibility: 中高——#29 的粉末反应 + 扩散偶方法学可直接迁移；与用户 EBC/CMAS 主线属姊妹方向，可共用材料与表征资源。
- Risks: 与用户博士课题主线（CMAS 腐蚀）偏离，需权衡投入；真实涂层闭环实验周期长。
- Literature needed: 其他候选材料（高熵锆酸盐/钽酸盐等）× Al2O3 反应数据；MCrAlY/Pt-Al 体系 TGO 知识。
- Status: promising（姊妹方向，供用户权衡）

## Next Evidence Needed

- 钽酸盐/锆酸盐/高熵硅酸盐 1500 °C 腐蚀截面数据（≥3 RE 成分 × 2 体系）——Positioning 1 的直接前提。
- 其他 RE2SiO5 与高熵样品的 1500 °C 无 CMAS 对照 + TEM 晶界表征——Positioning 2 的前提。
- X1-RE2SiO5 反应区宽度与 RE 半径关系反向报道的原文数值核查（2026-08-28 已完成溯源：#36 原文核实其 X2 段为递减趋势、与主线一致；反向趋势为 X1 大半径系列内部现象，源头为 #21 Tian et al., JECS 2019, DOI 10.1016/j.jeurceramsoc.2018.12.015，未入库）。
- 该组 2026 年新工作检索（2026-08-28 已完成一轮：发现 Extreme Materials 2025 层叠法 RE2SiO5、2026 Y4Al2O9/Y2O3 1300/1500 °C 等；Positioning 1 窗口部分收窄，钽酸盐/锆酸盐 1500 °C 仍开放）。
- 候选新论文（inbox.md Pending Papers）是否补录入库，待用户确认。
- 待用户填写 `memory/project_profile.md` 的核心研究问题与 Excluded 范围——定位方向将据此校准（当前三条定位为 AI 基于 7 篇语料的推断，标注 `AI 推断`）。

## Maintenance Checklist

- [x] Updated after important gap analysis.
- [x] Positioning claims linked to papers, claims or gaps.
- [x] Weak or speculative positioning marked as `AI 推断` or `待确认`.
- [x] Important changes reflected in `index.md`.
- [x] Operation recorded in `log.md`.
