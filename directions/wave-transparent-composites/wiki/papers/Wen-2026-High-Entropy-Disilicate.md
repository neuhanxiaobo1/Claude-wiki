---
direction_id: wave-transparent-composites
type: paper
title: Data-Driven Discovery of Composition–Structure–Property Relationship in Novel
  Wave-Transparent High-Entropy Rare Earth Disilicate
year: 2026
authors:
- Shuping Wen
- Zhilin Tian
- Yuhong Du
- Lin Chi
- Zhilin Chen
- Liya Zheng
- Bin Li
venue: Research
status: processed
review_status: draft
created: '2026-09-17'
updated: '2026-09-17'
source: D:\shuju\zotero1\llm-for-zotero-mineru\10070\full.md
source_version: 英文主附件的MinerU解析；MD哈希见sources.json
zotero_collection: BSQRX4DM
zotero_item_key: 534JVRMI
zotero_attachment_key: MMDH3DHB
pdf_attachment_name: Wen 等 - 2026 - Data-Driven Discovery of Composition–Structure–Property
  Relationship in Novel Wave-Transparent High-.pdf
doi: 10.34133/research.1308
tags:
- paper
---

# Data-Driven Discovery of Composition–Structure–Property Relationship in Novel Wave-Transparent High-Entropy Rare Earth Disilicate

## Metadata and Sources

主来源：`D:\shuju\zotero1\llm-for-zotero-mineru\10070\full.md`。英文主附件`MMDH3DHB`，用缓存`_llm_source.json`的parentItemKey/attachmentKey核对身份。

原PDF：`C:\Users\youthcookie\OneDrive\1.Science\1.Zotero\pdf2\2026-(Research)\Wen 等 - 2026 - Data-Driven Discovery of Composition–Structure–Property Relationship in Novel Wave-Transparent High-.pdf`（14页）。原件、译文及缓存只读；译文不作为独立证据。映射与读取时MD哈希见[sources.json](../../docs/ingestion-2026-09-17/sources.json)。

## Reading and Verification Status

- Processing mode: new-ingestion。
- Sections read: 摘要、引言、全部Results、Conclusion、Methods（制备、表征、DFT、机器学习）、数据声明和SI目录；参考文献仅作索引。
- Figures/tables rechecked: 原PDF页序7、9：Fig.4–5，含损耗纵轴、组成图例及温度轴。 页码均指PDF页序；其余完成Markdown正文/图注阅读，不声称全部图像均复核。
- Supplement/video status: 未读取独立SI或视频；附件名称不能证明SI不存在。影响见下方E#及局限。
- review_status: draft。主体阅读入库完成，局部PDF核查不升级为整页checked。

## Research Problem and Contribution

结合66组粉体相组成、24组块体性能及机器学习筛选Sc参与的高熵RE2Si2O7。模型关联、第一性原理解释与外部泛化验证的强度需分开。

Novelty status: not assessed。未做领域优先性检索，作者首次性宣称不作为独立确认。

## Study Design

| Element | Details | Source |
|---|---|---|
| 对象、条件、测试与模型 | RE=Sc/Gd/Tb/Dy/Ho/Er/Tm/Yb/Lu；66种五组元等摩尔粉体，24组β/γ块体，另设计5–9组元各一组。额外2%SiO2，1700 °C粉体3 h，1600 °C块体20 h。室温12–18 GHz波导；激光闪射α、Neumann–Kopp Cp及密度求κ。SQS 5×1×1、PBE/PAW、520 eV、k间距0.3 Å⁻¹。模型LOOCV、min–max缩放与相关筛选；是否全部在折内执行未明。 | 主文方法及结果节 |
| 对照及独立性 | 下列E#区分本文测量、计算、作者解释及转引；同源图表不计作独立验证。 | E#定位 |
| 误差与重复 | ±按原文保留；未核明的误差类型、独立制备批次与显著性不补造。明确重复见上行。 | 主文方法/图表 |

## Key Evidence

### E1

Evidence label: 相组成分类不是通用相图

- Evidence type: 实验XRD＋机器学习。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: 66组中48单相、18多相；GBDT报告准确率96.97%，减至1–2描述符后98.48%。平均离子半径<0.8864 Å偏β，0.8864–0.8916 Å为β+γ，0.8916–0.9040 Å偏γ，更高出现γ+δ。
- Source locator: Results相图节、Fig.2、Methods机器学习。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 为当前元素、等摩尔配比与烧结条件的经验边界，不是无温度/动力学条件的普适平衡相图。选择模型与特征后仍使用同组LOOCV可能带选择乐观性，是否嵌套验证待代码核查；不能断言已经泄漏。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E2

Evidence label: Sc关联低介电常数，损耗不等于全小于0.01

- Evidence type: 直接测量与关联模型。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: (Ho/Tm/Yb/Lu/Sc)等摩尔样品ε约5.4，(Ho/Er/Yb/Lu/Sc)约5.0（结论定位15 GHz）；24组室温12–18 GHz ε<9。Fig.4B损耗分布含明显高于0.01的数据，正文只称10⁻²量级。Elastic Net在比较模型中RMSE最低。
- Source locator: Fig.4、介电结果，PDF页序7。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 不能把最低ε=5.0错配给综合最优的Ho/Tm配方，也不能把“10⁻²量级”写成所有样品tanδ<0.01。Sc存在、平均半径与相结构协变，单一重要性不证明因果。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E3

Evidence label: 低导热率的温度与估算

- Evidence type: 测量输入＋Cp计算；Clarke模型另列。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: (Ho/Tm/Yb/Lu/Sc)2Si2O7在1273 K的κ约1.3 W·m⁻¹·K⁻¹；Clarke理论最小值约1.25，为不同性质的估算。图5温度轴从373 K起，正文写323 K处范围2.0–5.1，低温起点存在原文差异。
- Source locator: Fig.5、Methods Eq.2–3，PDF页序9。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 1.3不是室温值；不把Clarke值当测量。低温323/373 K待核原始数据，当前仅引用无冲突的1273 K结果。Cp为Neumann–Kopp计算，误差和孔隙影响未独立定量。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E4

Evidence label: 机制与泛化证据未完整开放核查

- Evidence type: DFT及作者解释；SI依赖。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: 作者以CDD/ELF解释Sc降低极化，以质量涨落/畸变解释散射增强；另5个5–9组元配方的预测/实验比较仅在Fig.S16。数据声明为向通讯作者合理索取。
- Source locator: Fig.4G–I、Fig.5G–I、SI Fig.S15–S16和Tables S1–S8；Data Availability。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 电荷转移增强不单独证明共价性增加或给出介电响应分量；平均半径相关不等于唯一控制因素。未读S16、未取得数据/代码，不能独立确认泛化误差、折内预处理或全面复现模型。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

## Conclusions for Reuse

### Finding 1

- Finding / safe wording: 可复用Sc参与配方的室温介电和1273 K导热联合筛选结果（E2–E3），必须分清两个不同最低ε配方。相边界为条件性经验规律（E1）；强泛化与完整机制判断待SI和数据核查（E4）。
- Evidence: [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E1|E1]], [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E2|E2]], [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E3|E3]], [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate#E4|E4]]。
- Support: partial；支持上述限定结果，不支持未测工况、完全因果解释或跨方法无条件排名。
- Author interpretation / this reading: 作者解释在E#中标注；本页限制性判断为AI证据评价，不是新增实验。
- Decision: narrow；保留有定位的结果，对冲突及未读SI依赖项保持pending。

## Limitations and Open Questions

SI含28幅图、8张表，本轮未读取；影响泛化、全24组分数据、硬度/热膨胀雷达排名及拉曼机制核查。热学低温轴冲突与预处理流程未明，整页保持draft。Zotero日期2026-01-01与原文Published 1 June 2026不同：本文采用原文2026-06-01，未修改Zotero元数据。

未做领域系统检索，不将本文未测事项自动认定为领域空白。

## Downstream Review

本方向首次建立该论文页，入库前无已有本方向论断/综述依赖；未修改其他方向。已更新方向索引与导入清单，未决结果不作为确定下游依据。

相关阅读仅表示明确材料/方法比较关系，不表示条件相同或可直接排名：

- [[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7|稀土锡酸盐：理论与实验筛选]]
- [[directions/wave-transparent-composites/wiki/papers/Liu-2024-Entropy-ZrP2O7|中熵焦磷酸盐：相变抑制]]
- [[directions/wave-transparent-composites/wiki/papers/Tian-2025-RETaO4-CMAS|层合法RETaO4抗CMAS筛选]]
