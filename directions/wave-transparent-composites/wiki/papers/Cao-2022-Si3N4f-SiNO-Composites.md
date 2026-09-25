---
direction_id: wave-transparent-composites
type: paper
title: Microstructure, high-temperature mechanical and dielectric properties of novel
  Si3N4 f/SiNO wave-transparent composites
year: 2022
authors:
- S. Cao
- D. Zhang
- J. Wang
- J. Zhang
- J. Zhang
- R. Yao
- Y. Yao
- Y. Zhang
venue: Journal of the European Ceramic Society
status: processed
review_status: draft
created: '2026-09-21'
updated: '2026-09-25'
source: C:\Users\youthcookie\OneDrive\1.Science\1.Zotero\pdf2\2022-(J. Eur. Ceram.
  Soc.)\Cao 等 - 2022 - Microstructure, high-temperature mechanical and dielectric
  properties of novel Si3N4 fSiNO wave-tra.pdf
source_version: 正式PDF及MinerU缓存；本次核查范围见正文
zotero_collection: PI5UBPW7
zotero_item_key: AMF2F9G9
zotero_attachment_key: 9553Q666
doi: 10.1016/j.jeurceramsoc.2022.03.055
tags:
- paper
---

# Microstructure, high-temperature mechanical and dielectric properties of novel Si3N4 f/SiNO wave-transparent composites

> 2026-09-25 B/C迁移：P0002；范围为EV000005—EV000008；旧E2/E3相关温度结构、介电及力学边界。后续BC事实维护见[正式工作簿](../../synthesis/review_BC/BC_review_evidence.xlsx)，流程见[[directions/wave-transparent-composites/rules/bc-review-workflow]]。以下保留历史阅读记录及本轮必要纠错；旧E#不变，整页仍draft，未迁移部分不自动放行。

## Metadata and Sources

- MinerU：`D:\shuju\zotero1\llm-for-zotero-mineru\12803/full.md`；manifest与_llm_source父条目/附件key已核，PDF与缓存均为10页。
- 来源哈希及映射见[[directions/wave-transparent-composites/docs/ingestion-literature-2026-09-21/report]]及其sources.json。外部原件只读，未复制、移动或修改。

## Reading and Verification Status

- new-ingestion；4号。已读摘要、引言、§2、§3.1—3.3与结论。视觉核对PDF第4页图3—5、第8页图10和第9页图11—13；其余图读正文/图注，未逐点数字化。SI与引文原始研究未读。

## Research Problem and Contribution

以连续Si3N4纤维浆料缠绕、粉体与硅溶胶形成SiNO命名基体，研究温度相关性能。基体不是未经核查即可认定的单相Si2N2O；均匀填充和经济性为作者论述，未独立核算成本。

## Study Design

- 材料密度1.83 g/cm³；氮气热处理系列800—1550℃。纤维束拉伸至少15次，复合体方法称5个试样平均。
- 介电采用高Q腔法，室温及高温谐振腔测量；频率扫描与固定频点升温分开，方法写7—18 GHz，但图12含18.8 GHz。

## Key Evidence

### E1

- 类型：室温力学测量。拉伸强度87.8 MPa、拉伸模量41.2 GPa；弯曲强度171.2 MPa、弯曲模量27.5 GPa。
- 定位§3.1、图4—5，PDF第4页已核。图4仅显示4个拉伸试样，图5有5个弯曲试样，与方法统一称5个存在数量差异；不补造第五个拉伸值，不将两种模量混用。

### E2

- 类型：热处理后力学测量。氮气中1000/1200/1550℃热处理后拉伸强度为54.6/44.5/24.2 MPa；作者以界面反应、纤维表面缺陷及晶化解释下降。
- 定位§3.2、图9—11；图10—11视觉核，数值按正文。保温时间和测试时温度的表述不充分，保守写热处理后，不写1550℃空气原位服役强度。

### E3

- 类型：高温介电测量。正文给800℃、约7.2/12.1/18.8 GHz三点ε为3.72—3.75、tanδ为1.3—1.9×10⁻³；PDF第9页图12视觉核，支持该量级。
- 图12(b)图例低频点写7.1 GHz，图注/正文写7.2 GHz；不能抹平差异。本页保留约7.1—7.2 GHz口径待核，不称连续全频段的统一范围。RT至800℃损耗先因加热而下降的解释为吸附水逸出，未独立水分控制试验。

### E4

- 类型：作者解释及转引比较。图13把强度和εtanδ组合成性能指数，含多来源陶瓷及本篇数据。
- 定位§3.3、PDF第9页；只作作者评价框架，不据此宣布全球领先或真实构件功率损耗，不把不同温频条件的点视为统一实验比较。

## Conclusions for Reuse

- Finding 1：可用于温度相关介电稳定性章节（E3，限定频点支持充分），并与热处理后力学退化分开讨论（E2）。
- Finding 2：材料名、拉伸/弯曲模量、热处理/原位测试需独立字段（E1—E2）；不能从题名高温机械性能直接推出1550℃透波与承载同时实现。

## Limitations and Open Questions

图4试样数与方法不一致、图12低频标签与文字不一致、热处理保温与力学测试温度需进一步核查。无长期空气氧化服役证据。

## Downstream Review

与[[directions/wave-transparent-composites/wiki/papers/Meng-2023-PIP-Heating-Rate-Si3N4]]的介电测试温度不同，可为综述建立温频条件字段；不直接比较绝对损耗高低。既有综合未引用本页。
