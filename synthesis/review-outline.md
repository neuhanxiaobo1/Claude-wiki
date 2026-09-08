---
type: synthesis
status: draft
review_status: checked
created: 2026-08-28
updated: 2026-09-07
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

## Writing Contract

- 输出：暂定综述大纲、论证映射和三段可复用草稿，不是完整论文或已确定投稿结构。
- 用途：用户陶瓷-腐蚀领域的文献综述积累；具体读者/目标期刊、篇幅、格式和核心研究问题待确认。
- Working question：当前语料中，哪些实验结果能够支持陶瓷腐蚀评价，哪些机制与设计推论仍需证据？
- 范围：截至 2026-09-07 已复核的七篇论文；六篇 CMAS 为当前主要语料，Hf–Al₂O₃ 为可选界面案例。未建立领域系统检索覆盖，不永久排除其他材料/介质。
- 语言与引用：中文，英文题名/期刊保留；本页用 paper E# / claim 双链追溯源页图表与 DOI。正式引用样式未确定。
- 完成边界：旧主线、章节和草稿已替换，证据映射完成；不表示源内冲突、新颖性或用户选题已解决。

## Corpus and Evidence Readiness

完整实验/计算与比较矩阵见 [[synthesis/literature-map]]；材料范围见两个 topic。七篇来源集中于同一 collection 且作者有重叠，属于 local corpus。

四项 claim supported、Lu 相演化机制 partially-supported、三项跨体系/温度/双机制因果 insufficient-evidence。只有条件内事实可以确定陈述；后两类在正文中明确作为解释、局限或问题。五项 gap 为一项 corpus-gap 与四项 candidate-question，均无本轮领域新颖性检索支持。

## Writing Evidence Matrix

| ID | Proposed point | Evidence | Independent basis | Conditions / metric | Assessment and comparison | Boundary / allowed wording |
|---|---|---|---|---|---|---|
| R1 | 同名抗蚀指标并不自动可比 | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E1]]、[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] | 2019-corrosion；2023/2024 自身实验，对照重复引用 2019 | 衰退层 vs 最深渗透；负载/制备/供液不同 | 限定比较边界 supported/checked；not-directly-comparable | 不算 219/50 温度劣化倍数，不制造半径翻转 |
| R2 | 部分研究有条件内成分关联 | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E2]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]] | 2019-corrosion、2025-RETa-stack | 分别 1300 °C/50 h 衰退层与层叠渗透 | 本篇描述 supported/checked；内部 directly-comparable，跨体系 qualitative-only | 不是普适半径因果；层叠化学独立性未成立 |
| R3 | 四元样品表现性能折中 | [[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]、[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E2]]、[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]] | 2022 实验/计算，部分热物性对照转引 | 各热物性温区；1300 °C/20 h 作者深度 | supported/checked；腐蚀仅本篇直接描述比较 | Cp 估算/孔隙校正，HE 优于 Ho/Eu、劣于 Lu/Yb；不证熵协同 |
| R4 | 特定产物类别已有相证据 | [[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]、[[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]] | 2022-products、2025-RETa-stack；2019 既有相限制首次性 | 指定 1300 °C 暴露，XRD/局部成分/TEM | 类别 supported/checked；跨材料 qualitative-only | 精确通式、相作用和全部文献争议未确立 |
| R5 | Lu 相演化可能参与侵入 | [[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E1]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E5]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E6]] | 2024 热处理对照与腐蚀观察 | 1500 °C；初始二硅酸盐、局部 TEM | partially-supported/checked；控制条件仅定性机制线索 | 保留可能贡献，撤回唯一主因与高熵必然稳定化 |
| R6 | 黏度/热化学/无序解释不等于机制验证 | [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E5]]、[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E6]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]]、[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]]、[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | FactSage、Risbud/Costa 转引、固定 DFT、2026 实验 | 模型/参考态、映射与变量混杂 | 三项因果 claim insufficient-evidence/checked；不可合成统一定量律 | 模型结果/作者解释注明身份；样品映射先核清 |
| R7 | 析出时序与冷却损伤尚未闭合因果 | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E7]]、[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E4]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]] | 三篇各自观察，不是同一热历程重复 | 离位裂纹与原位选帧/正文时序 | 因果证据不足；qualitative-only | 不写仅冷却析出或每次冷却必然致损伤 |
| R8 | Hf 指定工艺反应不能直接转换为 TGO 寿命 | [[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]、[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]]、[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] | 2025 粉末/扩散偶及弹性模型 | 1400 °C 已反应；热压初始与追加退火分开 | 反应 supported/checked；向 TGO qualitative-only | 不套 YSZ 剪切限值判废，实际涂层验证未覆盖 |

## Candidate Thesis and Stress Test

### T1 — 从可比指标出发评价条件内结果与机制边界

- Thesis：这组文献提供了条件内成分差异、产物类别和性能折中的证据；将它们用于机制解释或选材之前，应保留测量定义、实验边界与原始来源，当前尚不能合成普适抗蚀排序。
- Evidence：R1–R7；包含 2019、2022、2023、2024、2025、2026 的不同原始实验组，但同源转引不重复计数。
- Scope：六篇 CMAS 的本地语料综合；不声称领域不存在规律或其他研究未解决问题。
- Status：provisional（写作框架）；其使用的限定事实/限制按矩阵评级。用户核心问题未确认，不能将框架写回 project_profile。
- Stress test：去掉 2019，需删去其成分趋势和被转引温度对照讨论，但 2022 性能折中、2025 独立性及 2026 映射问题仍支持证据分层的组织。去掉 2022，需删除特定四元性能/石榴石段，不以其他数据顶替。
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
| 1 评价对象、指标与语料边界 | 先说明比较什么、数据来自哪里 | 材料/条件 → 衰退层与最深渗透区别 → 比较资格 | R1/R2；literature-map | 仅本地语料；不把涂层背景扩大为已有服役验证 | 领域背景覆盖与最终纳排范围 | ready（语料说明与指标限定） |
| 2 条件内实验结果与性能折中 | 现有数据确实支持什么 | 单篇成分关联 → 四元收益/代价 → 产物类别 | R2/R3/R4 | 非严格单调、层间影响、精确相式未决；不能跨体系总排名 | 原始统计/相组成限制强推论，但不阻止限定事实 | ready（限定事实） |
| 3 从观察到机制解释 | 哪些链条尚不能写成因果 | 黏度/焓计算身份 → Lu 相演化线索 → 结构映射 → 时序/损伤 | R5/R6/R7 | 初始杂相、局部检测、同源转引与图文冲突 | 视频、热化学定义、样品对应及独立控制 | provisional（明确呈现未决） |
| 4 可比评价与候选研究问题 | 需要什么证据改变当前判断 | 指标/独立性验证 → 时序/映射核查 → 条件性研究问题 | R1–R7；新版 Q1–Q6 | 一项语料缺口及候选问题，不是已确认领域空白 | 新颖性检索、资源与用户目标 | provisional（研究建议） |
| 5 当前语料的综合认识 | 回答 working question，收束证据边界 | 保留限定事实 → 限制机制和排序外推 → 说明扩展条件 | R1–R7 | 不用“尚未证实”推断“全领域错误” | 最终问题与新增证据可能改变表述 | ready（本语料总结） |
| 可选模块 A Hf–Al₂O₃ 界面案例 | 区分反应存在与服役损伤 | 指定工艺反应 → 模型应力 → 实际 TGO 候选验证 | R8；Q7 | 单篇、块体/真实界面不同、应力分量不可套用 | 目标结构、实际热历程、前文全文 | provisional（纳入范围待定） |

ready 只表示可写表中限定功能。blocked 的强论证包括：普适半径律、已证黏度反转、无序输运确证、冷却析出必然致裂与 TGO 必然判废；这些不作为待填充的确定章节保留。

## Draft Paragraphs

### Paragraph 1 — 指标与温度比较

2019 年单硅酸盐研究将衰退层定义为溶解前沿至玻璃中含磷灰石层顶部的距离；2024 年 Lu₂SiO₅ 研究采用原表面至最深 CMAS 渗透位置，两者测量对象不同。[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E1]] [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] 后者引用前者约 50 μm 的 1300 °C/50 h 数据，与自身 1500 °C/50 h 的 219 μm 比较时，还存在制备、负载及供液差异，因此这一数值比不能解释为单独升温造成的抗蚀性劣化倍数。[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]]

- Sentence-to-evidence：句 1 → R1 的两项定义；句 2 → R1 的来源同源性及条件边界。
- 必须保留：指标基准、引用身份与比较限制；不能改写成两温度的同批受控实验。

### Paragraph 2 — 四元配方的收益与代价

2022 年四元 (Ho₀.₂₅Lu₀.₂₅Yb₀.₂₅Eu₀.₂₅)₂SiO₅ 研究报告热导为 1.07–1.47 W·m⁻¹·K⁻¹，该结果由热扩散测量、热容估算和孔隙校正得到。[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E2]] 在 1300 °C/20 h 的作者渗透指标下，四元样品为 125.4±8.7 μm，低于 Ho/Eu 对照、高于 Lu/Yb 对照，显示的是该配方的性能折中。[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]] 单一等摩尔配方及其对照不足以分离各元素贡献或确认熵效应，不能将这组结果概括为高熵材料全面优越。[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]]

- Sentence-to-evidence：句 1 → R3 热导计算身份；句 2 → R3 同条件排序；句 3 → R3 的因果限制。
- 必须保留：特定配方、温区/腐蚀条件、估算身份与代价；不能称全部热物性对照同批实测。

### Paragraph 3 — 可选界面案例

Hf₆Ta₂O₁₇–Al₂O₃ 研究在指定 1400 °C 粉末及扩散偶条件下观察到含 AlHf₃TaO₁₀ 的反应产物或反应层，支持这些工艺条件下的反应不相容。[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]] [[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]] [[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] 文中较高界面应力来自简化弹性模型，不能与另一材料的剪切许用值直接对照来确认实际涂层失效；实际 TGO 界面损伤仍需在对应结构和热历程中验证。[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] [[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E8]]

- Sentence-to-evidence：句 1 → R8 反应证据；句 2 → R8 模型、应力分量与应用覆盖限制。
- 必须保留：不是绝对反应阈值、不是应力实测、不是已测 TGO 循环寿命。

## Gaps, Citations and Revision

研究问题与检验/否定条件统一引用 [[synthesis/open-questions]]，具体 gap 分类以其原页面为准；定位只引用 [[synthesis/research-positioning]] 中 provisional 提案，不作创新性结论。正式正文采用源论文题名/DOI 等引用信息时回到 paper Metadata and Sources，当前双链不能代替最终参考文献排版。

2026-09-07：核心 thesis、章节顺序和原示例段落整体替换；每个实质性句子均有 E# 依据，不使用未读外部候选的精确排序或首次性。此次完成大纲及示例的证据映射，未完成全文撰写、领域检索或用户选题确认。同步 [[synthesis/core-argument-map]]，不保留旧主线作为恢复任务的入口。
