---
direction_id: ceramic-corrosion
type: claim
status: active
review_status: checked
assessment: insufficient-evidence
created: 2026-08-23
updated: 2026-09-07
source_papers:
  - "[[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
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

# 黏度降低导致 RE 抗蚀性规律弱化或反转（待验证）

## Claim Statement

- Statement: 待检验假说：CMAS 从 1300 °C 升至 1500 °C 时的黏度降低，导致 RE₂SiO₅ 抗蚀性与 RE 成分的关系弱化或反转。
- Claim type: causal mechanism
- Assessment: insufficient-evidence
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

以 2023 年单硅酸盐研究为主，区分 FactSage 黏度计算、块体侵入深度与原位可见析出。因变量为成分—抗蚀指标关系，解释变量为黏度；升温同时改变溶解、析出、相稳定性等，未实现黏度独立控制。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E5]] | support | calculated | 2023-FactSage | 1300/1500 °C 黏度 | 作者计算前者大于后者四倍；不等于黏度实测或腐蚀倍数 | checked；模型参数未完整复现 |
| [[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E1]]；[[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E6]] | limit | direct | 2023-corrosion | 1500 °C；5/20/50 h 覆盖样品不同 | 5 h 七 RE，20 h 缺 Tb，50 h 仅 Y/Er/Tm/Yb；趋势非简单单调 | checked；ESM 未读 |
| [[directions/ceramic-corrosion/wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation#E7]] | limit | cited prior work | 2019-corrosion | 1300 °C 对照来自 2019 | 对照不是同批温度单变量试验，测厚定义不同 | checked |
| [[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]]；[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]]；[[directions/ceramic-corrosion/wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E8]] | limit | direct / author interpretation | 2024-Lu-corrosion | 仅 Lu；1500 °C/50 h 最深渗透 219 μm | 未测黏度/多 RE 排名；冷却析出时序存在图文冲突 | partial |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

计算支持名义熔体黏度随升温下降这一模型结果，但不足以归因成分排序变化。2023 缺测与非单调数据不能写成完整七成分三时长的反转；2024 单一 Lu 不能作第二次多 RE 排名验证。

## Challenging or Limiting Evidence

2023 同时长且实际有数据的样品可按本篇指标比较（directly-comparable，统计仍有限）。与 2019 衰退层对照 not-directly-comparable；2023 与 2024 原位不同材料/热历程仅 qualitative-only。未见表面析出不等于无溶解或无反应。

## Use in Synthesis or Review

- Safe wording: 2023 年研究的 FactSage 计算给出 1300 °C 黏度大于 1500 °C 的四倍；作者据此讨论传输影响，但现有实验未独立证明黏度使 RE 抗蚀性规律反转。
- 使用边界：仅作为待验证解释、研究限制或候选问题使用，不得作为已成立前提组织大纲。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回已证方向反转、双篇独立确认、Lu 抗蚀性劣化四倍、保温全程无反应及完整七成分×三时长数据等表述。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[directions/ceramic-corrosion/wiki/gaps/CMAS-Corrosion-Data-1500C]]、[[directions/ceramic-corrosion/wiki/gaps/Cooling-Precipitation-Coating-Integrity]] 以及 [[directions/ceramic-corrosion/synthesis/review-outline]] 的温度反转与仅冷却析出前提待修。
- 共同入口：[[directions/ceramic-corrosion/synthesis/literature-map]]、[[directions/ceramic-corrosion/synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[directions/ceramic-corrosion/synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
