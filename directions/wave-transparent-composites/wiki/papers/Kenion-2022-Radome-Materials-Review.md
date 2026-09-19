---
direction_id: wave-transparent-composites
type: paper
title: 'Dielectric and mechanical properties of hypersonic radome materials and metamaterial design: A review'
year: 2022
authors: [Taylor Kenion, Ni Yang, Chengying Xu]
venue: Journal of the European Ceramic Society
status: processed
review_status: draft
created: 2026-09-18
updated: 2026-09-18
source: Zotero English PDF and MinerU Markdown
source_version: 'Published version, 42(1):1–17; 17 PDF pages'
zotero_collection: '毕设 > 组内文章 > 博士 > 田老师 > 透波复合材料 > 综述 (GS7STC5N)'
zotero_item_key: G8TMSGFC
zotero_attachment_key: XABPJSGR
pdf_attachment_name: 'Kenion 等 - 2022 - Dielectric and mechanical properties of hypersonic radome materials and metamaterial design A revie.pdf'
doi: 10.1016/j.jeurceramsoc.2021.10.006
tags: [paper, review]
---

# Dielectric and mechanical properties of hypersonic radome materials and metamaterial design: A review

## Metadata and Sources

- 正式英文PDF：Zotero附件XABPJSGR；MinerU：`D:/shuju/zotero1/llm-for-zotero-mineru/11100/full.md`。
- 已核对`_llm_source.json`和manifest；完整PDF路径、MD哈希与附件映射见[sources.json](../../docs/ingestion-reviews-2026-09-18/sources.json)。外部原件只读。
- 作者单位为美国北卡罗来纳州立大学，本页作为外部综述入库，不计为组内成果。
- 大部分性能数值来自所引研究；§5.7另含作者本人的初步实验与模型结果，分别记录，不能把整篇都标成新实验或全是转引。

## Reading and Verification Status

- Processing mode: new-ingestion。
- 已读摘要、引言、§2各材料与概览、§3微结构/热冲击、§4介电及环境因素、§5超材料讨论与初步实验、§6结论及创新总结。
- 已查看PDF第7页Table 5、Fig.7–9图像；PDF第13页原生文字复核§5.7、结论与创新总结。
- 其他图表主要阅读解析文字与图注；未逐图核查超材料曲线，未重做模型或实验。没有读取各被引论文全文及独立SI。
- `draft`：材料比较表有频率、样品及来源口径问题；初步实验的高温验证范围不足以支持高温性能结论。保留有条件的综述结论，不宣称完整证据复核通过。

## Research Problem and Contribution

- 问题：陶瓷及复合材料的介电、力学与环境稳定性如何共同限制应用；超材料结构能提供什么额外调控可能。
- 作者声称贡献：归纳10类材料、微结构与环境因素，并讨论超材料，附初步实验。
- 本次确认贡献：跨材料的指标与条件导航、微结构权衡和原始论文入口。不是当前国际最高性能数据库。
- Novelty status: not assessed。本文2022年的“数据不足”描述不能直接成为2026年的领域gap。

## Study Design

| Element | Details | Source |
|---|---|---|
| 材料覆盖 | Pyroceram、SCFS、Rayceram、RBSN、HPSN、celsian、nitroxyceram、BN、磷酸盐复合物、钇硅酸盐 | §2 |
| 数据性质 | 文献/商品材料信息归纳；不同制备、频率与测试方法并存 | §2、Table 1–5 |
| 微结构因素 | 孔隙率、晶粒尺寸及温度/环境对介电和力学的影响 | §3–4 |
| 自有研究 | 超材料样品的初步传输测量与模型；不与综述转引混记 | §5.7 |
| 系统检索方法 | 所读正文未给出可复现完整检索式及系统偏倚评价 | 阅读范围内 |
| 统计限制 | 汇总表不提供统一样本数、误差、方向和测试规范 | Table 5 |

## Key Evidence

### E1

Evidence label: 常温汇总表不能与Tmax拼接成高温实测数据。

- 类型：转引文献。
- 对象与条件：Table 5标题为25 ℃材料性质概览，并另列Tmax；介电列统一标注10 GHz，但部分行与正文频率不一致，见E2。
- 指标与结果（只记录表中转引，未确认原始样品条件）：

| 材料 | ε（表头10 GHz） | tanδ（表头10 GHz） | 弯曲强度 | CTE（×10^-6 ℃^-1） | 密度 |
|---|---:|---:|---:|---:|---:|
| SCFS | 3.17 | 0.0005 | 44 MPa | 0.54 | 2.20 g/cm³ |
| HPSN | 7.40–8.50 | 0.0040 | >350 MPa | 3.20 | 3.20 g/cm³ |
| BN | 4.4 | 0.0003 | 100 MPa | 3.20 | 2.00 g/cm³ |

- 定位：Table 5，PDF第7页；§2.11。
- 独立性：多源转引；同一行亦未必来自同一样品。原始引用SCFS为[9,15,23,30]，HPSN为[15,20,30]，BN为[30,51]。
- 支持：展示不同材料可能面临的性能权衡，并导航原始数据。不能证明上述指标在Tmax下同时保持，也不能直接与纤维复合材料排统一排名。
- 核查：已看PDF原表图像核对数值、单位与标题；CTE温区未在表内报告，未追原始研究。

### E2

Evidence label: 汇总数据存在测试频率和指标口径差异。

- 类型：来源内部核对；不是新增实验。
- 对象与条件：celsian、HPSN、SCFS等综述表格与正文。
- 结果：§2.6描述celsian ε=6.55、tanδ=0.0008是在35 GHz，Table 3和Table 5相应列却写10 GHz；§2.5的HPSN室温tanδ=0.007，而Table 5列0.0040；SCFS Table 1室温ε=3.39、强度37 MPa，Table 5为E1所列另一组值。
- 定位：§2.2/Table 1、§2.5–2.6/Table 3、Table 5（PDF第3–7页）。
- 独立性：不同引用或样品可能解释部分差别，不能未经原始文献核查就强行统一或判定全部为笔误。
- 支持：数据库必须保留表格/正文来源、频率和样品标识。不能把全部表格数值视为已归一到10 GHz。
- 核查：正文MD已读，原PDF表5图像已看，原PDF第4–5页文字复核；原始引用[20,30,44]等仍待读。相关数据不能用于定量排名。

### E3

Evidence label: 孔隙率和晶粒尺寸的作用存在多目标权衡及体系依赖。

- 类型：转引结果、模型及作者解释。
- 对象与条件：§3–4涉及多种粉体陶瓷、复合物；不构成同一材料的统一对照实验。
- 结果：作者讨论增孔降低有效介电常数与损伤力学性能之间的权衡；介电损耗不必与介电常数同向变化。氧化铝与BST的晶粒尺寸—损耗关系例子方向不同，作者明确不存在单一精确关系。
- 定位：§3.1–3.2、§4.1、Fig.11–14、Eq.(1)–(2)。
- 独立性：转引[71,72,80,81,83]等；模型与实验均来自原始文献。
- 支持：同时记录孔隙、介电常数、损耗、强度及样品条件。不能将“孔隙越多损耗越低”或“晶粒越小越好”普适化。
- 核查：已读正文、解析公式与图注；除PDF第7页以外未逐图复核拟合与实验点，未验证模型参数/适用区间，故不将公式作为已验证预测方法入库。

### E4

Evidence label: 湿环境与高温测量缺项是综述识别的评价维度。

- 类型：转引及作者综述判断。
- 对象与条件：多孔陶瓷吸湿、常温/高温介电与力学；作者所覆盖历史文献截至该综述形成时。
- 结果：§4.2讨论水分导致的介电劣化；§2.11/Fig.8因资料缺失对不同材料/指标使用不同温度，不能把缺柱当作零损耗。结论指出相关高温高频资料有限或陈旧。
- 定位：§2.11、Fig.8、§4.2、§6。
- 独立性：综述评述及历史文献，不是系统检索对当前领域的穷尽证明。
- 支持：评估湿度、气氛、频率和温度覆盖；记录缺测而非补零。
- 不支持：不能认定任何具体材料在2026年仍无高温介电研究；不能据此声称已找到创新点。
- 核查：相关段落及Fig.8原PDF图像已查；本轮未追加外部领域检索。

### E5

Evidence label: 超材料初步实验不等于已完成高温服役验证。

- 类型：作者本人实验与模型，分开理解。
- 对象与条件：§5.7报告一组室温样品测试及另一组更耐温材料构成的样品；使用网络分析仪与天线进行传输测量，并提供模型结果。
- 结果：存在样品实验及模型预测；但所读实验叙述未明确报告第二组样品在何种高温下原位测量，也未给出热循环、氧化后性能保持的验证链。本文的“high-temperature”材料/设计称谓不能充当高温试验条件。
- 定位：§5.7（PDF第12–13页）、Fig.22–26、§6。
- 独立性：本节属于作者自己的初步研究，区别于E1–E4转引。未将这些结果作为组内材料的性能基准。
- 支持：存在结构电磁调控的研究路线。不能说高温透波稳定性或完整构件性能已被验证。
- 核查：已读正文并复核PDF第13页文字；曲线未逐点读取，模型细节和高温测量条件不足，不作定量设计建议。

### E6

Evidence label: 两篇综述的应用阈值不一致，不能当作统一标准。

- 类型：作者转引的应用要求。
- 对象与条件：本篇§2/§2.11以ε<5、tanδ<0.1叙述，§6又以ε<4表述；另一篇Zhou综述引言采用tanδ<0.01。
- 定位：本文§2、§2.11、§6；[[directions/wave-transparent-composites/wiki/papers/Zhou-2023-Nitride-CFCMCs-Review#E1]]。
- 支持：确定研究指标前须给定应用与测量条件。不能从一篇综述摘取阈值作为通用验收标准。
- 核查：正文及PDF第13页损耗指数已核；没有检索或确认工程标准，保留差异不自动修正作者数字。

## Conclusions for Reuse

### Finding 1

- Finding / safe wording：本综述可作为材料类别、性能维度和原始来源导航；跨材料量化比较需要重新核对样品、频率、温度与力学测试定义。
- Evidence：E1、E2、E6。
- Support：对条件不统一的判断支持充分；对材料优劣排名证据不足。
- Author interpretation：多类候选各有局限，需要热、电、力学综合评价。
- This reading's assessment：AI推断——用于本方向时，应先建带条件的数据表，不能把综述Table 5当作国际最高水平表。
- Decision：retain with limits。

### Finding 2

- Finding / safe wording：孔隙、环境和温度是需要同时记录的变量；初步结构电磁试验与高温材料性能验证属于不同证据层级。
- Evidence：E3–E5。
- Support：定性框架部分支持；尚不足以形成针对本组材料的优化处方。
- Author interpretation：微结构与超材料结构均可能影响电磁表现。
- This reading's assessment：优先用于检查[[directions/wave-transparent-composites/wiki/papers/Liu-2024-Porous-Si3N4|组内多孔Si3N4]]及[[directions/wave-transparent-composites/wiki/papers/Wen-2026-Laminated-SiO2f-SiO2|层合SiO2f/SiO2]]的比较资格；不自动改变本方向研究目标为超材料。
- Decision：retain as evaluation framework；具体创新性pending。

## Limitations and Open Questions

- E2源内频率/数值差异必须回原始引用解决；本页既不擅改原文，也不把多来源差异视作重复独立证据。
- Table 5为历史综述概览，不能支持“当前国际领先”或组内落后百分比。
- 原文个别单位/化学式有疑点（如§2.10导热率单位、§4.1氧化铝式），本轮不据此录入导热数值或化学计量结论。
- 没有逐幅检查全部图、补充资料和被引全文；页面保留draft。

## Downstream Review

- 新建与相关组内论文及另一篇综述的限定链接；未改动已有组内证据或综合矩阵。
- 后续涉及数值排名、阈值或高温验证时，应先处理E2、E5、E6；不把综述中的历史数据不足当成已确认领域gap。
