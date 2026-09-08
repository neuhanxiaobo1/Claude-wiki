---
type: gap
status: narrowed
review_status: checked
gap_type: candidate-question
novelty_status: not-assessed
created: 2026-08-23
updated: 2026-09-07
priority: pending
papers:
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
---

# 结构与 RE 半径效应的可辨识性（先核清数据）

## Gap Statement

针对 2026 年高熵锆酸盐，先恢复可追溯的样品—结构—半径—厚度对应关系，再判断现有数据或可实现对照能否区分结构状态、平均 RE 半径与其他组成因素对腐蚀指标的影响。

- Current classification: candidate-question
- 边界：仅复用七篇复核源页与八项新版 claim；本轮未做领域新颖性检索。review_status: checked 指前提、分类和使用边界已核查，不表示问题已解答或实验可行性已确认。

## Origin and Preconditions

evidence boundary + AI inference。缺陷萤石双机制与跨体系半径因果 claim 均为 insufficient-evidence。不能以“缺陷萤石最佳”或“X1/X2 已证翻转”为既定前提；此问题首先是数据可信度，其次才是解释变量可辨识性。

## Existing Coverage

| Work/evidence | What is already addressed / conditions | What remains | Independence / review status |
|---|---|---|---|
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E2]]；[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]] | 结构表征与腐蚀截面已提供 | 样品标签、Fig. 13 半径与补充厚度表身份冲突，不能按行自动对应 | checked 范围内发现冲突；定量关系未决 |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | 提出无序输运与产物热化学解释 | 没有直接输运或独立半径/结构控制；Costa 为转引 | 解释/转引，不算机制实测 |
| [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E2]]；[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E8]] | 2019 单硅酸盐有限条件层厚关联 | 晶型归属及外部 JECS 对照未核全，指标也须比较 | checked；不构成晶型翻转确证 |

## Why It Matters

AI 推断：只有变量身份和比较资格可靠，才可能判断结构控制是否具有超出组成关联的解释力。不能先在“选结构/选小半径”间二选一，再寻找适配证据。用户未确认该体系为选题。

## Novelty Assessment

- Novelty status: not-assessed。
- 本轮没有执行领域检索，不能声称“尚无人研究”“首次”或“领域普遍缺失”；旧 high/medium 和 strong 不能作为新颖性或选题优先级。
- 已有最接近工作及限制见上表。外部工作可能已解决问题，后续若要认定 scoped-field-gap，必须记录日期、检索源/检索式、纳排范围、最接近工作及反例。

## Research Question and Required Evidence

- 可检验问题（AI 推断）：在样品映射修复后，现有组成覆盖是否足以识别结构/半径的独立关联？若不足，能否制备具有实测结构差异、可比组成和微结构的对照，并在同一腐蚀指标下检验差异？
- 所需证据与比较：先取得原始样品 ID、半径计算口径、结构表征与逐样品厚度原数；无法恢复时只保留可核子集，不进行全集回归。随后检查变量共变与覆盖，再评估对照可行性。统计控制不能自动代替独立因果实验，半径相近也不等于其余化学性质相同。
- 回答或削弱前提的结果：若映射修复后原趋势消失，应撤回基于该趋势的设计论据；若无可识别的独立变化，则不能估计两机制权重。可靠对照显示结构变化无可重复作用也能回答所测范围的问题；若发现已有同范围充分验证的研究，则进一步收窄新颖性候选。

## Feasibility and Research Path

AI 推断：原始数据核查先于配方设计；结构能否在近似相同组成下调节需要实际验证，可行性 pending。旧提案在固定 Zr 半径且固定平均 RE 半径时又要求半径比跨阈值，按比值定义不能成立；删除该伪正交路径，不预设可自由改变结构。

## Risks, Alternative Explanations and Counter-Evidence

晶型、有序度、价态、孔隙和产物化学可能共同变化。2019 JECS 原文尚未完成复核，不写已证 X1/X2 翻转；其他体系的半径关联也不证明本体系独立因果。与高温数据 gap 的区别是本页关注变量可辨识性，而非温度覆盖。

## Status and Revision History

- 2026-09-07：status 改为 narrowed；用复核后的证据替换旧“真实 gap”及确定性机制前提，保留原路径。priority: pending 表示未完成研究价值、资源和新颖性排序。
- 本轮完成五项 gap 的前提与分类修订，并同步 index、计划和维护记录；未改原始资料或重新复核外部文献。
- 下游待复核：[[synthesis/open-questions]] 应替换旧问题前提与评级；[[synthesis/research-positioning]] 应撤回依赖旧 gap 的确定方向；[[synthesis/review-outline]]、[[synthesis/core-argument-map]] 和 [[synthesis/literature-map]] 应依据当前边界重组，不将候选当作已证领域结论。
- 相关主题正文仍待同步：[[wiki/topics/Ceramic Corrosion]]。源页/claim 历史 gap 待办由本轮修订接续；具体原文未决仍有效。

## Use in Positioning or Review

- Safe wording: 当前锆酸盐证据先受样品/半径映射冲突限制；在恢复可信对应关系后，结构与组成效应能否分离可作为候选问题，尚不能将双机制权重未知包装成已确认的领域空白。
- 更强使用前提：先解决会改变论断的原始证据疑点，再按用户研究范围评估已有研究、可行性与新颖性；本页不是用户已确认的选题。
