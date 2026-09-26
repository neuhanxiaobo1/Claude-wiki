# 本方向B/C工作簿工具

从vault根运行：

```powershell
python -B directions/wave-transparent-composites/scripts/review_bc/validate_workbook.py
python -B directions/wave-transparent-composites/scripts/review_bc/check_contract.py
```

依赖当前环境的Python、openpyxl。校验只读：字段/ID/外键/状态、逐篇Source_Manifest中的PDF/MD及可用身份文件哈希、DOI/item映射、旧E锚点和Git可跟踪性。不能自动核实科学结论、样品独立性、模型物理正确性或未取得SI。

`workbook_io.append_batch(updates, expected_hash)`是唯一通用追加接口；调用者必须先完成原文阅读并正确分类。写前哈希校验、临时保存及重读校验后替换；若存在pending文件或Excel锁定，停止覆盖，按恢复规则处理。表范围不够时拒绝追加，先同步扩展表/验证范围。

字段定义在`../../rules/bc-evidence.schema.json`，事实库在`../../synthesis/review_BC/BC_review_evidence.xlsx`。本目录不内嵌文献数据；校验统计可作为带源哈希的批次快照，不能手工当第二库维护。
