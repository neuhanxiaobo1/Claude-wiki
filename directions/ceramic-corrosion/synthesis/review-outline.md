---
direction_id: ceramic-corrosion
type: synthesis
status: draft
review_status: checked
created: 2026-08-28
updated: 2026-09-09
reviews:
  - "[[directions/ceramic-corrosion/wiki/reviews/CMAS-Review-Section-1-Evaluation-and-Comparability]]"
topics:
  - "[[directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion]]"
  - "[[directions/ceramic-corrosion/wiki/topics/Thermal Barrier Coatings]]"
papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
claims:
  - "[[directions/ceramic-corrosion/wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]"
  - "[[directions/ceramic-corrosion/wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[directions/ceramic-corrosion/wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]"
  - "[[directions/ceramic-corrosion/wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - "[[directions/ceramic-corrosion/wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - "[[directions/ceramic-corrosion/wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - "[[directions/ceramic-corrosion/wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
  - "[[directions/ceramic-corrosion/wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
gaps:
  - "[[directions/ceramic-corrosion/wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[directions/ceramic-corrosion/wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[directions/ceramic-corrosion/wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[directions/ceramic-corrosion/wiki/gaps/High-Throughput-Screening-Transfer]]"
  - "[[directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
tags:
  - synthesis
  - review
---

# Review Outline

## Writing Contract

- 输出：暂定综述大纲、论证映射和五段可复用草稿，不是完整论文或已确定投稿结构。
- 用途：用户陶瓷-腐蚀领域的文献综述积累；具体读者/目标期刊、篇幅、格式和核心研究问题待确认。
- Working question：当前语料中，哪些实验结果能够支持陶瓷腐蚀评价，哪些机制与设计推论仍需证据？
- 范围：截至 2026-09-09 已入库的十篇论文；九篇 CMAS 为当前主要语料，Hf–Al₂O₃ 为可选界面案例。未建立领域系统检索覆盖，不永久排除其他材料/介质。
- 语言与引用：中文，英文题名/期刊保留；本页用 paper E# / claim 双链追溯源页图表与 DOI。正式引用样式未确定。
- 完成边界：旧主线、章节和草稿已替换，证据映射完成；不表示源内冲突、新颖性或用户选题已解决。

## Corpus and Evidence Readiness

完整实验/计算与比较矩阵见 [[directions/ceramic-corrosion/synthesis/literature-map]]；材料范围见两个 topic。十篇来源集中于同一 collection 且作者有重叠，属于 local corpus。

四项 claim supported、Lu 相演化机制 partially-supported、三项跨体系/温度/双机制因果 insufficient-evidence。只有条件内事实可以确定陈述；后两类在正文中明确作为解释、局限或问题。五项 gap 为一项 corpus-gap 与四项 candidate-question，均无本轮领域新颖性检索支持。

## Writing Evidence Matrix

| ID | Proposed point | Evidence | Independent basis | Conditions / metric | Assessment and comparison | Boundary / allowed wording |
|---|---|---|---|---|---|---|
| R1 | 同名抗蚀指标并不自动可比 | [[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E1]]、[[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]、[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] | 2019-corrosion；2023/2024 自身实验，对照重复引用 2019 | 衰退层 vs 最深渗透；负载/制备/供液不同 | 限定比较边界 supported/checked；not-directly-comparable | 不算 219/50 温度劣化倍数，不制造半径翻转 |
| R2 | 部分研究有条件内成分关联 | [[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E2]]、[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]]、[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]] | 2019-corrosion、2025-RETa-stack | 分别 1300 °C/50 h 衰退层与层叠渗透 | 本篇描述 supported/checked；内部 directly-comparable，跨体系 qualitative-only | 不是普适半径因果；层叠化学独立性未成立 |
| R3 | 四元样品表现性能折中 | [[directions/ceramic-corrosion/wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]、[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E2]]、[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]] | 2022 实验/计算，部分热物性对照转引 | 各热物性温区；1300 °C/20 h 作者深度 | supported/checked；腐蚀仅本篇直接描述比较 | Cp 估算/孔隙校正，HE 优于 Ho/Eu、劣于 Lu/Yb；不证熵协同 |
| R4 | 特定产物类别已有相证据 | [[directions/ceramic-corrosion/wiki/claims/Garnet-Product-RE2SiO5-CMAS]]、[[directions/ceramic-corrosion/wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]] | 2022-products、2025-RETa-stack；2019 既有相限制首次性 | 指定 1300 °C 暴露，XRD/局部成分/TEM | 类别 supported/checked；跨材料 qualitative-only | 精确通式、相作用和全部文献争议未确立 |
| R5 | Lu 相演化可能参与侵入 | [[directions/ceramic-corrosion/wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]、[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E1]]、[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E5]]、[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E6]] | 2024 热处理对照与腐蚀观察 | 1500 °C；初始二硅酸盐、局部 TEM | partially-supported/checked；控制条件仅定性机制线索 | 保留可能贡献，撤回唯一主因与高熵必然稳定化 |
| R6 | 黏度/热化学/无序解释不等于机制验证 | [[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E5]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E6]]、[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]]、[[directions/ceramic-corrosion/wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]]、[[directions/ceramic-corrosion/wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | FactSage、Risbud/Costa 转引、固定 DFT、2026 实验 | 模型/参考态、映射与变量混杂 | 三项因果 claim insufficient-evidence/checked；不可合成统一定量律 | 模型结果/作者解释注明身份；样品映射先核清 |
| R7 | 析出时序与冷却损伤尚未闭合因果 | [[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E7]]、[[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E4]]、[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]] | 三篇各自观察，不是同一热历程重复 | 离位裂纹与原位选帧/正文时序 | 因果证据不足；qualitative-only | 不写仅冷却析出或每次冷却必然致损伤 |
| R8 | Hf 指定工艺反应不能直接转换为 TGO 寿命 | [[directions/ceramic-corrosion/wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] | 2025 粉末/扩散偶及弹性模型 | 1400 °C 已反应；热压初始与追加退火分开 | 反应 supported/checked；向 TGO qualitative-only | 不套 YSZ 剪切限值判废，实际涂层验证未覆盖 |
| R9 | 相对侵入与可见产物不是同一评价指标 | [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]]、[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]]、[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E3]]、[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E4]] | 2025-RE2SiO5-stack；本文新增实验，非2019数据转引 | 七RE层叠块体；1300 °C/20 h，30 mg/cm²；以Er为相对深度零点 | 本试样图示描述 supported/checked；与2019/2023/2024厚度 not-directly-comparable | Er最浅、Tm次之；Lu可见产物少却非最浅；零点非零侵入，不称显著最优或普适排名 |
| R10 | 层叠同炉比较已有实现，独立试样等效性仍需验证 | [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]]、[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E5]]；[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]] | 2025-RE2SiO5-stack 与 2025-RETa-stack；不同研究配置 | #59相对Er基准；RETaO₄原表面参照；各文条件分别保留 | 方法实施 supported/checked；跨方法 qualitative-only，独立成分本征排序未确立 | #59清晰EDS分区和局部供液差异，不能照搬RETaO₄跨RE点成分为其已证污染；未校准不等于方法无效 |
| R11 | 浅表层薄不代表晶界侵入浅 | [[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E1]]、[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E2]]、[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E3]] | 2024-MYTa-corrosion | 独立块体，1300 °C/5、50、80 h，约30 mg/cm²；双深度 | 同篇描述 supported/checked；跨文献 not-directly-comparable | 80 h浅区43.7±6.6、晶界346.3±3.7 μm；不以浅层代替最深侵入，不拟合普适速率 |
| R12 | 二硅酸盐已有同篇两温形貌证据 | [[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E1]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E2]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E4]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E5]] | 2019-disilicate-corrosion | 三种二硅酸盐，1300/1500 °C、50 h、约30 mg/cm² | 条件内形貌 supported/checked；两温 qualitative-only | 1500 °C广泛晶界玻璃/裂纹并存于Y/Yb表面磷灰石；无统一深度排名反转或普适临界温度 |
| R13 | 晶界物性、侵入与损伤须分别评价 | [[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E5]]、[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E6]]、[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E7]]；[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E6]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E7]] | 两篇腐蚀实验各自独立；#17引用#23作类比，#23部分内耗转引 | #17局部热处理TEM/5 h还原模量；#23内耗与离位裂纹 | 观察/测量checked；软化及损伤因果partial/insufficient，qualitative-only | 不能计为两次受控软化验证；未见分层不证热循环寿命；内耗4/10 °C/min冲突保留 |

## Candidate Thesis and Stress Test

### T1 — 从可比指标出发评价条件内结果与机制边界

- Thesis：这组文献提供了条件内成分差异、产物类别、性能折中及相对侵入筛选的证据；将它们用于机制解释或选材之前，应保留测量定义、实验边界与原始来源，当前尚不能合成普适抗蚀排序。
- Evidence：R1–R7、R9–R13；包含 2019、2022、2023、2024、2025、2026 的不同原始实验组，但同源转引不重复计数。
- Scope：九篇 CMAS 的本地语料综合；不声称领域不存在规律或其他研究未解决问题。
- Status：provisional（写作框架）；其使用的限定事实/限制按矩阵评级。用户核心问题未确认，不能将框架写回 project_profile。
- Stress test：去掉2019单硅酸盐论文，需删去其成分趋势和被转引温度对照讨论，但 2022 性能折中、2025 独立性及 2026 映射问题仍支持证据分层的组织。去掉 2022，需删除特定四元性能/石榴石段，不以其他数据顶替。
- #59 压力测试：去掉本篇，须删除 Er 相对参照及 Lu 产物/侵入对照实例；R1 的既有指标差异和 RETaO₄ 方法边界仍支持 T1。加入本篇不把 2019 与 2025 的不同排序改写为已证规律反转；S1 缺失不影响相对基准论证，但阻止其逐点组成进入确定机制。
- 新增来源压力测试：去掉#17须删除双深度和局部模量/无分层实例；去掉#23须删除同篇两温二硅酸盐实例。原指标比较框架仍成立，但不再由这两项补充支撑。#17对#23的类比及部分内耗转引不能重复计为独立软化验证。
- 依赖检查：不把三项 insufficient-evidence 机制当成正确前提；不将不可比数值用于排名。若后续取得统一指标/独立控制证据，应相应提升局部判断并调整章节。
- Result：reorganize；替代旧“公理—反转—缺失判据”叙事。

### T2 — 材料反应向实际界面的外推边界（可选模块）

- Thesis：Hf–Al₂O₃ 案例可以说明块体反应证据与实际界面损伤证据的区别。
- Evidence：R8；仅一篇原始研究，不能制造多篇独立支持。
- Status：provisional；若最终综述只讨论 CMAS，可不纳入此模块，不将其称为用户已确认的姊妹方向。
- Stress test：去掉 Hf 论文，本模块失去依据，应删除；T1 不受影响。模型应力不承担实际失效证明。
- Result：narrow；不保留“领域缺强制 TGO 判据”。

旧普适半径因果、高温必然反转、相稳定性/TGO 为全领域缺失判据均 withdraw，不能通过在文末补免责声明继续用作标题论点。

## Evidence-Based Outline

| Section | Question / function | Allowed claim sequence | Evidence IDs | Boundary / counter-evidence | Missing evidence | Readiness |
|---|---|---|---|---|---|---|
| 1 评价对象、测量基准与比较资格 | 明确测了什么，哪些数据能比较 | 材料/语料 → 衰退层、最深侵入与相对侵入与#17双深度 → 制备/供液/时长边界 | R1/R9/R10/R11/R12；literature-map | Er相对零点非零腐蚀；不比较绝对厚度倍数 | 领域背景与最终纳排范围；#59绝对基准/统计 | ready（定义与限定比较） |
| 2 条件内成分结果、产物与性能折中 | 区分侵入结果、产物表征和多性能收益 | 单篇关联及#23两温形貌 → #59 Er/Lu形貌与相对侵入 → 四元收益/代价 → 相类别 | R2/R3/R4/R9/R11/R12 | 图示排序限本配置；可见产物不是总产率；不同论文不合并排名 | 统计、定量产物/溶解量、S1与精确相式 | ready（限定事实） |
| 3 溶解、析出与侵入的机制证据 | 从哪些观察可以走向机制解释 | 终态形貌/组成 → 黏度与焓模型 → Lu相演化 → 晶界物性/时序/损伤 | R5/R6/R7/R13；#59 E6–E8 | S1未读；焓方向源内矛盾；裂纹不证明冷却析出因果；不重复计Costa | S1、视频、热化学定义、样品映射和独立控制 | provisional（作者解释与未决分开） |
| 4 层叠筛选的验证与候选研究问题 | 如何验证条件内排序向独立试样迁移 | 两种层叠已实施 → 各自基准/供液/层间证据 → 已有#17独立试样与配对缺口 → 独立/换序对照 → 条件性温度比较 | R1/R9/R10/R11/R12；Q1/Q4，机制问题接Q3/Q5/Q6 | 方法已实施不等于已校准；未校准不等于无效；不称跨体系尚无人尝试 | 独立试样、位置/层序、重复与等效判据；新颖性/资源 | provisional（候选验证路径） |
| 5 当前语料的综合认识 | 回答working question | 分开产物/溶解/侵入 → 保留条件内结果 → 明确机制与选材外推条件 | R1–R7、R9–R13 | 九篇CMAS不是领域代表性共识；不把未证实写成全领域错误 | 最终范围与领域补证据 | ready（本语料总结） |
| 可选模块 A Hf–Al₂O₃ 界面案例 | 区分反应存在与服役损伤 | 指定工艺反应 → 模型应力 → 实际 TGO 候选验证 | R8；Q7 | 单篇、块体/真实界面不同、应力分量不可套用 | 目标结构、实际热历程、前文全文 | provisional（纳入范围待定） |

ready 只表示可写表中限定功能。blocked 的强论证包括：普适半径律、已证黏度反转、无序输运确证、冷却析出必然致裂与 TGO 必然判废；这些不作为待填充的确定章节保留。

## Section Cards — 本轮细化

| Subsection | Function / claim sequence | Evidence / comparison | Boundary and transition | Readiness |
|---|---|---|---|---|
| 1.1 对象与数据范围 | 九篇CMAS块体研究；界面案例单列 | literature-map；R1–R13各自范围 | 本地语料，不能代表全部涂层服役研究 | ready |
| 1.2 测量基准与双深度 | 2019衰退层 → 2023/2024最深侵入 → #59相对Er基准 → #17浅表/晶界双深度 | R1/R9/R11；跨论文 not-directly-comparable | 先定义再解释排序；相对零点不提供绝对侵入量 | ready |
| 1.3 比较资格 | 温度、时长、负载、制样及局部供液逐项核对，区分跨文献拼接与#23同篇两温 | R1/R10/R12/R13；方法 qualitative-only | 同名指标、同炉和同名义配方均不能单独保证等效 | ready |
| 2.1 条件内成分差异 | 分别报告2019、RETaO₄与#59本试样结果 | R2/R9/R11/R12；内部限定描述，跨篇不总排名 | 把不同结果带入指标/实验边界解释，不预设物理反转 | ready |
| 2.2 产物形貌与侵入 | #59 Lu可见产物少但Er相对侵入更浅 | R9；同一试样内对照 | 可见覆盖不是总产率或析出速率；过渡到第3节机制证据 | ready |
| 2.3 物相与性能折中 | 保留原四元性能及产物类别段 | R3/R4 | #59整体XRD不能代替逐组精确相组成 | ready |
| 3.1 溶解—析出解释 | 把主文解释与实测结果分开列出 | #59 E4/E6/E8；R6 | S1未核、焓冲突及终态成分不能独立分离通量；不写成已证协同机制 | provisional |
| 3.2 相演化与损伤 | Lu相演化与#23晶界弱化假说分开；#17物性/未见分层与#59裂纹观察 | R5/R7/R13；#59 E7 | 冷却后截面不能给出起裂时刻，不升级为共同冷却致裂机制 | provisional |
| 4.1 两套层叠筛选 | 描述RETaO₄和RE₂SiO₅各自已实现的比较 | R10；qualitative-only | 相对基准与原表面参照不同；两文污染/供液证据不能互相移植 | ready（方法事实） |
| 4.2 排序的验证路径 | #17独立试样仅线索；层序/位置、局部供液、预设重复/等效界限 | Q4/P1；AI推断的候选对照 | 复现成立则收窄方法担忧；统计不显著不自动等效 | provisional |
| 4.3 定向补证据 | 先补能改变章节判断的来源，再评估温度扩展 | 下表；Q1/Q4/Q5 | 不以缺文献推断领域空白 | provisional |

## Targeted Evidence Needs

这是本地写作缺口清单，尚未启动新论文入库或领域检索；优先从本地PDF/MD与Zotero附件取得材料。

| Need | Serves section / question | What changes after obtaining it | Current action |
|---|---|---|---|
| #59 Table S1及测点/误差定义 | 2.2、3.1 | 核对残余熔体组成和统计；即使取得也不自动证明溶解通量 | 缺少时保留主文作者报告，不阻塞1.2/2.2限定事实 |
| 明确测厚端点、熔体负载/保持及独立试样的研究 | 1.2–1.3、4.1–4.2；Q1/Q4 | 判断指标与构型差异是否已有校准，补充其他团队视角 | 下一轮定向筛选，不能仅按相同材料关键词入库 |
| 同材料层叠/独立试样或位置/供液对照 | 4.2；P1 | 可支持或削弱配置偏差问题；决定P1是否仍有研究必要 | #17已有独立Y试样，尚非配对校准；先查最接近工作，再谈创新性 |
| Costa原始热化学及计算参考态 | 3.1；Q5 | 明确热化学对象、方向与可外推范围 | 不按多篇转引累计独立验证 |

## Draft Paragraphs

第一节连续正文已于2026-09-08试写为 [[directions/ceramic-corrosion/wiki/reviews/CMAS-Review-Section-1-Evaluation-and-Comparability]]，含1.1–1.3及指标对照表；下方五段保留为大纲层的论证示例，不代表五个章节全文均已完成。第一节仍为draft，现阶段优先审阅其范围和行文，再决定扩写第2节或定向补证据。

### Paragraph 1 — 指标与温度比较

2019 年单硅酸盐研究将衰退层定义为溶解前沿至玻璃中含磷灰石层顶部的距离；2024 年 Lu₂SiO₅ 研究采用原表面至最深 CMAS 渗透位置，两者测量对象不同。[[directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E1]] [[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] 后者引用前者约 50 μm 的 1300 °C/50 h 数据，与自身 1500 °C/50 h 的 219 μm 比较时，还存在制备、负载及供液差异，因此这一数值比不能解释为单独升温造成的抗蚀性劣化倍数。[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]]

- Sentence-to-evidence：句 1 → R1 的两项定义；句 2 → R1 的来源同源性及条件边界。
- 必须保留：指标基准、引用身份与比较限制；不能改写成两温度的同批受控实验。

### Paragraph 2 — 四元配方的收益与代价

2022 年四元 (Ho₀.₂₅Lu₀.₂₅Yb₀.₂₅Eu₀.₂₅)₂SiO₅ 研究报告热导为 1.07–1.47 W·m⁻¹·K⁻¹，该结果由热扩散测量、热容估算和孔隙校正得到。[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E2]] 在 1300 °C/20 h 的作者渗透指标下，四元样品为 125.4±8.7 μm，低于 Ho/Eu 对照、高于 Lu/Yb 对照，显示的是该配方的性能折中。[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]] 单一等摩尔配方及其对照不足以分离各元素贡献或确认熵效应，不能将这组结果概括为高熵材料全面优越。[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]]

- Sentence-to-evidence：句 1 → R3 热导计算身份；句 2 → R3 同条件排序；句 3 → R3 的因果限制。
- 必须保留：特定配方、温区/腐蚀条件、估算身份与代价；不能称全部热物性对照同批实测。

### Paragraph 3 — 可选界面案例

Hf₆Ta₂O₁₇–Al₂O₃ 研究在指定 1400 °C 粉末及扩散偶条件下观察到含 AlHf₃TaO₁₀ 的反应产物或反应层，支持这些工艺条件下的反应不相容。[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]] [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]] [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] 文中较高界面应力来自简化弹性模型，不能与另一材料的剪切许用值直接对照来确认实际涂层失效；实际 TGO 界面损伤仍需在对应结构和热历程中验证。[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E8]]

- Sentence-to-evidence：句 1 → R8 反应证据；句 2 → R8 模型、应力分量与应用覆盖限制。
- 必须保留：不是绝对反应阈值、不是应力实测、不是已测 TGO 循环寿命。

### Paragraph 4 — 相对测厚与产物评价

Zheng 等在七种 RE₂SiO₅ 的层叠块体上开展了 1300 °C/20 h、30 mg/cm² 的 CMAS 试验，并以侵入最浅的 Er 区域为相对深度参照。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]] [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]] 图中 Er 最浅、Tm 次之；Lu 表面可见腐蚀产物较少，却未呈现最浅的相对侵入。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E3]] [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E4]] 因而，本试样的形貌与侵入对照支持分别讨论可见产物和侵入指标，不能单凭产物少确定抗蚀排序。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E3]] [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E4]] 这一相对零点不表示 Er 无腐蚀；其数值也不能直接与以溶解前沿或原始表面起算的其他论文厚度合并。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]]

- Sentence-to-evidence：句1 → E1/E2；句2 → E3/E4；句3 → 两项观察的限定综合（R9）；句4 → E2及R1。
- 必须保留：层叠块体、温度/时长/负载、相对基准和图示描述；不写统计显著最优、总产物产率或跨论文反转。

### Paragraph 5 — 层叠方法的比较与验证

RE₂SiO₅ 与 RETaO₄ 研究均已采用层叠试样开展多成分 CMAS 比较，但前者以 Er 区域为相对侵入参照，后者使用原表面参照，两套测厚结果需分别解释。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]] [[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]] [[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]] RE₂SiO₅ 试样的 EDS 分区清楚，同时存在局部 CMAS 分布与侧边流动的差异；这些观察尚不能独立证明各层供液一致或全部传输为零。[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E5]] 因此，可将独立试样、层序或位置变换及局部供液对照作为检验排序稳定性的候选路径；这是本综述提出的验证建议，而非已经证实层叠方法失效。[[directions/ceramic-corrosion/wiki/gaps/High-Throughput-Screening-Transfer]]

- Sentence-to-evidence：句1 → R10的两套方法和各自测厚定义；句2 → #59 E5的观察与证据限制；句3 → Q4/P1，AI推断。
- 必须保留：未发现独立验证不等于不存在全部相关研究；#59未直接证明的跨RE污染不能由RETaO₄结果代替。

## Gaps, Citations and Revision

研究问题与检验/否定条件统一引用 [[directions/ceramic-corrosion/synthesis/open-questions]]，具体 gap 分类以其原页面为准；定位只引用 [[directions/ceramic-corrosion/synthesis/research-positioning]] 中 provisional 提案，不作创新性结论。正式正文采用源论文题名/DOI 等引用信息时回到 paper Metadata and Sources，当前双链不能代替最终参考文献排版。

2026-09-07：核心 thesis、章节顺序和原示例段落整体替换；每个实质性句子均有 E# 依据，不使用未读外部候选的精确排序或首次性。此次完成大纲及示例的证据映射，未完成全文撰写、领域检索或用户选题确认。同步 [[directions/ceramic-corrosion/synthesis/core-argument-map]]，不保留旧主线作为恢复任务的入口。

2026-09-08：正式纳入 #59 至元数据、R9/R10、T1压力测试、五节大纲及小节卡片；新增两段有E#定位的草稿和定向补证据表。R1–R8保留原编号；五节主结构与可选Hf模块保留。Q1/Q4/Q5与P1已同步；写作仍为draft，未形成完整正文或确认研究选题。

2026-09-09：#17/#23正式整合；大纲覆盖10篇，R1–R13及更新后小节卡片；第一节已由五篇扩展为七篇直接来源。第二节及后续仍为大纲/示例，未假定机制确证。P1/P2与Q1/Q3/Q4/Q6同步边界，未确认选题。
