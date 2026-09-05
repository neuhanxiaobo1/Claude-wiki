---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-28
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

- 已入库 7 篇（田志林组）：#36 RE2SiO5 1300 °C 衰退层-半径总规律（Corros. Sci. 2019，奠基工作）、#47 RE2SiO5 1500 °C 原位降解（JAC 2023）、#46 RETaO4 层叠法高通量（Adv. Sci. 2025）、#18 高熵锆酸盐高通量（JECS 2026）、#16 Lu2SiO5 1500 °C 原位定向生长（Surf. Coat. Technol. 2024）、#48 高熵 (Ho0.25Lu0.25Yb0.25Eu0.25)2SiO5（JAC 2022）、#29 Hf6Ta2O17-Al2O3 热化学相容性（JECS 2025）。
- 已沉淀：2 个主题页（Ceramic Corrosion、Thermal Barrier Coatings）、8 个 claim 页、5 个 gap 页；literature-map 与 open-questions 已更新（2026-08-27）；research-positioning 与 review-outline 已激活（2026-08-28）。
- 主线论点：形成焓随 RE 半径增大更放热（1300 °C 小半径抗蚀好，三体系一致；#36 给出单组分 8 组分奠基数据 + 光学碱度判据，#48 证明规律在固溶体/高熵体系同样成立——渗透排序与平均半径完全对应）；1500 °C 下低粘度 CMAS 使传质与反应加速、RE 效应弱化（#47 七体系 + #16 Lu2SiO5 219 μm 双证据），且 #16 揭示相分解诱导晶间渗透新机制、#47 暴露润湿流失与冷却二次析出——1300 °C 半径规律不能外推到 1500 °C；X1/X2 晶型依赖的趋势翻转（X1 系列 #21 未入库 vs #36 X2 段）归入 Structure-Radius-Decoupling gap；姊妹方向 TBC：#29 表明 TBC-TGO 热化学相容性是选材缺失判据。
- 候选待入库：58 篇清单剩 51 篇；CMAS 相关优先 #23/#52；检索候选 #59–64 已补录（不在 Zotero 文库，待用户确认）；#45 Si3N4 多孔缓存已生成。

## Next Tasks

- 入库暂停（2026-08-28 用户指示；#36 为 X1 争议核实而临时恢复，已完成）；3 条定位方向已沉淀于 `synthesis/research-positioning.md`：1500 °C 跨体系地图 / 相稳定性优先设计 / TBC-TGO 判据。
- 下一步：与用户讨论定位方向取舍；按选定方向恢复入库（Positioning 1 对应选号 CMAS 优先 #23/#52）。
- 积累 ≥8–10 篇后运行 `agents/synthesis_agent.md` 深化文献地图、`agents/review_agent.md` 更新综述大纲。
- 待用户填写 `memory/project_profile.md` 的核心研究问题与 Excluded 范围（定位方向将据此校准）。
- 每批入库后运行 `agents/lint_agent.md`。

## Open Questions

- 1500 °C RE 效应弱化与相分解的跨体系普适性（钽酸盐/锆酸盐/高熵硅酸盐缺高温数据）。
- 结构类型与 RE 半径的解耦（高熵锆酸盐二者共线；单硅酸盐 X1/X2 晶型翻转，#36/#21 证据）。
- 冷却析出产物/冷却热应力对涂层热循环完整性的影响（#47/#16 两篇原位证据 + #36 剥落观察，后果未评估）。
- 高通量方法跨体系推广（方法学机会点）。
- TBC-TGO 相容性判据与扩散障方案（姊妹方向，#29 单体系证据）。
