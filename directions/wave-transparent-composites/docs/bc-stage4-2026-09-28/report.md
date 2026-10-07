---
direction_id: wave-transparent-composites
status: completed-with-limitations
created: 2026-09-28
updated: 2026-09-28
---

# 7篇筛选、3篇定向复核与下一批补充文献

本阶段按用户“按照计划开始下一步工作”执行：筛选剩余7篇已有原始研究，选择能改变B/C证据组织的3篇复核，再判断需要补什么外部资料。结果已写入[唯一BC工作簿](../../synthesis/review_BC/BC_review_evidence.xlsx)，没有新增重复论文身份或长篇单文摘要。

## 七篇筛选结论

筛选以原主MD的问题、摘要/结论和章节覆盖为依据；前三篇进一步读必要方法、结果/讨论并回查关键PDF。后四篇本轮只做主题/用途筛查，没有重新核查全部图表、数值或SI。[七篇身份和原件哈希](screening-sources.json)保存S1—S7；[正式BC来源](sources.json)仅收录本轮三篇，避免把筛过的论文冒充已完成证据复核。

| 原有论文 | 对当前缺口的实际贡献 | 本轮决定 |
|---|---|---|
| Li 2017：BN/SiO₂热震与性能 | BN含量/取向/相对密度共变、混合律与热震后表层；可以检验“热震力学是否等于介电稳定”的边界 | P0016；B Context / C Core；6条EV000070—075 |
| Wen 2026：层合穿刺SiO₂f/SiO₂ | CT区分孔/裂纹，短时烧蚀后结构与制备态介电分开；补C4的结构量定义 | P0017；B Context / C Core；3条EV000076—078 |
| Chen 2026：混编纤维/BN | 局部TEM及push-in换算界面强度较具体；介电对照和弛豫公式可用于审视机制证据 | P0018；B Context / C Core；6条EV000079—084 |
| Du 2024：RE₂SiO₅ | 稀土组分与本征/块体介电参照，不是当前所缺的复合体热循环或界面单变量实验 | 保留旧页，暂缓迁移；以后B需要基体高温参照时再定向核查 |
| Wen 2025：RE₂Sn₂O₇ | 理论/实验材料筛选，主要提供组成及性能背景 | 保留旧页，暂缓迁移；不扩写成无关材料性能百科 |
| Liu 2024：中熵焦磷酸盐 | 固溶/缺陷与相变抑制可作B3.1参照，但不能直接代替陶瓷复合界面或循环恢复 | 保留为四篇中优先的B背景候选；未因含晶界相就静默升为核心复合体 |
| Wen 2026：高熵二硅酸盐 | 组成—相—性质、机器学习与验证方法参考 | 保留旧页，暂缓迁移；当前不增加机器学习专章，不把特征关联当界面因果 |

暂缓意味着暂不为本轮缺口重复精读，不是从文献库删除，也不是论文不适合透波方向。三个Core表示用途相关，不表示机制已核实；三篇均未补出可直接使用的热循环后介电恢复序列。

## 实际阅读与改动

| BC编号 | 本轮覆盖 | 留下的关键限制 |
|---|---|---|
| P0016 | 主MD研究问题、方法、§3.1—3.4、结论；PDF p3 Table 1/2、p6 Fig.4/5/式5、p7 Fig.6/7、p9 Fig.10 | ε正文/图不符；水淬完整协议不足；Fig.7正文1000℃而图注900℃；混合律没有逐样独立预测/误差验证 |
| P0017 | 主MD研究问题、方法、§3.1—3.4、结论；PDF p2方法、p3 Fig.3—5、p6 Fig.8/9、p7 Fig.10/11 | CT分辨率/阈值和全尺度孔隙不能混同；介电测温NR；无烧蚀后介电；DIC未逐帧重算 |
| P0018 | 主MD问题、制备/表征、界面及介电结果/讨论/结论；热学模型仅作上下文阅读；PDF p3方法、p7 Fig.4、p8 Fig.5、p9 Fig.6、p11式20—24、p12 Fig.7 | push-in界面强度是模型换算；介电测温NR；电学公式单位约定、实际多相输入和电阻率方法待核；雷达代表频率未明 |

未读独立SI/转引原文，未把热导或力学完整搬入BC。主PDF均可读，外部PDF、缓存及Zotero未修改。本轮来源哈希与原有MD映射核对一致。

两篇组内旧页把“没有说明测试温度的介电测量”标成室温，本次回查方法后撤回该标签，写为NR；同时修正[组内比较矩阵](../../synthesis/group-baseline-and-benchmarks-2026-09-18.md)两行及其依赖句。真实室温热导数据不随之删除。Li论文新发现的Fig.7温度冲突紧邻相关结构判断记录。其他已有关系链接不因此改写。

## 对B/C的实际影响

新增SYN-C-006，扩展SYN-C-005与SYN-B-003；原69条EV和原15篇Paper_Index的单元格保持不变。章节动作见[BC_synthesis_notes](../../synthesis/review_BC/BC_synthesis_notes.md)。

- **B仍需优先补热历程与介电的对应**：热震残余强度、烧蚀后形貌和热膨胀曲线各有价值，但不能填入“介电恢复/寿命”空格。本轮没有依据升级B的长期或可逆稳定结论。
- **C的组内基础更具体，但强机制仍不足**：局部界面表征、模型换算强度和制备态低损耗可以并列；仍缺等组分/等孔隙的界面控制及匹配温频的电学验证。公式被引用不等于模型已经验证。
- **目录不扩张**：C3保留机械界面证据与电学归因两层；C4区分相对密度、开孔、CT裂纹/孔和总孔隙；C5增加“输入—预测—验证”比较。继续并行评价，不因C Core数量增加而替用户决定最终主线。

## 需要补什么文献

本轮做了有限公开网页检索，未运行Scopus、未作系统检索或领域新颖性判断。候选只依据出版方可见摘要/章节片段，尚未入BC；全文获取及温度协议、对照设计必须另核。

| 优先级/候选 | 为什么需要 | 下一次准入检查 |
|---|---|---|
| 优先1：[Performance Optimization of SiO₂f/SiO₂ Composites Derived from Polysiloxane Ceramic Precursors，2025](https://doi.org/10.3390/molecules30061385) | 双层界面与不同温度处理的介电线索，可同时检验C的界面/残碳混杂和B的状态分类。9月21日集合快照已有SHMYTXHH、附件BGLYEFBA，无须新建重复Zotero条目 | 先读现有PDF：温度是制备还是服役暴露？是否真正有界面控制系列及介电对照？出版片段不能证明存在循环恢复 |
| 优先2：[Microstructure, mechanical and high-temperature dielectric properties of zirconia-reinforced fused silica ceramics，2016](https://www.sciencedirect.com/science/article/abs/pii/S0272884216000948) | 颗粒增强熔融石英、高温介电与组成对照的候选，可扩大B的代表性 | 主文能否匹配结构变化和介电温度？检索页引言中的循环耐受描述是转引，不能当该文已完成介电循环实验；尚未核实时Zotero附件 |
| 条件候选：[Optimizing the mechanical properties of Si₃N₄f/Si₃N₄ composites by tailoring the BN interphase structure，2026](https://doi.org/10.1016/j.jeurceramsoc.2026.118357) | 多类BN界面可供C的控制设计参考 | 目前可见内容以力学为主，若全文无对应介电控制，只能Context/Method，优先级低于能直接补电学缺口的文献 |

另核对[Yang 2019高温性质与界面演化](https://www.sciencedirect.com/science/article/pii/S0955221918305685)：出版摘要/结论侧重高温力学与界面，不据题名把它排成介电循环核心首选。已入库的Zhou 2020、Li 2023检索命中按DOI去重，不重复推荐入库；碳纤维吸波和树脂体系不为凑数加入。

下一次Scopus可按缺口使用以下检索式（本次未运行；检索结果仍需人工判定材料、测试状态及来源）：

```text
TITLE-ABS-KEY(("wave transparent" OR "wave-transparent" OR radome) AND (ceramic* OR silica OR "silicon nitride") AND (composite* OR aerogel*) AND ("thermal cycl*" OR "thermal shock" OR "thermal aging" OR "thermal ageing" OR "heat treatment") AND (dielectric OR permittivity OR "loss tangent"))

TITLE-ABS-KEY(("wave transparent" OR "wave-transparent" OR radome) AND (ceramic* OR Si3N4 OR SiO2 OR "boron nitride") AND (interphase OR "interface coating" OR "interfacial polarization") AND (dielectric OR permittivity) AND (thickness OR control* OR conductivity OR relaxation))

TITLE-ABS-KEY((ceramic* OR "silica composite*" OR "silicon nitride composite*") AND ("effective medium" OR Lichtenecker OR "Maxwell Garnett" OR "Maxwell-Garnett") AND (dielectric OR permittivity) AND (porosity OR interface*) AND (validation OR experiment* OR anisotrop*))
```

第一式较宽，以免题名不写cycling就漏检；真正核心须在正文看到热状态和介电对应。第二式并不保证找到单变量控制。第三式用于核模型条件，不能把树脂或低频导电复合模型直接外推至微波陶瓷。[有限检索记录](search-log.md)说明实际执行的查询与访问边界。

## 状态、验收与下一步

工作簿累计18篇、84条EV、9个SYN；69 Checked、15 Partial、36条Needs_Check；59观察/18作者解释/6模型输出/1来源未分类报告；8 Provisional、1限定用途Ready。B Core 5、C Core 12、交集3。配对字段为67 Unclear、7 NA、10 Different-state，未新增可宣称Same-specimen/Matched-batch的证据；同条件系列仍可有限比较。

全方向身份并集仍32篇，旧27页/108条E#保持；Excel有13篇与旧页重合、5篇仅Excel。22篇原始研究中18篇进BC、4篇已经筛选并暂缓；不是“还有4篇尚未筛”。综述/方法9篇和非核心候选1篇未变。

校验记录：[工作簿/全部登记源哈希](workbook-validation.json)、[契约负例](contract-checks.json)、[方向结构](structure-validation.json)、[本阶段变更与保留核验](delivery-validation.json)。它们不代替原文判断。规则/schema未增加新层；本轮一次性写入脚本完成后移除。

下一阶段先核SHMYTXHH的既有PDF，并按上列门槛定向补热循环/界面受控电学或模型验证材料；不再无差别迁移四篇背景。后续再做同源性、反例和已有综述重叠检查，决定题目承诺是否应收窄。本轮未确定最终主线、未写综述正文、未提交/上传；上一发布仍为calude_wiki_4.0，9月26日未发布成果已保留。
