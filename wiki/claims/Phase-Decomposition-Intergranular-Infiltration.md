---
type: claim
status: active
created: 2026-08-27
updated: 2026-08-27
source_papers:
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: medium-high（单体系单篇论文，但含无 CMAS 对照与 TEM 双重排除实验）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# 相分解诱导晶间渗透

## Claim

- 1500 °C 下 Lu2SiO5 发生相分解 2Lu2SiO5 = Lu2Si2O7 + Lu2O3；分解生成的 Lu2Si2O7 被 CMAS 优先侵蚀并成为晶间快速渗透通道，导致 CMAS 沿晶界向基体内部快速渗透——高温下稀土单硅酸盐 EBC 的失效根源可以是基体相失稳，而非 CMAS 反应产物本身。

## Evidence

- Source paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]" Key Claim 3
- Source section/page/table/figure: 图 6/7（无 CMAS 的 1500 °C/50 h 分解对照）、图 5（反应前沿 fringes）、图 8（TEM 晶界洁净）
- Evidence summary: 无 CMAS 对照实验直接证实分解（出现 Lu2Si2O7 与 Lu2O3 两相，Eq 1）；腐蚀样品反应前沿出现 Ca2Lu8(SiO4)6O2 fringes 与三叉晶界处残余 CMAS；TEM/EDS 显示晶界无非晶相与成分偏聚，排除晶界偏聚假说——Lu2Si2O7 是晶间渗透主因。渗透深度 1500 °C/50 h 219 μm（1300 °C 约 50 μm 的 >4 倍）。
- Evidence strength: strong（对 Lu2SiO5 体系内部结论）

## Scope

- Applies to: 1500 °C 下 Lu2SiO5 的 CMAS 腐蚀。
- Does not apply to: 1300 °C（Lu2SiO5 相稳定、渗透仅约 50 μm）；其他 RE2SiO5 成分（是否分解未核查）。
- Conditions: 分解在 1500 °C 无 CMAS 条件下即自发进行；Lu2Si2O7 与 CMAS 的高反应性引用本组前作（RE2Si2O7「blister」现象，ref [24]）。

## Supporting Papers

- Paper: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - Evidence: 分解对照 + TEM + 渗透深度（1500 °C/50 h 219 μm vs 1300 °C 约 50 μm）。
  - Notes: 与「冷却起始析出 + 垂直定向生长」共同解释 Lu2SiO5 的 1500 °C 失效。

## Challenging or Limiting Evidence

- 无直接反驳证据；主要限制：
  - 单体系（Lu2SiO5）单篇论文；#47（七体系 1500 °C）未做 TEM 与无 CMAS 对照，无法判断分解是否普遍。
  - #47 将 1500 °C RE 效应弱化归因于粘度剧降；本文提出相分解机制——二者可能叠加，相对权重未定量。

## Use in Review Writing

- Possible section: 「稀土单硅酸盐 EBC 的 1500 °C 失效机制」段落。
- Possible sentence role: contrast（与 1300 °C 对比）+ limitation（相稳定性作为选材判据）
- Citation need: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"

## Related Pages

- Papers: "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
- Reviews:

## Uncertainty

- 待确认：相分解在其他 RE2SiO5 成分（Tb–Yb）中是否普遍存在。
- 待核查：MinerU OCR 中分解反应式与 EDS 数据引用前与原文核对。
- AI 推断：高熵 RE2SiO5（#48）的 1500 °C 相分解行为（熵稳定效应是否抑制分解）。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
