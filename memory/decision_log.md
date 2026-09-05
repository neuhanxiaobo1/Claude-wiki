---
type: memory
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Decision Log

本页记录 ResearchWiki 的重要结构和规则决策。

## Record Format

```markdown
## [YYYY-MM-DD] Decision Title

- Decision:
- Reason:
- Impact:
- Status:
```

## [2026-06-03] Open-Source Template Initialization

- Decision: 将当前项目初始化为可开源的空白论文知识库模板。
- Reason: 开源版本应保留框架、agent、template 和通用 memory，不应包含个人论文数据、Zotero 记录、真实论文分析或本机路径。
- Impact: 新用户 clone 后需要先填写 `memory/project_profile.md`，再导入自己的论文。
- Status: active

## [2026-09-05] 规则完善阶段 1：公共证据标准与任务边界

- Decision: AGENTS 负责启动与路由，hard_memory 统一证据类型、支持程度、核查状态和结论边界；新入库、完整复核、局部修订分流，已读未变信息复用。
- Reason: 将笼统的证据原则变成可操作标准，控制局部修改范围，避免重复读取与错误向下游传播。
- Impact: 两份公共规则即刻生效；旧 agent/template 中重复启动、整页输出和无条件联动要求按公共规则执行，具体流程后续逐步对齐；不扩大原始资料或 Zotero 写入权限。
- Status: active（仅阶段 1 已完成，论文与综合结论仍待后续复核）。
