---
type: claim
status: active
review_status: checked
assessment: insufficient-evidence
created: 2026-08-23
updated: 2026-09-07
source_papers:
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
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

# 缺陷萤石高熵锆酸盐的 CMAS 抗蚀双机制解释（未确立）

## Claim Statement

- Statement: 待检验假说：在所研究五元稀土锆酸盐中，缺陷萤石无序抑制离子输运，并与小 RE 半径引起的产物热化学变化共同降低 CMAS 腐蚀层厚度。
- Claim type: causal mechanism
- Assessment: insufficient-evidence
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

19 种五元等摩尔块体，1300 °C/5 h、CMAS 25 mg/cm²；评价反应层厚度与结构/平均半径关系。这里只评价双机制因果，不把厚度范围当作涂层寿命。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E2]] | support / limit | direct | 2026-zirconate-structure | XRD/Raman 的结构分组 | 支持结构类别；部分样品标注冲突须保留 | partial |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E7]] | limit | direct | 2026-zirconate-corrosion | Fig. 13 与补充厚度表 | S3/S8 等半径映射冲突；补充表无样品 ID，不能按行补配 | partial |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | limit | author interpretation | 2026-mechanism-interpretation | 无新扩散实验或本体系扩散能垒计算 | 输运抑制未直接验证，结构/半径效应未分离 | checked |
| [[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput#E8]] | limit | cited prior work | Costa-thermochemistry | 产物形成焓转引 | 未测多元产物形成焓，原始热化学未全面复核 | pending |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

当前不足首先涉及样品—半径—厚度映射可信度，其次才是机制分离。不能在底层数据未对应时继续保留强定量趋势，只把剩余问题表述为“两机制贡献比例未知”。组间存在重叠，19 个组成也不等于 19 次机制独立验证。

## Challenging or Limiting Evidence

本研究结构组间目前仅 qualitative-only；映射解决前不做定量回归或最佳配方排名。YSZ/Gd₂Zr₂O₇ 的旧文献厚度存在材料、介质与条件差异（含 CAS 与 CMAS），属于 not-directly-comparable，不能据区间直接宣布全面优越。

## Use in Synthesis or Review

- Safe wording: 该研究提出无序输运与产物热化学共同影响腐蚀的解释；但关键图表映射尚未核清，且未独立测量输运或分离半径与结构贡献，因此该解释仍待验证。
- 使用边界：仅作为待验证解释、研究限制或候选问题使用，不得作为已成立前提组织大纲。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回小半径缺陷萤石最佳、显著薄于全部烧绿石、优于 YSZ/Gd₂Zr₂O₇ 的统一排名及已证双机制。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[wiki/gaps/Structure-Radius-Decoupling]] 应先区分数据对应问题与实验解耦问题；[[synthesis/research-positioning]]、[[synthesis/review-outline]] 不得沿用已验证设计准则。
- 共同入口：[[synthesis/literature-map]]、[[synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
