---
type: claim
status: active
review_status: checked
assessment: partially-supported
created: 2026-08-27
updated: 2026-09-07
source_papers:
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
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
  - ebc
---

# Lu₂SiO₅ 相演化对晶间侵入的可能贡献

## Claim Statement

- Statement: 在本文 1500 °C 的 Lu₂SiO₅–CMAS 实验中，基体相演化及二硅酸盐相关区域可能参与晶间侵入路径的形成。
- Claim type: causal mechanism
- Assessment: partially-supported
- Review status: checked

本轮基于七篇已复核论文页的 E1–E8 进行下游证据迁移。checked 表示本页判断及边界已核查，不代表未决原文、外部转引或机制均已验证。

## Scope and Definitions

无压烧结 Lu₂SiO₅ 块体初始含 0.3 wt% Lu₂Si₂O₇；CMAS 35 mg/cm²，1500 °C/5、20、50 h；无 CMAS 对照为 1500 °C/50 h。判断涉及相演化的可能贡献，未限定为唯一或主要根源。

## Evidence Ledger

| Evidence | Role | Evidence type | Independence group / original data source | Conditions and metric | What it supports | Verification |
|---|---|---|---|---|---|---|
| [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E1]] | limit | direct | 2024-Lu-initial | Fig. 1 精修 | 初始已有二硅酸盐，不能把全部二硅酸盐算作新生分解量 | checked |
| [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E5]] | support | direct / author interpretation | 2024-Lu-heat-control | 无 CMAS 1500 °C/50 h；Fig. 6/7 | 相组合/邻近关系支持 2Lu₂SiO₅ = Lu₂Si₂O₇ + Lu₂O₃ 的分解解释 | checked；缺定量相平衡 |
| [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E4]] | support | direct / author interpretation | 2024-Lu-corrosion | Fig. 5 截面与点分析 | 存在晶间侵入及二硅酸盐相关区域；先后顺序非实时追踪 | checked |
| [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E6]] | limit | direct | 2024-Lu-heat-control | Fig. 8 局部 TEM/线扫 | 局部未见非晶膜/明显偏聚，不能排除全部晶界因素 | checked |
| [[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E3]]；[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth#E7]] | limit | direct / cited prior work | 2024-Lu-corrosion；2019-corrosion | 原位选帧及 219 μm 最深渗透 | 析出时序冲突；与 2019 约 50 μm 衰退层不直接可比 | partial |

同组原始数据的多种表征或多篇转引不重复计数。Verification 中的 partial/pending 保留对应证据的未决，不被页面 checked 覆盖。

## Assessment Rationale

无 CMAS 热处理对照和侵入形貌为作者机制提供部分支持；缺少初始杂相梯度、取向控制、同位置路径追踪及分解量测定，尚不能确立优先侵蚀次序或量化贡献。产物排列通路与其他晶界因素也未排除。

## Challenging or Limiting Evidence

有/无 CMAS 条件对照可 qualitative-only 支持相演化解释，不能当作独立控制了所有杂相和取向的因果试验。219/50 μm 跨研究 not-directly-comparable，不保留四倍劣化。单个 Lu 结果不证明全部 RE 或高熵样品同样分解。

## Use in Synthesis or Review

- Safe wording: Lu₂SiO₅ 的 1500 °C 热处理对照显示支持分解解释的相组合，结合 CMAS 晶间侵入形貌提示相演化可能参与侵蚀；其独立贡献与优先侵蚀过程尚待验证。
- 使用边界：仅作为待验证解释、研究限制或候选问题使用，不得作为已成立前提组织大纲。

## Revision History and Downstream Review

- 2026-09-07：保留原路径和正确证据，替换旧 Claim/Confidence；撤回初始完全纯相、TEM 排除全部晶界因素、分解为唯一主因、二硅酸盐全由本次分解新生及温度劣化四倍。
- 本轮更新：本 claim、其余七项 claim 及索引/维护记录；未重写 gap、topic 或综合页正文。
- 下游待复核：[[wiki/gaps/CMAS-Corrosion-Data-1500C]] 与 [[synthesis/review-outline]] 的普遍分解主线、[[synthesis/research-positioning]] 的高熵必然抑制分解前提待修。
- 共同入口：[[synthesis/literature-map]]、[[synthesis/core-argument-map]] 应使用当前 Assessment 与独立来源分组替换旧强度/共识；[[synthesis/open-questions]] 的候选前提须随之核对。用户核心研究问题仍未确定，本页不代替选题确认。
