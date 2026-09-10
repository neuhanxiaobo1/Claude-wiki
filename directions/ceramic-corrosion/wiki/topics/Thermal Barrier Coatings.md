---
direction_id: ceramic-corrosion
type: topic
status: active
review_status: checked
created: 2026-08-27
updated: 2026-09-07
papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
methods:
datasets:
metrics:
claims:
  - "[[directions/ceramic-corrosion/wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
gaps:
  - "[[directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
tags:
  - topic
  - ceramics
  - corrosion
  - tbc
---

# Thermal Barrier Coatings

## Definition and Scope

本页是热障涂层相关证据的导航入口，当前只围绕 Hf₆Ta₂O₁₇ 与 Al₂O₃ 的相容性案例展开。论文中的 Al₂O₃ 粉末与块体扩散偶不是实际生长的 TGO；材料反应、模型应力与涂层损伤必须分别评价。

CMAS 相关候选材料另见 [[directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion]]，两页存在应用交集。本页不代表对所有 TBC 的领域综述，也不确认用户已选择 TBC 界面为课题方向，用户目标以 [[directions/ceramic-corrosion/memory/project_profile]] 为准。

## Corpus Coverage

仅纳入 2025 年 Hf 相容性论文一篇，已核 E1–E8；来源为当前 collection，代表性为 local corpus。粉末反应、热压/退火扩散偶、相表征与简化应力计算是主要证据；实际涂层/粘结层热循环与全领域候选材料比较未覆盖。Li 前文仅核出版社摘要，全文争议仍未裁定。

## Main Questions

| Question | Evidence | Current status | Scope limit |
|---|---|---|---|
| 在指定工艺下是否反应？ | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] | answered | 1400 °C 已有反应，不是绝对温度阈值 |
| 反应层是否确定由单向 Al 扩散控制？ | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E4]] | open in corpus | 静态梯度/微孔不独立确认通量和 Kirkendall |
| 模型应力是否证明实际涂层失效？ | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E5]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] | 外推证据不足 | 模型、不同物性来源及应力分量需保留 |
| 如何检验实际 TGO 行为？ | [[directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility]] | candidate-question | 需先明确涂层结构/热历程，非确定选题 |

## Evidence Map

| Claim | Assessment / review status | Independent evidence basis | Conditions | Reusable role and boundary |
|---|---|---|---|---|
| [[directions/ceramic-corrosion/wiki/claims/Hf6Ta2O17-TGO-Incompatibility]] | supported / checked | 2025 粉末物相与块体扩散偶；同一研究的不同表征 | 指定 1400 °C 工艺 | 发生反应；不确定实际 TGO 损伤与寿命 |

## Corpus-Supported Understanding

- [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]] 支持指定粉末条件下形成含 AlHf₃TaO₁₀ 的反应产物；1400 °C 已反应。1300 °C XRD 变化小不等于绝对惰性。
- [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] 的 2.93±0.38 μm 层来自真空 1400 °C、40 MPa/10 min 热压；追加空气 10/30/50 h 后为 3.16±0.35、4.32±0.43、4.61±0.62 μm。同工艺序列可描述比较，但有限时点/统计不建立动力学定律。
- [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] 中约 272.6、880.6、1030.8 MPa 为简化弹性计算，不是实测热循环应力，也不能与 YSZ 剪切许用值直接比较。反应风险值得在目标结构中评估属于 AI 推断，不是材料一票否决。

## Disagreements and Boundary Conditions

| Comparison | Status | Consequence |
|---|---|---|
| 同一扩散偶热压/追加退火序列 | directly-comparable，仅描述层厚 | 分清初始制备与追加退火，不声称每个增量显著 |
| 粉末、块体与实际 TGO | qualitative-only | 接触几何、压力和热历史不同，不直接预测涂层速率/寿命 |
| 模型正应力与外部 YSZ 剪切许用值 | not-directly-comparable | 撤回越阈值即失效论证 |
| 当前研究与 Li 前文 | not-directly-comparable，前文仅摘要 | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E8]] 已核摘要为 2012 年、1600 °C/8 h 且谈及结构/扩散；不能猜测温度不足或宣称争议彻底解决 |

## Method and Evidence Routes

| Route | Valid use | Source | Limit |
|---|---|---|---|
| 粉末退火与 XRD/相精修 | 指定接触/热历程后的相反应 | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]] | 离散温度和检测限不定义绝对阈值 |
| 扩散偶与局部成分分析 | 反应层/裂纹/微孔的空间观察 | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E4]] | 不能直接确定唯一扩散方向、体积膨胀或起裂原因 |
| 膨胀/压痕及弹性模型 | 指定物性和假设下的应力估算 | [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E5]]、[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] | 实测与转引参数混合，简化模型需服役验证 |

## Candidate Gaps and Open Questions

- [[directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]：candidate-question；Hf–Al₂O₃ 反应向实际 TGO 界面外推。

该页 narrowed/checked、novelty_status: not-assessed、priority: pending。撤回“所有候选材料普遍缺数据”和“界面问题被系统忽略”；本单篇不足以证明领域覆盖或首创。

## Downstream Review

2026-09-07：本轮替换两个 topic 与 [[directions/ceramic-corrosion/synthesis/literature-map]] 的旧正文，保留路径。源页、claim、gap 历史交接中的 topic/matrix 待办由本轮接续；原始证据未决仍保留。

- [[directions/ceramic-corrosion/synthesis/open-questions]]：按新版五项 gap 替换旧问题前提和高/中优先级。
- [[directions/ceramic-corrosion/synthesis/research-positioning]]：撤回以普适规律、领域空白和必然失效推出的确定方向，不冒充用户选题。
- [[directions/ceramic-corrosion/synthesis/review-outline]]：用当前矩阵重构主线与段落依据；不保留“1300 °C 公理—1500 °C 反转”的确定叙事。
- [[directions/ceramic-corrosion/synthesis/core-argument-map]]：旧快照仍待替换；恢复任务以 [[directions/ceramic-corrosion/memory/current_context]] 与本轮矩阵为入口。

上述四页本轮未重写，不能因主题/矩阵 checked 而认定其旧结论已同步。
