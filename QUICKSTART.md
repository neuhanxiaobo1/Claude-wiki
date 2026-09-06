# Quickstart

## 1. 打开与恢复

打开当前项目目录，也可作为 Obsidian vault 使用。首次使用按 AGENTS 读取公共规则和 project_profile；继续已有任务时按 context_policy 当前状态恢复，无需重新初始化或清空知识库。

新用户填写研究领域、来源和输出偏好；尚未确定的研究问题可以保留待确认。当前用户已有配置直接复用。标签和别名仅按需要补充。

## 2. 根据已有输入选择入口

| 已有输入 | 操作 |
|---|---|
| Zotero collection，尚需选择论文 | 用 import_zotero 生成候选清单 |
| 已知题名/条目标识、附件、PDF 或缓存 | 直接用 pdf_read_agent 新入库，核对来源并去重 |
| 已有论文页 | 用 pdf_read_agent 完整复核或局部修订，保留路径 |

仅列候选：

```text
请按 agents/import_zotero.md 读取 Zotero collection「我的研究方向」，只生成候选清单。
```

从已明确的清单入库：

```text
请按 agents/pdf_read_agent.md 入库 raw/zotero_imports/我的研究方向/import_plan.md 中编号 1 的论文。
```

读取本地来源：

```text
请按 agents/pdf_read_agent.md 读取 raw/papers/example-paper.pdf，完成单篇入库。
```

局部修订：

```text
请按 agents/pdf_read_agent.md 修订 wiki/papers/<已有论文>.md 中指定结论，核对其原文与图表，只更新受影响段落并记录下游待复核项。
```

以上路径和名称是示例，使用时替换成实际目标。已授权的单篇或明确批次不再逐篇确认；批次范围遵循 project_profile 和当前指令。

## 3. 来源与阅读

Zotero connector 只在实际可用时使用；已知 PDF/缓存不依赖先生成 collection 清单。缓存和译文需核对来源版本，关键图表、数值或歧义按 pdf_read_agent 回查原件；原件缺失只暂停依赖它的判断。

不为阅读强制复制 PDF。原始文件受保护，生成的 import_plan/manifest 可在授权任务内同步。详情见 docs/zotero-workflow.md。

## 4. 检查与维护

```text
请按 agents/lint_agent.md 检查刚完成的论文页面及必要引用，区分结构结果、证据核查范围与待修项。
```

结构通过不代表科学正确；processed 不代表 checked。重要操作记 log，index 按实际变化维护。

## 5. 按问题开展综合

需要多论文比较、gap 或综述时，再使用对应 agent。先核对具体证据与可比条件，再组织主线；不按入库数量强制产出 gap 或大纲，也不把旧页自动视为已复核。

当前规则完善进度见 docs/rules-improvement-plan.md。公开发布准备与日常维护分开，继续工作不触发上传或数据清理。
