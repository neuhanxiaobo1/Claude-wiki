---
type: synthesis
status: active
review_status: checked
created: 2026-08-23
updated: 2026-09-09
questions:
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
claims:
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
  - "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
papers:
  - "[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]]"
  - "[[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C]]"
  - "[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening]]"
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
tags:
  - synthesis
  - open-question
  - gap
---

# Open Questions

## Scope and Status

本页依据 [[synthesis/literature-map]]、八项新版 claim 与五项 gap 更新，覆盖十篇已入库论文的声明范围证据。Q1–Q7 保留旧编号便于追溯，但问题含义按本页修订；旧优先级、确定反转与领域空白结论不再有效。

问题均为当前语料边界或 AI 推断的候选，未完成领域新颖性检索，研究优先级 pending。用户尚未确定材料主线/核心研究问题，见 [[memory/project_profile]]。checked 只表示问题前提与分类已核查，不表示已有答案。

## Question Triage

| ID | Current question | Basis and assessment | Classification / dependency | Evidence that could answer or weaken it |
|---|---|---|---|---|
| Q1 | 统一指标和实验边界后，指定体系的 1300/1500 °C 成分排序是否变化？ | [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]]；指定单硅酸盐的旧跨文献温度对照不可直接比较；[[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E1]]、[[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E4]] 新增二硅酸盐同篇两温50 h形貌证据，尚无统一厚度排序；[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]] 新增1300 °C单温相对基准，不能补成统一两温对照 | [[wiki/gaps/CMAS-Corrosion-Data-1500C]]，corpus-gap；不预设黏度致反转 | 同制备/供液/指标与重复统计的温度对照；排序稳定则削弱反转假说 |
| Q2 | 样品映射修复后，结构/半径效应是否可辨识？ | [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E2]]、[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]]；双机制 claim insufficient-evidence | [[wiki/gaps/Structure-Radius-Decoupling]]，candidate-question；先核身份 | 可追溯样品/半径/厚度、实测结构与可实现对照；映射修复后趋势消失则撤回原设计依据 |
| Q3 | 经确认的析出变化是否对冷却损伤有独立贡献？ | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E7]]、[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E4]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]]；时序冲突，离位裂纹不证因果；[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E6]]、[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E7]] 的局部模量/未见分层未验证循环寿命，[[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E7]] 的blister也不提供起裂时刻 | [[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]，candidate-question | 原视频/热历史、相演化与起裂同步及匹配对照；裂纹早于析出或受控后无贡献会削弱致裂解释 |
| Q4 | 不同基准下的层叠排序是否能由独立试样复现，位置/邻层/供液造成多大偏差？ | [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]] 的跨RE点成分；[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E5]] 的相对Er基准、清晰EDS分区与局部供液差异；两文证据各自保留；[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E2]]、[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E3]]、[[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E8]] 已有独立Y块体双深度，但尚非层叠配对对照 | [[wiki/gaps/High-Throughput-Screening-Transfer]]，candidate-question；RETaO₄与RE₂SiO₅层叠已有实施，不称迁移未开展 | 统一测厚定义后对比独立试样、层序/位置和局部供液，预设等效界限；复现成立则收窄配置担忧，偏差超出重复变异则限定排序 |
| Q5 | 统一热化学对象/参考态后，形成焓能解释哪些条件内腐蚀关联？ | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E6]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]]、[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]]；跨体系因果 insufficient-evidence；[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E8]] 仍转引Costa且主文焓方向不一致，不新增独立量热 | candidate-question，留在本页；不新增同义 gap | 原始量热/计算定义与可比反应体系；关联消失或受其他变量解释则削弱统一因果 |
| Q6 | Lu 的相演化在侵入中贡献多少，其他配方是否出现类似过程？ | [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E1]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E5]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E6]]；局部机制 partially-supported；[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]] 不证熵稳定；[[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C#E6]] 与 [[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E5]] 的晶界弱化假说不同于Lu单硅酸盐相分解，不能合并为已证共同根源 | candidate-question；与 Q1 的温度覆盖相关但不同 | 初始杂相定量、有/无 CMAS、相分数/路径追踪与可比配方；无相演化贡献或其他配方不分解则限定范围 |
| Q7 | 指定 Hf 涂层/TGO 结构中，块体反应是否转化为可区分损伤？ | [[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]、[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]]、[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]]；反应 supported，服役外推未验证 | [[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]，candidate-question | 明确界面温度/热历程、相层与损伤对照；目标条件下无可分离损伤则限定失效担忧 |

Q1 的“语料缺口”不等于全领域缺数据；Q5/Q6 是候选提案，不因没有独立 gap 页而消失，也不因引用多就升级为确定领域 gap。可行性与新颖性尚未确认，具体资源/混杂因素见对应 gap。

## Verification Order

以下是证据依赖顺序（AI 推断），不是研究价值排行榜：

1. 写作中只使用已经核实的事实与限制；Q2 映射、Q3 时序、Q5 参考态有疑点时暂停相关强推论。
2. 若要回答温度或方法比较（Q1/Q4），先统一指标、样品身份和实验边界，不能从不可比旧数值直接计算效应。
3. 若推进机制或涂层外推（Q3/Q6/Q7），先确认实际目标与可行对照，再决定是否需要新实验；本文提案不表示已启动实验。
4. 若要评估选题新颖性，围绕选定范围检索最接近工作和反例；历史检索线索不是本轮完整检索结论。

## Smaller Candidate Questions

| Candidate | Known basis | What remains / disconfirming evidence |
|---|---|---|
| 石榴石型相的作用 | [[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E7]]，相类别有支持；精确式未决 | 先相鉴定再控制相含量/分布与侵入；无独立影响会削弱保护/损伤假说 |
| 四元配方比例与性能折中 | [[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]]、[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]]，HE 不优于 Lu/Yb | 比例梯度与统一指标/微结构；收益伴代价或无改善均是可能结果，不预设最优 |
| RETaO₄ 晶间侵蚀的力学后果 | [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E4]]，局部产物与晶间形貌 | 独立损伤/力学数据及对照；产物存在本身不证明失效 |
| 锆酸盐富 Zr 颗粒的形成路径 | [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E6]]，相类别/成分线索 | 先核精确相与时序，再检验反应路径；不把含 Ca 区域直接当纯 ZrO₂ |
| Er/Lu 原位差异 | [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E4]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]] | 纳入 Q3 前置核查；视频/温标核清前不归因为 RE 形成焓差异 |

这些条目均为 AI 推断的候选，novelty_status: not-assessed，不另建 gap，不据此确认学术优先权。

## Revision and Handoff

2026-09-07：替换旧高/中优先级和确定机制前提，保留 Q1–Q7 身份，增加可回答/否定条件。此前提到的 #59、JECS 2019 及其他第三方候选仅保留在历史记录中作为检索线索，未经本轮原文核查的排序不进入当前证据。

[[synthesis/research-positioning]] 将这些问题作为条件性提案；[[synthesis/review-outline]] 只以其作为局限或候选研究方向。本页不决定用户课题，也不默认恢复新论文入库。

2026-09-08：#59 已正式进入Q1/Q4/Q5前提；Q3/Q6因果评价不因其离位裂纹/未核S1升级，其余问题范围保留。对应大纲R9/R10与P1已同步；旧“#59仅历史线索”状态由本次整合接续，新颖性仍not-assessed。

2026-09-08 #17/#23接续：Q1已补二硅酸盐同篇两温覆盖。Q3/Q4/Q6后续可分别考虑#17局部未见分层/独立Y试样与#23晶界路径，但不视为热循环、层叠等效或软化因果已被验证。

2026-09-09：#17/#23正式进入Q3/Q4/Q6（Q1两温覆盖已接续）；只更新问题前提和区分所需证据，不提升因果或新颖性评级。
