---
type: memory
status: template
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Error Log

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
