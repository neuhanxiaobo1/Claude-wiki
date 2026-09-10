---
direction_id: ceramic-corrosion
type: claim
status: active
review_status: checked
assessment: supported
created: 2026-08-27
updated: 2026-09-07
source_papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
topics:
  - "[[directions/ceramic-corrosion/wiki/topics/Thermal Barrier Coatings]]"
methods:
datasets:
metrics:
tags:
  - claim
  - ceramics
  - corrosion
  - tbc
---

# Hf₆Ta₂O₁₇ 与 Al₂O₃ 在指定热处理下的反应不相容

## Claim Statement

- Statement: Hf₆Ta₂O₁₇ 与 Al₂O₃ 在本文 1400 °C 粉末反应及热压/退火扩散偶条件下发生反应，形成含 AlHf₃TaO₁₀ 的产物或界面反应层。
- Claim type: descriptive result
- Assessment: supported
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

粉末混合物空气 1400 °C/10 h；块体扩散偶真空 1400 °C、40 MPa/10 min 热压后追加空气退火。Al₂O₃ 用作相容性对照材料；并非真实粘结层上生长的 TGO。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E1]]；[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E2]] | support | direct | 2025-Hf-powder-products | 粉末 XRD/Raman 及参考相精修/局部 TEM | 1400 °C 已出现新相；综合鉴定支持 AlHf₃TaO₁₀/Pbcn | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E3]] | support | direct | 2025-Hf-diffusion-couple | 热压后与追加 10/30/50 h | 层厚依次 2.93±0.38 / 3.16±0.35 / 4.32±0.43 / 4.61±0.62 μm | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E4]] | limit | direct / author interpretation | 2025-Hf-diffusion-couple | 裂纹、微孔及元素线扫 | 不独立证明 Al 单向扩散、Kirkendall 或 9.2% 实测膨胀 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E5]]；[[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E6]] | limit | calculated / cited prior work | 2025-Hf-elastic-model | 简化弹性应力与外部材料参数 | 应力为模型；YSZ 剪切许用值不是本材料相同应力分量判据 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility#E8]] | limit | cited prior work | Li-prior-abstract | 出版社摘要为 2012 年、1600 °C/8 h | 摘要已谈结构变化和 Al 扩散，不能说低于阈值所以未反应 | partial；全文未核 |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

粉末物相与扩散偶反应层充分支持所列条件下的反应不相容。初始热压层与追加退火层必须分开；少数时点、有限误差说明不足以确定动力学定律、温度阈值或涂层寿命。

## Challenging or Limiting Evidence

本篇扩散偶按同一工艺序列可 directly-comparable 描述层厚，但不宣称各增量统计显著。粉末、扩散偶与实际 TGO 仅 qualitative-only；模型正应力与 YSZ 剪切许用范围 not-directly-comparable。1300 °C XRD 变化小不等于绝对无反应。

## Use in Synthesis or Review

- Safe wording: 该研究在 1400 °C 粉末及块体扩散偶实验中发现 Hf₆Ta₂O₁₇–Al₂O₃ 反应及含 AlHf₃TaO₁₀ 的反应层，提示需评估其作为涂层候选时的界面相容性；实际 TGO 热循环失效尚未验证。
- 使用边界：可作为限定事实用于综述，必须保留上述材料、条件、指标及 E# 来源；不能外推为机制或服役定律。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回 >1400 °C 才反应、2.93 μm 对应退火 10 h、Al 单向扩散已证、应力实测并越过本材料失效阈值及已推翻 Li 全文等判断。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[directions/ceramic-corrosion/wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]、[[directions/ceramic-corrosion/wiki/topics/Thermal Barrier Coatings]] 与 [[directions/ceramic-corrosion/synthesis/review-outline]] 的阈值、扩散机制及涂层失效推论待修。
- 共同入口：[[directions/ceramic-corrosion/synthesis/literature-map]]、[[directions/ceramic-corrosion/synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[directions/ceramic-corrosion/synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
