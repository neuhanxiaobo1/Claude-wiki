---
direction_id: wave-transparent-composites
status: active
created: 2026-09-25
updated: 2026-09-25
---

# 目录职责与规则入口

本方向保留公共目录骨架，工作入口只指向当前文件。原件、旧paper路径和E#不移动；历史设计留在原路径，通过下方导航分组，避免破坏既有引用或将用户方案当作现行规则。

```text
wave-transparent-composites/
├─ AGENTS.md                      # 唯一方向路由
├─ index.md                       # 当前研究导航
├─ memory/                        # 目标、短状态、决定/错误
├─ rules/
│  ├─ bc-review-workflow.md        # 执行顺序、准入、交付
│  ├─ bc-evidence-contract.md      # 材料/状态/介电/机制判据
│  └─ bc-evidence.schema.json      # 唯一生效字段定义
├─ scripts/review_bc/             # 写入接口、只读校验及契约检查
├─ synthesis/review_BC/
│  ├─ BC_review_evidence.xlsx      # 唯一维护事实及综合库
│  ├─ BC_synthesis_notes.md        # 章节功能、ID导航、目录决定
│  └─ source_check_log.md          # 补核动作及闭环
├─ wiki/papers/                   # 旧27页保留；非BC任务仍可使用
├─ docs/                          # 批次成果/来源清单/验收及历史设计
└─ raw/                           # 原件与本地读取、导入管理记录
```

| 问题 | 应读文件 | 不应作为替代的内容 |
|---|---|---|
| 当前目标和下一步 | profile、current_context | 历史方案、旧log |
| 怎么执行阅读/综合 | workflow，按需读evidence-contract | 历史四扩展草案 |
| 某数值/论断能否写 | 工作簿EV、原文定位和Source_Manifest | index、目录表或交付摘要 |
| 哪章留/合并/缩题 | BC_synthesis_notes的章节表及SYN | Core计数自动投票 |
| 如何运行校验 | scripts/review_bc/README.md | 旧验收JSON里的历史命令 |

当前交付：[[directions/wave-transparent-composites/docs/bc-batch2-2026-09-25/report]]；原始五篇试点：[[directions/wave-transparent-composites/docs/bc-pilot-2026-09-25/report]]。

历史设计导航：[[directions/wave-transparent-composites/docs/review-workflow-plan-2026-09-21/report]] → [[directions/wave-transparent-composites/docs/review-options-2026-09-21/report]] → [[directions/wave-transparent-composites/docs/c-oriented-rules-2026-09-21/report]] → [[directions/wave-transparent-composites/docs/c-rules-design-v2-2026-09-21/report]] → [[directions/wave-transparent-composites/docs/bc-integration-2026-09-25/report]]。仅按溯源需要读取；其中两篇写作参照继续有效，旧A/C优先方案不再执行。

本轮实际迁移（旧位置→新位置）：

| 旧路径（相对方向根） | 当前路径 |
|---|---|
| synthesis/review_BC/workbook_io.py | scripts/review_bc/workbook_io.py |
| synthesis/review_BC/validate_workbook.py | scripts/review_bc/validate_workbook.py |
| synthesis/review_BC/schema.json | rules/bc-evidence.schema.json |

迁移核验见[迁移记录](bc-batch2-2026-09-25/migration.json)。历史验收JSON保留当时路径，不改写成当前验收；当前Markdown入口已修复。候选schema只描述历史空白模板，不是生效规则。
