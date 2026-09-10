# Scopus标题与摘要筛选：背景补缺

2026-09-09；来源为本机 Zotero Integrated MCP 实时读取，四个指定collection均按offset分页读至空页。未网络检索，未读取Zotero数据库，未修改Zotero条目或附件。

## 覆盖与口径

| Collection | key | 条目数 | Zotero摘要数 |
|---|---|---:|---:|
| scopus_1 | B822V64I | 92 | 92 |
| scopus_2 | 8DJAALBC | 124 | 124 |
| scopus_3 | J9DF9F59 | 6 | 6 |
| 毕设 > 组内文章 > 博士 > 田老师 > 陶瓷+腐蚀 | QUNDVKXV | 3 | 1 |

共225次collection成员记录，对应186个不同item key；按DOI/规范化题名分组后仍为186篇。39次为跨collection重复出现，不是需要删除的重复Zotero条目。与当前十篇wiki论文的DOI/item key核对未发现已入库对应页；不代表整个Zotero文库不存在其他版本。

2篇缺失摘要已从已有本地PDF第1页补读：S052/WIYBSDHY、S144/WAYPSM88。此前指定的三篇为S052、S144、S031，均返回PDF附件；其余183篇此次未返回附件，不能据此判断其他位置也没有全文。未读取这些PDF的结果/图表章节。

本轮是分层初筛：全部186篇检查题名和摘要或摘要节选；A与B1全部阅读完整摘要，B2/C部分依题名与摘要节选作初筛，逐条在screening.csv和manifest中保留实际覆盖。未完成全库逐篇完整摘要复核或任何新增论文全文复核。没有把摘要机制说法写成已验证结论。

S编号只绑定本清单2026-09-09版本，不替代原“田老师#17/#23/#59”编号；各collection的局部编号另存于import_plan/manifest。

## 筛选标准与数量

优先能补齐应用/真实沉积物、独立物性、明确对照、实际涂层损伤及原位时序的文献；不按引用量或新近年份简单排序。排除仅限当前CMAS涂层背景任务，不改变用户较宽的陶瓷腐蚀领域。

- A 优先全文核查：12篇。
- B1 第二批候选：14篇。
- B2 专题储备：87篇。
- C 本轮暂不纳入：73篇。

## 第一批：12篇优先全文核查

建议顺序：S073 → S137 → S021 → S180 → S022 → S144 → S052 → S031 → S145 → S101 → S106 → S086。每次再按2–3篇入库推进，本轮没有入库授权扩展。S073为综述，S137为方法研究，S086为会议论文；来源类型不混计。

| 编号 | 年份/日期 | 题名 | 作用与核查重点 | DOI | Zotero item key |
|---|---|---|---|---|---|
| S073 | 2022 | Failure mechanism and protection strategy of thermal barrier coatings under CMAS attack | 摘要涵盖CMAS组成、流变、热化学与热机械失效，适合作为背景入口；综述中的原始事实仍须追溯来源。 | 10.7527/S1000-6893.2022.27613 | V9H4UGN4 |
| S137 | 2022 | Protocol for selecting exemplary silicate deposit compositions for evaluating thermal and environmental barrier coatings | 从真实沉积物数据经降维与聚类选择代表配方，直接服务实验CMAS代表性与可比性；方法论文不是已采纳的行业标准。 | 10.1111/jace.18413 | THL3XCM8 |
| S021 | 2012 | Calcium-magnesium-alumino-silicate (CMAS) degradation of EB-PVD thermal barrier coatings: characterization of CMAS damage on ex-service high pressure blade TBCs | 摘要明确分析退役高压叶片EB-PVD涂层，补充实验室块体以外的实际损伤；服役热历史和因果对照仍需核查。 | 10.1016/j.surfcoat.2012.07.074 | KMKUZS4S |
| S180 | 2022 | Viscosity of CaO-MgO-Al2O3-SiO2 (CMAS) melts: experimental measurements and comparison to model calculations | 摘要明确报告不同Ca/Si及添加氧化物的实测黏度，并比较模型，补足独立物性证据；核查配方与温区。 | 10.1016/j.jnoncrysol.2022.121508 | LZ7H6HGY |
| S022 | 2024 | Calcium–magnesium–aluminum-silicate melt viscosities influenced by lanthanides, yttrium, and zirconium | 摘要报告镧系/Y/Zr添加及浓度相关黏度变化，直接关联现有RE效应解释；不能据此推出普适抗蚀半径律。 | 10.1111/jace.19646 | XT4FIUCE |
| S144 | 03/2024 | Resistance of ytterbium silicate environmental barrier coatings against molten calcium-magnesium-aluminosilicate (CMAS): A comprehensive study | PDF摘要比较APS Yb单/二硅酸盐与富Ca/贫Ca CMAS，补充当前块体语料；溶解度、相稳定及因果解释待全文核查。 | 10.1016/j.surfcoat.2024.130540 | 5JLHDZDM |
| S052 | 02/2022 | Effect of CMAS viscosity on the infiltration depth in thermal barrier coatings of different microstructures | PDF摘要比较三种CMAS与SPPS涂层微结构；黏度为FactSage预测，须与实测黏度区分，摘要的solely因果表述须回查。 | 10.1016/j.surfcoat.2021.128039 | 4VTYJ45V |
| S031 | 03/2024 | CMAS infiltration behavior of atmospheric plasma-sprayed thermal barrier coating with tailored pore structures | 摘要含APS孔结构调控、侵入及热物性/热震评价，补充结构因素；核对热震试验是否实际与CMAS耦合。 | 10.1016/j.ceramint.2023.09.172 | NE9UVQA9 |
| S145 | 2021 | Rheological and chemical interaction between volcanic ash and thermal barrier coatings | 摘要比较五种灰熔体及两种材料/两种涂层工艺，连接黏度、润湿和侵入；各因素并非自动独立控制。 | 10.1016/j.surfcoat.2021.127049 | H2KT556T |
| S101 | 2017 | Lifetime and failure modes of plasma sprayed thermal barrier coatings in thermal gradient rig tests with simultaneous CMAS injection | 摘要明确热梯度、循环载荷与连续CMAS注入，改变停留时间及沉积速率并评价剥落寿命；优先核对试验边界。 | 10.1016/j.surfcoat.2017.04.071 | Z2SRQLJB |
| S106 | 2017 | Mechanistic study on the degradation of thermal barrier coatings induced by volcanic ash deposition | 摘要包括有/无火山灰对照、随温度变化的梁挠度测量及损伤模型；分清测量、反演与有限元输出。 | 10.1007/s11666-017-0576-z | Y474XY3E |
| S086 | 2024 | In-situ synchrotron X-ray diffraction volcanic ash infiltration studies on high temperature ceramic coatings | 摘要明确原位同步辐射XRD及应变/相演化，适合核查熔融与凝固过程；为会议论文，不先宣称已证冷却致裂。 | 10.2514/6.2024-2047 | RTEJB3QN |

## 第二批：14篇按缺口接续

| 编号 | 年份/日期 | 题名 | 作用与核查重点 | DOI | Zotero item key |
|---|---|---|---|---|---|
| S010 | 2017 | An experimental simulation of volcanic ash deposition in gas turbines and implications for jet engine safety | 多种火山灰在合金叶片靶上沉积，补充组成/晶体比例/粒径影响；与涂层腐蚀分开。 | 10.1016/j.chemgeo.2016.11.024 | 94FX7Y3P |
| S026 | 2020 | Characterization of thermochemical and thermomechanical properties of eyjafjallajokull volcanic ash glass | 摘要含天然灰结晶、热膨胀、模量和实测黏度，作为模型CMAS的参照。 | 10.3390/coatings10020100 | MZE6ZGMW |
| S042 | 2025 | Damage quantification and failure mechanism of EB-PVD thermal barrier coatings under CMAS corrosion | 室温压缩+DIC与屈曲模型评估界面损伤，适合补评价指标；不等于原位服役裂纹追踪。 | 10.1016/j.surfcoat.2024.131554 | UTE2QIHK |
| S045 | 2026 | Densification and embrittlement mechanisms of EB-PVD columnar YSZ coatings under volcanic ash corrosion via in-situ micropillar compression | 腐蚀后原位SEM微柱压缩、TEM与模型；适合检查强度提高和应变容限下降是否可并存。 | 10.1016/j.corsci.2026.114102 | UWZNHAYD |
| S061 | 11/2025 | Effects of seasalt and sulfate additions on the melting and crystallization behavior of CMAS glass | 海盐/硫酸盐加入CMAS后的熔化结晶实验及CALPHAD，扩展四元模型适用边界。 | 10.1111/ijac.70043 | GAC7DQPH |
| S080 | 07/2024 | High-temperature corrosion of sintered RE2Si2O7 (RE = Yb and Ho) environmental barrier coating materials by volcanic ash | Yb与Ho二硅酸盐1400°C天然灰对照，可对照当前#23；保留各自指标，勿直接拼排名。 | 10.1007/s12613-024-2899-3 | Y2KD6QZH |
| S093 | 2018 | Integrated testing approach using a customized micro turbine for a volcanic ash and CMAS related degradation study of thermal barrier coatings | 微型燃机同时腐蚀/冲蚀评价7YSZ与GZO，可能改变仅据静态侵入选材的判断。 | 10.1016/j.surfcoat.2018.01.030 | WABHYJH6 |
| S113 | 2023 | Microstructure refinement of EB-PVD gadolinium zirconate thermal barrier coatings to improve their CMAS resistance | EB-PVD GZO不同微结构与多熔体暴露，可与APS案例互补；成分和制样效应分开。 | 10.3390/coatings13050905 | MFJEAK5F |
| S118 | 2025 | Modeling the viscosity and infiltration kinetics of silicate melt -thermal barrier coating systems based on deep-learning and experimental approach | ML黏度预测并有侵入/温度梯度实验；核查合成数据、训练测试独立性及物理验证。 | 10.1016/j.actamat.2025.121081 | XU7QXRNP |
| S131 | 2026 | Phase-informed design strategy of volcanic ash analogues for jet engine degradation | 天然灰与五种递增复杂配方对照，核查96%相似性定义及循环证据；论文方法不等于领域标准。 | 10.1016/j.corsci.2025.113484 | J4PEAY5I |
| S141 | 2026 | Recession behavior of plasma-sprayed ytterbium monosilicate environmental barrier coating against silicate deposits | APS Yb单硅酸盐在天然灰/合成CMAS下反应，适合检验反应层能否持续保护；热力学平衡解释待核。 | 10.1016/j.surfcoat.2026.133275 | MKJBTUZG |
| S143 | 2023 | Research progress of CMAS corrosion and protection method for thermal barrier coatings in aero-engines | 摘要覆盖CMAS物性、失效与保护；与S073功能重叠，可先择一，后按引文互补。 | 10.11933/j.issn.1007-9289.20221120001 | VU7XHVZD |
| S160 | 2022 | Surface roughness affects metastable non-wetting behavior of silicate melts on thermal barrier coatings | 抛光改变APS YSZ粗糙度并比较三类灰熔体，补润湿/侵入区分；短期润湿不直接证明寿命。 | 10.1007/s12598-021-01773-6 | 53HZI54F |
| S185 | 09/2022 | Water vapor and CMAS corrosion tests of Y2SiO5/Si thermal and environmental barrier coating | Y2SiO5/Si涂层分别进行水蒸气和CMAS试验，补实际EBC背景；摘要未证明两环境同时耦合。 | 10.1016/j.heliyon.2022.e10262 | HHJ5IJBX |

## 对当前背景与研究问题的影响（待全文验证）

- “代表性CMAS如何选”已有S137及S131候选，不能直接提出领域缺乏选择方法。
- “稀土溶入后黏度如何变化”有S022、S180候选；S052的黏度则为模型预测，三者的证据身份不同。
- “块体侵入能否代表涂层寿命”可由S021、S031、S101、S106核查；已有动态涂层验证不等于当前层叠材料排序已经校准。
- “晶界/孔隙填充与力学损伤的关系”由S042、S045等补充；局部强度与宏观耐久性分别评价。
- “冷却析出/裂纹时序”可追踪S086等原位工作；不能只据题名认定其完整回答当前材料机制。
- 当前优先清单仍偏TBC；EBC水蒸气防护、完整多层EBC/CMC应用背景的系统覆盖不足。S185可补一个实验实例，S144补CMAS涂层对照，二者都不能单独替代完整EBC背景综述。热化学原始来源及层叠/独立样品配对校准仍待定向追溯。

## 检索与元数据注意事项

scopus_2包含较多锅炉、煤灰、冶金与水泥文献。本轮不知道用户实际执行的检索式、过滤及导出范围，不能据这些条目推断某个搜索规则失败；建议后续保留实际检索式和检索历史。仅有6条的scopus_3不被视为该领域只有6篇。

S020题名重复；S029/S165摘要高度相似但DOI不同，保留版本/研究重叠待核查，不自动合并或算两次独立验证。年份沿用Zotero日期，网络先行与卷期年份可能不同；未进行全体出版社书目核验。

## 全量清单

CSV见 [screening.csv](screening.csv)，包括全部186篇、原collection、item key、附件key、理由与实际阅读范围。以下按层级列出，暂不纳入不等于永久删除或质量较低。

### B2 专题储备

| 编号 | 年份/日期 | 题名 | 作用与核查重点 | DOI | Zotero item key |
|---|---|---|---|---|---|
| S001 | 12/2014 | 2ZrO2 ·Y2 O3 Thermal Barrier Coatings Resistant to Degradation by Molten CMAS : Part I, Optical Basicity Considerations and Processing | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1111/jace.13210 | WPTGSGFH |
| S002 | 2014 | 2ZrO2·Y2O3 thermal barrier coatings resistant to degradation by molten CMAS: part II, interactions with sand and fly ash | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1111/jace.13209 | KLZDK3BH |
| S004 | 2024 | Advances in the research of surface modification on the resistance of thermal barrier coatings to CMAS corrosion | 背景或策略概述与核心综述部分重叠，保留作补充，避免先大量入库同功能综述。 | 10.16490/j.cnki.issn.1001-3660.2024.16.003 | X4LLTF56 |
| S006 | 2022 | Al2O3-modified 7YSZ thermal barrier coatings for protection against volcanic ash corrosion | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1038/s41529-022-00308-3 | 2HB85468 |
| S009 | 2026 | An aluminum surface modification strategy for enhancing CMAS corrosion resistance of environmental barrier coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.26599/JAC.2025.9221222 | 68SMK7Y5 |
| S018 | 2025 | Basicity of volcanic ash determining the degradation of thermal barrier coatings at elevated temperatures | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.jmst.2024.12.083 | 4QV2CWEN |
| S020 | 2015 | Blade surface blade surface blade surface blade surface-particle interaction and multifunctional coatings for gas turbine engines | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 题名含重复Blade surface，保留原题名，书目需核对。 | — | R5BQNGXG |
| S023 | 2023 | Ceramic coatings in turbine applications | 背景或策略概述与核心综述部分重叠，保留作补充，避免先大量入库同功能综述。 | 10.1016/B978-0-323-99624-2.00001-2 | 5Y5SX6RG |
| S025 | 2020 | Characterization and hot corrosion behavior of the La2(Zr0.7Ce0.3)2O7/8YSZ:Eu double ceramic layer coating prepared by atmospheric plasma spraying | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfin.2020.100777 | KMWVLG98 |
| S029 | 2015 | CMAS degradation of EB-PVD TBCs: the effect of basicity | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 与S165摘要高度相似，DOI不同；保留两个条目，可能存在研究重叠，全文核查前不重复计为独立验证。 | 10.1016/j.surfcoat.2015.03.009 | 4LIHSMBV |
| S030 | 2023 | CMAS infiltration and mitigation strategies for minimizing premature degradation failure of high temperature ceramic coatings in turbine engines | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 会议摘要明确整合前期工作与初步CFD，不能全部计作新独立实验。 | 10.2514/6.2023-0179 | ETQVGXTG |
| S032 | 2014 | CMAS-resistant plasma sprayed thermal barrier coatings based on Y 2O3-stabilized ZrO2 with Al3+ and Ti4+ solute additions | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s11666-014-0077-2 | H8C2MPCY |
| S035 | 2026 | Comparative study on the CMAS and volcanic ash corrosion resistance of (Sm0.7Yb0.3)2Zr2O7 ceramics | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2025.12.379 | N8PIIR98 |
| S036 | 2025 | Corrosion behavior of (Yb0.9Y0.1)2SiO5environmental barrier coating material against CMAS and volcanic ash: experimental and first-principles calculation | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2025.08.055 | RZQN43UZ |
| S037 | 2011 | Corrosion of thermal barrier coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | — | EMFKSLIY |
| S038 | 2026 | Corrosion of YSZ by different types of CMAS | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2025.11.441 | VCAZHYKD |
| S039 | 2024 | Corrosion resistance of multicomponent disilicate (Ho0.2Er0.2Tm0.2Yb0.2Lu0.2)2Si2O7 against CMAS and volcanic ash | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.corsci.2024.112484 | 293TZ36N |
| S040 | 2012 | Crystallization of coal ash slags at high temperatures and effects on the viscosity | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 煤灰结晶-黏度可作方法参考，暂不外推为TBC/EBC证据。 | 10.1021/ef201894p | W8RCP364 |
| S041 | 2015 | Damage progression of thermal barrier coatings by CMAS | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.2472/jsms.64.134 | IPL7U8WM |
| S043 | 2019 | Degradation mechanisms of air plasma sprayed free-standing yttria-stabilized zirconia thermal barrier coatings exposed to volcanic ash | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.apsusc.2019.03.084 | X6AND7WH |
| S044 | 2013 | Degradation of La2Zr2O7 and other novel EB-PVD thermal barrier coatings by CMAS (CaO-MgO-Al2O3-SiO2) and volcanic ash deposits | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2013.07.029 | GXRN8299 |
| S046 | 2026 | Droplet size effects on the interfacial behavior between CMAS and GYbZ thermal barrier coating material surface | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.apsusc.2026.166000 | IPBYVK4C |
| S047 | 2025 | Dual-phase barrier formation and inhibition of environmental deposit-induced grain boundary corrosion in rare earth zirconia-based TBCs | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2025.132614 | DZXEDTUS |
| S048 | 2026 | Dynamic redissolution-reprecipitation of a “coral-like” reaction layer enables self-healing corrosion resistance in Yb-Gd-Y co-stabilized zirconia against molten volcanic ash | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.corsci.2026.114098 | PP459KXK |
| S049 | 2018 | EB-PVD alumina (Al2O3) as a top coat on 7YSZ TBCs against CMAS/VA infiltration: deposition and reaction mechanisms | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.jeurceramsoc.2018.03.027 | 8UJ2YKVC |
| S054 | 2025 | Effect of configuration entropy on resistance of rare-earth zirconate ceramics to CaO-MgO-Al2O3-SiO2 | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.14062/j.issn.0454-5648.20240647 | 8EKFEKR3 |
| S055 | 2016 | Effect of semi-molten particulate on tailored thermal barrier coatings for gas turbine engine | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.2514/6.2016-4852 | S9NJYQGR |
| S062 | 2020 | Effects of yttria content on the CMAS infiltration resistance of yttria stabilized thermal barrier coatings system | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.jmst.2019.09.039 | YUWL2DCS |
| S063 | 2018 | Evaluating the sand resistance of tailored thermal barrier coatings for gas turbine engines | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.2514/6.2018-4829 | NLLDU3CE |
| S064 | 2024 | Evaluation of molten sand, dust, and ash infiltrating thermal barrier coatings: numerical and analytical approaches | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1063/5.0234882 | KPPJW9AL |
| S065 | 2017 | Evolution of hardness and young's modulus with phase transformation of EB-PVD thermal barrier coatings corroded by volcanic ash | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | — | B4S9R8QC |
| S066 | 2022 | Evolution of the microstructure and mechanisms of performance degradation in EB-PVD YSZ thermal barrier coatings corroded by volcanic ash at 1150 °C | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.corsci.2022.110626 | PYN9N5B4 |
| S067 | 2017 | Evolution of the thermal conductivity of Sm2Zr2O7 under CMAS attack | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/978-3-319-52333-0_21 | QMRV4G5N |
| S071 | 2024 | Exploring the comprehensive performance of lotus-leaf-inspired biomimetic NdYbZr2O7 thermal barrier coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2024.10.181 | WQ5X59JC |
| S072 | 2019 | Factors influencing the penetration depth of molten volcanic ash in thermal barrier coatings: theoretical calculation and experimental testing | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.rinp.2019.102169 | 39LHJRUQ |
| S074 | 2015 | Function of reaction layer in pyrochlore thermal barrier coatings against CMAS corrosion | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1149/06618.0053ecst | 9MQSB7UI |
| S076 | 2020 | Fusion and TBC penetration characteristics of volcanic ash collected from active volcano | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1007/s11666-020-01015-8 | WZDBZVBY |
| S077 | 2026 | High temperature composition-controlled spreading dynamics of volcanic melts | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.chemgeo.2026.123436 | JC99PYQW |
| S078 | 2024 | High temperature infiltration behavior and reaction characteristics of colima volcanic ashes on gadolinium zirconate coatings deposited by atmospheric plasma spraying | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s42247-024-00677-2 | LN7MUQ2N |
| S079 | 2023 | High temperature interactions between coal ash and MgO-based refractories in lime kiln conditions | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 MgO耐火材料腐蚀属于较宽陶瓷腐蚀范围；本轮CMAS涂层背景优先级较低。 | 10.1016/j.fuel.2023.127711 | IVME957G |
| S081 | 2013 | Hot corrosion behavior of plasma sprayed 4 mol% Y2O 3-ZrO2 thermal barrier coatings with volcanic ash | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.4191/kcers.2013.50.6.353 | EY8LD6U5 |
| S082 | 08/2017 | Hot corrosion of RE 2 SiO 5 with different cation substitution under calcium–magnesium–aluminosilicate attack | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2017.04.045 | 4SG3G9KM |
| S084 | 2019 | Impact interaction of in-flight high-energy molten volcanic ash droplets with jet engines | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.actamat.2019.04.011 | TZTKDQLF |
| S088 | 2020 | Influence of molten volcanic ash infiltration on the friability of APS thermal barrier coatings | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.ceramint.2020.01.166 | 3UZM3X7C |
| S094 | 2017 | Interaction and infiltration behavior of eyjafjallajökull, sakurajima volcanic ashes and a synthetic CMAS containing FeO with/in EB-PVD ZrO2-65 wt% Y2 O3 coating at high temperature | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.actamat.2017.06.055 | BQY44J7M |
| S096 | 2023 | Interactions between rare-earth zirconates (RE2Zr2O7) and CMAS silicate melts | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.corsci.2023.111526 | MLFF3E4L |
| S097 | 2020 | Investigation of CMAS resistance of sacrificial suspension sprayed alumina topcoats on EB-PVD 7YSZ layers | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s11666-019-00951-4 | WR6SIB8J |
| S098 | 2022 | Investigation of vermiculite infiltration effect on microstructural properties of thermal barrier coatings (TBCs) produced by electron beam physical vapor deposition method (EB-PVD) | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.surfcoat.2022.128645 | 3F2PXAP6 |
| S102 | 2024 | Lotus leaf inspired hierarchical micro-nano structure on NdYbZr2O7 ceramic pellet with enhanced volcanic ash repellence | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2024.05.057 | MYFCVUV3 |
| S103 | 12/2014 | Mechanisms and mitigation of volcanic ash attack on yttria stablized zirconia thermal barrier coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2014.09.015 | 36ZIPAMJ |
| S104 | 2024 | Mechanisms of La2Ce2O7/YSZ double-ceramic-layer thermal barrier coatings against volcanic ash corrosion | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.3390/coatings14070877 | H9Y7JDKA |
| S107 | 2022 | Medium-entropy (me,Ti)0.1(Zr,Hf,Ce)0.9O2 (me = Y and Ta): promising thermal barrier materials for high-temperature thermal radiation shielding and CMAS blocking | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.jmst.2022.01.019 | 45H8KRHD |
| S110 | 2014 | Microstructural characterization of the interaction between 8YPSZ (EB-PVD) thermal barrier coatings and a synthetic CAS | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.surfcoat.2013.11.014 | A4AKW65N |
| S111 | 2016 | Microstructure characteristics of EB-PVD YSZ thermal barrier coatings corroded by molten volcanic ash | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.surfcoat.2015.12.003 | GFDNU358 |
| S116 | 2011 | Mitigation of damage from molten fly ash to air-plasma-sprayed thermal barrier coatings | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.msea.2011.06.041 | 3B2RYI5U |
| S119 | 2017 | Modes of deposit-induced accelerated attack of MCrAlY systems at 1100 °C | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 金属粘结层沉积腐蚀，可作界面背景，不能代替陶瓷顶层证据。 | 10.1007/s11085-016-9669-1 | CXZMZBFF |
| S120 | 2018 | Molten particulate impact on tailored thermal barrier coatings for gas turbine engine | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1115/1.4037599 | MTELWNGT |
| S121 | 2018 | Molten salt attack on multilayer and functionally-graded YSZ coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2018.04.062 | 5N2FEVRM |
| S122 | 2026 | Molten-silicate-induced degradation of ultra-high temperature ceramics | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 超高温陶瓷熔融硅酸盐腐蚀是拓展候选，不因本轮偏CMAS涂层而从整个陶瓷腐蚀范围排除。 | 10.1016/j.jeurceramsoc.2026.118324 | 9IWH2EPU |
| S123 | 2023 | Molten-volcanic-ash-phobic thermal barrier coating based on biomimetic structure | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1002/advs.202205156 | U3G2X4VM |
| S124 | 2023 | Nanostructured Gd2Zr2O7: a promising thermal barrier coating with high resistance to CaO–MgO–Al2O3–SiO2 corrosion | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s41779-022-00822-2 | D93X4ERL |
| S125 | 2022 | NdYbZr2O7 thermal barrier coating resistant to degradation by volcanic ash and CMAS | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.corsci.2022.110795 | ILJ3L6A7 |
| S126 | 2020 | Novel thermal barrier coatings with hexagonal boron nitride additives resistant to molten volcanic ash wetting | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.corsci.2020.108587 | DHQT728K |
| S127 | 2020 | Numerical simulation of volcanic ash infiltration into thermal barrier coatings | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.4028/www.scientific.net/KEM.827.367 | DC45PPFU |
| S128 | 2016 | On the resistance of rare earth oxide-doped YSZ to high temperature volcanic ash attack | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2016.09.033 | WZVAANAM |
| S129 | 2026 | Partially molten environmental dust spreading on an EB-PVD TBC-analog surface: experimental results enhanced by physics informed machine learning | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.surfin.2026.108934 | HRQB4LAK |
| S132 | 1991 | Physicochemical effects influencing the measurements of interfacial surface tension of coal ashes | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 煤灰界面张力测量可作方法储备，须核温度/气氛与目标体系适用性。 | 10.1016/0016-2361(91)90050-K | CGGQFHXK |
| S133 | 2012 | Plasma sprayed gadolinium zirconate thermal barrier coatings that are resistant to damage by molten Ca-Mg-Al-silicate glass | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.surfcoat.2012.03.051 | 829FBCDH |
| S134 | 2023 | Plasma sprayed Yb4Hf3O12 thermal barrier coatings with excellent thermophysical properties and robust CMAS corrosion resistance | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.ceramint.2023.06.021 | 62UFUICB |
| S139 | 2022 | Reaction products from high temperature treatments of (LaxGd1-x)2Zr2O7 system and volcanic ash powder mixtures | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s11837-022-05302-3 | KPPFFL4K |
| S140 | 2021 | Reaction products of Sm2Zr2O7 with calcium-magnesium-aluminum-silicate (CMAS) and their evolution | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1007/s40145-021-0514-x | PXMJEXXM |
| S146 | 2001 | Rheological properties of high-temperature melts of coal ashes and other silicates | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 煤灰与高温硅酸盐流变综述作方法储备，不充当涂层损伤直接研究。 | 10.1016/S0360-1285(00)00023-X | LM5W9L5R |
| S147 | 1984 | Rheological properties of molten kilauea iki basalt containing suspended crystals | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 悬晶玄武岩流变可作部分熔融体系参照，尚非涂层腐蚀证据。 | — | 5CSSXXGQ |
| S148 | 2017 | Sand particle-induced deterioration of thermal barrier coatings on gas turbine blades | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.12989/aas.2017.4.1.037 | Z9YN223G |
| S149 | 2026 | Sea salt enhances the CMAS corrosion of thermal barrier coating | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.jeurceramsoc.2025.118030 | BLGXIZBD |
| S150 | 2022 | Silicate ash-resistant novel thermal barrier coatings in gas turbines | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.corsci.2021.109929 | R8QSNY2S |
| S152 | 2026 | Size-resolved CMAS deposition characteristics on film-cooled turbine vanes | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.powtec.2026.122525 | W67RVJBY |
| S163 | 2020 | The accumulation of molten volcanic ash in jet engines; simulating the role of magma composition, ash particle size and thermal barrier coatings | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1016/j.jvolgeores.2019.106707 | CWWP8QBD |
| S165 | 2016 | The degradation of thermal barrier coatings by molten deposits: introducing the concept of basicity | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 与S029摘要高度相似，DOI不同；保留两个条目，需核研究重叠。 | 10.1179/1878641315Y.0000000017 | 5VWS5F88 |
| S169 | 2025 | The impact of volcanic eruptions on aviation safety | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.13745/j.esf.sf.2025.7.8 | DKVGBA2H |
| S170 | 2018 | The microstructural investigation of vermiculite-infiltrated electron beam physical vapor deposition thermal barrier coatings | 与熔体物性、润湿或沉积相关；先用A/B1核心对照，再按具体缺口选择本篇。 | 10.1515/chem-2018-0097 | 8AXWU6CC |
| S175 | 2013 | Thermal cycling behaviour of plasma sprayed lanthanum zirconate based coatings under concurrent infiltration by a molten glass concoction | 与微结构或损伤有关；作为核心涂层验证文献的补充，具体试验与模型边界待全文核查。 | 10.1016/j.ceramint.2012.07.084 | JA72FYYY |
| S177 | 2015 | Turbomachinery blade thermomechanical interface science and sandphobic coatings research | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | — | EDE4YGWZ |
| S178 | 2025 | Ultrafast laser fabricated triple-scale micro/nano structured NdYbZr2O7 thermal barrier coatings with molten volcanic ash repellency | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2025.132465 | IGBFXNTQ |
| S179 | 2022 | Understanding the thermal barrier performance of plasma-sprayed rare-earth zirconate coating against volcanic ash ingestion | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.surfcoat.2022.128745 | YHKVEGWQ |
| S184 | 2013 | Volcanic ash-induced decomposition of EB-PVD Gd 2 Zr 2 O 7 thermal barrier coatings to Gd-oxyapatite, zircon, and Gd, Fe-zirconolite | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1111/jace.12251 | 8SDT3UXW |
| S186 | 2025 | YPO4: a promising environmental barrier coating candidate against corrosion of molten CMAS | 材料成分或表面防护案例相关，但当前优先补评价与背景证据，留作后续专题候选。 | 10.1016/j.jeurceramsoc.2025.117359 | ETJ2T4GB |

### C 本轮暂不纳入

| 编号 | 年份/日期 | 题名 | 作用与核查重点 | DOI | Zotero item key |
|---|---|---|---|---|---|
| S003 | 2024 | A raman spectroscopic study of lightning-induced glass produced from five mineral phases | 题名/摘要主要为火山/矿物形成与鉴定，未直接连接本轮涂层沉积腐蚀问题。 | 10.1029/2023EA003114 | ARMQ9DV5 |
| S005 | 2003 | Agglomeration in bio-fuel fired fluidized bed combustors | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.cej.2003.08.008 | 9D5N3QT4 |
| S007 | 04/2019 | Alkali silicate reaction of cement mortar with cattle manure ash | 题名/摘要对象是水泥、砂浆或骨料利用，不直接补充CMAS涂层背景。 | 10.1016/j.conbuildmat.2019.01.078 | Z8YITEJK |
| S008 | 2016 | Alkali transformation during single pellet combustion of soft wood and wheat straw | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuproc.2015.11.016 | UACKJF6U |
| S011 | 2015 | An investigation on the fusibility characteristics of low-rank coals and biomass mixtures | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2015.06.010 | CP2TW9DU |
| S012 | 2023 | Application of mössbauer spectroscopy and FT-IR to describe coordination of amphoteric ions in structure of glasses from the SiO2–Na2O–MgO–CaO–Al2O3–Fe2O3 system | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.molstruc.2023.135368 | 5E3JTM5K |
| S013 | 2013 | Ash and deposit characteristics from oil-palm empty-fruit-bunch (EFB) firing with kaolin additive in a pilot-scale grate-fired combustor | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuproc.2013.05.018 | 3GECLM32 |
| S014 | 2018 | Ash formation and deposition in coal and biomass fired combustion systems: progress and challenges in the field of ash particle sticking and rebound behavior | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.pecs.2018.02.001 | L96JT5BT |
| S015 | 2010 | Ash melting behavior and mineral transition mechanism under gasification condition | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | — | JNXQ7GZD |
| S016 | 2011 | Ash-forming elements in four scandinavian wood species part 3: combustion of five spruce samples | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.biombioe.2010.10.010 | XNMAMPEM |
| S017 | 2016 | Ash-related issues during biomass combustion: alkali-induced slagging, silicate melt-induced slagging (ash fusion), agglomeration, corrosion, ash utilization, and related countermeasures | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.pecs.2015.09.003 | IBKYRNTE |
| S019 | 2012 | Bed Agglomeration Characteristics in Fluidized-Bed Combustion of Biomass Fuels Using Olivine as Bed Material | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1021/ef300569n | WGLI3BBA |
| S024 | 2004 | Characterisation of the glass fraction of a selection of European coal fly ashes | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1002/jctb.1023 | W9D4N7I4 |
| S027 | 2006 | Chemical composition and evolution mechanism of ferrospheres in fly ash from coal combustion | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | — | DSMM8R3Q |
| S028 | 2005 | Chlorination behavior of zinc and lead from molten fly ashes: effects of metal forms and coexisting elements | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | 10.1252/kakoronbunshu.31.278 | PS5G9AJD |
| S033 | 2014 | Coating and melt induced agglomeration in a poultry litter fired fluidized bed combustor | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.biombioe.2014.07.013 | MJKFK5JY |
| S034 | 2022 | Comparative insights into flue gas-to-ash characteristics on co-combustion of walnut shell and bio-oil distillation sludge under atmospheric and oxy-fuel condition | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.combustflame.2022.112383 | MSQXMECM |
| S050 | 2021 | Effect of alkaline activator ratio on the compressive strength response of POFA-EACC mortar subjected to elevated temperature | 题名/摘要对象是水泥、砂浆或骨料利用，不直接补充CMAS涂层背景。 | 10.1080/09603409.2021.1897942 | V9L5HK9P |
| S051 | 2025 | Effect of chlorides on the melting behavior of municipal solid waste incineration fly ash | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.jece.2025.116009 | 683ZHMCJ |
| S053 | 2008 | Effect of coal-water slurry reburning on ash deposition in boiler | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | — | B3U992P3 |
| S056 | 2017 | Effect of silica and alumina on petroleum coke ash fusibility | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1021/acs.energyfuels.7b02843 | ACDW9LZK |
| S057 | 2024 | Effect of temperature on activity of water quenched slag prepared by reducing iron oxide of steel slag with coal gangue | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.14062/j.issn.0454-5648.20230603 | BR3SKTTZ |
| S058 | 2020 | Effect of thermal expansion additives on alleviating the ash deposition of high-sodium coal | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.jenvman.2020.110799 | DRXG4UJS |
| S059 | 2022 | Effects of atmosphere on mineral transformation of zhundong coal during gasification in CO2/H2O conditions | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2021.122428 | RC8IQR34 |
| S060 | 2022 | Effects of calcium, sodium and potassium on ash fusion temperatures of solid recovered fuels (SRF) | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.wasman.2022.06.032 | 8Z4WETIU |
| S068 | 10/2017 | Experimental investigation of ash deposition behaviour modification of straws by lignite addition | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.applthermaleng.2017.06.144 | PA9BJLAK |
| S069 | 2017 | Experimental study and thermodynamic modelling of high temperature interactions between molten miscanthus ashes and bed particles in fluidized bed reactors | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1007/s12649-017-9828-x | PDH5ZEQF |
| S070 | 2024 | Experimental study on treatment of Pb ion wastewater by alkali fusion modified steel slag | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | 10.19965/j.cnki.iwt.2023-0623 | AM2QJM5V |
| S075 | 2018 | Fusibility characteristic and flow properties of semi-char from industrial circulating fluidized bed gasification | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2018.07.129 | PRRB8QUZ |
| S083 | 2022 | Hydration development of blended cement paste with granulated copper slag modified with CaO and Al2O3 | 题名/摘要对象是水泥、砂浆或骨料利用，不直接补充CMAS涂层背景。 | 10.1016/j.jmrt.2022.03.008 | VQLHABR7 |
| S085 | 7/2020 | Improving the Interfacial Reaction Between Cristobalite Silica from Rice Husk and Al–Mg–Si by CVD-Si3N4 Deposition | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1007/s12649-019-00706-w | M68AKFVL |
| S087 | 2017 | Influence of coal blending on ash fusion property and viscosity | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2016.10.050 | DBT6ID3C |
| S089 | 2026 | Influence of occurrence mode of potassium and a calcium-based additive on ash transformation and agglomeration behavior for coal and phosphorus-rich biomass co-gasification | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.joei.2026.102521 | Z89T49QG |
| S090 | 2014 | Influential factors of alkaline content in alumina-removed residue by hydrothermal treatment from extraction process of alumina from fly ash with sub-molten salt method | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | — | 77DG6YSG |
| S091 | 2015 | Inhibition of lignite ash slagging and fouling upon the use of a silica-based additive in an industrial pulverised coal-fired boiler. Part 1. Changes on the properties of ash deposits along the furnace | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2014.06.054 | BF8Q6FY4 |
| S092 | 01/2015 | Inhibition of lignite ash slagging and fouling upon the use of a silica-based additive in an industrial pulverised coal-fired boiler: Part 2. Speciation of iron in ash deposits and separation of magnetite and ferrite | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2014.06.075 | Y6X5YRK5 |
| S095 | 2017 | Interactions between molten salts and ash components during zhundong coal gasification in eutectic carbonates | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2017.06.079 | SXWQGMIC |
| S099 | 2022 | Investigation on formation mechanisms of ash and deposit from cotton stalk vibrating grate boiler combustion based on their characteristics | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2022.124446 | 8A6K5CIM |
| S100 | 2023 | Laboratory evaluation of tundish covering powders and rice hull ash on cleanliness for a SAE 1055 modified steel | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1590/1980-5373-MR-2022-0216 | Z96Q8VNG |
| S105 | 2026 | Mechanistic insights into the effect of biomass ash on molten nitrate salt pyrolysis | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.cej.2026.174950 | 66HX6QPB |
| S108 | 1986 | Melting and crystallization of fly ashes | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | — | XZXJMW6S |
| S109 | 2024 | Melting and flow behavior of coal ash at high temperatures based on SiO2-Al2O3-CaO/Na2O pseudoternary phase diagram | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1021/acsomega.4c01678 | 4Y2UIRRE |
| S112 | 2008 | Microstructure of ferrospheres in fly ashes: SEM, EDX and ESEM analysis | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1631/jzus.A0820051 | N59BZVRG |
| S114 | 2015 | Mineral conversion regularity and release behavior of Na, Ca during zhundong coal's combustion | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.13334/j.0258-8013.pcsee.2015.05.018 | W8LZ5FFA |
| S115 | 2026 | Mineral transformation behavior in coal ash slag during plasma underground coal gasification | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1007/s40789-026-00876-8 | 4AGD2RZC |
| S117 | 2026 | Mitigation of steel corrosion in waste-to-energy from poultry litter by modifying ash chemistry | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.wasman.2026.115745 | R6UFWB35 |
| S130 | 2014 | Perils in distinguishing phreatic from phreatomagmatic ash; insights into the eruption mechanisms of the 6 august 2012 Mt. Tongariro eruption, new zealand | 题名/摘要主要为火山/矿物形成与鉴定，未直接连接本轮涂层沉积腐蚀问题。 | 10.1016/j.jvolgeores.2014.05.001 | NBE96JFT |
| S135 | 10/2003 | Potassic glass and calcite carbonatite in lapilli from extrusive carbonatites at Rangwa Caldera Complex, Kenya | 题名/摘要主要为火山/矿物形成与鉴定，未直接连接本轮涂层沉积腐蚀问题。 | 10.1180/0026461036750152 | JHMGQM53 |
| S136 | 2021 | Preparation of SiC reticulated porous ceramics with high strength and increased efficient filtration via fly ash addition | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.jeurceramsoc.2020.11.039 | SXLTEFT5 |
| S138 | 2019 | Rapid sintering of weathered municipal solid waste incinerator bottom ash and rice husk for lightweight aggregate manufacturing and product properties | 题名/摘要对象是水泥、砂浆或骨料利用，不直接补充CMAS涂层背景。 | 10.1016/j.jclepro.2019.06.010 | MD3BKCBV |
| S142 | 2024 | Relation between the viscosity and electrical conductivity of molten slag for coal gasification and their dependence on SiO2 content | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.cherd.2024.05.043 | M843MWHV |
| S151 | 2026 | Silicate rings in woody biomass ash melts based on molecular dynamics simulations | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1021/acsomega.5c12582 | 93CFCHLH |
| S153 | 2007 | Slagging behavior of wood ash under entrained-flow gasification conditions | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1021/ef700247t | HHT6PXWI |
| S154 | 2025 | Slagging characteristics of industrial waste incineration system in sections with different temperatures | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.joei.2025.102107 | 54P4REUQ |
| S155 | 2021 | Structures and diffusion motions of K and Ca in biomass ash slags from molecular dynamics simulations | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2021.121072 | M7DCEYM5 |
| S156 | 2016 | Study of bed materials agglomeration in a heated bubbling fluidized bed (BFB) using silica sand as the bed material and KOH to simulate molten ash | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.powtec.2015.12.030 | 9Y7GGCSX |
| S157 | 2012 | Study on structural and compositional transitions of coal ash by using NMR | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1007/s12404-012-0114-z | FHTMBKME |
| S158 | 2019 | Study on the slagging characteristics of xinjiang high-alkali coal in four-nozzle gasifier | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.13226/j.issn.1006-6772.19032502 | UTHR5ZXK |
| S159 | 2021 | Study progress on the composition characteristics of fly ash from municipal solid waste incineration and treatment technology of heavy metal melting and solidification | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | 10.13226/j.issn.1006-6772.A20111302 | GPHYX942 |
| S161 | 2025 | Sustainable avenue for biochar production using bamboo dust through a novel thermo-electrochemical process | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.ijhydene.2025.151794 | 4HFP4SEJ |
| S162 | 2020 | Systematic study on ash transformation behaviour and thermal kinetic characteristics during co-firing of biomass with high ratios of bituminous coal | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.renene.2019.09.103 | ET5SMBW6 |
| S164 | 1998 | The behavior of inorganic material in biomass-fired power boilers: field and laboratory experiences | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/S0378-3820(97)00060-X | SMLIPHIN |
| S166 | 03/2020 | The effect of co-firing coal and woody biomass upon the slagging/deposition tendency in iron-ore pelletizing grate-kiln plants | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuproc.2019.106254 | A4IKIZDW |
| S167 | 2003 | The effect of salt-phase composition on the rate of soda-ash roasting of chromite ores | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1007/s11663-003-0024-y | U5Q98PCB |
| S168 | 2007 | The formation mechanism of the vitrified slag in a plasma arc reactor for hazardous waste treatment | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | — | SJ499XEC |
| S171 | 2010 | The migration and distribution of heavy metals in melting flue gas during the melting process of MSWI fly ash | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | — | W4FTVHW3 |
| S172 | 2023 | The migration and transformation mechanisms of heavy metals during molten salt cyclic thermal treatment of MSWI fly ash | 题名/摘要关注废物处理或金属回收，缺少本轮需要的涂层/陶瓷侵蚀对象。 | 10.1016/j.cej.2023.144731 | QY5PEJ4W |
| S173 | 2025 | The role of coal components and modifications on direct carbon fuel cells | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1117/12.3067313 | JP3G733V |
| S174 | 1993 | Thermal analysis of reactions in soda–lime silicate glass batches containing melting accelerants: II, multicomponent systems | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1111/j.1151-2916.1993.tb03648.x | 6FBA2WI7 |
| S176 | 2013 | Towards a comprehensive thermodynamic database for ash-forming elements in biomass and waste combustion - current situation and future developments | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuproc.2011.08.008 | CHY8MRBY |
| S181 | 2020 | Viscosity of molten CaO–K2O–SiO2 woody biomass ash slags in relation to structural characteristics from molecular dynamics simulation | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.ces.2019.115464 | C9LPM3XC |
| S182 | 2009 | Viscosity predictions of the slag composition of gasified coal, utilizing FactSage equilibrium modelling | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.1016/j.fuel.2008.07.034 | BJ6U2EMS |
| S183 | 2019 | Viscosity property and melt structure of CaO-MgO-SiO                         2                         -Al                         2                         O                         3                         -FeO slag system | 题名/摘要对象主要为燃料灰、锅炉/气化炉、冶金或固废利用，暂不用于本轮CMAS涂层背景；不评价论文质量。 | 10.2355/isijinternational.ISIJINT-2018-479 | 8E74JV86 |

