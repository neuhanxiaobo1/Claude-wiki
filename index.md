# ResearchWiki Index

这是知识库的总索引。每次新增或更新重要页面后，都应同步维护本页。

## Quick Links

- [[README]]
- [[QUICKSTART]]
- [[inbox]]
- [[log]]
- [[AGENTS]]
- [[memory/project_profile]]
- [[memory/hard_memory]]
- [[memory/context_policy]]
- [[memory/style_snapshot]]
- [[memory/error_log]]
- [[memory/tag_taxonomy]]
- [[memory/term_aliases]]
- [[memory/decision_log]]
- [[synthesis/literature-map]]
- [[synthesis/core-argument-map]]
- [[synthesis/research-positioning]]
- [[synthesis/open-questions]]
- [[synthesis/review-outline]]

## Agent Rules

- [[agents/import_zotero]]：Zotero collection 候选清单与导入前置规则。
- [[agents/pdf_read_agent]]：单篇论文读取与结构化入库。
- [[agents/synthesis_agent]]：多论文综合、文献地图和方法路线比较。
- [[agents/gap_agent]]：research gap 挖掘、开放问题和研究定位。
- [[agents/review_agent]]：文献综述大纲、综述段落和写作组织。
- [[agents/lint_agent]]：知识库健康检查、标签统一、术语合并和错误修正。

## Memory

- [[memory/project_profile]]：项目说明书，新用户先填写。
- [[memory/hard_memory]]：长期通用硬规则。
- [[memory/context_policy]]：轻量上下文预算与历史压缩规则。
- [[memory/style_snapshot]]：默认输出风格和写作偏好。
- [[memory/error_log]]：错误记录与修正规则。
- [[memory/tag_taxonomy]]：统一标签体系。
- [[memory/term_aliases]]：术语同义词映射。
- [[memory/decision_log]]：结构和规则决策记录。

## Templates

- [[templates/pdf_ingestion_template]]
- [[templates/paper]]
- [[templates/topic]]
- [[templates/method]]
- [[templates/claim]]
- [[templates/gap]]
- [[templates/review]]

## Synthesis

- [[synthesis/literature-map]]：跨论文文献地图。
- [[synthesis/core-argument-map]]：项目短上下文快照。
- [[synthesis/open-questions]]：开放问题和 gap 候选清单。
- [[synthesis/research-positioning]]：研究定位工作区。
- [[synthesis/review-outline]]：文献综述大纲。

## Papers

- [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]：RE2SiO5 (RE = Tb, Dy, Ho, Y, Er, Tm, Yb) 在 1500 °C 的 CMAS 降解原位观察与机制，Ca2RE8(SiO4)6O2 沿 [001] 优先生长（2023, J. Adv. Ceram., DOI: 10.26599/JAC.2023.9220822）。
- [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]：层叠法高通量筛选 CMAS 抗性 RETaO4，主产物 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体，渗透深度随 RE 半径增大而增加（2025, Adv. Sci., DOI: 10.1002/advs.202412717）。
- [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]：高通量研究 19 种高熵稀土锆酸盐的热物性与 CMAS 抗性，小平均半径缺陷萤石结构抗蚀最佳（2026, J. Eur. Ceram. Soc., DOI: 10.1016/j.jeurceramsoc.2025.118014）。

## Topics

- [[wiki/topics/Ceramic Corrosion]]：陶瓷腐蚀主主题（当前以 CMAS 腐蚀为主线：RE2SiO5/钽酸盐/高熵锆酸盐三体系）。

## Methods

待导入论文后更新。

## Datasets

待导入论文后更新。

## Metrics

待导入论文后更新。

## Claims

- [[wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend]]：腐蚀产物形成焓随 RE 半径增大更放热，1300 °C 下小半径成分抗蚀更好（三体系证据链）。
- [[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]：1500 °C CMAS 粘度剧降致 RE 效应弱化且方向反转（单体系，medium）。
- [[wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification]]：RETaO4 主腐蚀产物澄清为 (Ca2-xREx)(Ta2-y-zMgyAlz)O7 固溶体+少量磷灰石，晶界腐蚀普遍。
- [[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]：小半径缺陷萤石高熵锆酸盐抗蚀最佳的双重机制（动力学+热力学）。

## Gaps

- [[wiki/gaps/CMAS-Corrosion-Data-1500C]]：钽酸盐/锆酸盐 1500 °C 级 CMAS 腐蚀数据缺失（high）。
- [[wiki/gaps/Structure-Radius-Decoupling]]：结构类型与 RE 半径对 CMAS 抗性的贡献未解耦（high）。
- [[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]：冷却析出产物对涂层热循环完整性的影响未评估（medium）。
- [[wiki/gaps/High-Throughput-Screening-Transfer]]：高通量筛选方法（层叠法/原位观察/并行制备）跨体系推广空白（medium）。

## Reviews

待导入论文后更新。

## Maintenance

- 当前状态：已导入 3 篇论文（2026-08-23，均为 CMAS 腐蚀方向），MinerU markdown 优先入库流程已启用；2026-08-23 完成首轮 lint 健康检查（无严重问题），并沉淀 4 个 claim 页、4 个 gap 页，激活 literature-map / open-questions / core-argument-map；2026-08-24 修复 Obsidian 图谱悬挂链接（graph.json hideUnresolved: true，图谱只显示已有文件）。
- 下一步：继续按 `raw/zotero_imports/田老师/import_plan.md` 编号入库（CMAS 优先 #36/#23/#48/#52）；每批入库后运行 `agents/lint_agent.md`。
