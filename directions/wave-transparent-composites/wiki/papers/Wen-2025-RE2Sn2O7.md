---
direction_id: wave-transparent-composites
type: paper
title: 'Rare earth stannates: A new high-performance wave-transparent material investigated
  through theoretical and experimental approaches'
year: 2025
authors:
- Shuping Wen
- Zhilin Chen
- Zhilin Tian
- Liya Zheng
- Bin Li
venue: Materials Today Physics
status: processed
review_status: draft
created: '2026-09-17'
updated: '2026-09-18'
source: D:\shuju\zotero1\llm-for-zotero-mineru\10147\full.md
source_version: 英文主附件的MinerU解析；MD哈希见sources.json
zotero_collection: BSQRX4DM
zotero_item_key: QXLQJ5J8
zotero_attachment_key: Q5AW7YYW
pdf_attachment_name: Wen 等 - 2025 - Rare earth stannates A new high-performance wave-transparent
  material investigated through theoreti.pdf
doi: 10.1016/j.mtphys.2024.101622
tags:
- paper
---

# Rare earth stannates: A new high-performance wave-transparent material investigated through theoretical and experimental approaches

## Metadata and Sources

主来源：`D:\shuju\zotero1\llm-for-zotero-mineru\10147\full.md`。英文主附件`Q5AW7YYW`，用缓存`_llm_source.json`的parentItemKey/attachmentKey核对身份。

原PDF：`C:\Users\youthcookie\OneDrive\1.Science\1.Zotero\pdf2\2025-(Materials Today Physics)\Wen 等 - 2025 - Rare earth stannates A new high-performance wave-transparent material investigated through theoreti.pdf`（13页）。原件、译文及缓存只读；译文不作为独立证据。映射与读取时MD哈希见[sources.json](../../docs/ingestion-2026-09-17/sources.json)。

## Reading and Verification Status

- Processing mode: new-ingestion。
- Sections read: 摘要、引言、方法、结果讨论各节及结论；主文图表说明和模型公式已读，SI未读。
- Figures/tables rechecked: 原PDF页序7–8：Fig.8、Table 3及热学结果相邻正文。 页码均指PDF页序；其余完成Markdown正文/图注阅读，不声称全部图像均复核。
- Supplement/video status: 未读取独立SI或视频；附件名称不能证明SI不存在。影响见下方E#及局限。
- review_status: draft。主体阅读入库完成，局部PDF核查不升级为整页checked。

## Research Problem and Contribution

以九种稀土锡酸盐比较介电、弹性和热学性质；将第一性原理与烧结样品测量结合。理论组成趋势与实测离散必须分开。

Novelty status: not assessed。未做领域优先性检索，作者首次性宣称不作为独立确认。

## Study Design

| Element | Details | Source |
|---|---|---|
| 对象、条件、测试与模型 | La/Nd/Sm/Eu/Gd/Tb/Dy/Er/Lu的RE2Sn2O7；1500 °C粉体8 h、1600 °C块体20 h；196点纳米压痕。室温9.6/14.4 GHz介电；激光闪射热扩散率、Neumann–Kopp估算Cp及密度求导热率，并进行孔隙修正。DFT使用PBE、600 eV；Markdown k网格识别异常，不作为可运行输入。 | 主文方法及结果节 |
| 对照及独立性 | 下列E#区分本文测量、计算、作者解释及转引；同源图表不计作独立验证。 | E#定位 |
| 误差与重复 | ±按原文保留；未核明的误差类型、独立制备批次与显著性不补造。明确重复见上行。 | 主文方法/图表 |

## Key Evidence

### E1

Evidence label: 室温低损耗候选

- Evidence type: 直接测量。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: 介电常数约7–9；La在14.4 GHz为7.62、Gd在9.6 GHz为8.78；9.6 GHz下Er tanδ约0.001，La约0.009。
- Source locator: Sec.3.3、Fig.8，PDF页序7。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 支持室温GHz介电候选筛选，不证明高温介电稳定；整体趋势不应替代逐组成数据，Tb等存在非单调变化。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E2

Evidence label: 理论与实测弹性不同

- Evidence type: 计算模型与直接测量。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: 理论E从La的199.2至Lu的240.5 GPa增加；实验报告La224.9±10.5、Gd245.3±13.6、Tb226.0±30.7、Dy218.0±17.2、Er214.1±25.7、Lu238.6±10.9 GPa。
- Source locator: Sec.3.4、Table 3，PDF页序8。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 实验不是严格单调；作者用约化模量近似杨氏模量，应保留该近似。纳米压痕不能代替宏观抗弯强度，表面不平的解释没有独立控制验证。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E3

Evidence label: 导热率的求得方式与温度

- Evidence type: 测量输入＋模型估算。
- Object and conditions: 见Study Design及本条条件。
- Metric and result: 200 °C时Er约2.60、Nd约5.79 W·m⁻¹·K⁻¹；1000 °C时Eu约1.85、Nd约4.28 W·m⁻¹·K⁻¹。κ由热扩散率、计算Cp、密度求得，孔隙率约0.84%–6.07%，文中采用κ/κ0=1−4φ/3修正。
- Source locator: Sec.3.5；导热率公式与热学图。
- Original data source / independence: 本文主文对应数据；转引或模型已单独说明，不算额外独立实验。
- Supports / does not establish: 可在注明温度、Cp及孔隙修正前提下引用；理论最小导热率约1.12–1.19不是实测值。高温辐射贡献使简单1/T模型不能覆盖所有温度。
- Verification status: 主体Markdown已读；已列页序对应图表回查PDF，其余不超出文本核查。冲突与未决保留于本条。

### E4

Evidence label: 锡酸盐热膨胀系数

- Evidence type: 本文膨胀测量的线性拟合。
- Object and result: La/Er热膨胀系数分别8.62/9.24×10⁻⁶ K⁻¹；图示测量温区约373–1273 K，精确拟合窗口未另列。
- Source locator: 原PDF页序11 Fig.14、页序12正文，2026-09-18补充局部核查。
- Supports / boundary: 仅描述本文陶瓷，不作为复合材料CTE，也不据不同温区结果计算定量差距；整页状态不升级。

## Conclusions for Reuse

### Finding 1

- Finding / safe wording: 室温低损耗与高温低导热为不同测试得到的互补性质（E1、E3）；不能合并为“高温低损耗已验证”。理论模量的单调趋势不适用于实测数据（E2）。
- Evidence: [[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7#E1|E1]], [[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7#E2|E2]], [[directions/wave-transparent-composites/wiki/papers/Wen-2025-RE2Sn2O7#E3|E3]]。
- Support: partial；支持上述限定结果，不支持未测工况、完全因果解释或跨方法无条件排名。
- Author interpretation / this reading: 作者解释在E#中标注；本页限制性判断为AI证据评价，不是新增实验。
- Decision: narrow；保留有定位的结果，对冲突及未读SI依赖项保持pending。

## Limitations and Open Questions

SI的键长、拟合及模型参数表未读；尚不足以复现DFT或严密核查全部声子机制。作者归因于键合、非谐性及散射；本页仅保留为解释，不宣称隔离验证。

未做领域系统检索，不将本文未测事项自动认定为领域空白。

## Downstream Review

本方向首次建立该论文页，入库前无已有本方向论断/综述依赖；未修改其他方向。已更新方向索引与导入清单，未决结果不作为确定下游依据。

相关阅读仅表示明确材料/方法比较关系，不表示条件相同或可直接排名：

- [[directions/wave-transparent-composites/wiki/papers/Du-2024-RE2SiO5|稀土单硅酸盐：力学与介电]]
- [[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate|高熵二硅酸盐：高通量与机器学习]]
