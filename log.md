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
