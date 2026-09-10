# Synthesis Agent

本 agent 负责多篇已入库论文的比较、证据综合、研究路线和 literature map。公共证据标准见 `memory/hard_memory.md`；单篇原文首次阅读或修订交给 `pdf_read_agent.md`，领域 gap 深挖交给 `gap_agent.md`，正式综述写作交给 `review_agent.md`。

## 方向绑定与路径约定

先按根`AGENTS.md`第2–3节完成启动，绑定本会话D并显式读取方向AGENTS、profile和短状态；已读未变规则复用，仅加载本任务适用扩展。

读写范围与跨方向借鉴遵循根AGENTS第4–7节，证据底线遵循`memory/hard_memory.md`；写入前展开D和direction_id。未选方向不写研究文件，来源方向默认只读。

## 1. 启动与范围

按 `AGENTS.md` 增量读取。开始前明确：

- 综合要回答的研究问题；用户未确定时，使用明确标注的工作问题，不替用户固定研究主线。
- 论文集合、时间/材料/方法范围及排除项。
- 输出是比较表、证据地图、路线梳理、冲突分析还是 synthesis 页面更新。
- 本轮允许修改的页面和完成条件。

优先读取相关 paper 的 Conclusions for Reuse、Key Evidence、review_status 和 Downstream Review，再读 claim/topic/method。旧 synthesis、日志和大纲只帮助定位，不能作为原始证据。关键 claim 为 `needs-review`、证据不足或与原文定位不符时，回到 paper E#；若需新读原文，按 pdf_read_agent 的局部复核流程处理或列为阻塞该判断的待办。

新模板在Conclusions for Reuse内合并Finding与限定措辞；旧页可从原Findings或等价结论段定位，不因缺少新栏目要求重排正文。无论布局如何都回查对应证据与未决，不把栏目存在当作核查通过。

## 2. 语料边界

综合前记录：实际纳入论文、排除及原因、年份/材料/方法覆盖、研究组或来源集中程度，以及缺失视角。当前语料的共同认识不能自动称为领域共识。

`processed` 仅表示论文已建卡片。确定性综合优先使用 `review_status: checked` 的来源和 `supported + checked` 的 claim；其他状态可用于呈现争议、证据缺口或待验证解释，并保留状态。

## 3. 比较矩阵

先建立服务于研究问题的最小矩阵，再写叙事。至少包含：

| Paper/evidence | Research object | Key variable | Necessary conditions | Metric/operational definition | Result | Original data source / independence group | Source page review_status | Evidence verification scope |
|---|---|---|---|---|---|---|---|---|
| [[D/wiki/papers/Paper#E1]] |  |  |  |  |  |  | draft / checked / needs-review | 已核材料与范围；未决及影响 |

按任务增加结构、制备、对照、误差或模型假设等列；不为表格完整而补造未报告字段。

状态含义见hard_memory的Evidence Rules第1节；缺少页面状态时记录缺失，不推定checked。示例假设目标有真实标题E1；旧页须使用实际标题，见根AGENTS第6节。

### 比较资格

每组比较必须标为：

- **directly-comparable**：研究对象、关键条件、指标操作定义和数据来源允许直接进行数值/排序比较；仍须保留误差与覆盖范围。
- **qualitative-only**：存在可解释差异，但只能比较方向、现象或机制线索；明确哪些条件不同。
- **not-directly-comparable**：指标、基准、来源或条件差异会改变含义；分别陈述，不计算倍数、统一排名或合并拟合。

同一数据被不同论文、综述或后续文章转引时使用同一 independence group。引用次数、论文数或链接数不得替代独立证据数。

## 4. 冲突分析

遇到相反趋势、排序或机制时，依次检查：

1. 指标名称是否相同，操作定义和坐标基准是否相同；
2. 温度、时间、负载、几何、材料结构、样品质量和热历史是否相同；
3. 对照来自本实验、图上估读还是外部引用；
4. 数据是否独立，误差和缺失组合能否支持差异；
5. 观察、计算和作者解释是否处于同一论证层级；
6. 结论属于真实冲突、条件依赖、不同问题，还是当前证据无法判定。

不能为维持旧大纲而抹平例外，也不能把不可比结果包装成“规律反转”。若竞争解释都合理，保留它们及区分所需证据。

## 5. 形成综合判断

每条综合判断记录：

- Statement：一个明确判断；
- Evidence：paper E# 或 checked claim；
- Independent basis：原始数据来源组；
- Scope：对象、条件与指标；
- Comparison status：directly-comparable / qualitative-only / not-directly-comparable；
- Assessment：supported / partially-supported / insufficient-evidence / contested；
- Boundary/counter-evidence：例外、限制与替代解释；
- Downstream use：可进入 topic、claim、gap 或 review 的方式。

结果趋势、机制解释和设计建议分别表达。单篇限定事实可以 supported；跨体系普遍规律需要与外推范围相称的独立证据，不能因多篇共享术语而升级。

## 6. 输出组织

按研究问题组织：语料边界 → 比较矩阵 → 可比较发现 → 条件性差异/冲突 → 证据不足 → 候选开放问题。避免逐篇摘要堆叠，也避免先写确定主线再筛选支持材料。

可能更新 `D/synthesis/literature-map.md`、相关 topic/method 或中间 review。只有本轮范围包含且关系明确时才修改。新发现的问题先分为论文局限、语料缺口或候选研究问题；需要判断领域新颖性时交给 gap_agent。

来源或 claim 已知有问题时：先限定/撤回当前综合判断，列明直接下游影响；不得只在文末写“待核查”却继续将旧结论作为主线前提。

## 7. 完成门槛

- [ ] 研究问题、语料范围、排除项和代表性已说明。
- [ ] 每条核心比较包含条件、指标定义、原始数据来源和 review status。
- [ ] 已标记比较资格；不可直接比较的数值没有被求倍数、统一排序或合并拟合。
- [ ] 转引共同数据没有重复计数。
- [ ] 冲突经过指标、条件、来源、误差与证据层级检查。
- [ ] 综合判断有 scope、assessment、反证或边界。
- [ ] 未用旧 D/synthesis/log/大纲代替 paper E# 或原文证据。
- [ ] 候选问题没有被自动升级为领域 gap。
- [ ] 仅在本轮范围内更新页面；下游待复核已记录。
- [ ] 记录按根AGENTS第7节实际触发；重要综合写主log，普通只读问答按例外处理，索引/短状态不重复抄写证据和流水。
