# 电子封装方向规则入口

方向ID：`electronic-packaging`。方向根：`directions/electronic-packaging/`。2026-09-09由用户明确要求创建；每次研究工作仍按根入口选择/绑定方向，先遵循根AGENTS和memory/hard_memory，再使用本方向配置。

## 研究配置与恢复

- [[directions/electronic-packaging/memory/project_profile]]：用户确认的范围、五类主要指标与待确定设置。
- [[directions/electronic-packaging/memory/current_context]]：本方向当前任务及下一步。
- [[directions/electronic-packaging/index]]：研究导航；操作日志和待办在本方向log/inbox。
- 领域标签和术语使用本方向memory/tag_taxonomy与memory/term_aliases，同时遵循根公共词表标准。

## 任务扩展

| 任务 | 适用规则 |
|---|---|
| 候选筛选、单篇阅读/入库/修订 | 根agents/import_zotero或pdf_read_agent，加本方向 [[directions/electronic-packaging/memory/reading_rules]] |
| 多论文比较、总结与gap | 根agents/synthesis_agent或gap_agent，加本方向 [[directions/electronic-packaging/memory/synthesis_rules]] |
| 综述、大纲和段落写作 | 根agents/review_agent与templates/review，加synthesis_rules中的指标报告和比较要求；语言默认沿用根memory/user_profile |
| 链接、标签、状态与纠错 | 根agents/lint_agent，默认只检查本方向 |

使用通用论文/claim等模板，按阅读规则在必要栏目增加本方向记录，不复制整份公共模板；目前无独立writing_rules或专用模板文件。用户未来提出新要求时仅更新本方向。

## 范围与记录

研究重点为烧结用电子银膏，主要指标是用户所称的焊接温度、剪切强度、孔隙率、热导率、导电性能。没有确认具体配方、粒径范围、压力路线、温度目标或综合评分权重；不得从检查清单推定这些研究决策。

原件、论文、综合与记录只写在本方向。研究错误记本方向memory/error_log，研究决定记本方向memory/decision_log，重要操作记本方向log；公共登记维护才更新根索引/注册表/日志。不加载其他方向的领域规则、研究目标、团队口径或文献清单。定向借鉴时来源方向默认只读，接收方向独立评价并保留适用条件与共同来源。
