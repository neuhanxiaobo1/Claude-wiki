# 只读结构检查

入口：[scripts/wiki_check.py](../scripts/wiki_check.py)。用于结构诊断，不代替agents/lint_agent的证据和流程判断。无自动修复、网络访问、Git操作或报告写文件功能；JSON输出到终端。任务要求保存结果时由对应公共/方向任务另行保存。

## 使用

需要Python 3.10及PyYAML；本机验证环境为Python 3.10.8、PyYAML 6.0.2，依赖记录在[scripts/requirements.txt](../scripts/requirements.txt)。缺依赖时明确退出，不自动安装。

三种范围必须显式选择一种：

```powershell
python -B scripts/wiki_check.py --public
python -B scripts/wiki_check.py --direction electronic-packaging
python -B scripts/wiki_check.py --all-directions
```

- public：公共入口、当前公共memory（排除错误/决定历史）、agent、template、shared及指定操作说明；不读方向研究正文。根log、日期报告和旧迁移内容不扫描。
- direction：该方向AGENTS/index/inbox、当前memory（排除错误/决定历史）、wiki和synthesis；不读另一方向全文。
- all-directions：公共范围加全部已登记方向的上述范围，仅在明确的全库结构检查任务使用。
- 所有模式都核对注册表结构、路径及已登记方向必要入口的存在性，不因此读取未选方向研究正文；工具不改变会话方向绑定。
- 可用`--root <实际知识库根目录>`检查另一个副本；未指定范围返回用法错误，不默认扫描全库。

## 检查能力与边界

| 项目 | 本版实现 |
|---|---|
| 注册表 | schema_version与entries结构、稳定ID、重复ID/显示名、规范路径、公共及方向必要入口存在；提示未登记方向目录，拒绝越界及符号链接/junction |
| Frontmatter | YAML安全解析、重复键、闭合与mapping类型；模板仅做语法检查，不把占位字段当真实数据 |
| 页面归属 | wiki/synthesis的direction_id；wiki分类与type对应；synthesis按用途保留，不强制登记表为synthesis |
| 状态与基本字段 | review_status合法值、tags列表、wiki部分缺失字段提示、paper题名和来源是否缺失/待核查 |
| 双链文件 | vault完整路径、同页链接和显示别名；短名在本次范围及根文件中有多个候选时提示歧义 |
| 双链定位 | 精确ATX标题存在/重名，块ID存在；双链外附E#提示。存在不等于证据有效或桌面已测试 |
| Markdown链接 | 简单行内本地文件目标、尖括号路径和百分号编码；Markdown锚点列未检查，不模拟渲染器slug |
| 范围隔离 | raw、历史正文、隐藏目录和外部文件不读取；范围外链接仅核对安全的本地目标存在性，锚点列未检查 |

围栏代码、行内代码和HTML注释不当真实链接；模板/公共说明的明确路径占位不判断链，真实知识页的未展开D/或模板占位链接报错。目录导航不是知识页缺失，不因此建页。

不验证题名真实性、原件是否读过、标签含义、别名同义、DOI去重、状态与科学正文一致性。不能把checked或有效链接当证据充分。无frontmatter的旧页提示待迁移，不伪造字段。

## 结果解释

- errors：能够确定的结构问题，如归属/类型错误、重复键、支持语法内的缺失目标/标题。
- warnings：待核对或未检查，如旧字段缺失、短名多候选、Markdown/范围外锚点；不等于已确认断链。
- selected_files是选中范围，read_files包含注册表及实际缓存计数；scientific_evidence_checked始终为false。
- 每项有路径、问题代码及可用行号。正文链接行号相对文件，YAML错误行号相对frontmatter片段，定位时留意首行分隔符。
- 退出码0：未发现确定结构错误，仍可能有warnings；1：发现结构错误；2：参数、依赖或执行问题。0不表示全库健康或全部锚点通过。

短名处理刻意保守，未实现Obsidian全部候选优先级；先人工核对意图，不据歧义提示批量改名。范围外同名页未扫描，不能据本次无歧义宣称全库唯一。

复杂/引用式Markdown、Setext标题、嵌套标题锚点、渲染器slug、代码内有意引用和完整块定位布局未验证。符号链接/junction跳过或报路径问题。检查不是原子快照，其他程序并行修改可能影响结果；重要验收先协调写入。

## 验证

```powershell
python -B scripts/test_wiki_check.py
```

测试只在系统临时目录建立虚构方向/页面，验证正反例和不写文件。平台功能若跳过须单独报告；修复后只复查受影响范围。该工具不提供后台锁、备份创建或恢复。
