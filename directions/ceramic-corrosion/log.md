# ResearchWiki Log

本页记录重要操作。开源模板默认不包含任何个人论文入库历史。

## [2026-06-03] init | Open-Source Template Initialization

- 输入：将 ResearchWiki 初始化为适合开源的空白论文知识库模板。
- 操作：保留项目框架、agent 规则、模板和通用 memory；清理个人论文数据、Zotero 导入记录、真实 synthesis 分析和本机路径。
- 新建：README、QUICKSTART、.gitignore、docs、空目录占位文件。
- 更新：memory、synthesis、index、log、inbox。
- 发现：待用户 clone 后填写 `directions/ceramic-corrosion/memory/project_profile.md`。
- 后续：导入第一篇论文并运行 `agents/lint_agent.md`。

## [2026-08-20] init | Zotero MCP 连接测试

- 输入：启动本地论文知识库系统整理，第一步测试 Zotero MCP。
- 操作：MCP 只读测试 get_libraries、get_collections(recursive)。
- 新建：无。
- 更新：无。
- 发现：MCP 连接正常；文库「我的文库」(libraryID=1)；顶层 collection 共 10 个（1分类、2项目、My Notes、ansys、其他、毕设、科研论、编织复合材料振动、翻译），子 collection 较多；文献主题集中在高温复合材料、烧蚀热解、超高温热-振动、尺寸效应、增减材制造、阻尼增材、本构模型等。
- 后续：填写 `directions/ceramic-corrosion/memory/project_profile.md`；选定首个导入 collection，按 `agents/import_zotero.md` 生成候选清单。

## [2026-08-20] ingest | 填写项目画像并生成田志林 collection 候选清单

- 输入：用户画像配置（研究领域：陶瓷-腐蚀；博士课题文献综述；输出语言中文；允许复制 PDF 到 directions/ceramic-corrosion/raw/papers/）；首个导入 collection：田志林。
- 操作：填写 `directions/ceramic-corrosion/memory/project_profile.md`；向 `directions/ceramic-corrosion/memory/tag_taxonomy.md` 增加领域标签 ceramics、corrosion；向 `directions/ceramic-corrosion/memory/term_aliases.md` 增加术语 Ceramic Corrosion；MCP 读取 collection「毕设 > 组内文章 > 田志林」(key LED7JJ3Y) 共 53 条目；生成候选清单。
- 新建：`directions/ceramic-corrosion/raw/zotero_imports/田志林/import_plan.md`、`directions/ceramic-corrosion/raw/zotero_imports/田志林/manifest.json`。
- 更新：`directions/ceramic-corrosion/memory/project_profile.md`、`directions/ceramic-corrosion/memory/tag_taxonomy.md`、`directions/ceramic-corrosion/memory/term_aliases.md`。
- 发现：52 个论文条目全部无入库记录（无重复）；15 个条目无 PDF 附件需确认；1 个非论文条目（文章汇总）标记待核查；子 collection「专利」未纳入。
- 后续：用户从候选清单选择编号，按 `agents/pdf_read_agent.md` 单篇入库。

## [2026-08-23] ingest | 系统补全 + 入库 #1：Si3N4 高温熔盐-水氧腐蚀（MinerU 流程首篇）

- 输入：田老师 import plan #1（Zotero item MUIK76GL，DOI: 10.15541/jim20230391）；MinerU 解析缓存 `llm-for-zotero-mineru/9609/full.md`。
- 操作：补全系统漏洞（创建 `directions/ceramic-corrosion/wiki/` 九个子目录结构）；更新 `agents/pdf_read_agent.md` 加入 MinerU full.md 优先读取规则；按新流程读 MinerU markdown 全文入库 #1。
- 新建：`directions/ceramic-corrosion/wiki/papers/2024-Si3N4-Molten-Salt-Corrosion.md`、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`。
- 更新：`directions/ceramic-corrosion/index.md`（Papers/Topics/Maintenance）、`agents/pdf_read_agent.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`（#1 标记已入库 + MinerU 缓存映射附录）。
- 发现：MinerU 缓存位于 `D:\shuju\zotero1\llm-for-zotero-mineru\<itemID>\`（LLM for Zotero 插件，2026-08-23 解析）；田老师 58 篇中 40 篇已有 full.md，17 篇 Zotero 无 PDF 附件，1 篇（#45）有附件但暂无缓存（疑似队列中）。
- 后续：继续按编号入库；#45 缓存生成后核对；积累数篇后运行 `agents/lint_agent.md`。

## [2026-08-23] ingest | 替换入库：3 篇 CMAS 腐蚀论文（#47、#46、#18）

- 输入：用户指示 #1（Si3N4 熔盐-水氧腐蚀）参考意义较低，替换为 3 篇 CMAS 腐蚀论文入库：RE2SiO5 1500 °C 原位降解（#47）、RETaO4 层叠法高通量筛选（#46）、高熵稀土锆酸盐高通量研究（#18）。
- 操作：按 MinerU 优先流程读缓存（itemID 9513/10100/10087 的 full.md）入库三篇；将 Si3N4 论文页归档至 `directions/ceramic-corrosion/raw/notes/`（wiki 中移除）；重写主题页 Ceramic Corrosion（以 CMAS 腐蚀为主线，3 条共识/2 条争议/4 条 gap）；标签体系新增 `cmas`、`ebc`；术语表新增 CMAS、EBC 条目。
- 新建：`directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation.md`、`directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening.md`、`directions/ceramic-corrosion/wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput.md`；归档 `directions/ceramic-corrosion/raw/notes/2024-Si3N4-Molten-Salt-Corrosion.md`。
- 更新：`directions/ceramic-corrosion/index.md`、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`、`directions/ceramic-corrosion/memory/tag_taxonomy.md`、`directions/ceramic-corrosion/memory/term_aliases.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`（#1 标记替换移除；#47/#46/#18 标记已入库）。
- 发现：三篇论文同属田志林组 CMAS 腐蚀系列工作，主线一致——腐蚀产物形成焓随 RE 半径增大更放热（1300 °C 下小半径抗蚀更好）；#47 揭示 1500 °C 时 CMAS 粘度剧降使 RE 效应弱化；#46 澄清钽酸盐腐蚀产物之争；#18 建立高熵锆酸盐成分-结构-性能关联。三篇 MinerU 缓存均命中，OCR 化学式上下标需引用前核对。
- 后续：继续按编号入库；清理 `tmp_zcopy.sqlite` 遗留临时文件已完成；积累数篇后运行 `agents/lint_agent.md`。

## [2026-08-23] lint + synthesis | 首轮健康检查与知识沉淀（claim/gap 页面化）

- 输入：3 篇已入库 CMAS 论文 + 主题页 Ceramic Corrosion（3 共识/2 争议/4 gap）；lint_agent.md、claim/gap 模板。
- 操作：运行 lint 健康检查（标签/术语/双链/孤页/证据标注，无严重问题）；将主题页共识与澄清争议沉淀为 4 个 claim 页；将主题页 4 条 gap 形式化为 4 个 gap 页；激活 directions/ceramic-corrosion/synthesis/literature-map.md、open-questions.md、core-argument-map.md（原模板状态）；回填 3 篇论文页与主题页的 claims/gaps frontmatter 字段及 Linked Pages；更新 import_plan.md 的 #45 MinerU 缓存映射（itemID 10110 正文 + 9500/9501 补充，缓存已生成）。
- 新建：`directions/ceramic-corrosion/wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend.md`、`directions/ceramic-corrosion/wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening.md`、`directions/ceramic-corrosion/wiki/claims/RETaO4-CMAS-Corrosion-Product-Clarification.md`、`directions/ceramic-corrosion/wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism.md`、`directions/ceramic-corrosion/wiki/gaps/CMAS-Corrosion-Data-1500C.md`、`directions/ceramic-corrosion/wiki/gaps/Structure-Radius-Decoupling.md`、`directions/ceramic-corrosion/wiki/gaps/Cooling-Precipitation-Coating-Integrity.md`、`directions/ceramic-corrosion/wiki/gaps/High-Throughput-Screening-Transfer.md`。
- 更新：`directions/ceramic-corrosion/index.md`（Claims/Gaps 分区 + Maintenance）、`directions/ceramic-corrosion/synthesis/literature-map.md`、`directions/ceramic-corrosion/synthesis/open-questions.md`、`directions/ceramic-corrosion/synthesis/core-argument-map.md`、3 篇论文页、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`。
- 发现：#45（ZSR932E8，Si3N4 多孔）MinerU 缓存已生成（此前疑似解析队列中）；论文页另有 6 条小 gap 暂留原位未建页（待积累后升级，已列入 open-questions 的 Not Yet True Gaps）；用户决定暂时暂停入库。
- 后续：待用户决定是否继续入库；积累 ≥8–10 篇后运行 synthesis_agent/review_agent 生成综述大纲。

## [2026-08-21] ingest | 重新读取田老师 collection 并更新候选清单

- 输入：用户指示 collection 已更换，重新读取 Zotero「田老师」collection 并更新候选清单。
- 操作：本会话 Zotero MCP 工具未加载，通过配置的 zotero-mcp HTTP 端点（http://127.0.0.1:23120/mcp）只读调用 get_collections / get_collection_details / get_subcollections / get_collection_items / get_item_details（58 条全量附件核查）；未修改 Zotero 任何数据。
- 新建：`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/manifest.json`。
- 更新：无（`directions/ceramic-corrosion/wiki/papers/` 仍为空，无重复条目）。
- 发现：collection 由「田志林」更名为「田老师」，路径变为 毕设 > 组内文章 > 博士 > 田老师；顶层条目 53 → 58（新增 5 篇 2026 年论文：SiO2f/SiO2 透波复合材料、Bagasse 基 C/Co 吸波、BN 纳米片、BN 透波复合材料、数据驱动高熵稀土二硅酸盐）；新增 5 篇中 4 篇无 PDF 附件；原编号 1-53 不变，新条目编号 54-58；子 collection「专利」21 条、「陶瓷+腐蚀」与「吸波」为空；旧版「田志林」清单目录按 directions/ceramic-corrosion/raw/ 规则保留未动。
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
- 操作：排查 `.obsidian/app.json`（userIgnoreFilters 排除 memory/、directions/ceramic-corrosion/synthesis/、agents/、templates/、directions/ceramic-corrosion/raw/、docs/ 等）与 graph.json；用脚本验证全部非排除文件的 wikilink 解析情况；将 graph.json 的 `hideUnresolved` 改为 true（图谱过滤器「只显示已有文件」）。
- 新建：无。
- 更新：`.obsidian/graph.json`（hideUnresolved: true）。
- 发现：根因是 directions/ceramic-corrosion/index.md 中 26 个指向被排除规则层文件（memory/synthesis/agents/templates）的 wikilink 在图中成为悬挂链接（dangling）——被排除文件不进入图谱索引；AGENTS.md 第 6/7 节示例链接均在代码块内，Obsidian 不解析，非污染源；showOrphans 已由用户改为 false。
- 后续：重启 Obsidian 或重开图谱面板验证；directions/ceramic-corrosion/index.md 规则层导航链接保留不动；未来新增断链将被 hideUnresolved 隐藏，需靠 lint_agent 定期兜底检查。

## [2026-08-24] error-fix | 图谱问题二次修复：路径过滤 scope 到 directions/ceramic-corrosion/wiki/

- 输入：用户反馈重启 Obsidian 后 index/inbox/README 等系统页的链接仍显示在关系图谱中。
- 操作：复查 `.obsidian/` 配置与 git diff；发现 app.json 的 userIgnoreFilters 已被清空为 null（规则层目录全部重新进入图谱）；将 graph.json 的 `search` 过滤条件设为 `path:directions/ceramic-corrosion/wiki/`（图谱只显示 directions/ceramic-corrosion/wiki/ 知识层）。
- 新建：无。
- 更新：`.obsidian/graph.json`（search: path:directions/ceramic-corrosion/wiki/）、`directions/ceramic-corrosion/memory/error_log.md`（合并修正规则）。
- 发现：上一轮 hideUnresolved 只消除悬挂幻影节点；index/inbox/README/log/AGENTS 等根目录系统页是真实存在的页面，通过 directions/ceramic-corrosion/index.md Quick Links 显示为节点——这才是用户所指「文件夹链接」；「排除目录」方案本身有缺陷（排除不彻底 + 制造悬挂链接），图谱路径过滤才是正解。
- 后续：用户在图谱面板顶部筛选框确认 `path:directions/ceramic-corrosion/wiki/` 生效（Obsidian 运行中可能覆盖配置文件，需在 UI 中输入一次）；如需 directions/ceramic-corrosion/synthesis/ 也进图谱，改为 `path:directions/ceramic-corrosion/wiki/ OR path:directions/ceramic-corrosion/synthesis/`；userIgnoreFilters 是否恢复由用户决定。

## [2026-08-24] update | 当前模型重读三篇 CMAS 论文并替换入库总结

- 输入：用户指出上一轮总结不全、结论不够深入，要求基于已入库三篇论文在当前模型下重新读取并替换入库总结。
- 操作：重新读取 MinerU 缓存 `llm-for-zotero-mineru/9513/full.md`、`10100/full.md`、`10087/full.md` 的摘要、引言、实验、结果、讨论与结论关键段落；替换三篇论文页的 `One-Sentence Takeaway` 与 `Abstract Rewritten`；同步更新 topic、literature-map、core-argument-map 和 index 的主线表述。
- 新建：无。
- 更新：`directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation.md`、`directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening.md`、`directions/ceramic-corrosion/wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput.md`、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`、`directions/ceramic-corrosion/synthesis/literature-map.md`、`directions/ceramic-corrosion/synthesis/core-argument-map.md`、`directions/ceramic-corrosion/index.md`、`directions/ceramic-corrosion/log.md`。
- 发现：#47 的高温结论应表述为低粘度传质加速 + RE 效应弱化 + 润湿流失 + 冷却二次析出的耦合，不应简化为单一“半径规律反转”；#46 的核心价值在于层叠法统一实验条件并用 TEM/EPMA 澄清 RETaO4 腐蚀产物和晶界腐蚀普遍性；#18 的核心价值在于把高熵锆酸盐设计拆成热导、TEC 与 CMAS 抗性的多参数框架。
- 后续：下一步宜激活 `directions/ceramic-corrosion/synthesis/research-positioning.md` 和 `directions/ceramic-corrosion/synthesis/review-outline.md`，或继续入库 CMAS 优先论文以验证 1500 °C 普适性与结构-半径解耦问题。

## [2026-08-27] ingest | 第二批三篇论文入库（#16 Lu2SiO5 1500 °C 原位 / #48 高熵 RE2SiO5 / #29 Hf6Ta2O17-Al2O3）

- 输入：用户指定三篇论文入库，并确认 PDF 附件与 MinerU 缓存均已就绪。
- 操作：按 MinerU 缓存优先流程读取 `llm-for-zotero-mineru/10149`（#16）、`10117/10119/10121`（#48）、#29 缓存全文；Zotero MCP 只读校验条目与附件键（#16 RLNIRS7B→JNS38XK5、#29 5PSRPWAQ→GSDAE8IV、#48 8IPQUSQL→I929AL9M/DMBMXKHX/DQTEV4JP）；按模板新建论文页并联动更新主题/claim/gap/synthesis/index。
- 新建：`directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth.md`、`directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC.md`、`directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility.md`、`directions/ceramic-corrosion/wiki/claims/Phase-Decomposition-Intergranular-Infiltration.md`、`directions/ceramic-corrosion/wiki/claims/Garnet-Product-RE2SiO5-CMAS.md`、`directions/ceramic-corrosion/wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design.md`、`directions/ceramic-corrosion/wiki/claims/Hf6Ta2O17-TGO-Incompatibility.md`、`directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility.md`、`directions/ceramic-corrosion/wiki/topics/Thermal Barrier Coatings.md`。
- 更新：`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`（+2 论文、+3 claims、Main Question 5、路线 4、产物谱争议）、`directions/ceramic-corrosion/wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend.md`（+#16/#48 固溶体证据，high）、`directions/ceramic-corrosion/wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening.md`（+#16 双论文证据，medium→medium-high）、`directions/ceramic-corrosion/wiki/gaps/CMAS-Corrosion-Data-1500C.md`（+相分解维度）、`directions/ceramic-corrosion/wiki/gaps/Cooling-Precipitation-Coating-Integrity.md`（+#16 两篇独立原位证据）、`directions/ceramic-corrosion/synthesis/open-questions.md`（Q1/Q3/Q4/Q5 更新，+Q6 相分解、Q7 TBC-TGO）、`directions/ceramic-corrosion/synthesis/literature-map.md`（+3 论文、+4 claims、+2 方法路线、+TBC-TGO gap）、`directions/ceramic-corrosion/synthesis/core-argument-map.md`（6 篇语料、主线扩充）、`directions/ceramic-corrosion/index.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`（#16/#29/#48 已入库 + 附件键 + 缓存附录更正）。
- 发现：#16 揭示 1500 °C 保温无反应、冷却起始析出 + 相分解诱导晶间渗透（219 μm，1300 °C 的 >4 倍），与 #47 构成 1500 °C 双证据；#48 渗透排序与平均 RE 半径完全对应（固溶体/高熵体系半径规律证据），并首次在 RE2SiO5-CMAS 鉴定石榴石型产物；#29 表明 Hf6Ta2O17 与 TGO 在 >1400 °C 反应生成 AlHf3TaO10、界面热应力超 YSZ 许用——TBC 选材缺 TGO 相容性判据。
- 后续：待运行 `agents/lint_agent.md` 健康检查（本轮批次后例行）；继续入库 CMAS 优先 #36/#23/#52。

## [2026-08-28] synthesis | 激活研究定位与综述大纲（暂停入库后第一步）

- 输入：用户指示暂停入库、进入下一步；经确认选择「研究定位 + 综述大纲」。
- 操作：按 AGENTS.md 路由，以 gap_agent 流程激活 `directions/ceramic-corrosion/synthesis/research-positioning.md`，以 review_agent 流程激活 `directions/ceramic-corrosion/synthesis/review-outline.md`；两页均由模板状态转为 active。
- 新建：无（两页为激活，非新建）。
- 更新：`directions/ceramic-corrosion/synthesis/research-positioning.md`（研究主线三层结构、5 条可继承方法、3 个拥挤方向、6 个切入空间、3 条定位方向：1500 °C 跨体系抗性地图 / 相稳定性优先设计 / TBC-TGO 相容性判据）；`directions/ceramic-corrosion/synthesis/review-outline.md`（核心论题三段式、六节大纲、8 个 claim 章节映射、核心论题段草稿）；`directions/ceramic-corrosion/index.md`、`directions/ceramic-corrosion/synthesis/core-argument-map.md`、`directions/ceramic-corrosion/log.md`。
- 发现：3 条定位方向均为 AI 基于 6 篇语料的推断（已在页内标注），待用户填写 `directions/ceramic-corrosion/memory/project_profile.md` 核心研究问题与 Excluded 范围后校准；Positioning 1/2 存在窗口期风险（田志林组工作节奏快，Q4 提示需检索该组 2026 新工作）；Positioning 3（TBC-TGO）与主线偏离度最大，标注供用户权衡。
- 后续：与用户讨论定位方向取舍；按选定方向决定是否恢复入库及选号（Positioning 1 对应 CMAS 优先 #36/#23/#52）。

## [2026-08-28] query | 窗口期检索：该组 2026 新工作 + X1 反向报道溯源

- 输入：定位方向讨论前的证据核查（Positioning 1/2 窗口期风险、Q5/X1 争议溯源）。
- 操作：WebSearch 检索田志林组 2026 年 CMAS 相关工作与 X1-RE2SiO5 反向报道原始文献；结果全部标注「待核查原文」写入知识库。
- 新建：无。
- 更新：`directions/ceramic-corrosion/inbox.md`（Pending Papers +6 篇检索候选，均不在田老师 collection 清单内）；`directions/ceramic-corrosion/synthesis/research-positioning.md`（Positioning 1 风险具体化——该组已发表 Extreme Materials 2025 层叠法 RE2SiO5 筛选，窗口部分收窄；Positioning 2 补第三方佐证；Next Evidence Needed 更新）；`directions/ceramic-corrosion/synthesis/open-questions.md`（Q1 补 Li et al. 2025 第三方方向佐证；Q5 反向报道源头锁定 #36）；`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`（争议 1 与 Uncertainty 的 X1 条目溯源更新）；`directions/ceramic-corrosion/log.md`。
- 发现：① Extreme Materials 2025（1(4): 27–32）层叠法 RE2SiO5 筛选不在 import_plan 58 篇清单内，若已含 1500 °C 则 Positioning 1 的 RE2SiO5 部分被抢占；② X1 反向报道源头为 #36（Tian et al., Corros. Sci. 2019, DOI: 10.1016/j.corsci.2018.12.032），检索摘要显示其整体趋势与主线一致（小半径层薄），争议可能在 X1 亚组内部；③ Li et al.（Ceram. Int. 2025）高熵单硅酸盐 1500 °C 层厚随平均半径单调递减，与 #47 高温反转方向一致，为第三方方向佐证。
- 后续：检索候选论文是否补录入库待用户确认；定位方向取舍待用户决定。

## [2026-08-28] ingest | 入库 #36（Tian 2019 Corros. Sci.，1300 °C 单硅酸盐总规律）——X1 争议核实

- 输入：用户「先补证据再定」——为核实 X1 反向报道与 1300 °C 主线证据，短暂恢复入库 #36（缓存 9612/full.md 已就绪）。
- 操作：按 MinerU 缓存优先流程读取 9612/full.md 全文；新建论文页并联动更新 2 个 claim、2 个 gap、主题页、index、import_plan、全部 synthesis 页。
- 新建：`directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend.md`。
- 更新：`directions/ceramic-corrosion/wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend.md`（+#36 奠基证据链，六篇独立支持；X1 反向挑战项溯源至 #21 JECS 2019）、`directions/ceramic-corrosion/wiki/claims/Garnet-Product-RE2SiO5-CMAS.md`（+#36 铝酸盐石榴石 RE3Al5O12 对照，两类石榴石区分）、`directions/ceramic-corrosion/wiki/gaps/Cooling-Precipitation-Coating-Integrity.md`（+#36 冷却热应力剥落最早证据）、`directions/ceramic-corrosion/wiki/gaps/Structure-Radius-Decoupling.md`（+X1/X2 晶型翻转证据）、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`（+论文/代表论文/共识 1/争议 1/3、Uncertainty）、`directions/ceramic-corrosion/index.md`、`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`（#36 → 已入库）、`directions/ceramic-corrosion/synthesis/literature-map.md`、`directions/ceramic-corrosion/synthesis/core-argument-map.md`、`directions/ceramic-corrosion/synthesis/open-questions.md`、`directions/ceramic-corrosion/synthesis/research-positioning.md`、`directions/ceramic-corrosion/synthesis/review-outline.md`。
- 发现：① #36 为 1300 °C 半径规律奠基工作——8 组分衰退层-半径近似线性 + Risbud 量热 + 光学碱度 ΔΛ 判据（Tb 0.134 → Lu 0.094），Lu2SiO5 约 50 μm/50 h 与 #16 的 1300 °C 对照定量吻合；② X1 反向报道澄清：源头为 #21（Tian et al., JECS 2019, DOI 10.1016/j.jeurceramsoc.2018.12.015，La/Nd/Sm/Eu/Gd X1 系列），#36 覆盖 Tb–Lu 段为递减趋势——1300 °C 半径规律存在晶型依赖翻转，归入 Structure-Radius-Decoupling gap；③ #36 单组分小半径组检出铝酸盐石榴石 RE3Al5O12（与 #48 硅酸盐石榴石物相不同），产物谱争议需区分两类石榴石；④ 衰退层 E/TEC 失配的冷却热应力剥落是「冷却损伤」最早观察。
- 后续：恢复入库暂停状态；定位方向取舍待与用户讨论（Positioning 1 对应 CMAS 优先 #23/#52；检索候选 #59–64 待确认）；待运行 lint。

## [2026-08-28] query | 核实 #59（Extreme Materials 2025 层叠法 RE2SiO5）原文——定位方向证据补充

- 输入：用户选择「先核实 #59 再定」定位方向，并将 #59 加入 Zotero collection。
- 操作：定位 MinerU 缓存 10185（与 10070=#58 透波二硅酸盐区分）；通读 full.md 全文核实实验条件与结论。
- 新建：无（未正式入库）。
- 更新：`directions/ceramic-corrosion/raw/zotero_imports/田老师/import_plan.md`（#59 行 + 附录缓存映射）、`directions/ceramic-corrosion/inbox.md`（#59 条目标注已核实）、`directions/ceramic-corrosion/synthesis/research-positioning.md`（Positioning 1 Risks/Literature needed/Status）、`directions/ceramic-corrosion/synthesis/open-questions.md`（Q4）、`directions/ceramic-corrosion/wiki/claims/CMAS-Corrosion-Enthalpy-RE-Radius-Trend.md`（+Challenging Evidence：#59 渗透深度排序非单调）、`directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion.md`（+新争议：最优成分指标依赖）。
- 发现：① 腐蚀条件为 1300 °C/20 h 单温度（C33M9A13S45，30 mg/cm²）——**未覆盖 1500 °C，RE2SiO5 高温窗口未收窄**；② 按渗透深度排序 Er2SiO5 最浅（非 Lu）——与 #36 衰退层厚度指标（Lu 最薄）不一致，最优成分因评价指标而异；③ 产物量仍随半径减小而减少（形成焓规律成立），但小半径端渗透反而深于 Er（溶解强、析出弱）；④ 观察到大半径侧热应力裂纹（Y2SiO5 区域，σ=EαΔT）——与 #36 冷却损伤一致；⑤ Y 缺 4f 电子被用来解释偏离规律。
- 后续：#59 是否正式入库待用户决策（缓存已就绪）；定位方向取舍重新开放（Positioning 1 高温窗口未收窄但需先统一评价指标）。


## [2026-09-05] lint | 本地知识库系统流程检查

- 输入：用户暂停论文修改，要求先检查系统是否造成执行繁杂。
- 操作：检查规则、路由、模板、上下文和七篇论文基础元数据；八个启动文件合计 31,896 字符。
- 新建：directions/ceramic-corrosion/docs/system-audit-2026-09-05.md。
- 更新：directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：启动读取过重、缺少局部修订和下游待复核机制；2022 高熵论文元数据类型错误；执行者重复读取和补丁错误也增加耗时。
- 后续：先分步调整系统，再恢复论文修订。本轮未改规则、论文或综合结论；未执行完整事实/链接审计。

## [2026-09-05] review | 完整规则审视与分步完善计划

- 输入：用户要求完整了解现有规则，重点审视论文解读、评价、总结和入库机制，并设计分步完善计划。
- 操作：通读或复用本次连续检查中已读的入口、六个任务规则、七个模板、八个 memory 文件及配套说明；将缺口映射到证据提取、判断、比较、gap、大纲和维护流程。
- 新建：directions/ceramic-corrosion/docs/rules-improvement-plan.md。
- 更新：directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：现有原则并非缺失，但缺少可操作的证据类型/强度/核查区分、比较资格、独立数据溯源、下游复核状态和语义验收；执行者也有未落实已有规则的问题。
- 后续：九阶段计划尚未实施；建议先修改 hard_memory 与 AGENTS 中公共证据底线和任务边界，再改论文阅读规则与模板。本轮未修改业务规则、论文或综合结论。

## [2026-09-05] update | 规则完善阶段 1：公共证据标准与任务边界

- 输入：用户要求按九阶段计划逐步完善。
- 操作：修改 AGENTS.md 与 memory/hard_memory.md，区分三类论文任务及证据类型/支持程度/核查状态；明确增量读取、索引更新条件、原件保护与下游待复核规则。
- 新建：无。
- 更新：上述两份核心规则；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md 维护记录。
- 发现：转引、计算、指标不一致和未观察到等典型案例已有对应判断边界；旧任务/模板按新公共规则过渡。桌面案例与格式检查完成，尚未做真实论文试运行。
- 后续：阶段 2 修改 pdf_read_agent 和两份入库模板；本轮未修改论文或综合结论，不自动进入下一阶段。

## [2026-09-05] update | 版本快照 calude_wiki_gpt1

- 输入：用户明确要求上传当前版本，并命名为 calude_wiki_gpt1。
- 操作：将当前知识库未提交内容及规则完善第 1 阶段纳入版本，提交名和 Git 标签均为 calude_wiki_gpt1；目标为现有 origin/main。
- 新建：Git 版本标签；无新增论文内容。
- 更新：directions/ceramic-corrosion/index.md 版本说明；清理本次核查产生的三个临时脚本/状态文件，不上传原始 PDF 或忽略的 Zotero 资料。
- 发现：准备时远程 main 与本地基线一致，远程不存在同名标签；此快照不表示七篇论文结论已完成修订。
- 后续：推送结果以远程 main/tag 引用核验为准；后续继续规则完善第 2 阶段。

## [2026-09-06] update | 规则完善阶段 2：论文阅读与入库模板

- 输入：用户要求继续第二阶段。
- 操作：重构 pdf_read_agent、pdf_ingestion_template 和 paper 模板；建立来源身份、实际覆盖、关键原件回查、E# 证据记录、结论七步评价、三种任务模式与下游复核流程。
- 新建：无。
- 更新：上述三份规则/模板；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：旧流程的重复长模板已被拆成过程检查单与唯一 paper 输出；processed 与证据复核状态已分开；阶段 3 前旧 claim/topic/method 仍沿用旧结构。
- 后续：三份文件 YAML、格式及典型错误桌面验收通过；未修改论文或综合结论。下一阶段规范 claim、topic、method 模板。

## [2026-09-06] update | 规则完善阶段 3：claim、topic、method 模板

- 输入：用户要求继续下一阶段。
- 操作：重构三类可复用知识模板；claim 增加单一论断、独立数据来源组和使用门槛，topic 增加语料覆盖与代表性，method 增加操作定义、验证用途和误用边界。
- 新建：无。
- 更新：templates/claim.md、templates/topic.md、templates/method.md；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：旧 confidence/strong/weak 自由文本不再作为模板核心；同源转引、不可比冲突和“被使用即有效”均有明确拦截字段。旧知识页面仍需后续逐页迁移。
- 后续：三份模板 YAML、格式和典型错误桌面验收通过；未修改任何论文、claim 实例或综合页面。下一阶段规范 synthesis、gap agent 和 gap 模板。

## [2026-09-06] update | 规则完善阶段 4：跨论文综合与 Gap

- 输入：用户要求继续下一阶段。
- 操作：重构 synthesis_agent、gap_agent 和 gap 模板；增加语料边界、比较矩阵、三级比较资格、独立数据来源、冲突检查、gap 四级分类与新颖性检索记录。
- 新建：无。
- 更新：agents/synthesis_agent.md、agents/gap_agent.md、templates/gap.md；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：不同指标/条件不再允许直接求倍数或统一排名；共同转引不重复计数；未完成范围明确的检索时，gap 只能停留在论文局限、语料缺口或候选问题。
- 后续：规则/模板 YAML、格式和典型案例桌面验收通过；未修改实际 synthesis、gap 或论文页面。下一阶段规范 review_agent 和 review 模板。

## [2026-09-06] update | 规则完善阶段 5：综述大纲与写作

- 输入：用户要求继续下一阶段。
- 操作：重构 review_agent 和 review 模板；增加写作契约、证据准入、Evidence Matrix、候选主线压力测试、章节 readiness、句子级来源追溯与前提变化后的重组规则。
- 新建：无。
- 更新：agents/review_agent.md、templates/review.md；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：旧大纲、日志和 synthesis 不再能单独支撑写作；needs-review 或不可比证据不能写成确定事实；核心证据失效会触发 thesis 和章节结构重审。
- 后续：规则/模板 YAML、格式和典型案例桌面验收通过；未修改实际 review、综述大纲或论文。下一阶段完善上下文、project profile 和风格规则。

## [2026-09-06] update | 规则完善阶段 6：上下文与项目适配

- 输入：用户要求继续下一阶段。
- 操作：将固定启动清单改为增量读取与任务恢复；在 context_policy 保存短状态；分离用户目标、语料观察与可选 CMAS 阅读项；统一来源定位要求和阶段汇报风格。
- 新建：无。
- 更新：directions/ceramic-corrosion/memory/current_context.md、directions/ceramic-corrosion/memory/project_profile.md、memory/style_snapshot.md；directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/memory/decision_log.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：旧规则把操作待办混入科学论点页，且将证据定位列为待确认偏好；新规则明确分工，保留用户原有来源与批次配置。
- 后续：增量恢复、局部修订和领域适配案例已桌面审查，格式与范围检查通过；未修改论文或综合页。下一阶段完善 lint 与维护规则。

## [2026-09-06] update | 规则完善阶段 7：校验与维护

- 输入：用户要求继续第七阶段。
- 操作：重构 lint 的结构/证据/流程检查、问题分级和旧页迁移；更新标签状态语义、术语同义边界与历史决策适用性。
- 新建：无；本阶段未增加自动校验工具。
- 更新：agents/lint_agent.md、directions/ceramic-corrosion/memory/tag_taxonomy.md、directions/ceramic-corrosion/memory/term_aliases.md、directions/ceramic-corrosion/memory/decision_log.md；directions/ceramic-corrosion/memory/current_context.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/log.md。
- 发现：有限抽查确认 2022 论文仍有类型及来源字段问题，保持待迁移；别名表的失效推荐页已改为目录导航，研究方向和相关概念不再被当成同义定义。
- 后续：规则桌面审查、有限结构抽查与差异格式检查完成；未执行整库语义检查或修改科学页面。下一阶段对齐入口及来源说明。

## [2026-09-06] update | 规则完善阶段 8：入口及来源说明

- 输入：用户要求继续第八阶段。
- 操作：对齐候选集合、已知来源、已有页修订的任务路由；明确工具可用性、稳定清单编号、生成记录同步、已有授权复用与独立发行范围。
- 新建：无。
- 更新：agents/import_zotero.md、agents/pdf_read_agent.md、CLAUDE.md、README.md、QUICKSTART.md、docs/zotero-workflow.md、docs/initialization.md、docs/privacy-and-gitignore.md；计划、index、context_policy、decision_log、error_log、log。
- 发现：旧入口重复启动与确认、固定联动以及发布约束已对齐公共规则；不会因已入库而跳过用户要求的修订。
- 后续：manifest 示例 JSON 解析、本地链接、冲突措辞与差异格式检查通过。未连接 Zotero、修改 directions/ceramic-corrosion/raw/wiki/synthesis 或提交推送；下一阶段以 2019 论文逐节试运行。

## [2026-09-06] query | Zotero MCP 原文连接核验

- 输入：用户指出可通过 Zotero MCP 索取 PDF/MD，要求尝试连接和读取。
- 操作：当前会话没有直接 Zotero 工具；从本机现有配置发现端点，完成 initialize、tools/list 及只读 get_item_details/get_content 调用；实际打开 PDF 验证 12 页。
- 新建：无。
- 更新：本记录、context_policy、error_log；未修改 Zotero 条目、附件或论文页。
- 发现：服务 zotero-integrated-mcp 1.1.0 在 http://127.0.0.1:23120/mcp 可用；9Q7A46HL 的附件 R6YQ3KNM 是链接附件。PDF 实际路径为 `C:/Users/youthcookie/OneDrive/1.Science/1.Zotero/pdf2/2019-(Corrosion Science)/Tian 等 - 2019 - General trend on the phase stability and corrosion resistance of rare earth monosilicates to molten.pdf`；此前 storage 目录无 PDF 不能证明原件缺失。
- 后续：get_content 使用 complete + preserveOriginal + prioritizeCompleteness + maxContentLength=100000 返回 33875 字符，truncated=false；preview 会抽句压缩，不用于证据完整性判断。MD 仍可复用 `D:/shuju/zotero1/llm-for-zotero-mineru/9612/full.md`。连接与读取已验证，论文修正尚未写回，继续阶段 9 时直接核对原 PDF。

## [2026-09-06] error-fix | 阶段 9：2019 论文复核与修订

- 输入：用户要求定位 llm-for-zotero 生成的 MD，继续第九阶段核对。
- 操作：核对 9612/_llm_source.json 与 PDF 映射，复用已读全文/图表并回查 PDF 争议段落及原页，写回 E1–E8 和保留/限定/撤回结论。
- 新建：无知识页；仅在系统临时目录渲染 PDF 页供核查。
- 更新：directions/ceramic-corrosion/wiki/papers/2019-RE2SiO5-CMAS-General-Trend.md；index、计划、context_policy、error_log、log。
- 发现：当前 PDF 形成焓措辞存在内部不一致；OB 只有七种数据且不是定量预测；跨材料图指标与条件混杂；裂纹观察不能独立证明冷却起裂；X1/X2 翻转及“首次/最早”缺乏本轮证据。
- 后续：论文主要证据按声明范围 checked，原始重复统计、晶型/跨文献比较与正式版差异保留未决；下游具体影响见论文页，其他六篇和综合页未改。YAML、证据编号、链接与差异格式检查通过；第九阶段单篇试运行完成，未提交推送。

## [2026-09-06] error-fix | 2023 RE₂SiO₅–CMAS 原位降解论文复核

- 输入：用户要求继续复核下一篇；沿 2019 半径趋势问题继续复核 2023 原位降解论文。
- 操作：通过本机 Zotero MCP 核对 TLPXY39S 的三份附件及 9513/_llm_source.json；MD 对应 T33IHQL9 中英混排附件，改以 9VVGQ2M5 英文 PDF 为主。阅读英文正文并视觉核对 pp. 4、8、9、12、13、14；建立 E1–E8，逐项替换过强总结。
- 新建：无知识页；PDF 核查图仅写入系统临时目录。
- 更新：directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation.md、directions/ceramic-corrosion/index.md、directions/ceramic-corrosion/docs/rules-improvement-plan.md、directions/ceramic-corrosion/memory/current_context.md、directions/ceramic-corrosion/memory/error_log.md、directions/ceramic-corrosion/log.md。
- 发现：Ho 升温过程误归 Er；20 h 缺 Tb、50 h 缺 Tb/Dy/Ho；Fig. 18 的 5 h 趋势非严格单调。黏度来自 FactSage，2019/2023 指标及实验条件不一致，不能确证黏度造成半径反转。Fig. 15(c) 为 1223 °C，约 1400 °C 析出起始仅按正文报告。
- 后续：ESM Fig. S1–S3、Movie S1–S3 未取得/未读；测量端点、起始时间、模型复现和下游论断保留待核。YAML、E1–E8 唯一性、源页双链及差异格式检查通过。现已按声明范围复核 2/7 篇，其余五篇和下游逐项处理；原始资料未改，未提交或推送。

## [2026-09-06] update | Claude_wiki_all 版本上传

- 输入：用户明确要求上传当前版本，并将上传记录命名为 Claude_wiki_all。
- 操作：将当前规则、模板、文档及 2019/2023 论文复核改动纳入同一版本；提交名及版本标签均使用 Claude_wiki_all，上传目标为现有 origin/main。
- 新建：版本标签 Claude_wiki_all（随本次提交创建）。
- 更新：本次版本包含此前尚未提交的阶段完善与两篇论文修订，以及本条操作记录。
- 发现：差异格式检查通过；本次变更为 Markdown 文档，没有新增原始 PDF 或 Zotero 附件。
- 后续：提交后核对远程 main 与同名标签是否指向本次提交；论文复核仍为 2/7 篇按声明范围完成，其余五篇及下游待逐步处理。

## [2026-09-07] error-fix | 2024 Lu₂SiO₅–CMAS 原位论文复核

- 输入：用户要求继续复核下一篇，沿高温解释核对 2024 Lu₂SiO₅ 论文。
- 操作：复用 10149/full.md，核对 _llm_source.json 与 manifest；本机 Zotero MCP 确认 RLNIRS7B/JNS38XK5 及实际链接路径，读取 9 页英文 PDF 关键文字并视觉核对 pp. 3–8（Fig. 1–10）。建立 E1–E8 并替换总结。出版社入口返回 403，Movie 1/2 未取得。
- 新建：无知识页；核查用 PDF 图仅写系统临时目录。
- 更新：2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth 论文页、index、计划、context_policy、error_log、log。
- 发现：初始 0.3 wt% 杂相、Fig. 4(d) 保温温标与正文析出叙述冲突、Fig. 8(c) 的二硅酸盐相标均被旧总结忽略；TEM 不构成排他证明，2019 对照与本文指标不同，四倍及独立半径反转结论撤回。
- 后续：按声明范围复核 3/7 篇；视频时序、定量相鉴定、原始统计与下游论断保留待核。原始资料及其他论文未改；本轮未提交或上传，既有 Claude_wiki_all 对应 1381ee0 已在此前推送并核验。

## [2026-09-07] error-fix | 2022 高熵 RE₂SiO₅–CMAS 论文复核

- 输入：用户继续要求复核下一篇，处理 2022 高熵四元硅酸盐。
- 操作：MCP 核对 8IPQUSQL 三份附件及 10117/10119/10121 缓存；以 I929AL9M 英文 PDF/10119 为主，读取主要章节并视觉回查方法及关键图表。建立 E1–E8，恢复 paper 类型和论文元数据。
- 新建：无知识页；PDF 核查图仅存系统临时目录。
- 更新：2022-High-Entropy-RE2SiO5-CMAS-EBC 论文页、index、计划、context_policy、error_log、log。
- 发现：译文误作补充材料、块体杂相遗漏、热物性计算/文献对照混写；HE 腐蚀性能介于单组元之间，不支持全面优越；石榴石类别有 XRD 支持，但 EPMA 近似比值及 Eq. (12) 配平存在原文疑点。
- 后续：当前按声明范围复核 4/7 篇，其余三篇与下游逐步处理；腐蚀端点/统计、精确相组成及机制归因仍待核。原始资料和其他论文未改，本轮未提交或上传。

## [2026-09-07] error-fix | 2025 RETaO₄–CMAS 高通量论文复核

- 输入：用户继续复核下一篇。
- 操作：MCP 核正 88RPHLC9/9TBX9XTZ/10100；核对正文 Fig. 1–17/Table 1，实际取得 Europe PMC 正式补充 ADVS-12-2412717-s001.docx 并读四表六图；建立 E1–E8。
- 新建：无知识页；核查图与补充副本仅在系统临时目录。
- 更新：2025 RETaO₄ 源页及 index、计划、context_policy、error_log、log。
- 发现：跨 RE 成分限制层间独立性；深度非严格单调，TEM 限 Y/Nd，50% 为阳离子归一化；Fig. 15 的正值/参考态和润湿解释未决。
- 后续：完成声明范围 5/7；其他论文、下游和原件未改，未提交上传。此记录在最后一篇复核时恢复前次问号化中文，依据已保存的源页与本会话核查记录，不表示重新执行来源读取。

## [2026-09-07] error-fix | 2026 高熵锆酸盐–CMAS 高通量论文复核

- 输入：用户继续复核下一篇。
- 操作：确认 YPQHNP84/L4TEUBTX/10087；核对正文 Fig. 2–13，取得官方 mmc1.docx 并实际读五表八图；建立 E1–E8。
- 新建：无知识页；补充与核查图仅存临时目录。
- 更新：2026 高熵锆酸盐源页及维护记录。
- 发现：重复 S4 表号、样品标签和半径/畸变/密度映射冲突、热导端点差异；最高 TEC 图表对应 S2 而非正文 S12；保留产物/厚度量级，暂停定量规律和双机制确证。
- 后续：完成声明范围 6/7；原始映射、精确计量及机制未决，未提交上传。此记录恢复前次有损编码内容，依据源页和会话记录，未重复执行论文阅读。

## [2026-09-07] error-fix | 2025 Hf₆Ta₂O₁₇–Al₂O₃ 相容性论文复核

- 输入：用户要求复核最后一篇。
- 操作：MCP 确认 5PSRPWAQ/GSDAE8IV，核对 10141 的来源映射/manifest；阅读主要章节、正文 Fig. 1–12/Tables 1–3，复算模量、热应力和局部错配；另核 Li 前文出版社摘要及日期。建立 E1–E8。
- 新建：无知识页，核查图仅存临时目录。
- 更新：2025 Hf 源页、index、计划、context_policy、error_log、log；同时修复前两轮问号化维护记录及滞后快照。
- 发现：1400 °C 已反应；2.93 μm 为热压 10 min 初始层，追加退火 10/30/50 h 为 3.16/4.32/4.61 μm。Spot 2/3 及线扫归一化存在源内问题；应力为可复算模型，不能套 YSZ 剪切判据判废。Li 前文摘要为 1600 °C/8 h、2012 年在线，并非温度不足。
- 后续：七篇源页按声明范围复核完成（7/7）；局部未决和下游论断仍需逐步处理。原件和下游正文未改，未提交上传。

## [2026-09-07] error-fix | 维护记录中文编码与恢复状态修复

- 输入：本轮启动发现快照仍写四篇/2022，数字却为 6/7，前两轮 log/error_log/index 中文变成问号。
- 操作：确认此前 PowerShell 管道向 Python 传中文存在有损编码；改用 Unicode 安全补丁，按会话和已保存源页恢复两轮记录并更新完整 7/7 快照。
- 新建：无。
- 更新：index、log、error_log、context_policy、计划。
- 发现：此前只校验进度数字与 YAML，未验证实际中文和完整状态，故“维护已同步”的报告不准确。
- 后续：维护写入检查问号/替换字符、中文标题及状态内容；不能以读取成功或退出码代替文字正确性。

## [2026-09-07] synthesis | 基于七篇复核证据修订八项 claim

- 输入：用户要求基于复核结论进入下一步，并要求继续工作。
- 操作：按 synthesis_agent/claim 模板复用七篇 E1–E8，逐项审查命题范围、证据类型、独立来源、比较资格及下游影响；替换旧正文和 confidence。
- 新建：无。
- 更新：directions/ceramic-corrosion/wiki/claims 下八页、index、规则完善计划、context_policy、error_log、log。索引注明旧 gap/topic/综合结论仍待修订。
- 发现：四项限定事实 supported，一项机制 partially-supported，三项因果假说 insufficient-evidence；八页均 checked，仅表示本轮证据评价完成。重复的 2019 对照和 Costa 转引不增加独立支持，缺失原始映射/视频/引用全文仍保留。
- 后续：先处理五个 gap 前提与领域证据资格，再更新 topic、综合矩阵和大纲。未重新读全部 PDF、未改原件或其他论文正文、未提交或上传；用户研究目标未被重设。
- 检查：八页 YAML/Assessment 一致，125 个双链目标及所用 E# 锚点通过；旧 confidence/Key Claim 引用已移除，中文编码检查与 git diff --check 通过。检查范围为本轮 claim 与维护文件，不代表整库科学结论通过。

## [2026-09-07] gap | 基于新版 claim 修订五项 gap

- 输入：用户要求继续下一步。
- 操作：按 gap_agent/template 审核五页旧前提，复用已核 paper E# 与八项 claim；区分语料覆盖和领域新颖性，替换过强判断并补检验/失败条件。
- 新建：无。
- 更新：directions/ceramic-corrosion/wiki/gaps 下五页、index、计划、context_policy、error_log、log。
- 发现：1 corpus-gap、4 candidate-question，均 narrowed/checked；novelty_status 均 not-assessed，priority 均 pending。旧晶型翻转、纯冷却析出、筛选无偏和 TGO 必然失效不能作为前提；固定分子分母却改变半径比的实验提案不成立。
- 检查：五页 YAML/分类及 88 个双链目标/E# 锚点通过；使用既有标签，五问题对象不同，未重复建页。科学范围仅本地语料前提评价，未做新颖性检索或执行所提实验。
- 后续：同步两个 topic 与综合证据矩阵，然后重构开放问题、定位及大纲。未修改原始资料、paper/claim 正文，未提交或上传。

## [2026-09-07] synthesis | 更新两个 topic 与七篇综合证据矩阵

- 输入：用户要求继续下一步。
- 操作：复用已核 E1–E8、八项 claim 与五项 gap，检查旧主题/地图，把领域共识降回当前语料认识；建立实验、计算/共同转引、比较资格和未决冲突矩阵。
- 新建：无。
- 更新：两个 topic、directions/ceramic-corrosion/synthesis/literature-map、index、计划、context_policy、error_log、log。
- 发现：旧主题仍将用户未确认方向写为课题主线，并把同源对照、不可比厚度、模型/转引与局部表征合成普适共识；本轮已替换正文。
- 检查：三页 YAML/中文、178 个链接与 E# 锚点、八项 claim 支持等级和五项 gap 分类一致性通过；数据来源组不等于独立统计重复。
- 后续：四个综合页 open-questions/research-positioning/review-outline/core-argument-map 仍待修订；历史 topic/matrix 待办由本次记录接续。原始资料和 paper/claim/gap 正文未改，未执行新颖性检索，未提交或上传。

## [2026-09-07] review | 重构开放问题、候选定位与证据驱动大纲

- 输入：用户要求继续下一步。
- 操作：按 review_agent/template 复用新版矩阵与源页，替换旧三个核心论题；Q1–Q7 重评，三个定位降回条件性提案；建立 R1–R8、主线压力测试、五节加可选界面模块、三段带句证映射的草稿。
- 新建：无。
- 更新：open-questions、research-positioning、review-outline、core-argument-map、index、计划、context_policy、error_log、log。
- 发现：旧公理/高温反转/缺失判据主线不成立，不能仅加免责声明；原定位的方向拥挤度、空白窗口和可行性承诺缺少对应证据。当前用户目标仍未确定。
- 检查：四页 YAML/中文、165 个双链及 E# 锚点、Q1–Q7/R1–R8 唯一编号、三段证据映射通过。大纲/定位保持 draft，所有页面的 checked 限于本轮映射核查。
- 后续：声明范围内七篇源页及下游链迁移已接续完成；可逐段写作或按指定问题补证据/检索。原始未决、全文写作、新颖性和选题确认未完成。未修改原始资料，未提交或上传。

## [2026-09-08] update | calude_wiki_R 版本快照

- 输入：用户明确要求上传当前版本，记录为 calude_wiki_R。
- 操作：核对 origin/main 与同名标签，提交当前工作树修订并以同名标签上传；远程落点通过 Git 核验。
- 新建：版本标签 calude_wiki_R。
- 更新：源页复核、八项 claim、五项 gap、两个 topic、五个 synthesis、维护记录及当前 Obsidian 图谱缩放配置。
- 边界：原始论文/私有附件仍按忽略规则排除；原文未决和定位/大纲草稿状态不因发布升级。
- 后续：本次上传结果以 origin/main 与标签指向核验为准；后续改动不自动发布。

## [2026-09-08] query | 田老师 collection 当前候选核对

- 输入：用户要求按当前研究方向检查还有哪些文章可入库；按候选清单任务执行。
- 操作：连接本机 Zotero MCP，读取 LED7JJ3Y 完整59条元数据及相关候选摘要，核对7个paper的item key/DOI；读取陶瓷+腐蚀子collection为空，未读专利/吸波内容。
- 新建：directions/ceramic-corrosion/docs/collection-candidates-2026-09-08.md。
- 更新：import_plan/manifest、inbox、index、log、error_log；64个旧编号保持一致，其中59条当前父collection、5条外部候选。
- 发现：57篇期刊+1书章+1笔记；7篇已入库，其余50篇期刊及1书章无当前paper页。#59已在collection，#13/#17现在有PDF附件，旧清单/manifest状态滞后。
- 后续：建议先#59，#21准备原文，其间可读#17/#23，再按范围考虑#38/#13；#52用于综述导航。仅元数据/摘要筛选，未读候选全文、未创建paper、未改Zotero或上传。


## [2026-09-08] ingest | #59 RE₂SiO₅–CMAS 层叠筛选

- 输入：用户指定 #59；Zotero X55RXI85/JNPL926R，MinerU 10185 与6页英文PDF。
- 操作：核对身份、阅读MD全文、回看PDF Fig.1–7及Eq.(1)；区分相对深度、产物形貌、作者机制与转引。
- 新建：[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening]]，processed/checked（主文声明范围）。
- 更新：比较矩阵、CMAS主题、半径—焓claim、层叠迁移gap、索引/恢复记录与导入计划/manifest；三个写作页记录新增证据交接。当前8篇。
- 发现：Er为相对深度零点而非零侵入；形成焓方向源内不一致；MD公式错序。补充S1未取得，出版商入口403。
- 后续：补S1/统计/独立性证据；按用户范围扩写评价与筛选段。原文和Zotero未修改，未提交/上传。


## [2026-09-08] review | 整合#59并更新综述大纲

- 输入：用户要求继续整合#59；复用已核论文E1–E8及本地写作规则。
- 操作：将相对Er测厚、产物/侵入分开评价、层叠独立性与供液边界纳入写作证据和章节；完成T1依赖压力测试。
- 新建：无独立页面；大纲新增R9/R10、小节卡片、两段草稿及定向补证据表。
- 更新：review-outline、open-questions的Q1/Q4/Q5、research-positioning的P1、#59下游记录、index及恢复记录。
- 发现：#59加强评价指标论证，但不足以证明普适排序、两温反转或独立试样等效；不提升机制claim或新颖性。
- 后续：大纲现含8篇、5段草稿，仍draft；可展开第1节并定向补证据。未新增文献、未开展网页检索、未提交上传。

## [2026-09-08] update | 版本上传 calude_wiki_59_outline

- 输入：用户要求上传并记录本次上传。
- 操作：将当前候选核对、#59入库及大纲整合成果提交为 `calude_wiki_59_outline`，使用同名附注标签定位版本；目标为 `origin/main`（https://github.com/neuhanxiaobo1/Claude-wiki）。
- 新建：#59论文页、2026-09-08候选报告及同名版本标签。
- 更新：相关主题/claim/gap、比较矩阵、大纲R1–R10与五段草稿、Q1/Q4/Q5、P1及索引/维护记录。
- 发现：当前8篇论文；S1等原文未决仍保留，大纲和研究定位仍为draft。
- 后续：上传是否完成以远程main与标签指向本提交的核验为准。原始PDF/MD与被忽略的本地导入管理文件不纳入Git上传；后续改动不自动发布。

## [2026-09-08] review | 第一节评价对象、测量基准与比较资格试写

- 输入：用户要求尝试扩写第一节；现有大纲R1/R9/R10及五篇源页的已核证据。
- 操作：形成1.1评价范围、1.2三种深度基准、1.3实验边界与比较资格的连续正文，配指标对照表；分开正文与写作核查记录。
- 新建：[[directions/ceramic-corrosion/wiki/reviews/CMAS-Review-Section-1-Evaluation-and-Comparability]]。
- 更新：大纲、Reviews索引与任务恢复记录；第一节为draft，证据映射在声明范围内checked。
- 发现：现有资料可支撑指标与比较边界论证；#59相对基准、2023缺测、跨论文2019转引与统计限制均已保留，不依赖未核S1机制。
- 后续：审阅第一节范围、行文与论证后，扩写第2节或按定向清单补证据。未新增论文、未访问网页、未提交上传本次草稿。


## [2026-09-08] ingest | #17 M-YTaO₄与#23 RE₂Si₂O₇

- 输入：用户明确授权两篇入库；MCP核对指定item/附件，本地MinerU10158/9636和8/10页PDF。
- 操作：阅读主要章节，PDF核对#17 Fig.1–7/Tables1–4与#23 Fig.1–12/Tables1–2；分开指标、相类别、物性与因果。
- 新建：[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]]；[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C]]，均processed/checked（声明范围）。
- 更新：比较矩阵、CMAS主题、RETa产物claim、高温gap、Q1、索引/恢复入口及导入管理；大纲/定位/第一节仅追加具体交接。库共10篇。
- 发现：#17深晶界侵入不等于浅表层厚；摘要热循环缺协议，局部未见分层不证寿命。#23有同篇两温50 h实验，但缺统一深度序列；内耗4/10 °C/min冲突且部分转引。
- 后续：按范围整合新证据到第一节和机制段；原始统计/机制未决保留。全部通过本地PDF/MD读取，无网页检索、无原件/Zotero改动、无提交上传。

## [2026-09-09] update | 上传 calude_wiki_10papers_section1 与进度背景整理

- 输入：用户要求上传、总结进度并介绍当前腐蚀研究背景。
- 操作：提交第一节试写、#17/#23入库及相关维护成果，使用同名附注标签；上传至origin/main（https://github.com/neuhanxiaobo1/Claude-wiki），远程完成以提交/标签核验为准。
- 新建：[[directions/ceramic-corrosion/docs/progress-and-background-2026-09-09]]；随本版本上传两篇新增论文页和第一节正文。
- 更新：索引、源页关联、比较矩阵、问题与恢复记录。当前10篇；大纲/定位仍draft，#17/#23的正文整合待接续。
- 发现：CMAS背景需分开应用需求、反应/侵入/损伤及评价口径；本地证据不等于领域新颖性检索。
- 后续：整合新增两篇至第一节/大纲后扩写第二节；原文未决保留。PDF/MD及被忽略导入管理文件不上传，后续改动不自动发布。


## [2026-09-09] update | 远程上传核验及#17/#23正式整合

- 输入：用户确认上传至既有GitHub仓库，并要求整合两篇论文。
- 操作：成功推送calude_wiki_10papers_section1；远程main与同名标签均解引用至3266d7161e854d1228f6679240740067422f55f2。随后完成新一轮正文整合。
- 新建：无独立页面；大纲新增R11–R13，第一节新增双深度、同篇两温和独立试样/损伤段。
- 更新：10篇大纲、七篇直接来源的第一节、P1/P2、Q3/Q4/Q6及索引/恢复/源页交接。
- 发现：同篇两温不等于统一深度反转，独立样品不等于已校准层叠，物性线索不等于软化/损伤因果确证。
- 后续：第一节可审阅，第2节可接续；本次后续整合尚未提交上传。

## [2026-09-09] query | 暂停扩写，背景文献查漏补缺

- 输入：用户要求2–3条Scopus检索式或网上下载候选。
- 操作：检查当前语料、大纲与定位；核查Scopus官方语法，初筛出版社页面。尚未实际运行Scopus，无检索命中数或完整性声明。
- 新建：无。
- 更新：本日志；未扩写、未新增入库或提升科学判断。
- 发现：建议补应用/天然沉积物背景、熔体组成与物性、实际涂层微结构及损伤。这是语料缺口，不是已确认领域gap。
- 后续：优先筛选2篇背景综述与4–6篇直接研究，获取PDF及补充材料后去重核查；暂不扩写第二节。

可复用Scopus Advanced Search检索式：

```text
TITLE-ABS-KEY((CMAS OR "molten silicate*" OR "volcanic ash" OR "sand deposit*") AND ("thermal barrier coating*" OR "environmental barrier coating*") AND (degrad* OR corrosion OR damage OR deposit*))

TITLE-ABS-KEY((CMAS OR "calcium magnesium aluminosilicate" OR "molten silicate*") AND ("rare earth silicate*" OR "rare-earth silicate*" OR monosilicate* OR disilicate* OR tantalate*) AND (composition OR viscosity OR wetting OR thermodynamic* OR dissolution OR crystallization OR precipitation))

TITLE-ABS-KEY((CMAS OR "molten silicate*") AND ("thermal barrier coating*" OR "environmental barrier coating*") AND (infiltration OR penetration) AND (microstructure OR porosity OR "thermal cycl*" OR stress OR crack* OR delamination OR spallation))
```

下载候选仅见出版社页面/摘要片段，未读全文、未查collection重复：

- Effect of CMAS viscosity on the infiltration depth in thermal barrier coatings of different microstructures：https://www.sciencedirect.com/science/article/pii/S0257897221012135
- Resistance of ytterbium silicate environmental barrier coatings against molten calcium-magnesium-aluminosilicate (CMAS): A comprehensive study：https://www.sciencedirect.com/science/article/pii/S0257897224001701
- CMAS infiltration behavior of atmospheric plasma-sprayed thermal barrier coating with tailored pore structures：https://www.sciencedirect.com/science/article/pii/S0272884223027980
- 语法来源：https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search

## [2026-09-09] error-fix | Scopus检索兼容性修正

- 输入：用户反馈通配符、特殊字符或字段代码报错。
- 操作：复查Scopus官方字段及高级检索说明；回复最小入口测试与三条不含通配符的替代式。
- 新建：无。
- 更新：directions/ceramic-corrosion/memory/error_log.md及本日志。
- 发现：TITLE-ABS-KEY为受支持字段；缺少实际提交式及入口，报错具体原因未确定，替代式亦未实际运行。
- 后续：用户先测试TITLE-ABS-KEY(CMAS)，再分别运行应用背景、熔体行为、涂层损伤三组查询；仍报错时核对完整输入和入口。

## [2026-09-09] query | Scopus三个collection与指定三篇标题摘要分层筛选

- 输入：用户指定scopus_1/scopus_2/scopus_3及田老师下陶瓷+腐蚀的三篇，要求基于标题和摘要筛选。
- 操作：本机Zotero Integrated MCP实时读取四个collection直接成员92/124/6/3条，分页至空页；225次成员记录对应186个不同item key及186个DOI/题名分组。39次为跨collection重叠；未改变Zotero条目。
- 新建：directions/ceramic-corrosion/docs/scopus-screening-2026-09-09/report.md、screening.csv；四份raw/zotero_imports下管理清单、manifest及本轮元数据/联合筛选记录（原件未修改）。
- 更新：index、context_policy及error_log中的元数据待核记录。
- 发现：12篇A优先、14篇B1第二批、87篇B2专题储备、73篇C本轮暂不纳入。全部检查题名及摘要/节选，A/B1完整摘要阅读，其余实际覆盖逐条标注；2篇缺摘要从已有PDF首页补读。仅指定3篇返回PDF附件，与现有10篇wiki未发现DOI/item key对应。
- 后续：先补优先候选全文和补充材料，再按2–3篇处理；没有自动入库或升级科学claim，没有上传。暂停扩写，EBC系统背景、原始热化学和层叠配对校准仍需补查。

## [2026-09-09] update | 筛选版本上传准备

- 输入：用户要求处理新文献前先上传当前版本。
- 操作：本次版本命名为calude_wiki_scopus_screening，包含#17/#23整合及186篇筛选报告、CSV和检索修正记录；上传既有origin main。
- 新建：版本提交与同名标签（结果以Git核验为准）。
- 更新：本日志。
- 发现：原始PDF和被忽略的raw管理文件沿用已有上传范围，不纳入本次提交。
- 后续：上传后独立增补陶瓷腐蚀方向的组内/组外及组外作者信息规则；本条不提前声明推送成功。

## [2026-09-09] update | 上传完成及方向专用作者信息规则

- 输入：用户要求先上传，后续区别组内/组外，额外记录组外一作/通讯作者单位、年份、国家与当前研究方向，仅作用当前方向。
- 操作：成功推送筛选报告版本87e3625；检查发现通用*.csv忽略规则排除配套表，显式加入该派生CSV并补推完整版本calude_wiki_scopus_screening_complete。远程main及完整标签均解引用至a383aef3b6261769800865b5cb702fd53faa57ce。
- 新建：directions/ceramic-corrosion/memory/reading_rules.md与synthesis/external-literature-register.md。
- 更新：仅project_profile加入方向规则入口、index导航、当前10篇paper的组内分类字段及恢复记录；未修改AGENTS、hard_memory、通用agent或通用模板。
- 发现：当前10篇作者元数据均含Tian Zhilin/Zhilin Tian，包括#17/#23，按用户指定口径记internal。未来新候选逐篇核查，不能按collection或检索批次判断。组外登记表当前为空，未虚构作者单位或研究方向。
- 后续：新入库组外论文按方向规则补充一作/通讯作者资料，非关键缺项待核；论文处理尚未开始。此次规则增补在上传快照之后，仍为本地未提交修改。

## [2026-09-09] update | calude_wiki_1版本记录

- 输入：用户要求上传当前版本，并命名为calude_wiki_1。
- 操作：将方向专用阅读规则、组外文献登记表、当前10篇组内分类及相关维护记录纳入同名提交和附注标签，推送既有origin main；远程完成状态以Git核验为准。
- 新建：calude_wiki_1版本提交及标签。
- 更新：index、context_policy及本日志的版本入口。
- 发现：本版本延续已上传的筛选报告与CSV；通用规则未改动，未新增论文入库。
- 后续：从calude_wiki_1接续，按方向规则处理选定组外论文，继续暂停扩写。

## [2026-09-09] decision | 多研究方向改造方案与分阶段边界

- 输入：用户要求将通用规则与方向规则分层，各方向独立文件夹、阅读/总结/记录，允许明确借鉴，并在开始工作时选择继续或新建方向；先设计再逐步实施。
- 操作：检查入口、公共记忆、领域规则、阅读流程尾部、模板路径引用、目录、最近日志、Obsidian与Git忽略配置；完成多方向方案，未执行目录迁移。
- 新建：[[docs/multi-direction-migration-plan]]。
- 更新：index导航、project_profile使用者身份及本日志、error_log；研究目标和科学证据未修改。
- 发现：CMAS检查仍在通用阅读流程；context_policy混合公共机制与方向进度；词表/日志需拆分；原raw忽略前缀和图谱path:directions/ceramic-corrosion/wiki/需随迁移调整。使用者旧“博士”记录与本轮教授身份不一致，已纠正。
- 后续：阶段0完成；下一步阶段1生成逐文件归属、旧新路径映射、完整备份与链接基线。阶段2协调启用规则和迁移现有方向；后续验收、新建实际方向及真实论文试运行。本轮未上传。

## [2026-09-09] update | 多研究方向改造阶段1：迁移准备完成

- 输入：用户同意方案并要求进入下一步；本轮范围为阶段1，尚不切换研究入口。
- 操作：盘点全部工作区源文件（排除Git对象、本地备份、本阶段生成目录），建立逐文件归属/新路径/哈希及混合文件逐段拆分表；生成ZIP并逐项读回核验，记录链接和路径引用基线。
- 新建：[[docs/migration-stage1-2026-09-09/report]]及配套JSON、拆分表、生成脚本；本地备份实际路径和哈希见summary.json。
- 更新：多方向方案、index及本日志；.gitignore新增/.migration-backups/并验证忽略生效。
- 发现：112个源文件、22个raw文件，10篇wiki论文；工作区raw没有PDF，外部Zotero/MinerU原件不在本备份。旧田志林与田老师清单独立保留；原始Si3N4笔记原文字节受保护，内部旧链接迁移后通过映射溯源。示例占位不作为知识页断链。
- 后续：阶段1完成，按报告进入阶段2前复查成员/哈希漂移，再协调拆分规则与迁移目录。现有研究文件未移动，研究结论/核查状态未修改，未提交上传。

## [2026-09-09] update | Scopus 筛选 C 级条目移入 Zotero 回收站

- 输入：用户要求将 Scopus 筛选结论为「C 本轮暂不纳入」的文献统一移入回收站（初始提供截图清单，图片未能加载，经确认以 screening.csv 全部 C 级为准）。
- 操作：经 Zotero MCP 写入操作（用户已开启插件 Write Operations）：先以 1 条（S003，ARMQ9DV5）试点验证「建临时 collection → 加入条目 → 删除 collection 连带条目进回收站」链路；再对剩余 72 条批量执行同一流程。notFound 为空，73 个 key 全部有效。
- 新建：无。临时 collection「C级-待删-20260909(-pilot)」执行后已删除。
- 更新：Zotero 文库状态（scopus_2 由 124 条减至 51 条）；本日志。
- 发现：删除后条目保留 key 但退出全部 collection、普通检索不可见，符合回收站语义；未被删除的 B1 条目（如 S061）检索正常。screening.csv 与 wiki 页面未改动。
- 后续：条目位于 Zotero 回收站，可恢复；如需彻底删除由用户在客户端清空回收站。C 级共 73 条，A/B1/B2 条目不受影响。本轮未提交上传。

## [2026-09-09] check | 回收站 73 条与当前研究方向相关性复核

- 输入：用户要求复核 73 条 C 级条目是否与当前研究方向（陶瓷-腐蚀、本轮 CMAS/TBC/EBC 涂层腐蚀背景）无关。
- 操作：按标题全量过筛，对 14 条疑似边界条目（硅酸盐熔体/玻璃物性、Si3N4/SiC 词面相关）调取 Zotero 摘要逐条核对。
- 更新：本日志。
- 发现：无一条为陶瓷/涂层腐蚀研究，排除结论成立。分层：60 条明确无关（锅炉/水泥/废物/火山学）；11 条方法相邻（熔体黏度/结构/热力学，与 B2 保留的 S040/S146/S147/S132 同类，最强为 S183 CMAS-FeO 渣系黏度与 S012 含 Fe 玻璃结构）；2 条词面相关主题无关（S085 Si3N4/Al 合金润湿、S136 SiC 多孔陶瓷过滤）。
- 后续：维持回收站现状，不恢复；若将来做熔体物性专题优先考虑恢复 S183、S012。本轮未提交上传。


> 2026-09-09迁移说明：以上为迁移前混合历史，含当时的公共维护记录。公共规则仍以根目录现行文件为准；后续本文件只记录本方向事项。阶段0/1在根日志保留的条目是同一操作的历史镜像，不重复计数。

## [2026-09-09] update | 迁入独立陶瓷腐蚀工作区

- 输入：用户授权多方向改造阶段2。
- 操作：保留原研究内容，迁移至本方向目录，修复派生文件路径并添加direction_id；领域阅读规则独立，研究进度提炼至current_context。
- 新建：本方向AGENTS、current_context及上下文历史归档。
- 更新：本方向索引、引用路径与维护记录。
- 发现：未新增论文；科学判断与核查状态不升级；原始笔记保留原文字节与旧链接，外部来源未移动。
- 后续：继续遵守暂停扩写与选定候选后处理的研究约束。公共隔离验收见根级阶段2报告/后续阶段3，不作为本方向科研待办。
