---
type: template
template_for: pdf-ingestion-checklist
status: active
created: 2026-06-02
updated: 2026-09-06
tags:
  - ingestion
---

# PDF Ingestion Checklist

本文件是阅读过程检查单，不是第二份论文卡片。工作结果写入 `templates/paper.md` 对应的 paper 页面。新入库和完整复核完整使用；局部修订只填与指定论断有关的部分。

## 1. Task Scope

- Mode: new-ingestion / full-review / local-revision
- Target paper/page:
- Requested claim or sections:
- Allowed downstream changes:
- Completion condition:

## 2. Source Identity

- Bibliographic identity and identifier:
- Source versions available: formal PDF / preprint / MinerU / translation / supplement / video / other
- Primary reading source:
- Zotero item / attachment (if applicable):
- Existing page / duplicate check:
- Source limitations:

## 3. Reading Coverage

| Part/material | Status | Evidence actually checked | Missing material and impact |
|---|---|---|---|
| Abstract/introduction | read / partial / unavailable |  |  |
| Methods | read / partial / unavailable |  |  |
| Results/discussion | read / partial / unavailable |  |  |
| Conclusion/limitations | read / partial / unavailable |  |  |
| Key figures/tables/formulas | checked / partial / unavailable |  |  |
| Supplement/video | checked / description-only / unavailable / not needed |  |  |

PDF recheck triggers: number/unit/sign/sample/formula/trend; figure-dependent comparison; OCR/translation conflict; error bars, missing combinations or exceptions.

## 4. Study Design and Comparability

- Objects/materials/data:
- Necessary conditions and coverage:
- Controls/baselines and whether same-condition:
- Metrics and operational definitions:
- Values, units, uncertainty/repeats/statistics:
- Measured, calculated, figure-estimated or cited:
- Variables that change together:
- Data source independence:

## 5. Key Evidence Records

Create only the records needed for major conclusions or disputes.

### E1

- Evidence type: direct observation/measurement / calculation/model / author interpretation / cited prior work / AI inference
- Object and conditions:
- Metric and result:
- Source locator:
- Supports:
- Does not establish / alternative explanation:
- Verification status and material checked:

Repeat as E2, E3… only when needed.

## 6. Claim Evaluation

For each proposed key finding:

- Claim:
- Evidence IDs:
- Support: sufficient / partial / insufficient — reason:
- Scope and exceptions:
- Author interpretation separated:
- Wording risks: causal / significant / none / all / first / best / universal / superior
- Decision: retain / narrow / withdraw / pending

## 7. Contribution, Limitations and Open Questions

- Author-stated contribution:
- Contribution confirmed by this reading:
- Author-stated limitations:
- Additional limitations from evidence boundary (`AI 推断`):
- Corpus gap or candidate question (optional):
- Field gap status: not assessed / searched within stated scope / pending

## 8. Write and Propagate

- Paper sections created/changed:
- Reused evidence IDs:
- Related pages updated within scope:
- Downstream claims/pages marked `needs-review` or listed for review:
- Error log needed:
- Index change needed and reason:
- Log entry added:

## Completion Gate

- [ ] Source identity and actual coverage are explicit.
- [ ] Major findings include conditions, metric, result, locator, evidence type and verification status.
- [ ] Author interpretation, cited work and AI inference are not presented as direct measurements.
- [ ] Comparability and data independence were checked before rankings, ratios or synthesis.
- [ ] Missing evidence limits only the dependent conclusion and is recorded nearby.
- [ ] Summary wording does not exceed the evidence.
- [ ] Local revision did not silently become a whole-page or whole-wiki rewrite.
- [ ] Downstream impact, log and index conditions were checked.


<!-- 方向约定：仅在已选方向D内生成；展开direction_id与D/路径。领域额外栏目只从D/AGENTS.md声明的扩展读取，不加载其他方向模板。 -->
