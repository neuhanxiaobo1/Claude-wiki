---
type: template
template_for: pdf-ingestion-checklist
status: active
created: 2026-06-02
updated: 2026-09-10
tags:
  - ingestion
---

# PDF Ingestion Checklist

本文件是一次完成核对入口，不是待填写或另存的论文卡片；结果只写目标paper及必要维护记录。执行步骤和阅读覆盖以agents/pdf_read_agent.md为准，证据底线见hard_memory，收尾触发条件见根AGENTS第7节。

新入库/完整复核核对全部适用项；局部修订只核对指定判断及直接影响，不重填整卡。用户要求保存核对报告时可另存本次结果，但引用已有证据，不重复转录一套数据。

| 核对项 | 判据 | 结果落点 |
|---|---|---|
| 任务与来源 | 对象、模式、范围明确；来源身份/版本与去重已核；非关键缺项不阻塞独立工作 | Metadata and Sources；必要的任务记录 |
| 阅读覆盖 | 实际章节、图表/公式、补充材料与未读影响明确；按阅读流程触发原件回查 | Reading and Verification Status |
| 设计与比较 | 对象、条件、对照、指标定义、单位、误差/统计及数据独立性足以判断；不可比不排名 | Study Design / E# |
| 证据定位 | 主要结论回指真实E#或等价原文定位；稳定ID与真实标题可对应 | Key Evidence |
| 结论评价 | 结果、作者解释、转引、AI推断分开；支持理由和适用边界明确 | Conclusions for Reuse / Finding |
| 局限与未决 | 作者局限、证据缺失与影响未丢失；语料缺口不自动升为领域gap；不确定性紧邻判断 | E# / Finding / Limitations and Open Questions |
| 直接下游 | 仅改本轮范围内直接依赖，范围外列具体待复核；不继续采用已知错误 | Downstream Review |
| 状态与收尾 | 局部核查不升级整页；原件未改；新标签/别名按需核对；记录只按触发条件更新 | 页面状态；所属范围log/index/短状态等 |

检查不通过时修正本轮可处理项，其余在受影响判断旁标明未决与使用限制；不得用一行“已检查”代替实际证据。已有页面记录足够时直接核对，不复制表格、不逐项写通过流水。
