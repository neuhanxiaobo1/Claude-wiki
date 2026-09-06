# CLAUDE.md

本目录是 ResearchWiki 论文知识库项目。Claude Code 使用与其他 Agent 相同的项目规则，不另设一套启动流程。

## 启动与路由

首次进入或上下文不足时按 `AGENTS.md` 第 3 节读取公共规则和项目配置；同一任务复用未变化的信息。跨阶段恢复使用 `memory/context_policy.md` 的当前任务与计划，不默认重读全部历史或科学综合页。

| 输入/任务 | 入口 |
|---|---|
| 指定 Zotero collection，生成候选清单 | agents/import_zotero.md |
| 已知论文、附件、PDF、缓存或已有页面的新入库/完整复核/局部修订 | agents/pdf_read_agent.md |
| 多论文比较、gap、综述 | 对应 synthesis_agent / gap_agent / review_agent |
| 结构、证据与流程检查 | agents/lint_agent.md |

公共证据标准以 `memory/hard_memory.md` 为准；页面存在、格式完整或 processed 不表示结论已核实。

## 来源与范围

Zotero 工具是否可用以当前环境为准；不可用时说明实际缺失，继续使用已知且可访问的来源。已有入库或修订授权不重复确认，不默认扩展范围。原件与生成管理记录按 hard_memory 区分；具体来源流程见 `docs/zotero-workflow.md`。

当前为含研究内容的工作库。开源发行准备是独立任务，不因日常阅读、修订或 lint 自动清理文件或发起发布。
