# 混合文件逐段归属与执行约束

阶段1的迁移准备清单，尚未执行拆分。下方 `D` 固定为 `directions/ceramic-corrosion`；阶段2执行时展开为真实路径。

## 一对多文件

| 源文件/段落 | 目标 | 阶段2处理 |
|---|---|---|
| memory/project_profile.md：Basic Information 的教授身份、多方向管理；Output Preferences 的中文、英文专名、双链默认偏好 | memory/user_profile.md | 仅提取跨方向个人默认项；不把陶瓷方向用途推广到其他方向 |
| 同文件：研究领域、原有用途、目标成果、Research Scope、Source Settings、初始领域标签/别名 | D/memory/project_profile.md | 保留用户确认/历史用途/语料观察的区别；collection与批次配置属于本方向，不作为新方向默认 |
| 同文件：Paper Ingestion Priorities | 公共 agents/pdf_read_agent.md 已有相应流程；方向 profile 保留简短入口 | 逐项对照公共流程，已有内容用引用代替重复；发现实际差异才补充，不丢失要求 |
| 同文件：CMAS 领域阅读辅助项 | D/memory/reading_rules.md | 表格、非适用项处理、领域规则入口合并到本方向阅读规则 |
| agents/pdf_read_agent.md：第10节 CMAS 项目附加检查 | D/memory/reading_rules.md | 将温度/熔体/样品/指标等检查与上述表格去重整合，保留有限熔体、储池/流失等额外项 |
| memory/ceramic_corrosion_reading_rules.md：全文 | D/memory/reading_rules.md | 作为合并主体；完整保存五节要求、日期来源和字段示例；组内/组外规则不得泛化 |
| memory/context_policy.md：目标、增量读取、触发、保留、写入位置、使用规则 | memory/context_policy.md | 保留通用恢复机制；明确每个方向独立短上下文与根级架构任务的恢复入口 |
| 同文件：当前任务及全部后续日期接续 | D/docs/context-history-pre-migration.md | 原研究交接历史完整归档，保留日期；更新实际导航但不重写当时研究结论 |
| 同文件：当前任务中仍有效的研究状态/下一步 | D/memory/current_context.md | 从最近相关记录提炼：10篇、暂停扩写、筛选完成、组外规则已建立、尚未开始新入库；核验历史相互覆盖，不再复制七篇到十篇的全部变更链 |
| 同文件：来源通道、MinerU根目录与附件身份 | D/memory/project_profile.md、方向历史/论文源页 | 方向profile保存来源配置；逐篇附件映射保留在历史和源页，不默认推广成全库路径 |
| memory/tag_taxonomy.md：Naming、General、Processing Status、Duplicate Policy | memory/tag_taxonomy.md | 公共标签命名/状态规则；领域标签查询改为所选方向词表 |
| 同文件：Domain Tags | D/memory/tag_taxonomy.md | ceramics、corrosion、cmas、ebc、tbc及登记出处完整保留 |
| memory/term_aliases.md：说明、Record Format、General Terms、示例 | memory/term_aliases.md | 通用词义保留；具体科学页导航改成方向相对职责，不在总规则中固定陶瓷方向 open-questions |
| 同文件：Domain Terms | D/memory/term_aliases.md | Ceramic Corrosion、CMAS、EBC、TBC保留原区别和目标关系；链接加方向前缀 |
| index.md：现有研究索引与版本记录 | D/index.md | 保留全部研究导航与重要未决状态；公共规则入口指向根目录；剔除仅属全库架构的导航到根index |
| index.md：全库入口职责 | index.md | 重建为方向目录、公共规则、迁移记录导航，不复制完整研究论证 |
| log.md、memory/error_log.md、memory/decision_log.md：旧混合流水 | D下同相对路径 | 保存完整历史并注明“迁移前混合历史”；通用规则旧决定仍有出处，不能把历史限定理解成全局当前任务 |
| 上述三个文件：迁移管理及未来公共操作 | 根下同相对路径 | 根文件建立新的公共段落和历史入口；本轮阶段0/1记录作为全局迁移记录保留于根，并明确方向归档副本是历史镜像，避免当作两项独立任务 |
| inbox.md：全文 | D/inbox.md | 陶瓷文献候选及旧图谱提示属于方向历史；根inbox重新作为未分配事项入口 |

## 保留公共层的文件复核

- `AGENTS.md`、`CLAUDE.md`、`README.md`、`QUICKSTART.md`：保留公共职责，启动、目录树、流程图、示例和维护路径统一采用方向路由。根级架构维护可直接进入本迁移报告。
- `memory/hard_memory.md`：证据底线完整保留；raw/wiki/研究log/index/词表路径明确指当前方向；公共记录另有归属。
- `memory/style_snapshot.md`：已读内容只有默认风格和维护原则，本轮没有证据支持额外抽出某方向风格。更新语言配置引用到user_profile，保留方向覆盖入口。
- 其余五个 agents、七个 templates：保留根目录；任务输出和示例链接在生成时展开方向根，通用模板不新增Tian作者背景字段。元数据去重明确限方向，跨方向同源不合并也不重复计为证据。
- `docs/initialization.md`、`docs/zotero-workflow.md`、`docs/privacy-and-gitignore.md`、`docs/obsidian-setup.md`：全文检查未发现必须搬走的具体研究报告，留公共层，仅改相应启动/路径说明。
- `docs/multi-direction-migration-plan.md` 与本阶段报告目录：属于全库架构记录，始终保留根级docs。
- `.vscode/settings.json`：只有环境管理器默认值，无方向路径，保留原内容。
- `.obsidian/app.json`、`graph.json`、`workspace.json`：前两者涉及链接格式/图谱搜索，后者属于本机打开文件状态；阶段2只处理真实旧路径，不把workspace作为用户已选方向。其他Obsidian设置保留。
- `.gitignore`：阶段1仅新增本地备份目录忽略；方向raw忽略和派生CSV例外在阶段2协调变更。
- `LICENSE`、`git-proxy-fix.bat`：保留根目录，无迁移需要；脚本未运行。

## 历史、原件与冲突处理

1. `raw/zotero_imports/田志林/` 与 `田老师/` 分别存在，按两个历史路径迁移。不能只凭中文名称或相同论文就覆盖其中一个。阶段2仍以当前profile指定集合为默认来源入口。
2. `raw/notes/2024-Si3N4-Molten-Salt-Corrosion.md` 是受保护的原始笔记，归陶瓷腐蚀方向；它不是现有10篇wiki卡片中的一篇。保留其内容和旧链接，通过本迁移映射定位新目标，不将其中旧gap/strong表述提升为当前科学判断。
3. 原始笔记迁移后内部旧链接可能不再直接跳转，这是原件保护下的明确例外。验收“无新增断链”针对活跃派生页/管理入口；原件内部链接列入保留清单，用映射溯源，不能为了消除告警修改原件或创建空壳知识页。若以后用户明确授权改写原始笔记，再单独处理。
4. `inventory.json` 的主目标之间无重复，无已存在的新方向目标。reading_rules 的多源汇入、根日志重建等是有意的组合，按本表合并段落，不按复制顺序覆盖。
5. 新建方向入口、注册表、公共user_profile、shared资源目录、方向模板骨架及历史context文件不存在，阶段2按方案创建；暂无研究专用总结/写作新要求时写明沿用公共规则，不凭空发明规则。

## 阶段2执行前的漂移检查

先对照 `inventory.json` 复查文件成员与哈希。阶段1产物目录及本地备份目录是显式排除项，始终保留；源文件若有新增或变化，先纳入补充清单与备份，不能直接按旧快照覆盖。混合文件的正文提取应使用标题定位，不能依赖旧行号。
