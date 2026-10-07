---
direction_id: wave-transparent-composites
created: 2026-10-07
updated: 2026-10-07
status: audit-complete-deletion-pending-upload
---

# 当前版本上传与方向冗余检查

## 实际完成边界

用户要求先上传当前版本，再检查并删除本方向冗余文件。清理前版本已经本地提交为 **d164ab6082f7e0d981b99f224af9bb4895537f35**（`d164ab6`）。本次提交19个文件的变更；相对于上一确认远程版本`413a8ca / calude_wiki_4.0`，累计待上传99个文件变更，完整路径见[上传范围](upload-files.txt)。未创建新版本标签。

**上传未完成，删除尚未执行。** 有两个独立阻塞：

1. Git全局配置指向本机代理127.0.0.1:7897，但端口不可连接；在单次命令覆盖GitHub专用代理及通用代理后，直连GitHub也连接失败。没有改变持久配置、关闭证书校验或强推。
2. 后续`git push origin main`被自动审批拒绝。理由是具体GitHub目的地及完整提交内容的授权尚未得到其认可。已向用户提交明确问题：是否将d164ab6及未上传祖先（上述99项变更）上传到`https://github.com/neuhanxiaobo1/Claude-wiki`的main分支。没有绕过拒绝，也没有换其他目的地。

审批认可目的地与范围后仍需解决连接问题；两者不是同一个阻塞。按用户“先上传”的顺序，当前保留所有待删文件。只清除了本轮自建且已完成工作的临时盘点脚本，不计入清理成果。

## 检查范围与判断方法

本方向原有421个文件（不含本报告目录）；其中raw的223个文件只盘点路径，不读原文、不删除。对其余非空文件做内容哈希比较，对候选旧草案、候选模板、现行规则和引用做定向语义核对。未读取其他方向研究内容或外部Zotero/MinerU原件。

冗余不由日期或文件名决定：内容相同但承担不同历史验收用途的记录可以保留；已被现行规则完全接替且可能引导执行旧流程的草案适合清理。当前多种导出格式分别承担阅读、筛选或机器读取用途，不一律删除。

## 确认的13个清理对象

精确路径、大小、SHA256、清理前Git对象、替代入口及引用定位见[manifest.json](manifest.json)。合计211,951字节，约207 KiB；本次价值主要是减少旧规则入口混淆，而非释放磁盘空间。

| 类别 | 文件 | 数量 | 删除依据 |
|---|---|---:|---|
| 旧C规则草案 | c-rules-design-v2-2026-09-21下corpus-rules-draft.md、reading-rules-draft.md、synthesis-rules-draft.md、writing-rules-draft.md | 4 | 未部署；旧C固定目标已退出。相应职责由bc-review-workflow、bc-evidence-contract及公共流程承担，写作参照独立保留 |
| 重复记录模板 | 同目录mechanism-record-template.md | 1 | 正式EV/SYN及schema已经承担记录，不再建立并行机制卡 |
| 旧空白候选库 | bc-integration-2026-09-25下BC_review_evidence_v2_candidate.xlsx、schema.json、build_candidate.py | 3 | 三个科学数据表均无非空数据；正式schema保留全部24/31/19旧列，Paper_Index增加Source_Manifest。一次性候选生成已经完成，无需保留另一套可执行入口 |
| 空目录占位 | docs/.gitkeep、synthesis/.gitkeep、wiki/papers/.gitkeep | 3 | 这些目录已有跟踪内容；其他空骨架目录的占位仍有作用，保留 |
| 可再生成缓存 | scripts/review_bc/__pycache__下validate_workbook.cpython-310.pyc、workbook_io.cpython-310.pyc | 2 | 源脚本保留，缓存可再生成，无科学事实或人工记录 |

其中11个跟踪文件已逐个核对工作区对应Git对象与d164ab6一致；另2个仅为缓存。此前被忽略的旧候选空表与35篇派生章节Excel已精确加入清理前提交，以保留可恢复版本，不扩大上传至原件。

## 应保留的文件

- **唯一事实库及来源**：BC_review_evidence.xlsx、sources、workbook-change、原文定位、问题记录、27篇旧paper及E#；本轮工作簿SHA256仍为`00e196b6fac783db3bc74101327fe2382b29cf02802a16c8351ae50fbbe3f28c`。
- **两篇指定写作参照及复读说明**：style-reference-notes.md、对应sources及本次reference-reread.md有不同职责，全部保留。
- **35篇映射与最新方案**：旧目录中的chapter-map.json仍保存完整身份与115条EV定位，最新crosswalk依赖它；不能随旧题目报告整目录删除。MD/JSON/Excel用于不同读取场景，保留。
- **历史决策与验收**：旧方案报告、部署说明、阶段校验结果和verify_delivery脚本保留溯源。旧C报告/部署说明应在清理时加“历史、不得执行”提示，避免误读。
- **相同字节的两个验收结果**：stage4与stage5的structure-validation.json相同，但属于不同阶段的检查记录；分别保留，不以同哈希直接认定冗余。
- **用户原始方案、raw快照和外部资料**：保持原件保护；通用清理授权不扩张到删除原始资料。

## 上传完成后的执行步骤

1. 得到上述具体目的地/范围授权并恢复连接；fetch确认远程关系，正常推送清理前提交；通过远程SHA确认d164ab6已可达，不以本地提交代替远程备份。
2. 再核manifest的13条文件哈希、实际绝对路径及无junction/symlink越界；若文件出现新内容，重新评估该项，不按旧清单直接删。
3. 修复旧C report中的5条文件链接，改指现行规则或保留历史文件名纯文本；在旧report/deployment开头标明历史状态与Git恢复提交。旧candidate report中的空表/schema链接改为正式入口，并标历史资产已移除。历史验收JSON保留当时路径，不伪改历史成功结果；旁边报告说明如何从d164ab6溯源。
4. 用同一套工具逐个删除manifest确认的文件；不使用递归目录删除。更新directory-guide及index，核对受影响链接。
5. 复查方向结构、受影响文档链接、工作簿哈希和实际删除数；保存完成边界。清理后的改动独立提交，便于恢复；用户本次明确要求上传的是清理前版本，不自动将后续清理提交推送。

## 验证与尚未解决事项

本轮方向结构检查0 errors / 0 warnings；清理前提交通过`git diff --cached --check`。检查不覆盖全部历史报告、原始科学内容或来源真实性；候选的直接引用已另行盘点。旧工作簿的14项外部MinerU清单哈希漂移仍未解决，见[此前发布核查](../publication-2026-10-07/report.md)，不因本轮结构检查通过而清除。

当前删除数为0；本报告是已完成的检查与待执行清单，不能写成“清理完成”。恢复入口为本报告、manifest及本方向current_context。
