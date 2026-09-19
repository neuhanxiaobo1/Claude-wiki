---
direction_id: wave-transparent-composites
type: audit
created: 2026-09-19
updated: 2026-09-19
status: completed-local
---

# 透波复合材料文献库主题筛查

## 范围与执行结果

用户明确要求移除High Throughput Screening of CMAS Corrosion-Resistant RETaO4 Based on Lamination Method，并检查其他误入文献。本轮沿用透波复合材料方向，不操作其他研究方向。

- 本地原11个paper页已检查研究问题及既有证据；原9篇另回读英文MD摘要/引言相关段落，两篇综述复用上一轮阅读核查。
- Zotero实时查询父集合BSQRX4DM及全部5个子集合，81个成员、81个唯一item key，其中包含1个检索词管理条目；核对全部题名，并阅读重点候选与透波综述集合的可用摘要。不是81篇全文复核。
- 用户近期扩充目录；“2.透波综述”现9项，“综述词条”14项，“吸波”22项，“透波词条”0项，“1.透波文献”26项；父集合直接成员10项。
- 指定CMAS论文已退出本地wiki/papers、核心索引及综合证据，历史阅读记录保存在[[directions/wave-transparent-composites/docs/excluded-papers/Tian-2025-RETaO4-CMAS]]。原E1–E3仅为历史，不再计入当前透波证据。
- Zotero的remove_items_from_collection请求被插件拒绝：Write Operations disabled。没有删除集合关联、总库条目或PDF，未绕过插件限制。返回见[removal-result.json](removal-result.json)。
- 其他候选只标注，不擅自扩大删除范围。rGO/MXene吸波页已排除核心计数；单独命名的“吸波”子集合视为明确分区，不批量清空。
- 当前本地wiki/papers有10页、43条E#；其中9篇核心/40条E#，另1篇吸波候选/3条E#；历史CMAS页另存3条E#。数量不代表独立验证数，review_status不升级。

## 筛选口径

以实际研究问题、频段、功能目标和测量结果判断，而非是否出现BN、SiO2、dielectric、低热导率等词。透波组成/孔结构研究即使不是纤维复合材料，也可作为直接材料基础；热机械、缺陷评价属于相关方法。一般绝缘/击穿、纯腐蚀、纯吸波或非线性光学不能自动充当微波透波成果。LLM属于用户允许的明确方法分支，保留但单列。未读全文的边界条目不判定为确定误入。

## 重点发现

| Item key | 判断 | 依据与边界 | 本轮处置 |
|---|---|---|---|
| 88RPHLC9 | 明确不属于透波核心；用户指定移除 | RETaO4抗CMAS腐蚀，原文未提供介电/透波验证。 | 本地移除并归档；Zotero写入被禁用，待同步 |
| CVNSDVQS | 明确不属于透波核心 | rGO/MXene/SiC的目标与核心结果为微波吸收，非透波。 | 标记为待移除候选，退出核心计数；未删除条目 |
| RKWD3F8J | 明确偏离当前微波透波主题 | Au/TiO2薄膜以800 nm激光Z-scan表征三阶非线性光学，用于光开关等。 | 建议移出透波文献；未删除，尚未本地入库 |
| TYYH429B | 非核心候选 | 碳/SiO2负介电常数与直流偏压调控；摘要未提供低损耗微波透射验证。 | 建议放入电磁超材料方法参考；正文待核 |
| JZPHE3K4 | 非核心候选 | HfSiO4的EBC/热力学、导热和弹性研究；摘要无微波透波验证。 | 热物性方法参考可选，不当作透波材料结果 |
| R7NQ774P | 非核心候选 | BN/芳纶导热绝缘薄膜；摘要介电数据在10^4 Hz，并报告击穿性能。 | 不将低频绝缘数据当作GHz透波结果；未删除 |
| RSKH7L4G | 非核心候选 | BN纳米片/芳纶薄膜面向高功率电子器件导热、绝缘和击穿性能。 | 不计透波实验证据；未删除 |
| NATGYNND | 边界候选，需全文判断 | SiCf/SiC的BN界面、力学与复介电；摘要不足以判定透波或吸波目标。 | 保留待核，不因含BN就归为透波 |
| VDK2SSNX | 边界候选，需全文判断 | 碳纤维/RBSN在X波段测介电参数，但摘要未给透射、损耗与明确透波验证。 | 保留待核，不因标题有dielectric就认定透波 |
| YJGX6KP7 | 允许的方法参考 | 材料NLP/LLM综述；用户明确允许大模型结合，非直接透波材料证据。 | 保留为方法候选；本轮未入库 |
| 3YULHPWU | 相关但应用不同 | 综述对象是微波烧结炉衬的高温透波材料，不是常规承载天线罩。 | 保留材料/隔热借鉴，不直接跨工况比较 |
| BPIRLTYT | 相关的失效评价综述 | 陶瓷天线罩缺陷、损伤与检测，服务于透波构件可靠性。 | 保留；不是因无新介电数据就误入 |
| RBB8BGIU | 相关的测试方法综述 | 陶瓷天线罩热机械性能测试与无损检测。 | 保留方法用途 |
| E9V8I5KH | 边界：吸透一体 | 题名同时包含吸收与透射；不能因absorption一词直接剔除。 | 题名初筛，全文待核 |
| 4W3QR2IX | 边界：同时讨论吸收与透射 | 题名明确同时覆盖两类功能。 | 保留候选，使用时分清证据用途 |
| YWS6K5JA | 边界：电磁功能较宽 | Si-C-N电磁性质；题名不足以确定透波覆盖。 | 摘要/全文待进一步核查 |
| 73RMHVUZ | 管理条目 | 透波复合材料检索词，不是研究论文。 | 不计文献数，不作为误入删除 |

以上题名和摘要原始快照见[collection-before.json](collection-before.json)。新候选摘要中的性能宣传未在本轮复核，不作为确定材料性能写入科学页面。

## 全部成员的主题初筛

下表“题名初筛相关”仅表示没有从题名发现明显偏题，不能替代全文审查；“吸波分区”表示集合用途已经明确，不计入透波核心。

| 集合 | Item key | 题名 | 初筛结果 |
|---|---|---|---|
| 透波复合材料（直接成员） | JIWA4YJA | Mechanical and dielectric properties of RE2SiO5 (RE=Ho, Er, Tm, Yb, and Lu) as high-temperature wave-transparent materials | 已入库核心，保留 |
| 透波复合材料（直接成员） | QXLQJ5J8 | Rare earth stannates: A new high-performance wave-transparent material investigated through theoretical and experimental approaches | 已入库核心，保留 |
| 透波复合材料（直接成员） | CVNSDVQS | Hierarchical rGO/MXene aerogels assembled with SiC nanowires for excellent electromagnetic wave absorption and multifunctionality | 明确不属于透波核心 |
| 透波复合材料（直接成员） | YTXGYWDT | Suppressing the phase transition of ZrP<sub>2</sub> O<sub>7</sub> by defect and entropy regulation for high-temperature wave-transparent material application | 已入库核心，保留 |
| 透波复合材料（直接成员） | ZSR932E8 | Synergistic promotion of dielectric and thermomechanical properties of porous Si<sub>3</sub> N<sub>4</sub> ceramics by a dual-solvent template method | 已入库核心，保留 |
| 透波复合材料（直接成员） | 88RPHLC9 | High Throughput Screening of CMAS Corrosion‐Resistant RETaO<sub>4</sub> Based on Lamination Method | 明确不属于透波核心；用户指定移除 |
| 透波复合材料（直接成员） | BANWJKZW | High-performance SiO2f/SiO2 wave-transparent composites based on laminated puncture method | 已入库核心，保留 |
| 透波复合材料（直接成员） | LDCDP9WH | Synergistic enhancement of the performance of BN based wave-transparent composites by hybrid weaving of Si3N4 and SiO2 fibers | 已入库核心，保留 |
| 透波复合材料（直接成员） | 534JVRMI | Data-Driven Discovery of Composition–Structure–Property Relationship in Novel Wave-Transparent High-Entropy Rare Earth Disilicate | 已入库核心，保留 |
| 透波复合材料（直接成员） | 73RMHVUZ | 透波复合材料检索词 | 管理条目 |
| 2.透波综述 | G8TMSGFC | Dielectric and mechanical properties of hypersonic radome materials and metamaterial design: A review | 已入库核心，保留 |
| 2.透波综述 | XLB9BUFZ | Development of high-temperature wave-transparent nitride-based CFCMCs for aircraft radomes | 已入库核心，保留 |
| 2.透波综述 | YJGX6KP7 | Applications of natural language processing and large language models in materials discovery | 允许的方法参考 |
| 2.透波综述 | 3YULHPWU | Progress on high-temperature wave-transmitting materials in microwave sintering | 相关但应用不同 |
| 2.透波综述 | BPIRLTYT | A survey on ceramic radome failure types and the importance of defect determination | 相关的失效评价综述 |
| 2.透波综述 | TU4KFIZW | Research progress of high temperature resistant electromagnetic wave-transparent materials | 题名初筛相关；全文待核 |
| 2.透波综述 | RBB8BGIU | A review of thermal-mechanical performance test technology for ceramic missile radome | 相关的测试方法综述 |
| 2.透波综述 | P7JYUXN5 | Composite materials for supersonic aircraft radomes with ameliorated radio frequency transmission-a review | 题名初筛相关；全文待核 |
| 2.透波综述 | HI3I6IRE | High temperature ceramic radomes (HTCR) – a review | 题名初筛相关；全文待核 |
| 综述词条 | 74IY5JUN | Progress of preparation process for ceramic matrix composites radomes | 题名初筛相关；全文待核 |
| 综述词条 | IMR28QBK | Development of Silicon Nitride‐Based Ceramic Radomes — A Review | 题名初筛相关；全文待核 |
| 综述词条 | E9V8I5KH | Research progress in integrated metamaterial with functionalities of absorption and transmission | 边界：吸透一体 |
| 综述词条 | UL5WFN9S | Research progress on polymer-derived nitride ceramics for wave transparent at high temperature | 题名初筛相关；全文待核 |
| 综述词条 | D7NXH2JX | Microwave-transparent refractory materials for high-temperature metallurgical applications | 题名初筛相关；全文待核 |
| 综述词条 | 4W3QR2IX | Principles, design, structure and properties of ceramics for microwave absorption or transmission at high-temperatures | 边界：同时讨论吸收与透射 |
| 综述词条 | YWS6K5JA | Electromagnetic properties of Si-C-N based ceramics and composites | 边界：电磁功能较宽 |
| 综述词条 | JNXF3L9K | Design, selection, manufacturing, and modeling strategies in airborne radome materials: a review | 题名初筛相关；全文待核 |
| 综述词条 | RAIGJA4F | Various types of ceramics used in radome: a review | 题名初筛相关；全文待核 |
| 综述词条 | G4BF5LW5 | Research progress of nitride based ceramic high temperature wave transparent materials | 题名初筛相关；全文待核 |
| 综述词条 | ERCTY2ZV | Polymer matrix wave-transparent composites: a review | 题名初筛相关；全文待核 |
| 综述词条 | QBV6974P | A green PI-SiO₂ aqueous sizing coating for tailoring the interphase of quartz fiber/PEEK composites toward enhanced mechanical performance and electromagnetic transparency | 题名初筛相关；全文待核 |
| 综述词条 | R7NQ774P | Large-scale preparation of high-performance boron nitride/aramid nanofiber dielectric composites | 非核心候选 |
| 综述词条 | RSKH7L4G | Plasma-modified boron nitride nanosheets for high-performance aramid-based dielectric films with enhanced multifunctionality | 非核心候选 |
| 吸波 | QXDIEJSJ | Facile synthesis of NiFe2O4/Ni3Fe/LAS core-shell-like composites with improved impedance matching and microwave absorption properties | 吸波分区，非透波核心 |
| 吸波 | Z5VJUQX5 | Research progress on microwave absorption stealth technology of honeycomb sandwich structure composites | 吸波分区，非透波核心 |
| 吸波 | Z8KEDXEX | Improved mechanical and microwave absorption properties of SiCf/SiC composites with SiO2 filler | 吸波分区，非透波核心 |
| 吸波 | BUBBMIYV | Mechanical and microwave absorption properties of SiCf/SiC–Al4C3 composite with EPD-SiO2/ZrO2 interphase prepared by precursor infiltration and active filler-controlled pyrolysis method | 吸波分区，非透波核心 |
| 吸波 | WZ2XBHJZ | Influence of different matrices on the mechanical and microwave absorption properties of SiC fiber-reinforced oxide matrix composites | 吸波分区，非透波核心 |
| 吸波 | G9D8IVLJ | Ultra-broadband electromagnetic wave absorbent: In-situ generated silica modified conductive carbon fiber aerogels | 吸波分区，非透波核心 |
| 吸波 | KVMV4BT8 | Honeycomb structure SiCf/Si3N4 composite with broadband electromagnetic absorption performance under a wide temperature range | 吸波分区，非透波核心 |
| 吸波 | K9TSVKEW | Effects of SiC contents on the dielectric properties of SiO2f/SiO2 composites fabricated through a sol-gel process | 吸波分区，非透波核心 |
| 吸波 | 54ZYHNCE | Microstructure, microwave absorbing and mechanical properties of SiCf/Si3N4composites containing frequency selective surface (FSS)-type fiber cloth | 吸波分区，非透波核心 |
| 吸波 | BEBCWLZE | Enhanced high-temperature dielectric and microwave absorption properties of SiC fiber-reinforced oxide matrix composites | 吸波分区，非透波核心 |
| 吸波 | QLXJLG3K | Wave absorption and mechanical properties of SiCf-SiO2f/SiC based on a jaumann structure | 吸波分区，非透波核心 |
| 吸波 | 53NKWTR6 | Corrugated structure SiCf/Si3N4 composite with high-temperature broadband microwave absorption through the regulation of high-temperature dielectric properties | 吸波分区，非透波核心 |
| 吸波 | FIARM8V5 | Carbon fiber reinforced SiBCN composite with broadband and tunable microwave absorption performance | 吸波分区，非透波核心 |
| 吸波 | 7STYAWAM | Evolution of high temperature oxidation properties of SiCf/SiCN composites with BN interphase | 吸波分区，非透波核心 |
| 吸波 | WKCXT8H7 | Carbon fiber/Si3N4 composites with SiC nanofiber interphase for enhanced microwave absorption properties | 吸波分区，非透波核心 |
| 吸波 | N87KUG97 | Electromagnetic wave absorption and mechanical properties of silicon carbide fibers reinforced silicon nitride matrix composites | 吸波分区，非透波核心 |
| 吸波 | TSZ5LXE7 | Self-healing SiBCN/SiC dual-phase matrix design for oxidation-resistant, electromagnetic wave absorbing SiC fiber-reinforced composites | 吸波分区，非透波核心 |
| 吸波 | RNINQT6T | Dielectric properties of Cf-Si3N4 sandwich composites prepared by gelcasting | 吸波分区，非透波核心 |
| 吸波 | Y37TDGJW | The dielectric adjustment in SiCf/mullite composites limited carbon content by in situ growth SiO2 layer | 吸波分区，非透波核心 |
| 吸波 | 3HBLIEXC | Sandwich structured SiCf/Si3N4-SiC-Si3N4 composites for tunable microwave absorption, mechanical strength and high-temperature tolerance | 吸波分区，非透波核心 |
| 吸波 | GX2F77KI | Interfacial mechanics and polarization behavior of structural-functional-integrated SiCf/Si3N4 composites in different fiber preform | 吸波分区，非透波核心 |
| 吸波 | MRJTQIPJ | Tuning SiC nanowires interphase to improve the mechanical and electromagnetic wave absorption properties of SiCf/SiCnw/Si3N4 composites | 吸波分区，非透波核心 |
| 1.透波文献 | 6VHBTFI2 | Low-cost needle-punched SiO2/SiO2ceramic composites with low permittivity and enhanced high-temperature mechanical behavior | 题名初筛相关；全文待核 |
| 1.透波文献 | PHA9BH6B | Effects of heat treatment on mechanical and dielectric properties of 3D Si3N4f/BN/Si3N4 composites by CVI | 题名初筛相关；全文待核 |
| 1.透波文献 | QYPDDWHK | 3D woven spacer quartz fiber/polyimide composites with integrated lightweight, electromagnetic transparency, and thermal stability | 题名初筛相关；全文待核 |
| 1.透波文献 | SRGTAHUF | Thermoplastic sandwich radomes via thermal expansion molding for enhanced wet-state reliability | 题名初筛相关；全文待核 |
| 1.透波文献 | Y3GE97F8 | High-temperature properties and associated structure evolution of continuous SiNO fiber-reinforced BN composites for wave transparency | 题名初筛相关；全文待核 |
| 1.透波文献 | 8LGUCHE3 | Mechanical properties and in situ fracture behavior of SiO2f/phosphate geopolymer composites | 题名初筛相关；全文待核 |
| 1.透波文献 | NATGYNND | Influence of dip-coated boron nitride interphase on mechanical and dielectric properties of SiCf/SiC composites | 边界候选，需全文判断 |
| 1.透波文献 | H3CRZINP | Mechanical, wave-transparent, and ablation properties of silicon oxycarbide aerogel composites | 题名初筛相关；全文待核 |
| 1.透波文献 | TYYH429B | Tunable negative permittivity performance of carbon/silicon dioxide ceramic metacomposites under external DC bias voltage | 非核心候选 |
| 1.透波文献 | SHMYTXHH | Performance optimization of SiO2f/SiO2 composites derived from polysiloxane ceramic precursors | 题名初筛相关；全文待核 |
| 1.透波文献 | 5RPEN4VF | Effect of boron doping on waterproof and dielectric properties of polyborosiloxane coating on SiO2f/SiO2 composites | 题名初筛相关；全文待核 |
| 1.透波文献 | K288KLS3 | Fabrication of high performance 3D SiO2/Si3N 4 composite via perhydropolysilazane infiltration and pyrolysis | 题名初筛相关；全文待核 |
| 1.透波文献 | VDK2SSNX | Mechanical and dielectric properties of carbon fiber reinforced reaction bonded silicon nitride composites | 边界候选，需全文判断 |
| 1.透波文献 | FDXFTASF | The antioxidative protection mechanism of the ultra-high temperature radome composite material BNf/SiBN | 题名初筛相关；全文待核 |
| 1.透波文献 | ULUQGIDU | Thermal stable, fire-resistant and high strength SiBNO fiber/SiO2 aerogel composites with excellent thermal insulation and wave-transparent performances | 题名初筛相关；全文待核 |
| 1.透波文献 | 9ZVJ7ZAL | Fabrication of high performance 2.5D SiO2f/Si3N 4-BN composites for high-temperature application | 题名初筛相关；全文待核 |
| 1.透波文献 | 4YN4LWP9 | Study on the fiber/matrix interface modification of Si3N4 f/SiO2 composites with polymer derived double-layer coatings | 题名初筛相关；全文待核 |
| 1.透波文献 | 9XKZZTPH | High-temperature structural evolution and mosaic-shell formation of sinoite fibers resistant to 1700 °C | 题名初筛相关；全文待核 |
| 1.透波文献 | CR3YICJ4 | Preparation of Si3N4f/Si3N4 wave-transparent composites by vat photopolymerization combined with chemical vapor infiltration | 题名初筛相关；全文待核 |
| 1.透波文献 | RKWD3F8J | Preparation and nonlinear optical properties of Au nanoparticles doped TiO2 thin films | 明确偏离当前微波透波主题 |
| 1.透波文献 | 8ZL4IPXL | Flexible and antistatic carbon fiber/silicone rubber composite coating with improved thermal stability, mechanical and wave-transmission properties | 题名初筛相关；全文待核 |
| 1.透波文献 | QTIG7JJC | Effect of sintering temperature on microstructure and flexural strength of 2.5D SiO2f/SiO2 composites | 题名初筛相关；全文待核 |
| 1.透波文献 | BPLNBGUI | Fabrication and properties of ceramic composites with a boron nitride matrix | 题名初筛相关；全文待核 |
| 1.透波文献 | JZPHE3K4 | The thermal and mechanical properties of hafnium orthosilicate: experiments and first-principles calculations | 非核心候选 |
| 1.透波文献 | ALEZKP3J | Effects of heating rate on mechanical and dielectric properties of the Si3N4f/BN/Si3N4composites by PIP | 题名初筛相关；全文待核 |
| 1.透波文献 | 6ZPJFGM5 | Fabrication and investigations on Si3N4/PAN/SiZrOCN ceramic aerogel composites with high-temperature wave permeability | 题名初筛相关；全文待核 |

## 后续与恢复

1. Zotero插件启用Write Operations后，按既有授权仅重试从BSQRX4DM移除88RPHLC9，并查询验证；不删除总库条目或附件。
2. 优先处置rGO/MXene吸波与Au/TiO2非线性光学两篇明确偏题候选；其他边界条目按实际引用用途评估，暂未删除。
3. 新增文献只完成主题初筛，不宣称已入库或已读全文。原综述清单D7TP8Z6X独立PDF当前不再列为集合直接成员，已有YJGX6KP7书目；两者是否附件映射相同本轮未核，旧快照保留为历史。
4. 所有外部原件、缓存和其他方向均未修改。没有提交或上传本轮修改。
