---
direction_id: wave-transparent-composites
type: paper
title: Applications of natural language processing and large language models in materials
  discovery
year: 2025
authors:
- Xue Jiang
- Weiren Wang
- Shaohan Tian
- Hao Wang
- Turab Lookman
- Yanjing Su
venue: npj Computational Materials
status: processed
review_status: draft
created: '2026-09-20'
updated: '2026-09-20'
source: C:\Users\youthcookie\OneDrive\1.Science\1.Zotero\pdf2\2025-(npj Comput Mater)\Jiang
  等 - 2025 - Applications of natural language processing and large language models
  in materials discovery.pdf
source_version: 期刊正式PDF及对应MinerU缓存；原始参考文献未逐篇核查
zotero_collection: GS7STC5N
zotero_item_key: YJGX6KP7
zotero_attachment_key: UWQCJYL9
pdf_attachment_name: Jiang 等 - 2025 - Applications of natural language processing
  and large language models in materials discovery.pdf
doi: 10.1038/s41524-025-01554-0
tags:
- paper
- review
---

# Applications of natural language processing and large language models in materials discovery

## Metadata and Sources

- 主附件：`UWQCJYL9`；PDF路径见元数据。
- MinerU：`D:\shuju\zotero1\llm-for-zotero-mineru\11106\full.md`；已先核对manifest与_llm_source中的父条目/附件映射。
- 本轮只读原件，未复制原PDF、修改缓存或Zotero；译文不作为独立证据。

## Reading and Verification Status

- new-ingestion；清单4号，第7篇，单列大模型/材料信息方法参考。
- 已读15页正式英文PDF对应MD中的摘要、引言、NLP发展、数据抽取、语言模型用于材料发现/预测、智能体、挑战与展望主体；视觉回查PDF第4页图2及相邻文字。
- 图3—9主要读图注与文字，转引原始数据集、代码和论文未复核；本页保持draft。
- Zotero当前摘要字段为空；本文摘要确实在PDF/MD中存在，知识库已补充内容概述及原文定位，不是缺PDF。旧3号D7TP8Z6X本次MCP返回not found；不再作为独立论文入库。

## Research Problem and Contribution

综述NLP/大模型在文献数据抽取、材料知识表征、性能预测及工具协作中的作用，并讨论数值理解、预测和科学推理限制。它不是透波材料性能综述，没有证明在本组陶瓷数据上有效。

摘要内容概述（本次中文归纳，非原文译文）：材料数据的大量信息分散在科学文献中，NLP与大模型可辅助提取与利用这些信息；文章围绕自动数据抽取、材料发现及自主研究梳理方法，并讨论挑战与发展机会。原文定位为PDF第1页摘要。

## Study Design

| 要素 | 内容 | 定位 |
|---|---|---|
| 任务 | 语料预处理、实体识别、关系与工艺序列抽取、词向量、性能预测、工具协作 | 图2—9及相关正文 |
| 数据来源 | 多篇既有材料/化学/合金/聚合物研究；不是本文统一基准 | 各案例引文 |
| 方法差异 | 提示词调用、监督微调、领域预训练、传统规则/ML、外部计算工具须区分 | 数据抽取与语言模型章节 |
| 评价 | 原研究的精确率、召回率、F1、预测误差等；任务和数据集不同 | Recent developments using LLMs等 |

## Key Evidence

### E1

- 类型：作者方法综述。
- 对象/结果：传统NLP与LLM路径均需语料获取、清理、抽取和关系归属；仅提取“材料—数值—单位”不足以保证关联到正确样品/工艺。
- 定位/核查：The NLP pipeline for automatic materials data extraction、Overview of NLP and how it differs from LLMs；PDF第4页图2及文字已视觉核对。
- 支持边界：支持构建有来源和关联约束的抽取流程，不证明任意提示词可自动可靠建库。

### E2

- 类型：综述转引多项案例。
- 结果：提示词、标注数据与微调在不同信息抽取任务上有成功案例，但分类准确率、字段抽取精确率/召回率与材料预测性能不是同一指标。
- 定位：Traditional NLP pipeline、Recent developments using LLMs、Fig.5相关文字。
- 核查/独立性：文字已读；原始划分、标注与代码未核，不将跨任务百分比合并或称作本组可达到的准确率。

### E3

- 类型：作者观点与转引。
- 结果：词向量相似性、领域编码器、属性预测网络与工具调用分别承担不同功能；知识相似度或语言生成不能直接作为材料可合成或性能优越的验证。
- 定位：Materials development driven by Language models、Fine-tuned language models and property prediction、AI agents for autonomous research in materials science。
- 核查/边界：主体已读，本文案例主要来自其他材料；不把BERT编码器、传统ML和对话式LLM混为同一方法，不把演示任务推广成无需人工验证的实验能力。

### E4

- 类型：作者局限分析。
- 结果：数值理解、组成—工艺—性能定量映射、数据质量、算力与幻觉均是限制；检索和计算工具可辅助但不自动消除错误。
- 定位：Challenges and future developments及Numerical understanding、Quantitative prediction、Efficiency and optimization of resources、Scientific reasoning。
- 核查/边界：主体已读；关于具体模型版本/能力的陈述属于2025年文章背景，本轮不核当前产品状态、不据此推荐现行模型或工具配置。

## Conclusions for Reuse

- Finding 1：可作为“证据定位—条件归一—结构化材料记录”的方法参考（E1—E2，限定支持）。
- Finding 2：先在人工核查的小规模陶瓷语料中评价字段与样品关联正确率，再考虑候选生成；此为AI提出的本方向迁移方案，不是论文已验证的透波课题（E3—E4）。
- Finding 3：大模型输出与传统机器学习预测、实验实测必须分列；有摘要/知识卡不等于性能预测已成立。

## Limitations and Open Questions

尚无本组语料上的准确率、数据泄漏检查或独立验证。综述中的模型历史、训练规模和厂商说法不作当前事实复用。未把“同行评审”视为文献数据无误的保证，原文数据冲突仍需保留并人工复核。

## Downstream Review

关联[[directions/wave-transparent-composites/wiki/papers/Wen-2026-High-Entropy-Disilicate]]时区分其传统机器学习与本篇语言模型方法；不宣称本组已开展大模型实验。
