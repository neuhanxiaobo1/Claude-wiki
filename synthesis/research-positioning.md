---
type: synthesis
status: draft
review_status: checked
created: 2026-08-28
updated: 2026-09-08
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

## User Goal and Evidence Boundary

用户已确认陶瓷-腐蚀领域和文献综述用途，尚未确定核心问题与具体材料主线（[[memory/project_profile]]）。本轮任务是纠正旧定位的证据前提，**没有选定研究方向**。以下均为 AI 推断、provisional；新颖性 not-assessed、资源可行性 pending，不使用 promising/high 等成熟选题评级。

八篇语料与比较边界见 [[synthesis/literature-map]]；Q 编号以 [[synthesis/open-questions]] 为准。同一 collection 的材料实例不足以判定一个方向“拥挤”“无人研究”或“窗口仍开放”。

## Existing Contributions and Remaining Boundaries

| Existing contribution | Evidence | Remaining boundary |
|---|---|---|
| 条件内成分差异及多性能折中 | [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E2]]、[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]] | 不证明跨体系半径律；测厚与微结构不同 |
| 局部相鉴定与相演化线索 | [[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E7]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E4]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E5]] | 精确组成/路径、因果贡献不随物相类别一并确证 |
| Hf–Al₂O₃ 指定工艺反应 | [[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]] | 不证明实际 TGO 循环失效或所有材料都缺数据 |
| 原位、层叠、并行制备与多性能表征 | [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E3]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E1]]、[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E1]]、[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]] | 方法已有用途；组合不是自动创新，层叠/映射/因果独立性须验证 |

## Candidate Positioning Statements

### P1 — 可比条件下的 CMAS 成分评价

- 对应：Q1/Q4；[[wiki/gaps/CMAS-Corrosion-Data-1500C]]、[[wiki/gaps/High-Throughput-Screening-Transfer]]。
- 候选定位：选定一个材料体系，先检验指标、供液与试样配置对排序的影响，再判断是否有必要扩展温度；不以“验证已知高温反转”为出发点。
- 新增直接基础：[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E3]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E5]] 表明七组分层叠筛选已实施，Er为相对侵入基准，且存在局部供液差异。P1需要验证测厚与构型对排序的影响，不能再把“把层叠法迁移至单硅酸盐”本身作为待实现贡献，也不以未校准推断方法无效。
- 已有基础：[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E1]]、[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]、[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]] 明确比较/独立性边界。潜在贡献是可验证的条件内评价关系，不是预设跨体系抗性总榜。
- 最小路径（AI 推断）：统一绝对/相对测厚与试样定义 → 独立试样、位置/层序及局部供液对照 → 预设重复性/等效判据 → 有目标依据时加温度对照。
- 可行性 pending：需要制样、热历程、熔体保持和表征资源；“仅把温度升高即可”不成立。
- 竞争工作/新颖性 not-assessed：需检索同材料、指标、方法与温区的最接近研究，包括已核主文的#59及其最接近独立试样/供液对照研究；不能由当前语料缺失判断空白。
- 收窄/放弃条件：已有工作已充分回答同问题；配置偏差可忽略且温度扩展不改变目标判断；或对照无法实现且无法界定外推范围。
- 状态：provisional，尚未由用户选择。

### P2 — 相演化与腐蚀路径的独立贡献

- 对应：Q3/Q6，必要时联系 Q2；[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]、[[wiki/gaps/Structure-Radius-Decoupling]]。
- 候选定位：对明确定义的单硅酸盐组成，先核查初始杂相及高温/冷却时序，再检验相演化与侵入/损伤的因果联系；高熵是否稳定仅是可选待检验假说。
- 已有基础：[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]] 为 partially-supported；[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E1]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]]、[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E6]] 限制排他机制；[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]] 不支持已证熵稳定。
- 最小路径（AI 推断）：核清视频/原始相证据 → 定量初始杂相和相演化 → 匹配热历史/微结构的对照 → 追踪侵入或损伤。若选择锆酸盐结构问题，须先解决样品映射，不能直接套此路线。
- 可行性 pending：需要可追踪相变化、定量相组成与适当损伤/路径测量；局部 TEM 不能独立排除全部晶界因素。
- 竞争工作/新颖性 not-assessed：需检索相稳定、杂相侵蚀与时序研究，区分本文未做和已有答案；不能把相稳定性列为此前缺失的普适首要判据。
- 收窄/放弃条件：相变化对所测侵入/损伤无独立贡献；差异被初始杂相或热历史解释；或外部工作已解决同范围问题。
- 状态：provisional，尚未由用户选择。

### P3 — 块体相容性结果向实际界面的外推

- 对应：Q7；[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]。
- 候选定位：只有目标确实涉及 Hf₆Ta₂O₁₇ 与含 Al₂O₃ 界面时，才评估反应层在指定涂层结构和热历程中的形成与损伤贡献。
- 已有基础：[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]、[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] 已确认指定工艺反应，[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] 仅为简化应力模型；不是“其他候选材料全无数据”的证据。
- 最小路径（AI 推断）：定义实际结构/界面温度 → 检查块体与目标边界差异 → 匹配对照和直接相层/损伤测量。扩散障是后续可选方案，未证有效，也非本轮任务。
- 可行性 pending：目标涂层、制备和循环资源均未确认；不能以粉末试验存在推断真实界面实验低成本可行。
- 竞争工作/新颖性 not-assessed：需核此前 Hf–Al₂O₃ 全文与相关界面研究，不能宣称已完全推翻 Li 或首次建立判据。
- 收窄/放弃条件：用户目标不含该界面；目标条件下没有可区分的反应损伤；已有研究已满足实际判断需要。
- 状态：provisional，尚未由用户选择；不再称为相对某个已确认主线的“姊妹方向”。

## What Would Make a Direction Reviewable

- 明确材料/腐蚀介质、目标输出与关键判据，并据用户研究目标确定纳排范围。
- 将对应的 source E# 未决限制到不会改变研究前提的程度；可保留暂时无答案，不强行补齐。
- 记录最接近竞争工作、检索范围与反例，判断新颖性；没有这一步不称领域 gap。
- 核对实际资源、对照可实现性和使方向失效的结果，避免只列设备名称就宣称可行。

这些条件是后续定位工作的依据，不妨碍当前基于可靠事实完成暂定综述结构。

## Revision Record

2026-09-07：撤回“1300 °C 公理—1500 °C 失效—缺失判据”定位、拥挤程度/空白窗口判断与高可行性承诺。P1/P2/P3 继承旧三条提案的讨论身份，但内容已收窄，均未确认为用户方向。大纲见 [[synthesis/review-outline]]，任务快照见 [[synthesis/core-argument-map]]。

2026-09-08：#59 正式补入P1及竞争工作范围；相对深度不作为绝对值、清晰EDS不作为完全独立性证明。P1继续provisional；本轮写作从评价指标部分展开不等于用户已选择P1作为博士课题。P2/P3不作扩展，新颖性和资源仍待评估。


## 2026-09-08 #17与#23入库交接

当前库10篇（9篇CMAS）；上文保留已完成的8篇大纲/定位版本，本次未重写全部章节。新增 [[wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]] 的浅表/晶界双深度、独立M-YTaO₄产物与局部模量，以及 [[wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C]] 的三种二硅酸盐同篇1300/1500 °C、50 h形貌对照。第1/3/4节、P1/P2后续整合须保留：双深度端点不同；热循环寿命未验证；两温形貌不同不等于统一指标排名反转；内耗/TEM支持机制线索，不证明软化独立因果。Q1和指定材料高温gap已作最小覆盖修正。
