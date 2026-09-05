---
type: memory
status: template
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Error Log

## 2026-09-05 | 论文证据评价与综合传播缺少操作判据

修复进度（2026-09-05）：阶段 1 已在 AGENTS/hard_memory 补充公共判据、增量读取、局部修订和下游待复核边界；具体任务与模板、既有论文和大纲尚未修复，不将规则生效等同于历史结论已通过核查。

### 错误表现

前期复核发现把转引当独立验证、混用腐蚀指标、把作者解释或计算结果提升为实测结论，并将语料局限扩展为领域空白。已有规则要求来源、不确定性及 gap 克制，但未形成统一的论断级判断流程；执行者也没有充分遵循已有约束。

### 原因

模板将证据类型、强度、核查状态混用；综合缺少比较资格和独立来源检查；下游大纲没有明确的来源修正后待复核规则。

### 修正规则

先核对原文条件、指标和证据类型，再评价对具体结论的支持程度；转引回溯共同数据来源；核心证据未确认时保留未决，不靠叙事补齐因果。

### 影响范围

论文卡片、claim、gap、topic 和综合大纲。完善方案见 [[docs/rules-improvement-plan]]；本轮只完成规则审视与计划，原有论文结论尚未修订。

### 以后避免方式

按计划分阶段修改规则，每阶段用典型错误案例验收；最后以 2019 论文试运行，再逐篇迁移旧页面。规则变更不等于既有知识自动通过复核。

## 2026-09-05 | 执行范围膨胀与结构校验缺漏

### 错误表现

用户要求逐步修改后，执行者仍重复读取大量上下文并准备整页重写；同路径删除并新增补丁被拒绝，未成功修改论文。系统检查另发现 2022 高熵单硅酸盐论文 frontmatter 误用 type: topic，并缺少 title、doi、zotero_item_key、source。

### 原因

规则缺少局部修订与读取边界，执行者也未充分复用上下文、控制范围和正确使用补丁。现有 lint 未明确目录/type/必填字段检查。

### 修正规则

遵循用户当前范围，复用已核实信息，按小节修改已有文件；不要把模板解释为每次必须整页重写。结构检查与语义证据审核分别进行。

### 影响范围

分步论文修订和后续综合可靠性，详见 [[docs/system-audit-2026-09-05]]。论文元数据错误尚未修复；本轮仅诊断并记录。

### 以后避免方式

先明确启动与局部修订规则，再简化模板、补结构检查；来源修正后应标记下游待复核。

本次维护发现的执行问题：补丁使用未核对的旧文锚点被拒绝。以后更新维护记录须先读取实际锚点，失败后纠正匹配文本，不重复提交相同无效补丁。

本页记录 AI 在维护论文知识库时犯过的错误，以及以后必须遵守的修正规则。没有实际错误时，只保留记录模板。

## Record Format

```markdown
## [YYYY-MM-DD] Error Title

- Error:
- Cause:
- Correction rule:
- Impact:
- Fixed: yes / no / pending
```

## Example

> Example only. Replace this section after real use.

## [YYYY-MM-DD] Example: Tag Drift

- Error: 同一概念被写成多个标签。
- Cause: 新建页面前没有检查 `memory/tag_taxonomy.md`。
- Correction rule: 新增标签前必须先查标签体系和已有页面。
- Impact: topic、method、claim 或 gap 可能分散。
- Fixed: pending

## [2026-08-24] Obsidian 图谱显示系统页/规则层页面（「文件夹链接」）

- Error: 用户两次反馈关系图谱出现「文件夹链接」：首次为带路径名的灰色悬挂节点，二次为 index/inbox/README 等系统页节点。
- Cause: 两层原因叠加。① 悬挂节点：userIgnoreFilters 排除规则层目录后，index.md 指向它们的 wikilink 成为悬挂链接（已用 hideUnresolved: true 修复）。② 系统页节点：index.md 的 Quick Links 把 README/QUICKSTART/inbox/log/AGENTS 等根目录页面连成星型簇，这些页面真实存在、未被排除，必然显示；2026-08-24 用户又清空了 userIgnoreFilters（null），规则层页面全部涌入图谱。
- Correction rule: 图谱必须用路径过滤 scope 到知识层：graph.json 的 `search` 设为 `path:wiki/`；`hideUnresolved` 保持 true。不要用「排除目录」控制图谱内容（排除不彻底且制造悬挂链接）；排除列表只用于全局搜索卫生，且修改后要检查指向被排除文件的链接。
- Impact: 图谱视觉污染，掩盖真实知识关系。
- Fixed: yes（待用户在图谱筛选框确认生效）
