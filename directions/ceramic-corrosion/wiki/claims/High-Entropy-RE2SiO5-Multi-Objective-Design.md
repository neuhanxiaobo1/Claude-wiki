---
direction_id: ceramic-corrosion
type: claim
status: active
review_status: checked
assessment: supported
created: 2026-08-27
updated: 2026-09-07
source_papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
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
  - ebc
---

# 四元高熵 RE₂SiO₅ 的多性能组合与抗蚀代价

## Claim Statement

- Statement: 本文四元 (Ho₀.₂₅Lu₀.₂₅Yb₀.₂₅Eu₀.₂₅)₂SiO₅ 展示低推算热导、较低热膨胀与中等 CMAS 抗性的性能组合，其腐蚀深度优于 Ho/Eu、劣于 Lu/Yb 对照，属于性能折中。
- Claim type: descriptive result
- Assessment: supported
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

限定于本配方块体及所列温区/腐蚀条件；烧结块体含少量二硅酸盐。多性能组合是描述性结果，不将元素功能分工、熵效应或全面最优包含在此判断中。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E1]]；[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E2]] | support / limit | direct / calculated | 2022-HE-thermal | RT–1000 °C；LFA、估算 cₚ 与孔隙校正 | 热导报告 1.07–1.47 W·m⁻¹·K⁻¹；非热导/热容全部直接实测 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E4]] | support / limit | direct / cited prior work | 2022-HE-expansion；SiC-reference | RT–1200 °C；TEC (4.0–5.9)×10⁻⁶ K⁻¹ | 与所引 SiC 范围接近；不等于同基底逐点匹配或热循环验证 | checked；外部原文未全面复核 |
| [[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E6]] | support | direct | 2022-HE-corrosion | 1300 °C/20 h；约 35 mg/cm²；作者渗透指标 | Lu 40.2、Yb 75.1、HE 125.4、Ho 166.5、Eu 248.6 μm | checked；统计及端点定义有限 |
| [[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E3]]；[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E4]]；[[directions/ceramic-corrosion/wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC#E8]] | limit | author interpretation / calculated | 2022-HE-mechanism | XPS 拟合、畸变与单配方设计 | 不独立确认氧空位浓度、声子因果或逐元素贡献 | checked |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

限定配方与指标后的性能折中有数据支持；HE 深度 125.4±8.7 μm 高于 Lu/Yb。比四单组元均值 132.6 μm 低约 5.4% 不证明显著协同，更不能量化熵效应。低模量也不直接等于高强度或长寿命。

## Challenging or Limiting Evidence

五样品腐蚀结果可在名义同条件、本篇指标内作 directly-comparable 描述性排序，但微结构、Eu 晶型和统计不足限制因果。热物性部分单组元对照来自文献，只作 qualitative-only 比较，不称全部同批新测。与 2019/2024 的深度不直接合并。

## Use in Synthesis or Review

- Safe wording: 该四元单硅酸盐展示低推算热导和较低 TEC；1300 °C/20 h 下其 CMAS 深度位于 Lu/Yb 与 Ho/Eu 之间，体现所选配方的性能折中。元素分工和熵效应仍是待验证解释。
- 使用边界：可作为限定事实用于综述，必须保留上述材料、条件、指标及 E# 来源；不能外推为机制或服役定律。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回功能分工已有效验证、全温区精确匹配 SiC、截距即缺陷浓度、本文 DFT 已证负 Grüneisen 机制、平均半径定律及显著熵协同。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[directions/ceramic-corrosion/wiki/gaps/CMAS-Corrosion-Data-1500C]]、[[directions/ceramic-corrosion/synthesis/research-positioning]]、[[directions/ceramic-corrosion/synthesis/review-outline]] 的高熵全面优越或确定稳定化前提待修。
- 共同入口：[[directions/ceramic-corrosion/synthesis/literature-map]]、[[directions/ceramic-corrosion/synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[directions/ceramic-corrosion/synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
