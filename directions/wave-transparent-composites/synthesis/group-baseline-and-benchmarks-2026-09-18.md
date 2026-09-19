---
direction_id: wave-transparent-composites
type: synthesis
title: 组内透波材料基础与公开性能参照
status: draft
review_status: draft
created: 2026-09-18
updated: 2026-09-19
tags: [synthesis]
---

# 组内透波材料基础与公开性能参照

## 范围与判断口径

用户问题：组内研究哪些材料、关注哪些指标、达到什么数值，与国际领先水平有多大差距。组内依据限原指定清单中7篇直接涉及透波材料的论文（2024–2026），不是课题组全部成果。2026-09-19按用户范围要求排除纯吸波和CMAS腐蚀论文；后者已移出当前文献页。本轮回查复合材料热学、介电、压痕原图与锡酸盐膨胀图；所有paper仍为draft，逐条限定证据使用。

2026-09-18检索公开国际期刊原始研究，以SiO2f/SiO2、Si3N4纤维/BN、热导率、介电与强度为关键词，另核对组内参考文献中的代表工作。纳入下列可核原始来源，未进行穷尽检索，未取得所有全文/原始数据，不宣称世界纪录或全球排名。“国际”包括在国际期刊公开的中国及其他国家团队，不能与“国外”混用。

核心评价（AI综合）：现有资料体现两条相互支撑的路线——纤维织构/界面和孔结构调控，以及新型氧化物组成/熵设计；关注的是透波—隔热—承载—热稳定的协调。高通量、DFT及传统机器学习是已展示的方法；现有7篇透波相关原始研究不构成已应用大模型的证据。

## 组内指标矩阵

κ单位W·m⁻¹·K⁻¹，CTE单位K⁻¹，εr无量纲。每行是对应论文的独立原始数据组，表内多指标不代表同一试样同时处于同一工况；±按原报告，不补造统计意义。

| 材料/变量 | 介电结果及条件 | 热学结果及条件 | 力学结果/操作定义 | 证据及核查 |
|---|---|---|---|---|
| 层合穿刺SiO2f/SiO2；Z向纤维、溶胶凝胶 | 室温12–18 GHz εr≈3、tanδ<0.004 | κ约0.3–0.6（作者概括，273–1273 K）；CTE约6.66×10⁻⁷（373–1073 K） | 抗弯93±18.1 MPa、压缩146±9.6 MPa；不是模量 | [[directions/wave-transparent-composites/wiki/papers/Wen-2026-Laminated-SiO2f-SiO2#E1]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2026-Laminated-SiO2f-SiO2#E4]]；本轮新增Fig.11核查；draft |
| (Si3N4–SiO2)f/BN；混编、PIP、差异界面 | 室温12–18 GHz εr<3.8；tanδ约0.005，Fig.7代表值0.0058 | κ室温0.822、1073 K为1.752；CTE约(2–4.5)×10⁻⁶，图示约500–1273 K | 抗弯87.17±13.79 MPa，KIC=3.52±0.12 MPa·m½；组元压痕模量147.08/63.16/21.60 GPa分别对应氮化硅纤维/石英纤维/BN，不是整体模量 | [[directions/wave-transparent-composites/wiki/papers/Chen-2026-Hybrid-Fibers-BN#E1]]、[[directions/wave-transparent-composites/wiki/papers/Chen-2026-Hybrid-Fibers-BN#E3]]、[[directions/wave-transparent-composites/wiki/papers/Chen-2026-Hybrid-Fibers-BN#E5]]、[[directions/wave-transparent-composites/wiki/papers/Chen-2026-Hybrid-Fibers-BN#E6]]；本轮Fig.4/6核查；draft |
| 双溶剂模板多孔Si3N4；1:2配比、孔结构 | 室温12.4–18 GHz εr≈3.3；高温另法25–1100 °C εr约5.0–5.5、tanδ<0.006 | 室温κ≈4.2 | 抗弯95±14.8 MPa、压缩132±4.5 MPa（摘要口径）；正文最大值不同，保持争议 | [[directions/wave-transparent-composites/wiki/papers/Liu-2024-Porous-Si3N4#E1]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Porous-Si3N4#E2]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Porous-Si3N4#E4]]；已核关键原图，draft |
| RE2SiO5；Ho/Er/Tm/Yb/Lu | 室温9.7/14.5 GHz εr约5.3–6.6，Yb tanδ约0.0017 | 本文不能用引言转引κ冒充新测量 | 压痕约化模量均值约131.55–160.33 GPa；并非复合材料宏观模量 | [[directions/wave-transparent-composites/wiki/papers/Du-2024-RE2SiO5#E1]]、[[directions/wave-transparent-composites/wiki/papers/Du-2024-RE2SiO5#E2]]；高温损耗图文冲突，draft |
| RE2Sn2O7；九种稀土 | 室温9.6/14.4 GHz εr约7–9，Er tanδ约0.001 | 1000 °C Eu κ≈1.85、Nd≈4.28；CTE La/Er 8.62/9.24×10⁻⁶，曲线约373–1273 K | 实验压痕推得模量均值约214.1–245.3 GPa；不是宏观抗弯模量，实测不严格随半径单调 | [[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7#E2]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7#E3]]；CTE本轮原PDF Fig.14核查，draft |
| (Ti1/3Zr1/3Hf1/3)P2O7；固溶、MgO助剂 | 室温εr约7.2–7.5；100–1100 °C εr约7.59–8.47、tanδ约0.0085–0.012 | κ约0.82–1.28（约25–1000 °C）；CTE≈8×10⁻⁶ | 抗弯115±8.2 MPa；DSC扫描内无ZrP2O7对应相变峰 | [[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7#E1]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7#E2]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7#E3]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7#E4]]；不能写全温区tanδ<0.01，draft |
| 高熵RE2Si2O7；Sc引入、高通量+ML | Ho/Tm/Yb/Lu/Sc等摩尔配方εr≈5.4；另一个Ho/Er/Yb/Lu/Sc配方≈5.0，15 GHz；不是同一配方两个值 | 前一配方κ≈1.3（1273 K）；κ由α、计算Cp、密度求得 | 本文侧重硬度与结构，不能补造整体抗弯或模量纪录 | [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E2]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E3]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E4]]；SI及模型独立复现未核，draft |

主题范围更新：纯吸波论文和CMAS腐蚀论文不纳入本综合的透波材料证据集；历史记录与筛查依据见[[directions/wave-transparent-composites/docs/scope-audit-2026-09-19/report]]。

## 国际公开原始研究参照

以下只使用原论文或出版商原始摘要，不将综述表中的重复转引当独立实验。摘要可支持报告值，不能证明完整测试条件相同；外部来源未创建checked论文页。

| 原始来源/年份 | 可核结果 | 与组内比较资格与含义 |
|---|---|---|
| [三维七向编织石英复合材料，2012](https://www.sciencedirect.com/science/article/pii/S0272884211009230) | 三点抗弯约107 MPa、弯曲模量17.5 GPa；出版商摘要已读 | qualitative-only：组内93±18.1 MPa与107 MPa同为百MPa量级，但织构、循环数不同，107亦落在组内报告均值±范围附近，不能判显著差距；该老文不是2026全球纪录 |
| [PIP Si3N4f/BN/Si3N4，2021](https://www.sciencedirect.com/science/article/pii/S0955221920307688) | 抗弯189±17 MPa、KIC 5.6±0.6 MPa·m½；出版社索引摘要可核，完整全文未得 | qualitative-only：提供更高承载/韧性的另一体系参照。与组内87.17±13.79、3.52±0.12分别列示；不同纤维/基体与密度，不能计算统一落后率或断言热/介电全面优越 |
| [PESO前驱体石英复合材料，2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/) | 抗弯63.3 MPa；κ=0.446/0.317/0.350，对应表5的200/400/600 °C；εr约2.4–2.6、tanδ<0.01 | qualitative-only：组内κ约0.3–0.6处于相同数量级，不能称独占最低。该文表5“处理温度”和正文测试温度措辞有歧义；方法写8.2–12.4 GHz、结果写2–18 GHz，不据此作精确百分比比较 |
| [SiON/BNNT薄片，2022，美国NC State](https://www.nature.com/articles/s41598-022-18563-4) | 26.5–40 GHz平均εr=1.52–1.55，tanδ=0.0074–0.0266；约0.3 mm薄片透射最高约97%；作者明确成本与薄片脆弱限制 | not-directly-comparable：展示低ε方向空间，但频段、厚度和结构用途不同；低ε并不同时给出较低tanδ或93 MPa承载，不据此算组内“介电差一倍” |
| [Si3N4气凝胶，2026](https://ceramics.onlinelibrary.wiley.com/doi/10.1111/jace.71019) | 出版商索引摘要报告25 °C κ=0.0344、密度1.02 g/cm³、压缩48 MPa，2–18 GHz εr=2.19–2.36；全文未读 | not-directly-comparable：近期多孔形态参照；不把压缩当抗弯，不以摘要代替热学/孔隙全核查，不能据此评价组内整体落后程度 |

## 能回答的差距与不能回答的差距

1. **材料与指标重点**：supported within corpus。复合材料路线已做纤维织构、混编和界面表征；陶瓷路线已做孔结构、稀土组成、固溶和熵调控。主要目标是低κ、较低εr/tanδ、受控CTE与足够的强度/韧性，不是单独追求高模量。证据为上述7个独立组内数据组。
2. **性能位置**：partially-supported / qualitative-only。层合石英体系的力学和隔热数值与公开同类处于相近量级；混编BN体系已展示性能协调，但另一些氮化硅基纤维体系给出更高强度/韧性。不能把两条路线写成一个总分或“离国际领先差X%”。
3. **模量口径**：supported。组内131–160、214–245 GPa主要来自陶瓷局部压痕，混编页147/63/22 GPa来自组元；国际石英107 MPa文中的17.5 GPa为复合材料整体弯曲模量。指标层级不同，not-directly-comparable，不构成组内高一个数量级的优势。
4. **验证完整度**：insufficient-evidence for world-leading service performance。这7篇透波相关论文中的两种纤维复合材料主要证明室温介电与分别测得的热/力学性质，尚缺同一服役工况下高温透射/插入损耗、受载后性能、长期循环与残余强度的完整链条；这是当前语料的验证缺项，不推定课题组从未开展，也不直接称领域空白。
5. **低指标不是万能目标**：AI评价。低κ有利于隔热，不代表散热应用更好；低CTE需兼顾连接匹配；低εr需同时看tanδ、厚度和透射率；高模量需与强度/韧性及热应力一起评价。后续课题应选定应用和比较条件再设门槛。

## 本轮结论与后续

可以用一段话概括为“已有组成设计—结构/界面—介电热力学表征的组内基础，面向综合性能优化”；不能据7篇透波相关论文与有限公开参照宣布综合世界领先或量化全局落后百分比。进一步严谨差距评估需固定材料体系、试样密度/织构、温度/频率、加载方向和测量定义，再读取领先候选全文及SI。目前不生成确定gap或指定实验配方。

该综合是calude_wiki_3.0上传后的新工作，未移动版本标签、未自动上传本轮新增分析；本轮修正了混编论文强度误差末位并新增E5/E6，其他方向未改。
