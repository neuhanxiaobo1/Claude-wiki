---
type: claim
status: active
created: 2026-08-27
updated: 2026-08-27
source_papers:
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
datasets:
metrics:
confidence: strong（EPMA 定量 + 反应式证据链，单篇）
tags:
  - claim
  - cmas
  - corrosion
  - ceramics
  - ebc
---

# RE2SiO5-CMAS 腐蚀产物中的石榴石相

## Claim

- RE2SiO5 与 CMAS 在 1300 °C 反应除生成磷灰石 Ca2RE8(SiO4)6O2 外，还生成石榴石型产物 (CaxRE3-x)(MgyAlzSi5-y-z)O12（(Ca+RE):(Mg+Al+Si)≈3:5）；该相为 RE2SiO5-CMAS 体系首次报道，将硅酸盐 EBC 的腐蚀产物谱从「单一磷灰石」扩展为「磷灰石 + 石榴石」。

## Evidence

- Source paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]" Key Claim 5
- Source section/page/table/figure: EPMA 点定量（表 7）、反应式 Eq 11/12、产物形貌（块状 vs 棒状）
- Evidence summary: 1300 °C/20 h 腐蚀后高熵样品反应层中检出块状石榴石 (CaxRE3-x)(MgyAlzSi5-y-z)O12，EPMA 定量 (Ca+RE):(Mg+Al+Si)≈3:5；棒状磷灰石（Ca:RE≈1:4）并存。
- Evidence strength: strong

## Scope

- Applies to: (Ho0.25Lu0.25Yb0.25Eu0.25)2SiO5-CMAS 1300 °C 腐蚀。
- Does not apply to: 单组分 RE2SiO5-CMAS 体系是否同样生成未核查（#47/#16 仅报道磷灰石）。
- Conditions: 腐蚀条件 1300 °C/20 h 单点；石榴石形成可能与高熵成分（多 RE 混合、Eu 价态）有关，亦可能为普遍现象但此前被忽略。

## Supporting Papers

- Paper: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - Evidence: EPMA 定量 + 反应式（Eq 11/12）+ 形貌。
  - Notes: 论文给出反应路径，但石榴石对 CMAS 抗性的作用（有益/有害）未厘清。

## Challenging or Limiting Evidence

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Challenge: 7 种单组分 RE2SiO5 在 1500 °C 的腐蚀产物均报道为 Ca2RE8(SiO4)6O2，未提及石榴石。
  - Evidence: #47 XRD/SEM-EDS（1500 °C）；#16（Lu2SiO5，1500 °C）亦未报道石榴石。
- 限制：仅高熵体系单篇报道；石榴石在单组分体系中「未生成」还是「未检出」待核查。

## Use in Review Writing

- Possible section: 「RE2SiO5-CMAS 腐蚀产物谱与反应路径」段落。
- Possible sentence role: background（产物谱扩展）+ future work（石榴石作用未明）
- Citation need: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"

## Related Pages

- Papers: "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Datasets:
- Metrics:
- Gaps:
- Reviews:

## Uncertainty

- 待确认：石榴石产物是否仅高熵体系特有，或单组分体系中同样存在（此前报道聚焦磷灰石）。
- 待核查：石榴石的晶体学数据（空间群、晶格参数）与 MinerU OCR 反应式核对。
- AI 推断：石榴石形成与 Eu2+/氧空位或 Mg/Al 富集的关系。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Source evidence checked.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
