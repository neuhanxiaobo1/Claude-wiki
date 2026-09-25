---
direction_id: wave-transparent-composites
status: active
created: 2026-09-25
updated: 2026-09-25
---

# B/C综述工作入口

唯一事实库：[BC_review_evidence.xlsx](BC_review_evidence.xlsx)。正式流程：[[directions/wave-transparent-composites/rules/bc-review-workflow]]。逐条结果、条件和综合论点都在工作簿，本页不再复制数值或单论文摘要。

## 当前阶段与目录决定

2026-09-25完成首批五篇试点（P0001—P0005）。B/C仍并行验证，不因当前小样本的核心数量定主次。旧C优先和四扩展部署路线不再执行。

- B：保留B2状态定义及B3—5的验证问题；SYN-B-001为暂定综合，尚未建立可配对的完整因果链。下一批优先补同状态结构—介电、冷却恢复或循环证据，不以制备温度/力学耐温替代。
- C：SYN-C-001为孔结构共变问题的暂定综合；SYN-C-002仅可用于说明界面力学与介电归因的用途边界，不能作为机制已成立的结论。下一批优先检查真正具有界面或孔结构介电对照的原始研究。
- 多孔陶瓷参照仍保留，且与复合材料核心分开统计。是否最终扩大题目对象需由后续材料覆盖决定，不能因已有组内论文自动扩题。
- 指定两篇写作参照继续有效；当前不写完整引言/综述正文，不绘制装饰性图表。

交付及验收：[[directions/wave-transparent-composites/docs/bc-pilot-2026-09-25/report]]。问题处理见[source_check_log.md](source_check_log.md)。两份文档只维护论证决定及复核行动；实际论文/证据状态以工作簿为准。

## 使用与恢复

打开工作簿按Paper_ID或Evidence_ID筛选；旧paper入口保留对应Paper_ID，Legacy_Evidence_Ref回指原E#。字段见[schema.json](schema.json)。可运行`python -B directions/wave-transparent-composites/synthesis/review_BC/validate_workbook.py`只读检查本库；不会写入事实或升级状态。

本地专用流程和工作簿已启用，正式工作簿纳入calude_wiki_3.9.9发布范围，实际上传状态以Git引用核验为准。工作簿Instructions及试点验收中的未提交说明记录的是试点交付时状态。外部PDF、MinerU缓存、raw复核图不在本次Git发布范围。
