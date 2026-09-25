---
direction_id: wave-transparent-composites
status: active
created: 2026-09-25
updated: 2026-09-25
---

# B/C综述专用流程

## 适用与权威入口

用户2026-09-25授权启用。仅用于本方向B/C综述筛选、原文阅读、证据整理、综合和写作。B为热暴露—结构演化—介电稳定性；C为界面/孔结构—物理解释—介电响应。A退出候选，B/C并行验证，最终主次和目录尚未固定。

公共证据底线仍见[[memory/hard_memory]]；按任务读取根agents对应流程。本规则按用户要求覆盖默认“新文献必须生成长篇paper页”的输出格式，改用本方向唯一工作簿[synthesis/review_BC/BC_review_evidence.xlsx](../synthesis/review_BC/BC_review_evidence.xlsx)。不降低原文阅读、证据准入、纠错或来源保护要求。非BC任务仍沿用公共输出。字段定义见[schema.json](../synthesis/review_BC/schema.json)，设计论证见[[directions/wave-transparent-composites/docs/bc-integration-2026-09-25/report]]，历史C四扩展不启用。

## 1. 身份、筛选与阅读

1. DOI/正式版/条目身份去重，一篇一个Paper_ID。同一数据被多文转用时归为同一Data_Group_ID；未知独立性不得增加独立验证数。
2. 初筛读摘要、问题与结论；明确无关只填Paper_Index及排除理由。进入核心阅读须读必要方法、结果、讨论与结论，并回查支撑论断的PDF图表；局部迁移不伪称全篇复核。已知论文不重扫Zotero集合。
3. B_Use/C_Use分别选Core、Context、Method、Review、Exclude；相关度与用途分开。Core不表示核查通过。多孔单相陶瓷默认组成/结构参照，不自动当纤维复合材料核心。
4. B区分制备热处理、原位测量、热后冷却测量及循环/氧化。暴露温度/时间/气氛与测量温度/频率/方法分别写清。没有恢复过程不判可逆性，没有时间/循环依据不判长期稳定。
5. C记录实际界面/孔变量和共变的密度、相组成、残碳、批次。频谱、模型、DFT是证据类型，不能自动成为机制等级；检验是否能区分竞争解释。

## 2. 三表唯一记录

- Paper_Index：身份、用途、来源版本、实际覆盖及论文级未决；不复制所有数值。
- Evidence_Records：每行一个主要可引用断言，按必要样品、条件、指标/单位、结果、定位、限制记录。观察、模型、作者解释、转引和AI判断分开，Related_Evidence_IDs关联，不重复抄事实。Both只记一次。文字NR表示未报告，NA表示不适用，不以0代替缺失。
- Synthesis_Map：至少两篇围绕同一问题才建行；明确Supporting/Limiting_Evidence_IDs、来源独立性、可比条件、支持强度理由与Readiness。两篇不等于两次独立验证。单篇事实可作为综合中的实例，不为它制造另一论文支持。

P0001、EV000001、SYN-B-001/SYN-C-001在本工作簿稳定且不复用。旧页E#保留原锚点，以Legacy_Evidence_Ref建立映射。撤回时保留ID、撤回原因与替代ID；Review_Usable_Claim注明撤回，Support_Assessment=Insufficient、Needs_Check=Yes，相关综合降为Blocked/Provisional，完成修订后保留处置历史。

同试样/同批匹配/不同状态/未知分别记录。Matched-batch只用于来源明确说明同批可匹配时；仅同配方或同论文而批次未交代，用Unclear，并在条件中写“同配方系列”。破坏性测试允许匹配样，不强求同一试样；必须有可核对应关系。

## 3. 核查与写作准入

Verification_Status区分Checked、Partial、Pending、Unavailable；Checked限本行声明范围且有具体原文定位。Direct仅相对于本行断言，不自动代表机制因果。Support_Assessment另判Sufficient/Partial/Insufficient并说明理由。Paper_Index的Read_Status=Core-read不因若干Checked而自动变Verified。

正式BC证据接口以“声明范围的证据集”承担公共checked门槛：核对原始来源/必要方法/样品条件/主要图表/结果解释映射，处理该断言的关键矛盾及直接下游，才能由EV替代paper E#。Verification_Scope须记录具体完成范围和旧页状态；复制旧draft或改ID不构成复核。旧页保持原状态，未迁移结论继续受旧状态约束。

Ready只表示当前限定表述可用：所需证据在该范围完成上述核查，支持充分且可比性明确，已知核心未决不改变本句；科学假说仍必须写为假说。Partial/Pending或未解决关键矛盾不得支持确定性机制/数值结论，内部综合用Provisional；前提缺失用Blocked。核查“作者确实这样说”不表示该机制成立。

非关键问题集中复核；身份、单位、样品/热状态、趋势冲突影响当前论断时先回查或隔离。source_check_log只记问题ID、影响EV、动作/处置，不重复维护事实。没有独立SI只能写未读/未取得，不能声明不存在。

## 4. 综合、目录与写作

先用比较矩阵核对象、指标定义、温频、方法、原始数据来源，区分直接可比、条件可比、仅定性及不可比；跨方法数据不拼连续曲线、不统一排名。Strong/Moderate/Weak必须相对于具体判断说明依据，不按方法数或论文数打分。

B优先验证热暴露—结构—介电是否能配对；C优先验证界面/孔结构变化是否能与介电解释相连。证据不足删小节/缩题，不扩至纯吸波/腐蚀凑数。语料缺口不是全领域gap；新颖性需要另行限定检索。

正文由Synthesis_Map组织判断、Evidence_Records供给事实，必要时回查原文；不在阅读阶段写完整综述，不另生成长篇单论文摘要。复杂SI/冲突允许定向附记。两篇指定风格参照见[[directions/wave-transparent-composites/docs/c-oriented-rules-2026-09-21/style-reference-notes]]，学习问题组织和表达，不迁移未核物理结论或抄写文字。

## 5. 保存、迁移与验收

工作簿单写入者；写前核对哈希，先保存同目录临时文件、重新打开校验，再替换目标。发现漂移停止覆盖并合并。人工Excel编辑与脚本写入不能同时进行。

旧页只增加Paper_ID、迁移范围及正式库入口；原E#不变。不同时手改新旧两套事实。确有旧错误时定向纠错并检查直接下游，不能以历史归档为由继续采用错误。

本方向.gitignore仅对正式工作簿设置例外；候选、外部PDF及raw仍不自动备份。Git可跟踪不等于已提交或上传。schema是格式定义，不是第二事实源；只读校验脚本可以生成带源工作簿哈希的统计报告，不生成可手改的事实副本。

每篇最低交付：Paper_ID、B/C用途、EV条数、Needs_Check及一句用途。批次交付：去重论文及Both交集、证据类型/直接性/核查分布、有效配对、综合单元、关键缺口及下一步。引用完整性、枚举/必填项、旧锚点、来源哈希与结构检查通过不等于科学充分；验收必须另说明原文覆盖和未决。
