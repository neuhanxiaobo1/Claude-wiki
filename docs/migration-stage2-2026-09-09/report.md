# 阶段2：公共规则拆分与当前方向迁移

2026-09-09，目录与规则入口已切换并通过声明范围校验。当前研究入口为 [[directions/ceramic-corrosion/index]]。唯一旧位置清理例外：screening.csv被Windows占用，已保留为明确退役副本；当前工作表使用新方向目录中的文件。

阶段3也已完成文件演练与规则逐案验收，见 [[docs/migration-stage3-2026-09-09/report]]。阶段4/5尚未执行。

## 交付与验证

- 公共AGENTS/CLAUDE、证据规则、个人默认偏好、词表、通用流程/模板与方向注册表已就位；研究方向选择由对话规则提供，不是桌面弹窗。
- 陶瓷腐蚀的AGENTS、profile、阅读规则、短上下文、词表、原件、wiki、synthesis及日志/报告独立存放。
- 10篇论文、8项claim、5项gap、2个topic、1篇review和6个synthesis页面保留，共32页科学内容逆向去掉路径和direction_id变更后与源文本一致，原有状态字段不变。
- 公共hard_memory的Evidence Rules完整保留。10项受保护raw文件原字节一致；12项导入管理记录仅适配路径。raw共22文件，无工作区PDF，外部Zotero/MinerU文件未移动、未备份、未重新核验。
- 常见链接校验无未处理错误；原始Si3N4笔记中10处旧链接通过路径映射溯源，3处任务示例不建空壳页。锚点/复杂语法/Obsidian桌面不在实测范围。
- 7项Git忽略样例通过：方向raw及备份被忽略，原已跟踪的派生screening.csv新路径可纳入版本管理；没有提交或上传。
- JSON/YAML可解析。两个新增辅助Python脚本只将固定旧目录改为自身目录，未执行它们的网络/文件生成操作。

## 并行变化保留

阶段1有112个源文件。准备期间其他任务追加两条研究日志并新增8个文件；用户确认暂停后，已核对并补充为120项执行前快照。完整补充清单见 [accepted-drift.json](accepted-drift.json)。新增研究清单、JSON、CSV和辅助脚本迁入方向，.claude本机配置保留原路径原字节；不以这些记录替代外部操作核验。

首次切换前被哈希/成员检查拦截，未覆盖并行新增内容。之后应用已写入并核验129项目标/更新文件，清理旧位置时遇到CSV占用，恢复脚本完成其余枚举清理。

## 文件占用例外

旧路径 `docs/scopus-screening-2026-09-09/screening.csv` 与新路径 `directions/ceramic-corrosion/docs/scopus-screening-2026-09-09/screening.csv` 在迁移时逐字节一致，旧文件已包含在执行前备份。77项旧文件已退役，1项被占用旧副本暂留；旧目录README明确指向新入口。

已请用户关闭占用CSV的程序。占用解除后运行finish_retirement.py，仅处理执行清单中仍存在、内容与备份一致的旧文件；它会核对迁移后维护哈希，不能以reset/整库覆盖代替。原位置如被后来改写，必须先核对差异，不能直接删除。

## 证据文件与回退

- [execution.json](execution.json)：实际映射、已枚举退役清单、备份/预览ZIP及哈希、旧副本状态。
- [verification-live.json](verification-live.json)：实际工作区校验；预览结果另见verification-preview.json。
- [ignore-checks.json](ignore-checks.json)：7个Git忽略样例。
- [post-migration-updates.json](post-migration-updates.json)：阶段3修正及收尾维护的明确文件哈希，避免将这些已知更改误当意外漂移。
- [migrate.py](migrate.py)：一次性生成/迁移工具，现已执行，不能在新目录上重跑。
- [finish_retirement.py](finish_retirement.py)：占用释放后的限定清理；不会操作未登记的新文件。

ZIP为本机同盘回退副本，实际路径/哈希以execution为准；未包含Git对象库和外部来源。需要回退时按执行清单和迁移后维护记录逐项恢复，保留后来新增的用户内容，不整库覆盖。阶段1/2准备文件及测试样例不作为研究证据。
