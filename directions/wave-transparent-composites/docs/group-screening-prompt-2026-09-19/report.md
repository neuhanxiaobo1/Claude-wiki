---
direction_id: wave-transparent-composites
created: 2026-09-19
updated: 2026-09-19
---

# 组内材料与文献筛选提示词依据

交付：[单段提示词](透波文献筛选Prompt_组内材料与研究范围_2026-09-19.txt)。输出归透波方向；陶瓷腐蚀方向只读借鉴。本文为定性范围梳理，不做性能排名或资源可用性认证。

## 覆盖与证据边界

2026-09-19只读查询田老师父集合LED7JJ3Y、陶瓷子集合QUNDVKXV、透波直接集合BSQRX4DM，分别59、6、10条成员记录，共75条集合关联、66个唯一条目；[元数据快照](group-collection-metadata.json)保留题名、作者、DOI、摘要。按陶瓷方向既定口径，作者全名Zhilin Tian / Tian Zhilin匹配者56条，但包含非陶瓷/非透波研究，不能称为56篇透波成果。TV8YNAAA只有Z. Tian，身份待核；TTV8VL6D未匹配田志林全名，不能据目录认定组内。综述介绍的方法不当作本组实验能力。新筛选外部文献不受该作者规则限制。

现有陶瓷10篇论文页与透波7篇原始研究页用于材料、研究设计与证据范围复核；补查父集合全部题名/作者，并读相关新增论文摘要。不是56篇全文逐篇复核，也不是本组历史发表全集。陶瓷页的checked限于各页声明范围，透波页仍为draft；此次不升级状态。纯CMAS论文退出透波核心库，不妨碍其作为陶瓷方向材料与方法背景；同一来源不重复计为独立证据。

## 定性材料与方法矩阵

以下仅支持定性材料/方法关联（qualitative-only），不跨温度、频率或样品形态计算性能差距。新增摘要的定位为快照中相应key的abstractNote；材料是否已用于透波需另判。

| 范围 | 材料与变量/方法 | 原始来源及核查范围 | 可支持的用途与限制 |
|---|---|---|---|
| 纤维复合材料 | 层合穿刺SiO2f/SiO2；混编Si3N4/SiO2纤维增强BN；浸渍、界面、织构 | [[directions/wave-transparent-composites/wiki/papers/Wen-2026-Laminated-SiO2f-SiO2]]、[[directions/wave-transparent-composites/wiki/papers/Chen-2026-Hybrid-Fibers-BN]]的Study Design及E#；draft | 直接复合材料基础；宏观力学、局部界面和介电测量须分开，不能推定具有纤维制备能力 |
| 多孔和打印 | 双溶剂Si3N4/SiO2、光固化Si3N4浆料与蜂窝 | [[directions/wave-transparent-composites/wiki/papers/Liu-2024-Porous-Si3N4]]；NHWNLW5D、CP78IM7I、HBMWPIR2摘要 | 已有成孔、成型与结构研究；蜂窝力学论文不能因为缺介电测试而直接排除；摘要不证明全套高温透波验证 |
| 氧化物介电组分 | RE2SiO5、RE2Sn2O7、Ti-Zr-Hf焦磷酸盐、高熵二硅酸盐 | [[directions/wave-transparent-composites/wiki/papers/Du-2024-RE2SiO5]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7]]、[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7]]、[[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate]]的研究设计及E#；draft | 组分、相变、热/力/介电协同，DFT与传统机器学习；不是所有结果都可直接用于纤维复合体系，机器学习不是大模型 |
| 稀土陶瓷环境稳定性 | RE2SiO5/RE2Si2O7固溶及高熵、RETaO4、RE2Zr2O7、高通量/层叠CMAS筛选 | [[directions/ceramic-corrosion/index]]所列10篇研究的材料/方法证据；快照9Q7A46HL、42UX6GZL、8IPQUSQL、88RPHLC9、YPQHNP84、X55RXI85等 | 可借鉴组成、相稳定性、腐蚀/环境表征与筛选思路；纯腐蚀不进入透波核心，块体反应不等于实际涂层寿命 |
| 相邻热学陶瓷 | Hf6Ta2O17/Al2O3、Al2O3/YAG及高熵共晶、堇青石、Si2N2O、Lu4Si2O7N2 | 陶瓷Hf6Ta2O17论文页；6Q565WS9、I6FJFWHH、THPYAVII、YLMQK2HS、KC5AHZTM、VI7A2ABN摘要 | 支持热学、相容性、定向凝固与声子研究基础；不能据低热导推定低介电损耗 |
| 纤维界面与BN | BN包覆Si3N4纤维、BN纳米片制备 | 7FNBQDVG、G6JHU82J摘要 | 氧化/结晶稳定性与填料方法可迁移；光学透明不等于微波透波，摘要未确定的CVI等具体制法不列已掌握 |
| 非核心关联研究 | SiBCN传感、复杂/高熵碳化物、Cr2AlC相容性 | DIVMKP87、HHTZYQ4E、EML8AIBE、XU8SL9SV摘要 | 仅表示有相关发表基础；导电性、功能目标和迁移路径需核，不能直接纳入低损耗体系 |

## 筛选取舍与未验证扩展

已有主线是纤维/基体/界面与多孔结构调控、氧化物组成和多目标性能研究。SiAlON、其他Si-B-N-O体系、莫来石或新的沉积/浸渍组合属于AI提出的相邻扩展，不是已确认组内成果；设备、原料、合作条件与成本仍需确认。大模型证据抽取、条件归一与实验决策是候选路径，不是已完成研究。任何新课题的国际新颖性都需进一步检索反证。

新版采用A核心、B具体方法/材料迁移、C待核、D不相关。外部旧文件“透波文献筛选方案与Prompt.md”的统一ε<5、纯力学/热学一律排除及材料关键词硬排除可能漏掉已有打印、界面与组分基础，故另存新版，不覆盖旧文件；详见方向error_log。既有吸波/腐蚀资料不据此自动移回核心库。用户报告激光文献已移除，本轮不再操作该条目。

## 交付边界

外部目标：F:/industry software/onedrive/1.Science/1.Zotero/fenqu/透波文献筛选Prompt_组内材料与研究范围_2026-09-19.txt。提示词可独立读取，不依赖Wiki链接；仅生成筛选建议，不执行批量筛选或Zotero写入。本次文件未自动提交或上传Git。
