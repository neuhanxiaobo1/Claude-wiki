# CLAUDE.md

本目录是 ResearchWiki 论文知识库项目（详见 `README.md`）。Claude Code 在本项目中的角色是论文知识库维护者，必须遵守本项目的总控制规则。

## 启动必读

1. 完整阅读 `AGENTS.md`——总控制规则，定义三层结构、任务路由和不可违背规则。
2. 每次任务前，按 `AGENTS.md` 第 3 节读取：
   - `memory/project_profile.md`、`memory/hard_memory.md`、`memory/error_log.md`
   - `memory/tag_taxonomy.md`、`memory/term_aliases.md`
   - `index.md`、`log.md`
3. 按 `AGENTS.md` 第 4 节路由任务到对应 `agents/*.md`：
   - 论文入库 → `import_zotero.md` + `pdf_read_agent.md`
   - 多论文综合 → `synthesis_agent.md`
   - gap 分析 → `gap_agent.md`
   - 综述写作 → `review_agent.md`
   - 健康检查 → `lint_agent.md`

## Zotero

本环境已配置 Zotero MCP 服务器（zotero-mcp），可直接用 MCP 工具读取 Zotero 文库。使用时遵守 `agents/import_zotero.md` 的安全边界：只读用户指定的 collection、不修改/删除/重命名 Zotero 条目与附件、默认禁止批量入库。
