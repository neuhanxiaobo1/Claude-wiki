# ResearchWiki Log

本页记录重要操作。开源模板默认不包含任何个人论文入库历史。

## [2026-06-03] init | Open-Source Template Initialization

- 输入：将 ResearchWiki 初始化为适合开源的空白论文知识库模板。
- 操作：保留项目框架、agent 规则、模板和通用 memory；清理个人论文数据、Zotero 导入记录、真实 synthesis 分析和本机路径。
- 新建：README、QUICKSTART、.gitignore、docs、空目录占位文件。
- 更新：memory、synthesis、index、log、inbox。
- 发现：待用户 clone 后填写 `memory/project_profile.md`。
- 后续：导入第一篇论文并运行 `agents/lint_agent.md`。

## [2026-08-20] init | Zotero MCP 连接测试

- 输入：启动本地论文知识库系统整理，第一步测试 Zotero MCP。
- 操作：MCP 只读测试 get_libraries、get_collections(recursive)。
- 新建：无。
- 更新：无。
- 发现：MCP 连接正常；文库「我的文库」(libraryID=1)；顶层 collection 共 10 个（1分类、2项目、My Notes、ansys、其他、毕设、科研论、编织复合材料振动、翻译），子 collection 较多；文献主题集中在高温复合材料、烧蚀热解、超高温热-振动、尺寸效应、增减材制造、阻尼增材、本构模型等。
- 后续：填写 `memory/project_profile.md`；选定首个导入 collection，按 `agents/import_zotero.md` 生成候选清单。

## [2026-08-20] ingest | 填写项目画像并生成田志林 collection 候选清单

- 输入：用户画像配置（研究领域：陶瓷-腐蚀；博士课题文献综述；输出语言中文；允许复制 PDF 到 raw/papers/）；首个导入 collection：田志林。
- 操作：填写 `memory/project_profile.md`；向 `memory/tag_taxonomy.md` 增加领域标签 ceramics、corrosion；向 `memory/term_aliases.md` 增加术语 Ceramic Corrosion；MCP 读取 collection「毕设 > 组内文章 > 田志林」(key LED7JJ3Y) 共 53 条目；生成候选清单。
- 新建：`raw/zotero_imports/田志林/import_plan.md`、`raw/zotero_imports/田志林/manifest.json`。
- 更新：`memory/project_profile.md`、`memory/tag_taxonomy.md`、`memory/term_aliases.md`。
- 发现：52 个论文条目全部无入库记录（无重复）；15 个条目无 PDF 附件需确认；1 个非论文条目（文章汇总）标记待核查；子 collection「专利」未纳入。
- 后续：用户从候选清单选择编号，按 `agents/pdf_read_agent.md` 单篇入库。

## [2026-08-23] ingest | 系统补全 + 入库 #1：Si3N4 高温熔盐-水氧腐蚀（MinerU 流程首篇）

- 输入：田老师 import plan #1（Zotero item MUIK76GL，DOI: 10.15541/jim20230391）；MinerU 解析缓存 `llm-for-zotero-mineru/9609/full.md`。
- 操作：补全系统漏洞（创建 `wiki/` 九个子目录结构）；更新 `agents/pdf_read_agent.md` 加入 MinerU full.md 优先读取规则；按新流程读 MinerU markdown 全文入库 #1。
- 新建：`wiki/papers/2024-Si3N4-Molten-Salt-Corrosion.md`、`wiki/topics/Ceramic Corrosion.md`。
- 更新：`index.md`（Papers/Topics/Maintenance）、`agents/pdf_read_agent.md`、`raw/zotero_imports/田老师/import_plan.md`（#1 标记已入库 + MinerU 缓存映射附录）。
- 发现：MinerU 缓存位于 `D:\shuju\zotero1\llm-for-zotero-mineru\<itemID>\`（LLM for Zotero 插件，2026-08-23 解析）；田老师 58 篇中 40 篇已有 full.md，17 篇 Zotero 无 PDF 附件，1 篇（#45）有附件但暂无缓存（疑似队列中）。
- 后续：继续按编号入库；#45 缓存生成后核对；积累数篇后运行 `agents/lint_agent.md`。

## [2026-08-23] ingest | 替换入库：3 篇 CMAS 腐蚀论文（#47、#46、#18）

- 输入：用户指示 #1（Si3N4 熔盐-水氧腐蚀）参考意义较低，替换为 3 篇 CMAS 腐蚀论文入库：RE2SiO5 1500 °C 原位降解（#47）、RETaO4 层叠法高通量筛选（#46）、高熵稀土锆酸盐高通量研究（#18）。
- 操作：按 MinerU 优先流程读缓存（itemID 9513/10100/10087 的 full.md）入库三篇；将 Si3N4 论文页归档至 `raw/notes/`（wiki 中移除）；重写主题页 Ceramic Corrosion（以 CMAS 腐蚀为主线，3 条共识/2 条争议/4 条 gap）；标签体系新增 `cmas`、`ebc`；术语表新增 CMAS、EBC 条目。
- 新建：`wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation.md`、`wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening.md`、`wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput.md`；归档 `raw/notes/2024-Si3N4-Molten-Salt-Corrosion.md`。
- 更新：`index.md`、`wiki/topics/Ceramic Corrosion.md`、`memory/tag_taxonomy.md`、`memory/term_aliases.md`、`raw/zotero_imports/田老师/import_plan.md`（#1 标记替换移除；#47/#46/#18 标记已入库）。
- 发现：三篇论文同属田志林组 CMAS 腐蚀系列工作，主线一致——腐蚀产物形成焓随 RE 半径增大更放热（1300 °C 下小半径抗蚀更好）；#47 揭示 1500 °C 时 CMAS 粘度剧降使 RE 效应弱化；#46 澄清钽酸盐腐蚀产物之争；#18 建立高熵锆酸盐成分-结构-性能关联。三篇 MinerU 缓存均命中，OCR 化学式上下标需引用前核对。
- 后续：继续按编号入库；清理 `tmp_zcopy.sqlite` 遗留临时文件已完成；积累数篇后运行 `agents/lint_agent.md`。

## [2026-08-23] lint + synthesis | 首轮健康检查与知识沉淀（claim/gap 页面化）

- 输入：3 篇已入库 CMAS 论文 + 主题页 Ceramic Corrosion（3 共识/2 争议/4 gap）；lint_agent.md、claim/gap 模板。
- 操作：运行 lint 健康检查（标签/术语/双链/孤页/证据标注，无严重问题）；将主题页共识与澄清争议沉淀为 4 个 claim 页；将主题页 4 条 gap 形式化为 4 个 gap 页；激活 synthesis/literature-map.md、open-questions.md、core-argument-map.md（原模板状态）；回填 3 篇论文页与主题页的 claims/gaps frontmatter 字段及 Linked Pages；更新 import_plan.md 的 #45 MinerU 缓存映射（itemID 10110 正文 + 9500/9501 补充，缓存已生成）。
- 新建：`wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend.md`、`wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening.md`、`wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification.md`、`wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism.md`、`wiki/gaps/CMAS-Corrosion-Data-1500C.md`、`wiki/gaps/Structure-Radius-Decoupling.md`、`wiki/gaps/Cooling-Precipitation-Coating-Integrity.md`、`wiki/gaps/High-Throughput-Screening-Transfer.md`。
- 更新：`index.md`（Claims/Gaps 分区 + Maintenance）、`synthesis/literature-map.md`、`synthesis/open-questions.md`、`synthesis/core-argument-map.md`、3 篇论文页、`wiki/topics/Ceramic Corrosion.md`、`raw/zotero_imports/田老师/import_plan.md`。
- 发现：#45（ZSR932E8，Si3N4 多孔）MinerU 缓存已生成（此前疑似解析队列中）；论文页另有 6 条小 gap 暂留原位未建页（待积累后升级，已列入 open-questions 的 Not Yet True Gaps）；用户决定暂时暂停入库。
- 后续：待用户决定是否继续入库；积累 ≥8–10 篇后运行 synthesis_agent/review_agent 生成综述大纲。

## [2026-08-21] ingest | 重新读取田老师 collection 并更新候选清单

- 输入：用户指示 collection 已更换，重新读取 Zotero「田老师」collection 并更新候选清单。
- 操作：本会话 Zotero MCP 工具未加载，通过配置的 zotero-mcp HTTP 端点（http://127.0.0.1:23120/mcp）只读调用 get_collections / get_collection_details / get_subcollections / get_collection_items / get_item_details（58 条全量附件核查）；未修改 Zotero 任何数据。
- 新建：`raw/zotero_imports/田老师/import_plan.md`、`raw/zotero_imports/田老师/manifest.json`。
- 更新：无（`wiki/papers/` 仍为空，无重复条目）。
- 发现：collection 由「田志林」更名为「田老师」，路径变为 毕设 > 组内文章 > 博士 > 田老师；顶层条目 53 → 58（新增 5 篇 2026 年论文：SiO2f/SiO2 透波复合材料、Bagasse 基 C/Co 吸波、BN 纳米片、BN 透波复合材料、数据驱动高熵稀土二硅酸盐）；新增 5 篇中 4 篇无 PDF 附件；原编号 1-53 不变，新条目编号 54-58；子 collection「专利」21 条、「陶瓷+腐蚀」与「吸波」为空；旧版「田志林」清单目录按 raw/ 规则保留未动。
- 后续：用户从新清单选择编号入库；无附件条目需先确认附件。

## [2026-08-24] error-fix | git 推送失败排查 + 代理启动器

- 输入：用户报告 git 无法正常上传；`vscode.git.Git.log`。
- 操作：定位为直连 github.com 不稳定（19:49–19:59 四次 `Connection was reset` / `Could not connect to server`）；确认本机代理 127.0.0.1:7897 可用（3.5s vs 直连 10.7s 且时断时续）但 git 未配置代理；命令行 push 成功补齐本地领先的 3 个提交（`cb263cd..eb06043`），main 与 origin 已同步；按用户要求新建 `git-proxy-fix.bat` 启动器（GBK+CRLF 编码，双击即设置 github.com 代理并测试连通，`off` 参数关闭）。
- 新建：`git-proxy-fix.bat`。
- 更新：git 全局配置 `http.https://github.com.proxy = http://127.0.0.1:7897`（已生效）。
- 发现：Git Bash 终端（UTF-8）下看 GBK 批处理输出为乱码属正常，双击 cmd（CP936）显示正常；.bat 必须 GBK+CRLF，UTF-8/LF 会导致 cmd 解析错乱。
- 后续：再遇推送失败时双击 `git-proxy-fix.bat`；代理端口变更需改脚本首行 PROXY 变量。

## [2026-08-24] error-fix | Obsidian 图谱「文件夹链接」问题根治

- 输入：用户反馈 Obsidian 关系图谱仍出现文件夹样式的链接节点。
- 操作：排查 `.obsidian/app.json`（userIgnoreFilters 排除 memory/、synthesis/、agents/、templates/、raw/、docs/ 等）与 graph.json；用脚本验证全部非排除文件的 wikilink 解析情况；将 graph.json 的 `hideUnresolved` 改为 true（图谱过滤器「只显示已有文件」）。
- 新建：无。
- 更新：`.obsidian/graph.json`（hideUnresolved: true）。
- 发现：根因是 index.md 中 26 个指向被排除规则层文件（memory/synthesis/agents/templates）的 wikilink 在图中成为悬挂链接（dangling）——被排除文件不进入图谱索引；AGENTS.md 第 6/7 节示例链接均在代码块内，Obsidian 不解析，非污染源；showOrphans 已由用户改为 false。
- 后续：重启 Obsidian 或重开图谱面板验证；index.md 规则层导航链接保留不动；未来新增断链将被 hideUnresolved 隐藏，需靠 lint_agent 定期兜底检查。

## [2026-08-24] error-fix | 图谱问题二次修复：路径过滤 scope 到 wiki/

- 输入：用户反馈重启 Obsidian 后 index/inbox/README 等系统页的链接仍显示在关系图谱中。
- 操作：复查 `.obsidian/` 配置与 git diff；发现 app.json 的 userIgnoreFilters 已被清空为 null（规则层目录全部重新进入图谱）；将 graph.json 的 `search` 过滤条件设为 `path:wiki/`（图谱只显示 wiki/ 知识层）。
- 新建：无。
- 更新：`.obsidian/graph.json`（search: path:wiki/）、`memory/error_log.md`（合并修正规则）。
- 发现：上一轮 hideUnresolved 只消除悬挂幻影节点；index/inbox/README/log/AGENTS 等根目录系统页是真实存在的页面，通过 index.md Quick Links 显示为节点——这才是用户所指「文件夹链接」；「排除目录」方案本身有缺陷（排除不彻底 + 制造悬挂链接），图谱路径过滤才是正解。
- 后续：用户在图谱面板顶部筛选框确认 `path:wiki/` 生效（Obsidian 运行中可能覆盖配置文件，需在 UI 中输入一次）；如需 synthesis/ 也进图谱，改为 `path:wiki/ OR path:synthesis/`；userIgnoreFilters 是否恢复由用户决定。
