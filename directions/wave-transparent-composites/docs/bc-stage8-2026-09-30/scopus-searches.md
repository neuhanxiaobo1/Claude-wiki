---
direction_id: wave-transparent-composites
status: S1-screened-S2-S3-pending
created: 2026-09-30
updated: 2026-10-01
---

# 补证据用Scopus检索式

2026-10-01执行更新：用户返回检索式1至“透波词条”，当前95篇已完成摘要筛选，见[[directions/wave-transparent-composites/docs/scopus-S1-screening-2026-10-01/report|BC-S1清单与少量补PDF建议]]。以下保留原始检索设计；检索式2/3仍按缺口安排。本轮未核用户实际检索参数、总命中数及每条导入日期，不将集合95篇等同于Scopus总命中数。

当前要补的是B的热历程/恢复与C的可区分结构归因，不继续泛搜所有透波材料。本轮已补P0014的S1/S6，温度频谱覆盖改善，但没有循环/回程、热态结构配对或碳单因素控制。以下是待用户在Scopus执行的策略，不宣称已检索、命中数已知或新颖性已证。

按1→2→3分别粘贴到Advanced Search；字段、括号和双引号按[Scopus官方高级检索说明](https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search)。保存每条实际检索日期、命中数和最终字符串，分别命名BC-S1、BC-S2、BC-S3。

## 1. B：高温微波介电及热态结构（先跑）

```text
TITLE-ABS-KEY(
  (ceramic* OR "ceramic matrix" OR SiBCN OR SiCN OR Si3N4 OR silica)
  AND ("wave transparent" OR "microwave transparent" OR "electromagnetic transparent" OR radome* OR "low loss")
  AND (dielectric* OR permittiv*)
  AND ("high temperature" OR "elevated temperature" OR "temperature dependent" OR "in situ")
  AND (microwave* OR GHz OR "X band" OR "Ku band")
)
```

需要的全文证据：明确测温而非仅高温制备；温度/频率/方法；结构与介电同条件对应。既保留性能改善也保留损耗上升/失效；低频机制文章可少量补充但单列频段。

若结果太少，先删最后的频段一组，避免摘要不写GHz造成漏检。若太多，增加`AND TITLE-ABS-KEY(microstructur* OR oxidation OR crystallization OR interfac*)`；此时记录收窄操作，不声称全面覆盖。

## 2. B：热循环、氧化/退火后的介电与恢复（与1分开跑）

```text
TITLE-ABS-KEY(
  (ceramic* OR SiBCN OR SiCN OR Si3N4 OR silica)
  AND ("wave transparent" OR "microwave transparent" OR radome* OR "low loss")
  AND (dielectric* OR permittiv* OR "loss tangent")
  AND ("thermal cycling" OR "thermal cycle" OR "heating cooling" OR reversib* OR recover* OR "thermal shock" OR oxidation OR anneal* OR aging OR ageing)
)
```

优先：同配方热前/热后介电、升降温回线、重复循环、明确气氛/时间及相/孔/裂纹变化。只有热震后强度、TG残重或制备热解次数，不视作命中核心证据。结果多时加`AND TITLE-ABS-KEY(microwave* OR GHz)`；结果少时不要再强制摘要同时出现循环和微结构，转用1及相关原文的引文追踪。

## 3. C：界面/孔结构与碳等共变量（第二优先）

```text
TITLE-ABS-KEY(
  (ceramic* OR "ceramic matrix" OR SiBCN OR SiCN OR Si3N4 OR silica)
  AND ("wave transparent" OR "microwave transparent" OR "electromagnetic transparent" OR radome* OR "low loss")
  AND (dielectric* OR permittiv* OR "loss tangent")
  AND (interfac* OR interphase* OR porosity OR "pore structure" OR "free carbon" OR "carbon content")
)
```

优先：陶瓷复合体界面改变同时有介电对照；等组成/近似等孔隙的对照；独立电导/弛豫证据；孔隙率相近而形态/连通性不同。块体PDC按Context处理。检索词不是入库判据，不能因摘要出现interface/polarization就当已证机制。

结果过多时加`AND TITLE-ABS-KEY(composite* OR fiber* OR fibre* OR interphase*)`，优先内部界面子集；若只关心组成/孔混杂则保留宽式。暂不强制"controlled"或"matched"，这些实验细节可能仅在方法中。

## 返回什么、如何筛

- 第一轮先1和2，以近十年为阅读优先；不要永久排掉早期关键原始文献。优先Article，Review另存作引文/覆盖导航，不混同原始证据。
- **先导出题录，不必批量下载PDF或全部导入正式文献集合。** 每条≤100条则导出全部；结果更多先反馈总数，再收窄，避免只截高被引前几篇。导出CSV或RIS，勾选题名、作者、年份、期刊、DOI、摘要和关键词；保留每个检索组，后续按DOI去重。[Scopus官方导出说明](https://www.elsevier.support/scopus/answer/how-do-i-export-documents-from-scopus)
- 可存到用户惯用的`F:/industry software/onedrive/1.Science/1.Zotero/fenqu/review`，告知文件名即可；本轮助手没有向此外部目录写入。
- 筛选继续执行本方向“IF<6.0尽量少用/少入/少读”：用可核实的最新JCR JIF及年份，未知标待核。不要把Scopus CiteScore≥6当成JIF≥6。先保留题录，核实后决定精读/引用；必要低IF关键反例或不可替代方法可作少量例外。
- 不在宽检索中全局排除absorption、carbon或polymer，因为陶瓷前驱体、导电损耗及透波/吸波比较文献可能包含这些词；全文筛掉纯吸波和树脂核心即可。
- 收到题录后，助手交付去重候选表：B/C用途、补哪条缺口、JIF来源/年份、PDF有无、选/缓/排理由。再选少量全文精读，用户只需补确切缺件。
