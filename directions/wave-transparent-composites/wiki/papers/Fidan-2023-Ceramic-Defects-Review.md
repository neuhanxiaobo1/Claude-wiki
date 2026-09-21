---
direction_id: wave-transparent-composites
type: paper
title: A survey on ceramic radome failure types and the importance of defect determination
year: 2023
authors:
- Şeyma Saliha Fidan
- Rahmi Ünal
venue: Engineering Failure Analysis
status: processed
review_status: draft
created: '2026-09-20'
updated: '2026-09-20'
source: C:\Users\youthcookie\OneDrive\1.Science\1.Zotero\pdf2\2023-(Eng. Fail. Anal.)\Ünal
  - 2023 - A survey on ceramic radome failure types and the importance of defect determination.pdf
source_version: 期刊正式PDF及对应MinerU缓存；原始参考文献未逐篇核查
zotero_collection: GS7STC5N
zotero_item_key: BPIRLTYT
zotero_attachment_key: ERYB97WH
pdf_attachment_name: Ünal - 2023 - A survey on ceramic radome failure types and the
  importance of defect determination.pdf
doi: 10.1016/j.engfailanal.2023.107234
tags:
- paper
- review
---

# A survey on ceramic radome failure types and the importance of defect determination

## Metadata and Sources

- 主附件：`ERYB97WH`；PDF路径见元数据。
- MinerU：`D:\shuju\zotero1\llm-for-zotero-mineru\12614\full.md`；已先核对manifest与_llm_source中的父条目/附件映射。
- 本轮只读原件，未复制原PDF、修改缓存或Zotero；译文不作为独立证据。

## Reading and Verification Status

- new-ingestion；清单6号，第5篇；定位为陶瓷缺陷与通用测试方法参考。
- 已核31页正式英文PDF及MD；原文首页作者为Şeyma Saliha Fidan、Rahmi Ünal，知识库按原文补全，不按附件“Ünal”命名推定作者完整性。
- 已读摘要、引言、材料背景、机械性质与Weibull方法及限制、亚表面损伤形成/检测、方法比较、Discussion and challenges、Conclusions；PDF第23页表2回查文本。没有完整精读装备载荷与专用试验系统章节，不记录其设计/运行参数。
- 图像未逐一视觉核对，参考文献未逐篇阅读；本页以材料级方法总结为限，保持draft。

## Research Problem and Contribution

讨论陶瓷缺陷、加工亚表面损伤、强度离散与检测方法之间的关系。作者综述包含专用结构与试验系统；本方向只复用通用陶瓷材料可靠性和表征边界，不把本文视为新材料性能实测。

## Study Design

| 要素 | 内容 | 定位 |
|---|---|---|
| 材料与缺陷 | 脆性陶瓷/玻璃陶瓷；表面、亚表面及体缺陷 | 机械性质及SSD章节 |
| 变量 | 样品尺寸、缺陷群体、加工历史、测试应力场 | Weibull及限制章节 |
| 表征 | 截面、抛光/腐蚀、TEM、OCT、激光散射、SAM、XCT | 检测章节、表2 |
| 比较性质 | 多文献定性综述，无统一样品下的检测准确率比较 | 表2、Discussion |

## Key Evidence

### E1

- 类型：综述转引与作者解释。
- 结果：陶瓷强度存在离散性与尺寸/缺陷效应，小试样的抗弯结果不能无条件代替大体积或不同加载形式下的性能。
- 定位：Determination of mechanical properties、Application of the Weibull method。
- 核查/边界：主体已读，支持记录尺寸、表面加工、加载方式和缺陷来源；不把“大尺寸必然按某固定比例变弱”当普遍定量规律。

### E2

- 类型：综述转引/统计模型适用性讨论。
- 结果：Weibull模型的适用性需检查缺陷分布、应力梯度、R曲线行为与样本量，不能默认优于其他统计分布；断口证据可帮助验证缺陷类型。
- 定位：Constraints of the Weibull method、Application of the Weibull method结尾及Finite element analysis of Weibull analysis。
- 独立性/核查：原始拟合数据与模型代码未核，本轮仅概念层阅读；不采用MD中疑似符号问题的公式或固定样本数作为通用标准。

### E3

- 类型：转引方法比较。
- 结果：破坏性截面/抛光观察通常局限于局部且制样可能引入损伤；OCT、激光散射、SAM和XCT的适用性受表面状态、材料响应、分辨率、检测范围及成本限制。
- 定位：Subsurface damage formation mechanism至Comparison and the challenges for defect determination；PDF第23页表2。
- 核查/边界：对应正文与原PDF表2文本已核；没有同条件检测概率/误报率数据，不将某方法“更精确”泛化到所有陶瓷，也不将空间分辨率等同最小可靠检出缺陷尺寸。

## Conclusions for Reuse

- Finding 1：性能数据集应同时保留试样尺寸、加工状态、加载方式及统计范围（E1—E2，概念层支持充分）。
- Finding 2：选择缺陷表征需匹配目标缺陷与样品，而非只比较仪器标称分辨率；结合局部截面与无损检测是AI提出的可验证方法连接，具体资源待确认（E3，限定保留）。
- Finding 3：本页归通用测试/可靠性参考，不提供新透波材料的独立性能证据。

## Limitations and Open Questions

未完整精读专用装备章节，不宣称全文全要素复核。未核原始统计数据，无法确定具体材料的分布参数、置信区间或工程寿命。原文标准编号仅为历史引用，现行版本未检索，不给出标准合规结论。

## Downstream Review

可为[[directions/wave-transparent-composites/wiki/papers/Wen-2026-Laminated-SiO2f-SiO2]]的μCT/DIC与力学证据提供缺陷/尺度解释框架，不据此补造原文未报告的重复数或可靠性结论。
