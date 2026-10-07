---
direction_id: wave-transparent-composites
created: 2026-10-07
updated: 2026-10-07
---

# 当前版本提交与上传记录

用户已明确授权上传当前版本。目标为既有`origin/main`（`https://github.com/neuhanxiaobo1/Claude-wiki.git`），基于上一发布`calude_wiki_4.0` / `413a8cab53c4ac6cc36d01d2f8237cdc5ef1c7b1`。本次未指定新版本号，不擅自新增版本标签。

当前成果已本地提交为`e576e1d`（86个文件）；本条状态修订由后续Git提交记录。**远程上传未成功**：`git push origin main`在TLS握手阶段失败；此前默认TLS、OpenSSL以及HTTP/1.1的fetch亦失败。未关闭证书验证、未改远程地址、未强制推送。已询问用户是否需使用本机代理；恢复连接后先fetch检查远程分叉，再推送并核远程SHA，无须再次申请上传授权。

## 提交范围

- 2026-09-26至2026-10-01透波复合材料方向的阶段3—8成果、规则偏好、来源/验收记录和直接相关旧页修订。
- 唯一BC科学事实工作簿：21篇、115 EV、9 SYN；本次发布不改科学内容，SHA-256为`00e196b6fac783db3bc74101327fe2382b29cf02802a16c8351ae50fbbe3f28c`。
- BC-S1：95篇摘要级候选筛选，相关30、边界20、排除45，含报告、来源记录、Excel和CSV。为两份派生筛选表增加方向级精确Git忽略例外，不扩大到其他Excel、CSV或原件。
- 本次发布前发现的外部解析清单漂移记录及发布状态；研究目标与B/C主线没有改变。

没有包括PDF、外部Zotero/MinerU原件、原始题录快照、raw导入管理记录或本机配置。筛选Excel/CSV能保留逐篇判定；raw原始摘要和manifest仍仅在本机，Git发布不等于外部来源已备份。

## 验证与限定

- 方向结构检查：0 errors / 0 warnings；只核结构，不代表科学结论通过。
- 证据契约8项反例检查通过，正式工作簿未变。
- 工作簿全检查：数据/ID/引用等未见其他错误，但**14个已登记外部MinerU `manifest.json`与历史哈希不同，因此全检查未通过**。原PDF、MD、身份记录及SI共57项哈希全部一致，另1项manifest一致。详见[完整检查](workbook-validation.json)、[逐篇漂移记录](source-drift.json)。
- 漂移涉及P0006—P0013、P0015—P0020。当前manifest可解析，换行归一化不能恢复旧哈希；旧字节快照未取得，不能断言差异仅为格式或自动升级。保留旧哈希及当前观测，不改源文件、不重写历史验收、不降级或升级已有EV以制造通过。
- 本轮是保存当前版本，带上述来源清单待核项提交；不能据此称“所有来源验证通过”。后续使用这些解析清单定位原文前重新核对应关系，原PDF/正文的既有哈希一致性仍有效。

候选与下一阶段阅读安排继续见[[directions/wave-transparent-composites/memory/current_context]]；本次发布不自动启动新论文入库。
