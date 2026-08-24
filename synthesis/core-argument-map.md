---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-23
tags:
  - synthesis
  - context
---

# Core Argument Map

本页保存长期对话后的短上下文快照，用于在上下文变长时快速恢复项目状态。

## Current Project Goal

- 使用 ResearchWiki 将论文转化为可维护的 Markdown 知识库，用于阅读、综合、gap 分析、研究定位和综述写作。用户博士课题：高温结构陶瓷 EBC/CMAS 腐蚀方向的文献综述。

## Confirmed Decisions

- `AGENTS.md` 作为轻量总控入口；`agents/` 任务型规则、`templates/` 页面模板、`memory/` 长期约束、`wiki/` 结构化知识、`synthesis/` 跨论文综合、`raw/` 原始资料。
- 输出语言中文；英文原文（题名、期刊名、专有名词）不翻译；引用编号须附题名+DOI。
- Zotero 导入模式：指定 collection 单篇确认制（默认单次最多 3 篇）；首个 collection「田老师」（key LED7JJ3Y，路径 毕设 > 组内文章 > 博士 > 田老师）。
- 入库优先数据源：LLM for Zotero 插件 MinerU 解析缓存 `D:\shuju\zotero1\llm-for-zotero-mineru\<itemID>\full.md`（40 篇已缓存，映射见 import_plan 附录）；未命中回退 Zotero MCP。
- 知识库主题主线：CMAS 腐蚀（#1 Si3N4 熔盐篇已按用户要求替换归档至 raw/notes/）。
- Obsidian 已安装用于查看；git 管理用 VSCode，不装 Obsidian Git 插件；git 提交由用户自行完成，不要主动 commit。

## Deprecated or Rejected Options

- 田志林旧版清单（collection 已更名「田老师」，旧目录按 raw/ 规则保留未动）。
- Si3N4 熔盐-水氧腐蚀方向入库（参考意义低，已替换为 CMAS 系列）。

## Current Paper Corpus

- 已入库 3 篇（田志林组 CMAS 腐蚀系列）：#47 RE2SiO5 1500 °C 原位降解（JAC 2023）、#46 RETaO4 层叠法高通量（Adv. Sci. 2025）、#18 高熵锆酸盐高通量（JECS 2026）。
- 已沉淀：1 个主题页（Ceramic Corrosion）、4 个 claim 页、4 个 gap 页；literature-map 与 open-questions 已激活（2026-08-23）。
- 主线论点：形成焓随 RE 半径增大更放热（1300 °C 小半径抗蚀好，三体系一致）；1500 °C 粘度剧降 RE 效应弱化（仅单硅酸盐证实）。
- 候选待入库：58 篇清单剩 55 篇；CMAS 相关优先 #36/#23/#48/#52；#45 Si3N4 多孔缓存已生成。

## Next Tasks

- 继续按 import_plan 编号入库（CMAS 优先 #36/#23/#48/#52）。
- 积累 ≥8–10 篇后运行 `agents/synthesis_agent.md` 深化文献地图、`agents/review_agent.md` 生成综述大纲。
- 待用户填写 `memory/project_profile.md` 的核心研究问题与 Excluded 范围。
- 每批入库后运行 `agents/lint_agent.md`。

## Open Questions

- 1500 °C RE 效应弱化的普适性（钽酸盐/锆酸盐缺高温数据）。
- 结构类型与 RE 半径的解耦（高熵锆酸盐二者共线）。
- 冷却析出产物对涂层热循环完整性的影响。
- 高通量方法跨体系推广（方法学机会点）。
