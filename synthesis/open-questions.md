---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-23
questions:
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
claims:
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
tags:
  - synthesis
  - open-question
  - gap
---

# Open Questions

本页记录跨论文开放问题（对应 `wiki/topics/Ceramic Corrosion` 的 Main Questions 与 `wiki/gaps/` 页面）。

## Question Triage

| Question | Priority | Related gap | Evidence strength | Status |
|---|---|---|---|---|
| Q1 1500 °C「RE 效应弱化」是否普适 | high | "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]" | strong（缺失为事实） | open |
| Q2 结构类型与 RE 半径如何解耦 | high | "[[wiki/gaps/Structure-Radius-Decoupling]]" | strong | open |
| Q3 冷却析出对涂层完整性的影响 | medium | "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]" | strong（析出事件）/ weak（后果推断） | open |
| Q4 高通量方法能否跨体系推广 | medium | "[[wiki/gaps/High-Throughput-Screening-Transfer]]" | strong | open |
| Q5 形成焓-RE 半径规律是否普适热力学规律 | medium | —（隐含于 Q1） | strong（1300 °C） | open |

## High Priority Questions

- Question: Q1 1500 °C 下 CMAS 粘度剧降导致的「RE 种类影响弱化」在钽酸盐、锆酸盐体系中是否同样成立？
  - Why important: 决定成分设计准则是否需按服役温度分级；若普适，1300 °C 小半径优选策略在高温失效。
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - Supporting papers: #47（单体系证实）、#46/#18（仅 1300 °C，构成空白）
  - Related claims: "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - Evidence strength: strong（空白是事实）；weak（规律外推）
  - Next evidence needed: 钽酸盐/锆酸盐 1500 °C 腐蚀截面数据（≥3 RE 成分 × 2 体系）

- Question: Q2 结构类型（烧绿石 vs 缺陷萤石）与 RE 平均半径对 CMAS 抗性的贡献如何解耦？
  - Why important: 决定高熵 TBC 设计优先「选结构」还是「选半径」。
  - Related gap: "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - Supporting papers: #18（19 成分共线数据）
  - Related claims: "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - Evidence strength: strong（共线为事实）；weak（双重机制解释）
  - Next evidence needed: 同半径异结构/同结构异半径正交成分组腐蚀数据

## Medium Priority Questions

- Question: Q3 冷却析出的短水平 Ca2RE8(SiO4)6O2 晶粒对涂层热循环完整性（剥落、开裂）的影响？
  - Why important: 实际服役含热循环，等温腐蚀研究系统性低估冷却析出损伤。
  - Related gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - Supporting papers: #47（原位观察析出事件）
  - Evidence strength: strong（析出事件）；weak（后果为 AI 推断）
  - Next evidence needed: 热循环实验 + 裂纹/剥落统计

- Question: Q4 层叠法/原位观察/并行制备三条高通量路线能否跨体系推广并统一到同一框架？
  - Why important: 方法学组合是用户课题的机会点；该组工作节奏快，窗口期有限。
  - Related gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - Supporting papers: 三篇论文（各自方法单体系验证）
  - Evidence strength: strong（作者自述可推广）
  - Next evidence needed: 跨体系预实验；检索该组 2026 年新工作确认空白是否已被填补

- Question: Q5 腐蚀产物形成焓随 RE 半径增大更放热是否为 CMAS 腐蚀的普适热力学规律？
  - Why important: 综述核心论点；若普适可成为设计公理，若不普适需按体系/温度分段表述。
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（高温段验证）
  - Supporting papers: 三篇（1300 °C 三体系一致）
  - Evidence strength: strong（1300 °C）
  - Next evidence needed: X1-RE2SiO5 反向报道原始文献核查；高温数据

## Not Yet True Gaps

- Candidate: 「晶界腐蚀对 RETaO4 力学性能的影响」（#46 Potential Gaps 3）
  - Why not yet a real gap: 晶界腐蚀普遍性已被证实，但力学后果目前仅 AI 推断，无任何直接证据链——待更多论文支撑后再升级为 gap 页。
  - Evidence needed: 晶界腐蚀产物的力学测试或服役失效案例。

- Candidate: 「ZrO2 球形颗粒形成机制」（#18 Potential Gaps 2）
  - Why not yet a real gap: 仅单篇观察，机制为 AI 推断；先积累 Zr 析出相关文献。
  - Evidence needed: ZrO2 析出路径的表征或热力学计算。

## Maintenance Checklist

- [x] New important gaps reflected here.
- [x] Each high-priority question linked to evidence or marked as `AI 推断`.
- [x] Answered questions moved out of active sections.
- [x] Important changes reflected in `index.md`.
- [x] Operation recorded in `log.md`.
