# 迁移前陶瓷腐蚀上下文历史

2026-09-09归档，保留原记录；当前入口见本方向current_context，旧状态不自动生效。



- 更新日期：2026-09-07。
- 对象与类型：规则完善后的七篇论文逐篇复核已完成（7/7）；最近完成 2025 Hf₆Ta₂O₁₇–Al₂O₃。入口：[[directions/ceramic-corrosion/docs/rules-improvement-plan]]、directions/ceramic-corrosion/log.md 最近复核记录。
- 完成边界：各源页建立 E1–E8、结论边界和 Downstream Review；checked 表示声明证据已核查，不表示原论文所有结论可靠或未决已解决。源页局部未决继续保留；下游 claim 已完成本轮迁移，五项 gap 亦已完成前提/分类迁移；两个 topic 与 literature-map 已完成迁移；其余四个综合页亦已完成本轮迁移。
- 下游进度：八项 claim 已逐页完成证据账本与 Assessment（4 supported、1 partially-supported、3 insufficient-evidence），review_status 均为 checked；仅四项收窄后的事实可确定复用，其余为解释/候选。
- Gap 进度：5/5 narrowed/checked；1 corpus-gap（1500 °C 对照），4 candidate-question（冷却损伤、筛选独立性、结构/半径可辨识性、实际 TGO 外推）。novelty_status 均 not-assessed，未做领域检索，priority 均 pending。
- 综合进度：两个 topic 与 literature-map 已修订/checked；矩阵覆盖七篇实验、计算/同源转引、比较资格、八项 claim 和五项 gap。无领域共识或新颖性确认。
- 下一步：依据矩阵更新 open-questions、research-positioning、review-outline 与 core-argument-map；不重做已完成层级。用户核心研究问题仍未确定，定位只能列候选。
- 来源通道：本机 Zotero MCP `http://127.0.0.1:23120/mcp`；OneDrive 链接附件以 complete 返回路径为准。MinerU 根目录 `D:/shuju/zotero1/llm-for-zotero-mineru/`，不由 storage 缺文件推断原件不存在。
- 2019：9Q7A46HL/R6YQ3KNM，英文 12 页，9612/full.md；晶型、原始统计和正式版差异待核。
- 2023：TLPXY39S/9VVGQ2M5，英文 16 页；9513 对应混排 T33IHQL9。ESM Fig. S1–S3、Movie S1–S3 未读，转引与独立验证须分开。
- 2024 Lu：RLNIRS7B/JNS38XK5，英文 9 页，10149/full.md；Fig. 1–10 已视觉核对，Movie 1/2 未取得。Fig. 4(d) 的保温图与冷却解释冲突、杂相和 219 μm 跨指标比较边界见源页。
- 2022 高熵硅酸盐：8IPQUSQL/I929AL9M，英文 15 页，10119/full.md；10117/10121 为混排/中文。块体杂相、估算热容/文献对照及性能折中已修正，石榴石精确式与统计/机制仍未决。
- 2025 RETaO₄：88RPHLC9/9TBX9XTZ，英文 13 页，10100/full.md；Method 3/4 为混排/中文。正式 ADVS-12-2412717-s001.docx 四表六图已读，下载入口见源页。跨 RE 成分限制层间独立性，Fig. 15 正值/参考态未决，深度不是严格单调。
- 2026 高熵锆酸盐：YPQHNP84/L4TEUBTX，英文 12 页，10087/full.md；1.pdf 为混排，无后缀为中文。正式 mmc1.docx 五表八图已读，两表重号 S4。样品标签、半径、畸变、密度和热导端点存在源内冲突，不能沿用定量设计规律及已证双机制。
- 2025 Hf：5PSRPWAQ/GSDAE8IV，英文 12 页，10141/full.md；正文 Fig. 1–12/Tables 1–3 已核。热压 1400 °C/10 min 已有 2.93 μm 层，追加 10/30/50 h 为 3.16/4.32/4.61 μm。应力为简化计算，单向扩散/Kirkendall 和涂层失效未独立证明；Li 前文仅核出版社摘要（1600 °C/8 h、2012 年），全文仍未核。
- 下游：七个源页 Downstream Review 中的 claim 待办是历史交接项，已由 2026-09-07 八项 claim 修订接续；其中 gap 待办已由五页新版本接续，topic 与 literature-map 待办亦由本轮接续，其余四个综合页待办亦由本轮替换接续。以新版 claim/gap/topic/synthesis 为当前状态，不重复执行已完成迁移；历史待办中指向原始证据缺失的部分仍未解决。被撤回旧论断不得继续作为确定性依据。
- 维护纠错：前两轮经 PowerShell 向 Python 传递中文时发生有损编码，导致维护记录问号化、快照只变数字未变描述；本轮已用 Unicode 安全补丁恢复。以后检查实际文字与状态，不能只检查 YAML/数字。
- 版本：此前 Claude_wiki_all 为 1381ee0；2026-09-08 用户已授权提交并上传当前修订为 calude_wiki_R，同名提交与标签定位此次快照；远程完成状态以 Git 核验为准，后续改动不自动发布。


### 2026-09-08 单篇入库接续

最新写作入口：[[directions/ceramic-corrosion/wiki/reviews/CMAS-Review-Section-1-Evaluation-and-Comparability]] 已完成第一节1.1–1.3试写和指标对照表；draft/checked限定为本次证据映射。由此接续审阅或第2节，不重读全库；本次正文尚未提交上传。

用户指定 #59 已完成入库：[[directions/ceramic-corrosion/wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening]]；X55RXI85/JNPL926R，10185/full.md，主文6页，PDF Fig. 1–7 与公式已核。当前8篇（7篇CMAS+1篇相容性）；Table S1 未取得，形成焓源内方向及相对测厚边界保留。原七篇下游迁移已完成，新增证据已同步相关矩阵/主题/claim/gap，三个写作页仅留交接。后续不重跑旧迁移或自动上传。


2026-09-08 #59整合接续：已完成大纲R9/R10、小节卡片及两段新增草稿，正式更新Q1/Q4/Q5与P1。此前“仅留交接/待整合”任务已完成；当前大纲覆盖8篇（7篇CMAS），共5段草稿，status仍draft。下一步可扩写第1节并按其定向证据清单补文献；S1等原文未决保留，不重做入库或旧七篇迁移。


2026-09-08 #17/#23入库恢复入口：[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]]、[[directions/ceramic-corrosion/wiki/papers/2019-RE2Si2O7-CMAS-1300-1500C]]；两篇processed/checked限各自E1–E8，库共10篇。MD缓存10158/9636，PDF分别8页/10页。#17摘要热循环缺协议、reduced modulus近似与局部TEM限制；#23内耗4/10 °C/min冲突和部分曲线转引均保留。当前第一节稿及本次入库尚未上传，后续可整合新证据。


2026-09-09最新状态：calude_wiki_10papers_section1（3266d7161e854d1228f6679240740067422f55f2）已上传，远程main及标签解引用均核验一致。随后#17/#23正式整合到10篇大纲R1–R13、第一节七篇直接来源、P1/P2及Q3/Q4/Q6；原“待整合”交接已完成。下一步审阅第一节并展开第2节；机制/统计未决不升级。本次整合晚于该上传版本，尚未提交发布。

2026-09-09后续指令优先：用户暂停扩写，改查背景缺口并导入三个Scopus collection。已实时完成四collection的186篇分层初筛，见 [[directions/ceramic-corrosion/docs/scopus-screening-2026-09-09/report]]；12篇优先全文核查、14篇第二批，其他实际摘要覆盖和取舍见CSV。指定三篇S052/S144/S031已有PDF；尚无新增wiki入库或上传，不自动继续第二节。

2026-09-09再接续：筛选报告及CSV已上传，完整标签calude_wiki_scopus_screening_complete，远程核验a383aef3b6261769800865b5cb702fd53faa57ce。随后新增 [[directions/ceramic-corrosion/memory/reading_rules]]，只作用陶瓷腐蚀方向；当前10篇按完整作者元数据均记internal。后续组外论文需补一作/通讯作者发表时单位、国家/地区、发表时间和有日期来源的当前方向，并维护 [[directions/ceramic-corrosion/synthesis/external-literature-register]]；不按collection判断组别。本次规则与分类增补尚未提交上传，未开始新论文入库。

2026-09-09版本接续：用户现已授权将上述规则及分类增补上传并命名calude_wiki_1；本轮提交与附注标签作为恢复入口，远程完成以Git核验为准。此前“规则增补未提交”仅为上一轮历史状态。继续暂停扩写，尚未开始组外论文入库。
