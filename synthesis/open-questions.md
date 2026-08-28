---
type: synthesis
status: active
created: 2026-08-23
updated: 2026-08-27
questions:
gaps:
  - "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - "[[wiki/gaps/Structure-Radius-Decoupling]]"
  - "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
claims:
  - "[[wiki/claims/CMAS-Viscosity-1500C-RE-Effect-Weakening]]"
  - "[[wiki/claims/Defect-Fluorite-CMAS-Resistance-Mechanism]]"
  - "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - "[[wiki/claims/Garnet-Product-RE2SiO5-CMAS]]"
  - "[[wiki/claims/High-Entropy-RE2SiO5-Multi-Objective-Design]]"
  - "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
papers:
  - "[[wiki/papers/2023-RE2SiO5-CMAS-In-Situ-Degradation]]"
  - "[[wiki/papers/2025-RETaO4-CMAS-High-Throughput-Screening]]"
  - "[[wiki/papers/2026-High-Entropy-Zirconates-CMAS-High-Throughput]]"
  - "[[wiki/papers/2024-Lu2SiO5-CMAS-1500C-In-Situ-Directional-Growth]]"
  - "[[wiki/papers/2022-High-Entropy-RE2SiO5-CMAS-EBC]]"
  - "[[wiki/papers/2025-Hf6Ta2O17-Al2O3-Thermochemical-Compatibility]]"
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
| Q3 冷却析出对涂层完整性的影响 | medium | "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]" | strong（析出事件 ×2 篇）/ weak（后果推断） | open |
| Q4 高通量方法能否跨体系推广 | medium | "[[wiki/gaps/High-Throughput-Screening-Transfer]]" | strong | open |
| Q5 形成焓-RE 半径规律是否普适热力学规律 | medium | —（隐含于 Q1） | strong（1300 °C，含固溶体） | open |
| Q6 1500 °C 相分解是否普适、高熵化能否抑制 | high | "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]" | strong（Lu2SiO5 单体系）/ weak（普适性） | open |
| Q7 TBC-TGO 相容性是否应成为选材强制判据 | medium | "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]" | strong（单体系证据） | open |

## High Priority Questions

- Question: Q1 1500 °C 下 CMAS 粘度剧降导致的「RE 种类影响弱化」在钽酸盐、锆酸盐体系中是否同样成立？
  - Why important: 决定成分设计准则是否需按服役温度分级；若普适，1300 °C 小半径优选策略在高温失效。
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - Supporting papers: #47（七体系）、#16（Lu2SiO5 单体系深度，219 μm vs 50 μm）；#46/#18/#48（仅 1300 °C，构成空白）
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

- Question: Q6 Lu2SiO5 在 1500 °C 的相分解（2Lu2SiO5 = Lu2Si2O7 + Lu2O3）是否普适于其他 RE2SiO5？高熵化（熵稳定效应）能否抑制分解？
  - Why important: 若分解普遍，1500 °C 下「选成分」不如「保相稳定」重要；高熵化可能同时是解药（熵稳定）与未知数（#48 无高温数据）。
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"
  - Supporting papers: #16（Lu2SiO5 分解证实 + 晶间渗透机制）、#47（1500 °C 七体系但未做 TEM/对照）、#48（高熵样品无 1500 °C 数据）
  - Related claims: "[[wiki/claims/Phase-Decomposition-Intergranular-Infiltration]]"
  - Evidence strength: strong（Lu2SiO5 单体系）；weak（普适性）
  - Next evidence needed: 其他 RE2SiO5 与高熵样品的 1500 °C 无 CMAS 对照 + TEM 晶界表征

## Medium Priority Questions

- Question: Q3 冷却析出的 Ca2RE8(SiO4)6O2 晶粒对涂层热循环完整性（剥落、开裂）的影响？
  - Why important: 实际服役含热循环，等温腐蚀研究系统性低估冷却析出损伤；#16 显示 1500 °C 保温无反应、产物集中于冷却起始析出，冷却环节的权重进一步上升。
  - Related gap: "[[wiki/gaps/Cooling-Precipitation-Coating-Integrity]]"
  - Supporting papers: #47（约 1400 °C 短水平晶粒析出）、#16（冷却起始垂直定向析出）
  - Evidence strength: strong（析出事件 ×2）；weak（后果为 AI 推断）
  - Next evidence needed: 热循环实验 + 裂纹/剥落统计

- Question: Q4 层叠法/原位观察/并行制备/高熵设计四条路线能否跨体系推广并统一到同一框架？
  - Why important: 方法学组合是用户课题的机会点；该组工作节奏快，窗口期有限。
  - Related gap: "[[wiki/gaps/High-Throughput-Screening-Transfer]]"
  - Supporting papers: 五篇 CMAS 论文（各自方法单体系验证；#48 高熵设计可与 #46/#18 高通量联用）
  - Evidence strength: strong（作者自述可推广）
  - Next evidence needed: 跨体系预实验；检索该组 2026 年新工作确认空白是否已被填补

- Question: Q5 腐蚀产物形成焓随 RE 半径增大更放热是否为 CMAS 腐蚀的普适热力学规律？
  - Why important: 综述核心论点；若普适可成为设计公理，若不普适需按体系/温度分段表述。
  - Related gap: "[[wiki/gaps/CMAS-Corrosion-Data-1500C]]"（高温段验证）
  - Supporting papers: 五篇（1300 °C 三体系 + #48 固溶体/高熵体系排序 + #16 Lu 对照）
  - Evidence strength: strong（1300 °C，含固溶体）
  - Next evidence needed: X1-RE2SiO5 反向报道原始文献核查；高温数据

- Question: Q7 TBC-TGO 热化学相容性是否应成为 TBC 选材的强制性判据？如何低成本评估？
  - Why important: #29 表明 Hf6Ta2O17 本体性能占优但 >1400 °C 与 TGO 反应、界面热应力超 YSZ 许用——选材流程缺此维度可能系统性漏检；与用户 EBC/CMAS 课题属姊妹方向，方法（粉末+扩散偶）可迁移。
  - Related gap: "[[wiki/gaps/TBC-TGO-High-Temperature-Compatibility]]"
  - Supporting papers: #29（单体系系统证据）
  - Related claims: "[[wiki/claims/Hf6Ta2O17-TGO-Incompatibility]]"
  - Evidence strength: strong（单体系）；weak（判据普适性）
  - Next evidence needed: 其他候选材料 × Al2O3 反应矩阵；真实涂层循环氧化验证

## Not Yet True Gaps

- Candidate: 「晶界腐蚀对 RETaO4 力学性能的影响」（#46 Potential Gaps 3）
  - Why not yet a real gap: 晶界腐蚀普遍性已被证实，但力学后果目前仅 AI 推断，无任何直接证据链——待更多论文支撑后再升级为 gap 页。
  - Evidence needed: 晶界腐蚀产物的力学测试或服役失效案例。

- Candidate: 「ZrO2 球形颗粒形成机制」（#18 Potential Gaps 2）
  - Why not yet a real gap: 仅单篇观察，机制为 AI 推断；先积累 Zr 析出相关文献。
  - Evidence needed: ZrO2 析出路径的表征或热力学计算。

- Candidate: 「石榴石型腐蚀产物的有益/有害作用」（#48 Potential Gaps 3）
  - Why not yet a real gap: 石榴石 (CaxRE3-x)(MgyAlzSi5-y-z)O12 仅单篇（高熵体系）报道，其对 CMAS 抗性的作用未厘清——先确认该产物在单组分体系是否普遍存在，再评估其作用。
  - Evidence needed: 单组分 RE2SiO5-CMAS 的产物复查；石榴石层致密性/渗透行为表征。

- Candidate: 「高熵 RE2SiO5 成分比例优化」（#48 Potential Gaps 1）
  - Why not yet a real gap: 等摩尔设计下 CMAS 抗性未超过 Lu/Yb 单组分，「比例优化可逼近最优」目前是 AI 推断；若后续有梯度成分研究则升级。
  - Evidence needed: 高熵 RE2SiO5 成分梯度（RE 比例变化）的 CMAS 腐蚀数据。

- Candidate: 「#47 与 #16 原位析出行为差异」（Er2SiO5 保温约 1 h 缓慢析出 vs Lu2SiO5 保温无析出）
  - Why not yet a real gap: 差异可能源于 RE 种类（形成焓）或观察分辨率，未构成明确研究空白；先核查两文实验细节。
  - Evidence needed: 同一装置/条件下多 RE 的原位对照观察。

## Maintenance Checklist

- [x] New important gaps reflected here.
- [x] Each high-priority question linked to evidence or marked as `AI 推断`.
- [x] Answered questions moved out of active sections.
- [x] Important changes reflected in `index.md`.
- [x] Operation recorded in `log.md`.
