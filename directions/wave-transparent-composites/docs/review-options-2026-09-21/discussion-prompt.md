# 可直接复制给其他大模型的讨论提示词

你是一名熟悉陶瓷基复合材料、电磁介电性能与热力学评价的综述写作顾问。请帮助我选择综述主线，暂时不要直接撰写完整综述，也不要把候选方案当成已经确定的方向。

【当前目标与任务顺序】
我要写一篇“陶瓷透波复合材料”综述。此前工作是梳理组内基础、寻找新课题，现在转为综述写作。外部文献范围不应受本组现有材料或设备能力限制。目标期刊、字数、应用场景、频段和温区尚未固定；不要自行限定为航空雷达罩或全部极端工况。大模型是可选工具，不是必须写入综述的主题。
我们计划先讨论两个已有候选方案；随后由我提出第三方案；三个方案统一比较并确定主线后，再制定专项入库、阅读、记录和总结规则。不要现在替我定稿或搭建一套适用于所有主题的复杂规则。

【已有资料与可信边界】
本地知识库共27篇：7篇组内原始研究、10篇外部原始研究、9篇综述/方法参考、1篇非核心吸波候选，共108条局部证据记录。页面均为draft，部分关键数据已核原PDF，但并非全部图表、SI和转引原始研究均已检查。入库数量不等于核心语料数量，也不等于独立实验数量。
你没有自动获得这些全文。以下是已入库笔记提供的讨论依据，请明确区分“用户提供的资料概述”“你实际检索/读取的来源”和“你的推断”。不能声称已经读过未提供的原文。不要编造作者、DOI、数值、期刊推荐或领域首次性。

代表性原始研究及已知边界：
1. Chen等，2026，Synergistic enhancement of the performance of BN based wave-transparent composites by hybrid weaving of Si3N4 and SiO2 fibers，DOI 10.1016/j.compositesa.2026.109897。混编纤维/BN用于界面、强韧与介电权衡；相对文中SiO2f/SiO2对照力学改善，介电参数并非全面降低；基体和纤维同时变化，高温介电未测。
2. Wen等，2026，High-performance SiO2f/SiO2 wave-transparent composites based on laminated puncture method，DOI 10.1016/j.jeurceramsoc.2026.118181。层合穿刺、层间约束、室温介电与短时烧蚀；线烧蚀和质量烧蚀存在取舍，形貌保持不能证明烧蚀后功能保持。
3. Li等，2023，Study on the fiber/matrix interface modification of Si3N4 f/SiO2 composites with polymer derived double-layer coatings，DOI 10.1016/j.jeurceramsoc.2023.08.010。BN/SiON双层界面、同文涂层对照；密度也变化，纤维与复合体性能须区分，单纤维数据有正文/结论不一致。
4. Meng等，2023，Effects of heating rate on mechanical and dielectric properties of the Si3N4f/BN/Si3N4 composites by PIP，DOI 10.1016/j.jmrt.2022.12.175。升温速率、残碳、孔隙与界面关联室温力学/介电；最佳强度与最佳韧性不对应同一速率，没有该批样品高温服役证据。
5. Wang等，2024，Preparation of Si3N4f/Si3N4 wave-transparent composites by vat photopolymerization combined with chemical vapor infiltration，DOI 10.1016/j.addma.2024.104540。短纤维打印+CVI，韧性提升同时弯曲强度下降，韧性方法仍需补核。
6. Jing等，2025，Mechanically robust Al2O3 f/LaPO4/Al2O3 composite for high-performance microwave transparent，DOI 10.1016/j.jallcom.2024.177974。氧化物体系；最高强度、最大位移和最低孔隙率来自不同配方，透射率是计算值。
7. Cao等，2022，Microstructure, high-temperature mechanical and dielectric properties of novel Si3N4 f/SiNO wave-transparent composites，DOI 10.1016/j.jeurceramsoc.2022.03.055。氮气热处理后拉伸与高温介电测量分开；不能拼成同一1550℃服役状态。
8. Cao等，2013，High-temperature properties and associated structure evolution of continuous SiNO fiber-reinforced BN composites for wave transparency，DOI 10.1016/j.matdes.2012.07.037。温度相关力学、介电、晶化和界面演变；高温气氛及频率覆盖存在核查边界，不等于空气长期服役验证。
9. Zhang等，2023，Resilient Si3N4@SiO2 nanowire aerogels for high-temperature electromagnetic wave transparency and thermal insulation，DOI 10.26599/JAC.2023.9220813。核壳气凝胶，室温导热与高温介电、压缩恢复；不同密度数据不能拼接，不能与承载材料直接排名，SI未读。
10. Li等，2017，Effect of the BN content on the thermal shock resistance and properties of BN/SiO2 composites fabricated from mechanically alloyed SiBON powders，DOI 10.1039/c7ra09905c。组成、力学和水淬热震；最高初始强度与最佳热震为不同配比，室温介电图文上限有冲突，热震协议仍需补核。
另有多孔Si3N4、低碳SiBCN及稀土陶瓷研究可作基础参照。单相、多孔、PDC并不自动等于复合材料；这些不是核心复合体性能的替代证据。

已有综述包括Zhou 2023（Development of high-temperature wave-transparent nitride-based CFCMCs for aircraft radomes，DOI 10.1016/j.compositesa.2023.107444）、Xiang 2023（Research progress of high temperature resistant electromagnetic wave-transparent materials，DOI 10.11896/cldb.22090029）、Nag 2021（High temperature ceramic radomes (HTCR) – a review）、Kenion 2022透波材料综述等。Zhou已有纤维—界面—基体—涂层框架，Xiang涉及增强体、界面和工艺，因此不能把“讨论界面”“讨论高温”直接当作创新。树脂基综述仅作跨体系背景；失效、测试、大模型综述按用途择用，不强制引用。

【两个候选方案】
A：陶瓷透波复合材料的增强结构与界面设计：工艺—微结构—介电及力学性能权衡。
以纤维增强陶瓷基复合材料为主体，按设计变量、实际微结构变化、收益与代价组织；工艺嵌入它改变的结构中。核心问题是如何有条件地协调承载、断裂和介电响应；热环境作为边界。现有证据相对集中，风险是范围过宽及重复已有结构单元综述。
B：陶瓷透波复合材料在热环境中的性能演化：结构退化、介电响应与承载保持。
以环境历程、结构变化和性能响应组织，区分原位高温、热处理后、氧化、热震及短时烧蚀。核心问题是低损耗与承载能力在何种状态下保持；现有案例可启动，但需补强配对性能、老化、保护层和构件证据。不能据不同试验拼接统一服役极限，也不能把语料缺口说成领域空白。

【请输出】
1. 判断两个方案是否有清晰且不同的核心问题，分别给出一个经收窄的题目、研究问题和论证主线。
2. 每个方案给出5—7个候选章节，注明每章回答的问题、可用资料、关键缺口和拟用图表；不只按论文逐篇罗列。
3. 区分已有资料可以支持的限定判断与必须补检索/复核才能成立的判断。指出各方案最有力的反例或替代解释。
4. 比较证据匹配、范围可控性、相对既有综述的潜在差异、补文献负担、组内基础关联和写作风险；给出理由，不作无依据的精确评分或录用承诺。
5. 各列最优先补充的3类证据，并说明补到什么程度才足以进入写作，而不是机械要求凑固定篇数。
6. 保留第三方案输入位置：我提出后再按同一标准进行三方案比较。在此前不要替我最终选择，也不要把两个方案合并成包罗万象的综述。

如果你能够联网并判断领域重复度或推荐新文献，请查原始来源，提供可核验题名、DOI/链接和检索日期；不能检索就明确“尚未验证”，不要把常识印象写成最新领域结论。请用中文回答，研究判断与证据出处对应，明确区分提议与已确认事实。
