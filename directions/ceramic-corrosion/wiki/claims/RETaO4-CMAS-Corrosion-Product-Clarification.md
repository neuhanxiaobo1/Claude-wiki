---
direction_id: ceramic-corrosion
type: claim
status: active
review_status: checked
assessment: supported
created: 2026-08-23
updated: 2026-09-08
source_papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
topics:
  - "[[directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
---

# 层叠 RETaO₄–CMAS 试验中的主要固溶体产物

## Claim Statement

- Statement: 本文 1300 °C 的 RETaO₄ 层叠筛选试验主要产物可归属为含 Ca/RE/Ta/Mg/Al 的复杂固溶体，并伴有少量磷灰石。
- Claim type: descriptive result
- Assessment: supported
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

八种 RE（Nd、Sm、Eu、Gd、Dy、Ho、Y、Er）的十层组合；C33M9A13S45（AlO₁.₅ 计量）、30 mg/cm²，1300 °C/25–100 h。支持产物类别，不将层片当作八套化学独立的单 RE 试验。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E4]] | support | direct | 2025-RETa-stack-products | XRD 与 Y/Nd 层 50 h 的 TEM/SAED | 支持主要复杂固溶体及少量磷灰石；局部 TEM 支持 FCC/六方类别 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E5]] | support / limit | direct / author interpretation | 2025-RETa-stack-products | EPMA 阳离子归一化 | Ca+RE 与 Ta+Mg+Al 约各半；排除了 O/Si，非完整原子分数 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E2]] | limit | direct | 2025-RETa-stack-products | Nd/Er 区域的跨 RE 点成分 | 存在其他 RE，不能将实际产物等同纯单 RE 模型 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening#E6]] | limit | calculated | 2025-RETa-DFT | 固定成分 Fd-3m 模型 | 模型不代替实际多 RE 产物的精确组成鉴定 | checked；能量定义未决 |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

XRD、局部 TEM/SAED 与成分分析共同支持所列产物类别。作者名义式 (Ca2−xREx)(Ta2−y−zMgyAlz)O7 及 Ca₂RE₈(SiO₄)₆O₂ 可作为相指认表达；不能据归一化比例断言全部占位/化学计量已确定，也不能把全部样品/时长均写成做过 TEM。

## 2026-09-08 独立单组分补充

[[directions/ceramic-corrosion/wiki/papers/2024-M-YTaO4-CMAS-Grain-Boundary-Infiltration#E4]] 提供1300 °C/5、50、80 h、约30 mg/cm²下独立M-YTaO₄的XRD/局部EDS及50 h EPMA，支持主要复杂固溶体、M′-YTaO₄与少量磷灰石的类别。原始数据组2024-MYTa-corrosion，与层叠实验不同；方法间仅qualitative-only。此来源补强相类别，保持本claim原层叠范围与supported评价，不证明八层独立性或全部前文错误。晶内/晶界两深度及热循环边界见E2/E3/E7。

## Challenging or Limiting Evidence

同一层叠试验内可 qualitative-only 比较产物类别；不同层的跨 RE 组成使化学独立性未成立。与旧文献不同材料/条件的争议为 not-directly-comparable，未逐篇复核前不能宣布全部争议彻底解决。

## Use in Synthesis or Review

- Safe wording: 在这组 1300 °C 层叠 RETaO₄–CMAS 试验中，XRD、局部 TEM 与成分分析支持主要复杂固溶体和少量磷灰石的归属；产物存在跨 RE 组成，精确化学计量和层间独立性仍需限定。
- 使用边界：可作为限定事实用于综述，必须保留上述材料、条件、指标及 E# 来源；不能外推为机制或服役定律。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回精确化学计量全面确认、八种独立单 RE 同时验证、所有局部均有 TEM 以及彻底澄清既有文献争议。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[directions/ceramic-corrosion/wiki/topics/Ceramic Corrosion]] 的争议已澄清表述、[[directions/ceramic-corrosion/wiki/gaps/High-Throughput-Screening-Transfer]] 的层间完全独立假设及 [[directions/ceramic-corrosion/synthesis/review-outline]] 的确定性机制结论待修。
- 共同入口：[[directions/ceramic-corrosion/synthesis/literature-map]]、[[directions/ceramic-corrosion/synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[directions/ceramic-corrosion/synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
