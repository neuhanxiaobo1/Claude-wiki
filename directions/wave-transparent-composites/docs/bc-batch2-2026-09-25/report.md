---
direction_id: wave-transparent-composites
status: completed
review_status: draft
created: 2026-09-25
updated: 2026-09-25
---

# 第二批五篇入库与方向结构完善

已完成用户授权的五篇顺序入库、三个综合单元及规则/目录实际接入；没有修改公共规则、其他方向、Zotero或外部原件。本报告是交付快照，后续事实维护只在[正式工作簿](../../synthesis/review_BC/BC_review_evidence.xlsx)。

## 选择依据与来源

2026-09-25通过本机HTTP Zotero MCP实时只读核对PI5UBPW7：libraryID=1，父BSQRX4DM，版本127469，路径“3.毕设→组内文章→博士→田老师→透波复合材料→1.透波文献”；88个直接成员，无子集合，offset=88返回空。重新查看88篇题名，定向比较8篇候选摘要；未对88篇全文做系统筛查。

优先补当前B的热后结构—介电联系及C的孔/界面变量对照。五篇DOI互异，不与已有27页或首批Excel重合；已核英文主PDF、MinerU身份映射及核心图表。清单编号11—15续接原1—10，Paper_ID是另一编号体系。

| 清单/Paper_ID | 文献及DOI | B/C用途与推荐理由 | 新增证据/待核 |
|---|---|---|---|
| 11 / P0006 | Zhou et al., 2020. Effects of heat treatment on mechanical and dielectric properties of 3D Si3N4f/BN/Si3N4 composites by CVI；10.1016/j.jeurceramsoc.2020.06.018 | B Core / C Core；连续纤维复合体热后界面/孔及介电的条件系列 | 5条EV000023—027；1条Needs_Check |
| 12 / P0007 | Song et al., 2019. Microstructure and dielectric property evolution of self-healing PDC-SiBCN in static air；10.1016/j.jallcom.2019.07.296 | B Context / C Context；氧化玻璃层与介电的基体化学参照，不能冒充纤维复合体 | 4条EV000028—031；2条Needs_Check |
| 13 / P0008 | Li et al., 2022. Evolution of microstructure and properties of Si3N4 whisker reinforced composites during densification by polymer infiltration and pyrolysis；10.1016/j.jeurceramsoc.2021.12.037 | B Context / C Core；填充、密度梯度及介电关系 | 4条EV000032—035；1条Needs_Check |
| 14 / P0009 | Wang et al., 2013. Effect of BN content on microstructures, mechanical and dielectric properties of porous BN/Si3N4 composite ceramics prepared by gel casting；10.1016/j.ceramint.2012.11.005 | B Context / C Core；组分、孔隙和相比例共变，检验过强的单因素解释 | 4条EV000036—039；1条Needs_Check |
| 15 / P0010 | Ye et al., 2024. Design and preparation of sandwich structured Si3N4 ceramics for broadband microwave transmission；10.1016/j.ceramint.2024.01.149 | B Core / C Core；晶须复合芯—致密壳设计、热后变化及宏观传输边界 | 6条EV000040—045；4条Needs_Check |

未选入不等于排除：FDXFTASF（BNf/SiBN抗氧化）摘要未提供热后介电对应；VQX2UVLY（BNf/Si3N4）有温度介电但变量对照较弱；5ZDJ4A4R（预氧化多孔Si3N4）作为单相参照暂后置，避免由参照材料主导题目。本批选择不是全领域排名。激光、树脂、器件条目未作本轮核心入库，也未自动移除。

来源版本见[sources.json](sources.json)。生成清单见[[directions/wave-transparent-composites/raw/zotero_imports/literature-PI5UBPW7/import_plan]]及同目录manifest（2026-09-25-v3）。MCP快照和复核图在本方向raw，仅本地留存；发布资料不复制附件临时下载链接。

## 实际阅读与缺失材料

五篇均读主MD的摘要、研究问题、方法、主要结果/讨论及结论，回查支撑EV的PDF正文、公式和图表。引言转引不视作已读原文。

| Paper_ID | 主PDF页数 | 核心视觉核查 | 未覆盖范围 |
|---|---:|---|---|
| P0006 | 11 | Fig.6—10及Table3；Table1原PDF文本核对 | 未重算残余应力模型；其他力学图仅正文覆盖 |
| P0007 | 9 | Fig.2、7、10；关键方法与结论原PDF | 其他XPS/Raman按正文/表读取，未重新拟合谱 |
| P0008 | 11 | Fig.5—7、11—12 | 致密化模型已读假设/公式，未复算拟合 |
| P0009 | 7 | Fig.4、7及Table1—3 | 热震为模型输出，未独立复算全部输入 |
| P0010 | 8 | Fig.4—12及Table1 | Fig.1只读正文/图注，未复现CST；SI推导未取得 |

五篇主PDF均可打开，未发现重复或缺主PDF。集合每篇仅列一个主PDF；独立SI未取得/未读，不据此判断不存在。P0010的SI影响宽频曲线来源和模型复现，需要按DOI经出版平台或机构权限补取，核层厚、入射/极化、输入温频和生成方式后再讨论传输验证。补全文本前不把该曲线确认为实测或已复现模拟。

## 新资料对综述的影响

B补入了热处理/氧化后结构与介电的同条件系列（核心P0006、P0010；P0007作基体参照），不宜继续说“完全没有对应资料”。但同试样/同批关系未确认，原位、恢复及长期介电稳定证据未由本批建立。新SYN-B-002限定这些层级，不外推为因果闭环。

C的孔结构关联比界面极化归因更集中。P0008与P0010提供填充和空间结构变化，但工艺气氛、组成、含碳/含水可能性及样品对应仍限制归因；P0009展示组分/孔/相共变。新SYN-C-003组织差异；SYN-C-004区分材料介电、解析指标和宏观透射用途。多篇并列不自动构成独立验证，部分作者团队重合也需检查数据来源。

章节功能、证据ID和保留/合并/收窄建议已写入[[directions/wave-transparent-composites/synthesis/review_BC/BC_synthesis_notes]]。B/C继续并行，没有按Core数量最终定题；未做全领域同题综述检索，不能声称已确认新颖性。

## 关键未决

具体数值只在EV维护，补核动作见[[directions/wave-transparent-composites/synthesis/review_BC/source_check_log]]。

- Q11：P0007结果段和结论的损耗量冲突，Partial隔离，不擅自勘误。
- Q14：P0009方法与结果频段不同，暂停跨文定量比较。
- Q15—17：P0010介电基线、宽频曲线来源/SI、强度图文/保持率问题；不同系列分开，未知来源隔离。
- Q10/Q12/Q13：批次、测量温度或图间样品对应不足；保留同条件关联，不升级同试样因果。

## 已落地的目录与规则改进

原有执行规程和领域判断混在一起，脚本/schema占据综述工作区；来源校验固定首批五篇，不能覆盖新增论文。本次按实际问题调整：

1. `AGENTS → workflow → evidence-contract/schema`分清任务路由、执行门槛、领域推理及字段结构，不再另建四份重复规则。
2. 综述工作区只保留工作簿、章节入口、复核行动三个主文件；两脚本移到`scripts/review_bc/`，schema移到`rules/`。原件和旧paper不移动。
3. 新增Source_Manifest一列，逐篇覆盖来源校验；Unclassified-report隔离来源未明的作者报告，不让强制分类制造伪证据。
4. 用现有字段区分同条件、同批、同试样和因果层级；不新增B/C双份数据或逐篇重复摘要。
5. 章节表引用SYN/EV并按证据决定保留、合并、收窄；写作沿用两篇指定参照的有效原则及既有阅读边界。

目录与规则职责见[[directions/wave-transparent-composites/docs/directory-guide]]；[迁移记录](migration.json)。历史验收保留原时点路径，当前Markdown链接已修复。旧27页/108个E#未改写，首批EV及核查状态未因格式变化升级。

## 验收和完成边界

正式库10篇、45条EV、6个SYN；本批新增23条（18条限定范围Checked、5条Partial）。全库39 Checked、6 Partial、16条Needs_Check；观察32、作者解释10、模型2、来源未分类1。Direct指该行断言的直接观察，不是32项因果证明。SYN为5 Provisional、1 Ready，唯一Ready仍限既有用途边界。

身份并集32篇：旧27页与Excel前5篇重合，再加5篇新文献。原始研究22篇（7篇既有组内、15篇外部），另9篇综述/方法参考和1篇非核心候选；不是88成员全部入库。多孔/块体参照与核心独立计数。

验收产物：[工作簿校验](workbook-validation.json)、[契约负例检查](contract-checks.json)、[结构检查](structure-validation.json)、[交付核验](delivery-validation.json)。自动检查验证字段/来源/引用及迁移保留，不替代科学判断；未决保留其限制。

本轮未提交/上传；上一发布为calude_wiki_3.9.9（1701cd3）。外部原件、候选xlsx和被忽略raw不属于Git备份。
