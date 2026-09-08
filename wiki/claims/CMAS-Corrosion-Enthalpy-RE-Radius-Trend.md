---
type: claim
status: active
review_status: checked
assessment: insufficient-evidence
created: 2026-08-23
updated: 2026-09-08
source_papers:
  - "[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening]]"
  - "[[wiki/papers/2019-RE2SiO5-CMAS-General-Trend]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
---

# RE 半径—形成焓—CMAS 抗蚀性的跨体系因果解释（未确立）

## Claim Statement

- Statement: 待检验假说：在约 1300 °C 的多类 RE 陶瓷中，RE 半径通过改变腐蚀产物形成焓，统一决定小半径成分具有较好的 CMAS 抗蚀性。
- Claim type: causal mechanism
- Assessment: insufficient-evidence
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

涉及单硅酸盐、RETaO₄ 和高熵锆酸盐块体。半径、物相、微结构与反应产物同时变化；各文的衰退层、最深渗透和腐蚀层不是统一指标。当前评价针对上述跨体系因果假说，不否定单篇的限定关联。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E2]] | support | direct | 2019-corrosion | 1300 °C/50 h；30 mg/cm²；八 RE 衰退层 | 小半径组总体层薄；不证明严格线性或独立半径因果 | checked |
| [[wiki/papers/2019-RE2SiO5-CMAS-General-Trend#E6]] | limit | cited prior work | Risbud-2001 | 无 Ca 氧磷灰石量热外推至含 Ca 产物 | 源页已核摘要/讨论；2019 自身焓方向表述矛盾，不是本文量热 | partial |
| [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]；[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] | limit | cited prior work | 2019-corrosion | 两篇的 1300 °C 对照来自 2019 | 不能增加独立腐蚀实验计数；与高温指标不可直接合并 | checked |
| [[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]]；[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]] | limit | direct / author interpretation | 2022-HE-corrosion | 1300 °C/20 h；35 mg/cm²；单个四元配方 | 深度 Lu < Yb < HE < Ho < Eu；晶型等未控制，不验证平均半径因果 | checked |
| [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]]；[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E3]] | support / limit | direct | 2025-RETa-stack | 1300 °C；层叠试样；25–100 h | 总体成分差异，100 h 非严格单调；跨 RE 产物限制化学独立性 | checked |
| [[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]] | limit | calculated | 2025-RETa-DFT | 固定成分结构模型；Fig. 15 为正值 | 参考态/符号/归一化未清，不保留更负、更放热解释 | partial |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]]；[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | limit | direct / author interpretation | 2026-zirconate-corrosion | 1300 °C/5 h；25 mg/cm² | Fig. 13 半径—样品映射冲突，不能确认定量回归 | partial |
| [[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]]；[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E8]]；[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]]；[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]]；[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | limit | cited prior work | Costa-thermochemistry | 多篇机制段转引同一热化学来源 | 原文未全面复核；不按转引次数计为独立量热 | pending |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## 2026-09-08 新增 #59 证据

[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E1]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E2]]、[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E3]] 提供新实验组 2025-RE2SiO5-stack：1300 °C/20 h、30 mg/cm² 下 Er 区相对侵入最浅，最小半径 Lu 并非最浅。它限制普适单调排序，但与 2019 衰退层不可直接对比。[[wiki/papers/2025-RE2SiO5-CMAS-Multilayer-Stacking-Screening#E8]] 的 Costa 转引不新增量热验证，主文形成焓方向亦不一致；assessment 保持 insufficient-evidence。历史“#59 未核”状态由本记录接续，不沿用旧摘要。

## Assessment Rationale

2019 支持自身条件下的总体关联，2025 层叠结果提供另一组有限关联；它们没有隔离半径、产物热化学及传输贡献。2019 焓外推、2025 DFT 定义不清、2026 映射冲突使跨体系因果链无法闭合。证据不足不等于已证明该假说为假。

## Challenging or Limiting Evidence

2019 内部八样品按本篇层厚可比较（directly-comparable，仅描述总体关联）。2019 与 2023/2024 的深度定义、制备及负载不同（not-directly-comparable），不能计算温度劣化倍数。不同材料体系只作 qualitative-only 比较，不统一排名。

## Use in Synthesis or Review

- Safe wording: 2019 年单硅酸盐实验显示，固定 CMAS 与 1300 °C 条件下，较小 RE 半径组总体衰退层较薄；形成焓是候选解释，其跨体系因果性尚未确立。
- 使用边界：仅作为待验证解释、研究限制或候选问题使用，不得作为已成立前提组织大纲。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回六篇独立支持、三体系普适规律、OB 严格线性预测、2025 DFT 更负及高熵配方独立验证。旧页所列 JECS 2019（10.1016/j.jeurceramsoc.2018.12.015）与 Extreme Materials 2025（10.1016/j.exm.2025.10.001）仅保留为待核来源身份，不在本轮证据集内；不沿用其未经本轮核实的排序或晶型翻转。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[wiki/gaps/Structure-Radius-Decoupling]] 的已证晶型翻转前提、[[wiki/gaps/CMAS-Corrosion-Data-1500C]] 的高温普适推广前提，及 [[synthesis/core-argument-map]]、[[synthesis/review-outline]] 的“1300 °C 公理”须撤回后重构。
- 共同入口：[[synthesis/literature-map]]、[[synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
