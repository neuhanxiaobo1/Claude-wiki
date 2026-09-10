# 新方向骨架模板

这是创建规程与占位示例，不是已登记方向。先按docs/direction-workflow.md确认名称、范围、稳定ID、路径无冲突；下方所有占位符生成时必须展开，不复制已有方向研究内容。

```text
directions/<id>/
  AGENTS.md
  index.md
  log.md
  inbox.md
  memory/
    project_profile.md
    current_context.md
    tag_taxonomy.md
    term_aliases.md
    error_log.md
    decision_log.md
  raw/papers/
  raw/notes/
  raw/assets/
  raw/zotero_imports/
  wiki/papers/
  wiki/authors/
  wiki/topics/
  wiki/methods/
  wiki/datasets/
  wiki/metrics/
  wiki/claims/
  wiki/gaps/
  wiki/reviews/
  synthesis/
  docs/
```

空目录如需版本管理可用.gitkeep。reading_rules、synthesis_rules、writing_rules和templates只在已有具体领域差异时创建；否则在方向AGENTS明确“沿用通用流程，无专用扩展”。

| 文件 | 初始内容要求 |
|---|---|
| AGENTS | 本方向名称/ID/真实路径；遵循根规则；profile与当前状态入口；每类任务适用扩展；领域要求只作用本方向 |
| profile | 用户给定名称与范围、已确定用途/问题；未定项明确待确认；默认偏好引用memory/user_profile，来源配置留待填写 |
| current_context | 创建日期、尚未开始的研究状态、用户指定下一步；不含其他方向论文或执行待办 |
| index | 仅链接已存在入口；空类别写暂无，不创建虚构知识页 |
| log / inbox | 本方向创建记录、已知待办；无任务时明确暂无 |
| tag_taxonomy / term_aliases | 指向根公共标准，本方向词条为空或仅包含用户已明确项 |
| error_log / decision_log | 标题与记录规则；不复制旧方向错误和研究决定 |

注册表追加项示例（可用JSON兼容YAML表示）：

```json
{"id":"<id>","name":"<display-name>","path":"directions/<id>","status":"active","last_used":null}
```

注册后更新根index/log。新建知识页使用通用模板，direction_id写本方向ID，双链采用vault根的完整路径；输出前移除未展开占位和无用空栏目。
