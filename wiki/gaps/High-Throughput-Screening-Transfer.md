---
type: gap
status: open
created: 2026-08-23
updated: 2026-08-23
priority: medium
evidence_strength: strong
papers:
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
topics:
  - "[[wiki/topics/Ceramic Corrosion]]"
methods:
claims:
tags:
  - gap
  - cmas
  - corrosion
  - ceramics
---

# 高通量筛选方法向其他 EBC/TBC 体系推广

## Gap Description

- 层叠法高通量筛选（#46）与高温原位观察（#47）均已在单一体系验证其有效性，但尚未推广到其他 EBC/TBC 材料体系（如 RE2SiO5、RE2Si2O7、高熵稀土硅酸盐/锆酸盐）；三篇论文使用的高通量策略（层叠法、19 成分并行制备）也未统一到同一框架下。

## Why It Matters

- 加速成分筛选是用户课题的方法学机会：把「层叠法统一条件对比 + 原位观察机制」组合推广到稀土硅酸盐/二硅酸盐体系，可直接生成「成分-结构-温度-抗蚀性」多维数据，支持综述中的规律归纳与选题定位。

## Supporting Evidence

- Paper: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - Evidence: 作者强调层叠法可推广至其他体系（#46 Potential Gaps 2）；层叠法目前在钽酸盐体系的渗透深度定量已达 ±2–10 μm 精度。
  - Source section/page/table/figure: 全文方法部分、Conclusion
  - Evidence strength: strong

- Paper: "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - Evidence: 高温原位观察方法仅用于 RE2SiO5（#47 Potential Gaps 3）；作者指出可推广至 RE2Si2O7、高熵稀土硅酸盐等。
  - Source section/page/table/figure: 全文
  - Evidence strength: strong

- Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Evidence: 19 成分高通量制备+表征流水线已建立，但腐蚀条件单一（1300 °C/5 h），未与层叠法/原位观察联用。
  - Source section/page/table/figure: §2
  - Evidence strength: strong

## Cross-Page Basis

- Page: "[[wiki/topics/Ceramic Corrosion]]"
  - What it shows: 主题页 Method Routes 已归纳 3 条方法路线（原位观察、层叠法、并行制备），但三者相互独立、无交叉验证。
  - Why it supports this gap: 方法路线之间的「组合」本身是空白——这正是可做的研究。

## Gap Type

- Type: 真实 gap
- Reason: 三篇论文各自声明方法可推广但均未跨体系实施（作者自述 + 客观空白）。

## How Existing Work Handles It

- Existing approach:
  - Paper: "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - Remaining limitation: 并行制备流水线仅覆盖锆酸盐；层叠法的统一条件优势（消除样品间误差）与并行制备的高成分通量尚未结合。

## What Remains Unsolved

- Unsolved part: 跨体系（硅酸盐/二硅酸盐/钽酸盐/锆酸盐）统一方法框架下的可比数据；原位观察与高通量腐蚀的联用。
- Why unresolved: 各方法由同一研究组分别开发，跨体系推广需要解决高温 CMAS 保持、层间扩散、成分-结构表征通量等具体问题。

## Possible Research Questions

- Question: 层叠法能否在 RE2SiO5/RE2Si2O7 体系中复现「渗透深度-RE 半径」规律并与钽酸盐数据直接对比？
  - Feasibility: high（方法成熟、材料制备工艺成熟）
  - Evidence needed: 层叠硅酸盐块体 + 1300 °C 腐蚀截面数据。

## Possible Research Paths

- Path: 层叠法 + 原位观察联用于稀土二硅酸盐体系（填补 #36/#23 入库后的体系对比需求）。
  - Required method/data: 层叠压制烧结 + 高温接触角仪/相机 + 截面 SEM/EPMA。
  - Risk: 二硅酸盐层间固相扩散高于钽酸盐，层间污染需预验证。

## Risks and Counter-Evidence

- Risk: 跨体系推广可能被他人抢先（该组工作节奏快，58 篇清单中已有大量后续工作）。
  - Evidence: 2025–2026 年该组已连续发表高通量系列（#46、#18、#58 数据驱动），方法学空白窗口有限。
  - How to check: 检索该组 2026 年新论文确认是否有跨体系工作（#52 中文综述可能已涉及）。

## Related Pages

- Papers: "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"、"[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"、"[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
- Topics: "[[wiki/topics/Ceramic Corrosion]]"
- Methods:
- Claims:
- Reviews:

## Uncertainty

- 待确认：该 gap 是否已被该组 2026 年新工作覆盖（待入库 #36/#23/#48/#52 核查）。
- 待核查：无
- AI 推断：跨体系推广的技术障碍程度。

## Maintenance Checklist

- [x] Added to `index.md`.
- [x] Evidence strength marked.
- [x] Related open question updated if needed.
- [x] Tags checked against `memory/tag_taxonomy.md`.
- [x] Aliases checked against `memory/term_aliases.md`.
