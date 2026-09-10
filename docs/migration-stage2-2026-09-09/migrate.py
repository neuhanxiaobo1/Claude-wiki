"""One-time stage2 migration. Default builds/validates a preview; --apply executes.
Source membership and hashes must match stage1. Never touches external sources.
"""
from pathlib import Path
import datetime, hashlib, json, os, re, sys, zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
S1 = ROOT/'docs/migration-stage1-2026-09-09'
D = 'directions/ceramic-corrosion/'
sha = lambda b: hashlib.sha256(b).hexdigest()
rows = json.loads((S1/'inventory.json').read_text(encoding='utf-8'))
summary = json.loads((S1/'summary.json').read_text(encoding='utf-8'))
assert sha((ROOT/summary['backup']).read_bytes()) == summary['backup_sha256']
drift_file=OUT/'accepted-drift.json'
if drift_file.exists():
    drift=json.loads(drift_file.read_text(encoding='utf-8'))
    by_source={r['source']:r for r in rows}
    for r in drift['files']:
        by_source[r['source']]=r
    rows=list(by_source.values())
old = {}
for r in rows:
    p = (ROOT/r['source']).resolve()
    assert p.is_relative_to(ROOT) and p.is_file(), r['source']
    old[r['source']] = p.read_bytes()
    assert sha(old[r['source']]) == r['sha256'], 'Source drift: '+r['source']
assert not (ROOT/'directions').exists(), 'Direction target already exists'
actual = set()
for base, dirs, names in os.walk(ROOT, followlinks=False):
    dirs[:] = [d for d in dirs if d not in {'.git','.migration-backups','migration-stage1-2026-09-09','migration-stage2-2026-09-09'}]
    for d in dirs:
        node = Path(base)/d
        assert not node.is_symlink() and not (node.stat().st_file_attributes & 0x400), node
    actual.update((Path(base)/n).relative_to(ROOT).as_posix() for n in names)
assert actual == set(old), {'added':sorted(actual-set(old)), 'missing':sorted(set(old)-actual)}
def text(p): return old[p].decode('utf-8-sig').replace('\r\n','\n')
new = {}
def put(p,t):
    assert (ROOT/p).resolve().is_relative_to(ROOT) and not p.startswith(('.git/','.migration-backups/'))
    new[p] = t.encode('utf-8') if isinstance(t,str) else t

mapping = {r['source']:r['target'] for r in rows}
mapping['memory/context_policy.md'] = D+'memory/current_context.md'
mapping['memory/tag_taxonomy.md'] = D+'memory/tag_taxonomy.md'
mapping['memory/term_aliases.md'] = D+'memory/term_aliases.md'
for p in ('log.md','index.md','inbox.md','memory/error_log.md','memory/decision_log.md'):
    mapping[p] = D+p

def translate(s):
    # Only known vault paths at token boundaries; no global material-word replacement.
    replacements = {k:v for k,v in mapping.items() if k != v}
    replacements.update({'wiki/':D+'wiki/', 'synthesis/':D+'synthesis/', 'raw/':D+'raw/'})
    pattern = r'(?<![\w/\\.-])('+'|'.join(re.escape(k) for k in sorted(replacements,key=len,reverse=True))+r')'
    s = re.sub(pattern,lambda m:replacements[m.group(1)],s)
    def link(m):
        val = m.group(1)
        base = re.split(r'[|#]',val,1)[0]
        key = base if base.endswith('.md') else base+'.md'
        target = mapping.get(key)
        if target and target != key:
            return '[['+target.removesuffix('.md')+val[len(base):]+']]'
        return m.group(0)
    return re.sub(r'\[\[([^\]\n]+)\]\]',link,s)

def scoped(s):
    # Public recipes use D placeholders for research outputs; root rule paths stay root.
    s = re.sub(r'(?<![\w/.-])(raw/|wiki/|synthesis/)',r'D/\1',s)
    for p in ('memory/project_profile.md','memory/error_log.md'):
        s = s.replace(p,'D/'+p)
    s = s.replace('`log.md`','`D/log.md`').replace('`index.md`','`D/index.md`')
    return s

def add_direction(s):
    if s.startswith('---\n'):
        return s.replace('---\n','---\ndirection_id: ceramic-corrosion\n',1)
    return '---\ndirection_id: ceramic-corrosion\n---\n\n'+s

protected = []
scientific = []
for r in rows:
    p, target = r['source'],r['target']
    if r['action'] == 'move':
        if p.startswith('raw/') and Path(p).name not in {'import_plan.md','manifest.json'}:
            put(target,old[p]); protected.append(p)
        elif p.endswith(('.md','.json')):
            s = translate(text(p))
            if p.startswith(('wiki/','synthesis/')) and p.endswith('.md'):
                s = add_direction(s)
                scientific.append(p)
            put(target,s)
        elif p.endswith(('/query_unpaywall.py','/merge_pdf_links.py')):
            # Keep the user's helper, adapt only its local data directory; never execute it.
            s=text(p).replace('import json\n','import json\nfrom pathlib import Path\n',1)
            s=re.sub(r'^base = r"[^"]+"$', 'base = str(Path(__file__).resolve().parent)',s,flags=re.M)
            put(target,s)
        else:
            put(target,old[p])

# Direction histories retain all previous text with mechanical path updates.
for p in ('index.md','log.md','inbox.md','memory/error_log.md','memory/decision_log.md'):
    s = translate(text(p))
    if p in {'log.md','memory/error_log.md','memory/decision_log.md'}:
        s += '\n\n> 2026-09-09迁移说明：以上为迁移前混合历史，含当时的公共维护记录。公共规则仍以根目录现行文件为准；后续本文件只记录本方向事项。阶段0/1在根日志保留的条目是同一操作的历史镜像，不重复计数。\n'
    put(D+p,s)

profile = text('memory/project_profile.md')
reading = text('memory/ceramic_corrosion_reading_rules.md')
cmas = profile.split('### CMAS 领域阅读辅助项\n',1)[1].split('## Source Settings',1)[0]
extra = text('agents/pdf_read_agent.md').split('## 10. CMAS 项目附加检查',1)[1]
reading = reading.replace('通过project_profile进入，不改变AGENTS、hard_memory、通用agent或通用论文模板。','通过本方向AGENTS与project_profile进入；总规则和公共证据标准独立生效。')
reading += '\n\n## 6. 材料腐蚀阅读核对项\n\n'+cmas
reading += '\n### 原通用阅读流程中的补充检查（现归本方向）\n'+extra
reading = reading.replace('本方向后续筛选、入库及修订还需读取 [[memory/ceramic_corrosion_reading_rules]]：','本方向后续筛选、入库及修订遵循本页前五节：')
put(D+'memory/reading_rules.md',translate(reading))
profile = re.sub(r'### CMAS 领域阅读辅助项\n.*?(?=## Source Settings)', '### 方向阅读入口\n\n筛选、入库与修订读取 [[directions/ceramic-corrosion/memory/reading_rules]]。通用重点沿用根目录 agents/pdf_read_agent.md 与 templates/paper.md。\n\n',profile,flags=re.S)
profile = re.sub(r'## Paper Ingestion Priorities\n.*?(?=### 方向阅读入口)', '## Paper Ingestion Priorities\n\n研究问题、方法、贡献/证据、对象、指标、设计、结果和局限的抽取遵循通用阅读流程；claim/gap按证据与需要创建，不强制产出。\n\n',profile,flags=re.S)
profile = re.sub(r'- 使用者：.*\n','- 使用者：见根目录 [[memory/user_profile]]。\n',profile)
profile = re.sub(r'- 研究阶段：.*\n','- 本方向研究阶段：文献阅读、证据整理与综述草稿；用户核心研究问题仍未确定。\n',profile)
profile = re.sub(r'## Output Preferences\n.*?(?=## Initial Candidate Tags)','## Output Preferences\n\n默认语言、专名与双链偏好沿用 [[memory/user_profile]]；本方向引用展示样式待确认，不影响公共来源定位要求。总结/写作要求见本方向AGENTS。\n\n',profile,flags=re.S)
profile += '\n## 已记录的本方向来源通道\n\n本机Zotero MCP历史入口为 `http://127.0.0.1:23120/mcp`；本轮未测试连接。MinerU缓存根目录记录为 `D:/shuju/zotero1/llm-for-zotero-mineru/`；OneDrive附件以工具实际返回路径为准。外部原件未在本次迁移中移动或备份；逐篇身份和版本见论文源页。\n'
put(D+'memory/project_profile.md',translate(profile))
context = text('memory/context_policy.md')
put(D+'docs/context-history-pre-migration.md','# 迁移前陶瓷腐蚀上下文历史\n\n2026-09-09归档，保留原记录；当前入口见本方向current_context，旧状态不自动生效。\n\n'+translate(context.split('## 当前任务',1)[1]))
taxonomy = text('memory/tag_taxonomy.md')
domain_tags = taxonomy.split('## Domain Tags',1)[1].split('## Duplicate Tag Policy',1)[0]
put(D+'memory/tag_taxonomy.md','# 陶瓷腐蚀方向标签\n\n通用标签与命名标准见 [[memory/tag_taxonomy]]。方向标签在本方向内登记和去重。\n\n'+domain_tags)
put('memory/tag_taxonomy.md',scoped(re.sub(r'## Domain Tags.*?(?=## Duplicate Tag Policy)','## Domain Tags\n\n方向词表在 `D/memory/tag_taxonomy.md`；不得将其他方向标签自动并入当前方向。\n\n',taxonomy,flags=re.S)).replace('`inbox.md`','`D/inbox.md`'))
aliases = text('memory/term_aliases.md')
domain_terms = aliases.split('## Domain Terms',1)[1].split('## 示例',1)[0]
put(D+'memory/term_aliases.md',translate('# 陶瓷腐蚀方向术语\n\n通用术语标准见根目录memory/term_aliases.md；本方向条目如下。\n\n'+domain_terms).replace(D+'memory/term_aliases.md；','memory/term_aliases.md；'))
put('memory/term_aliases.md',scoped(re.sub(r'## Domain Terms.*?(?=## 示例)','## Domain Terms\n\n见 `D/memory/term_aliases.md`。只在同方向、同义且科学边界一致时去重。\n\n',aliases,flags=re.S)).replace('[[D/synthesis/open-questions]]','D/synthesis/open-questions.md'))

binding = '''\n## 方向绑定与路径约定\n\n先遵循根目录AGENTS.md绑定本会话方向，再显式读取 `D/AGENTS.md`。D是已注册方向的真实根路径；未选方向不能写研究文件。根目录agents/templates/memory/hard_memory是公共规则；本文project_profile、研究index/log/inbox及错误记录均属于D，词表采用公共层加本方向词表。仅使用本方向声明的阅读/综合/写作扩展，未声明则沿用通用流程。模板中的D与direction_id必须展开，生成双链使用vault完整路径。\n\n默认读写范围限D；另一方向资源只按具体需要定向读取、来源方向默认只读。跨方向同DOI页面可以独立存在，但同一原始数据不能重复计为独立验证。去重/别名合并限本方向。公共架构lint无需科研方向，写入根级维护记录；单方向任务不得更新其他方向。\n'''
for p in old:
    if p.startswith('agents/') and p.endswith('.md'):
        s = text(p)
        if p == 'agents/pdf_read_agent.md': s=s.split('## 10. CMAS 项目附加检查',1)[0]
        s = scoped(s)
        at = s.find('\n## 1.')
        s = s[:at]+binding+s[at:] if at >= 0 else s+binding
        if p == 'agents/lint_agent.md':
            s=s.replace('当前任务与恢复入口归 context_policy','恢复机制归根context_policy，方向当前任务与恢复入口归 D/memory/current_context.md')
        put(p,s)
    if p.startswith('templates/') and p.endswith('.md'):
        s = scoped(text(p))
        if p != 'templates/pdf_ingestion_template.md':
            s=s.replace('---\n','---\ndirection_id: "{{direction_id}}"\n',1)
        s += '\n\n<!-- 方向约定：仅在已选方向D内生成；展开direction_id与D/路径。领域额外栏目只从D/AGENTS.md声明的扩展读取，不加载其他方向模板。 -->\n'
        put(p,s)

hard = scoped(text('memory/hard_memory.md'))
hard = hard.replace('具体研究领域、用户目标、Zotero 设置和写作偏好写入 `D/memory/project_profile.md`。','个人默认偏好见 `memory/user_profile.md`；具体研究领域、用户目标、Zotero设置与方向覆盖偏好见 `D/memory/project_profile.md`。D由根AGENTS绑定。')
hard = hard.replace('- `memory/` 保存长期规则、项目配置、错误记录、标签体系和术语别名。','- 根 `memory/` 保存公共规则与公共维护；`D/memory/` 保存方向配置、短上下文、错误与研究决定。')
hard = hard.replace('- 新增标签前先查 `memory/tag_taxonomy.md`。','- 新增标签前先查公共 `memory/tag_taxonomy.md` 与本方向 `D/memory/tag_taxonomy.md`。')
hard = hard.replace('先查 `memory/term_aliases.md` 和已有页面','先查公共 `memory/term_aliases.md`、本方向 `D/memory/term_aliases.md` 和本方向已有页面')
hard = hard.replace('- 默认使用 `D/memory/project_profile.md` 中指定的语言、术语和引用偏好。','- 默认语言、术语显示见 `memory/user_profile.md`，本方向 `D/memory/project_profile.md` 可覆盖默认风格，不得降低证据标准。')
hard += '\n## 多方向维护边界\n\n单方向操作追加D/log.md，研究纠错记D/memory/error_log.md；公共架构操作追加根log.md，公共错误记根memory/error_log.md。方向词表不影响其他方向；跨方向引用必须保留共同来源、适用条件和本方向独立评价。原件保护不因方向迁移而降低；用户明确授权的目录迁移可改变指定原件位置，原件内容保持不变。\n'
put('memory/hard_memory.md',hard)
style = text('memory/style_snapshot.md').replace('memory/project_profile.md','memory/user_profile.md').replace('`synthesis/`','`D/synthesis/`')
style = style.replace('具体研究领域和用途写入 `memory/user_profile.md`。','具体研究领域和用途写入 `D/memory/project_profile.md`；个人默认偏好写入 `memory/user_profile.md`。')
put('memory/style_snapshot.md',style+'\n方向可在D/memory/writing_rules.md补充写作格式；未声明时沿用公共风格。\n')

# Public quick reference docs: keep original attribution and full content, adjust routes.
for p in ['README.md','QUICKSTART.md','docs/initialization.md','docs/zotero-workflow.md','docs/privacy-and-gitignore.md']:
    s=scoped(text(p))
    for src,dst in mapping.items():
        if src.startswith('docs/') and src!=dst:
            s=s.replace(']('+src+')',']('+dst+')')
    if p=='README.md':
        s=re.sub(r'## File Structure / 文件结构\n.*?(?=## Usage Examples)', '''## File Structure / 文件结构\n\n```text\nResearchWiki/\n├── AGENTS.md / CLAUDE.md\n├── index.md / log.md / inbox.md   # 公共导航与维护\n├── agents/                       # 通用任务流程\n├── templates/                    # 公共模板与新方向骨架\n├── memory/                       # 公共底线、用户默认、注册表与恢复机制\n├── docs/                         # 使用说明与架构记录\n├── shared/                       # 可借鉴资源导航\n└── directions/\n    └── <direction_id>/\n        ├── AGENTS.md / index.md / log.md / inbox.md\n        ├── memory/               # 方向profile、扩展、当前任务与词表\n        ├── raw/                  # papers、notes、assets、zotero_imports\n        ├── wiki/                 # papers、topics、methods、claims等\n        ├── synthesis/            # 本方向综合与写作\n        └── docs/                 # 研究报告与历史\n```\n\n本库不在根目录保存方向raw/wiki/synthesis。方向专用模板仅在实际需要时放入该方向templates。\n\n''',s,flags=re.S)
        s=s.replace('| `memory/context_policy.md` | 增量读取、当前任务与恢复入口 |','| `memory/context_policy.md` | 公共恢复机制与架构任务入口 |\n| `D/memory/current_context.md` | 所选方向研究进度与恢复入口 |\n| `memory/user_profile.md` | 使用者与公共默认偏好 |\n| `memory/direction_registry.yaml` | 已登记方向导航 |')
        s=s.replace('### Step 2: Configure Project Profile / 配置项目画像','### Step 2: Select Direction / 选择或创建研究方向')
        s=s.replace('优先编辑：','先按根AGENTS选择已有方向或新建方向；D是所选方向根。首次配置时按需编辑：',1)
        s=s.replace('### Step 0: Clone / 克隆项目','### Step 0: Clone / 克隆项目')
        s=s.replace('`memory/` 保存当前任务和偏好','`D/memory/` 保存方向当前任务，公共默认偏好见根memory/user_profile')
    if p=='QUICKSTART.md':
        s=s.replace('首次使用按 AGENTS 读取公共规则和 project_profile；继续已有任务时按 context_policy 当前状态恢复，无需重新初始化或清空知识库。','首次使用按根AGENTS先选择已有方向或新建方向，再读D/AGENTS.md、D/memory/project_profile.md与D/memory/current_context.md；同一任务直接继续。公共维护不必选择科研方向。')
        s=s.replace('当前规则完善进度见 docs/rules-improvement-plan.md。','公共架构当前进度见根index及memory/context_policy.md；旧研究规则完善历史见方向docs/rules-improvement-plan.md。')
        s=s.replace('重要操作记 log，index 按实际变化维护。','研究操作记D/log，D/index按实际变化维护；公共维护记根log/index。')
    if p=='docs/initialization.md':
        s=s.replace('已有项目按 memory/context_policy.md 恢复当前任务','已有项目先按根AGENTS选择方向，按D/memory/current_context.md恢复研究任务')
        s=s.replace('按 AGENTS.md 读取公共规则，填写 project_profile 中','按AGENTS.md选择或新建方向，填写D/memory/project_profile.md中')
    s += '\n\n## 多研究方向入口（2026-09-09生效）\n\n按根AGENTS选择已有方向或新建方向；已明确点名方向直接进入，同一任务不重复选择。D代表本会话绑定的directions/<direction_id>，文中D/是路径占位，不是实际文件夹。个人默认配置见memory/user_profile.md，研究配置及进度见D/memory/project_profile.md和D/memory/current_context.md。公共维护由根index/log管理；论文、原件、研究索引/日志和synthesis均归D。具体操作见docs/direction-workflow.md。\n'
    put(p,s)

# Configuration path changes are structural; preserve unrelated values.
app=json.loads(text('.obsidian/app.json')); app['newLinkFormat']='absolute'
put('.obsidian/app.json',json.dumps(app,ensure_ascii=False,indent=2)+'\n')
graph=json.loads(text('.obsidian/graph.json')); graph['search']='path:directions/ceramic-corrosion/wiki/ '
put('.obsidian/graph.json',json.dumps(graph,ensure_ascii=False,indent=2)+'\n')
workspace=json.loads(text('.obsidian/workspace.json'))
def ws(v):
    if isinstance(v,dict): return {k:ws(val) for k,val in v.items()}
    if isinstance(v,list): return [ws(x) for x in v]
    if isinstance(v,str):
        if v in mapping: return mapping[v]
        if v.startswith(('wiki/','raw/','synthesis/')): return D+v
    return v
put('.obsidian/workspace.json',json.dumps(ws(workspace),ensure_ascii=False,indent=2)+'\n')
ignore=text('.gitignore')
ignore += '\n# Per-direction original/private materials (including JSON and Markdown)\n/directions/*/raw/**\n!/directions/*/raw/**/\n!/directions/*/raw/**/.gitkeep\n!/directions/*/raw/**/README.md\n\n# Reviewed derived screening table migrated from tracked docs\n!/directions/ceramic-corrosion/docs/scopus-screening-2026-09-09/screening.csv\n'
put('.gitignore',ignore)

stage0_marker='## [2026-09-09] decision | 多研究方向改造方案与分阶段边界'
with zipfile.ZipFile(ROOT/summary['backup']) as z:
    original_log=z.read('log.md').decode('utf-8-sig').replace('\r\n','\n')
rootlog='# 公共操作日志\n\n仅记录公共规则与全库架构维护。迁移前完整混合历史见 [[directions/ceramic-corrosion/log]]；下方保留阶段0/1公共记录，方向归档中的同名条目是历史镜像。\n\n'+stage0_marker+original_log.split(stage0_marker,1)[1]
rootlog+='''\n\n## [2026-09-09] update | 多研究方向改造阶段2：规则拆分与当前方向迁移\n\n- 输入：用户明确要求继续下一步，执行阶段2。\n- 操作：核对112文件快照无漂移，另存执行前与迁移预览ZIP；按归属表迁移当前方向，拆分规则与记录，修复派生文件路径及Obsidian/Git配置；注册方向并启用对话选择入口。\n- 新建：方向入口/短上下文、公共user_profile/注册表/新方向规程与骨架、shared目录、阶段2报告。\n- 更新：公共AGENTS/CLAUDE、通用agent/template、公共记忆与说明、根/方向索引及记录；原件内容不改，科学页仅机械链接与direction_id。\n- 发现：执行结果和数量/哈希/链接核验见 [[docs/migration-stage2-2026-09-09/report]]；原始笔记旧链接通过映射溯源，外部来源未移动也未备份。\n- 后续：阶段3隔离验收；新实际方向及真实论文试运行留阶段4/5。本轮未提交上传，未自动恢复综述扩写。\n'''
put('log.md',rootlog)
if drift_file.exists():
    put('log.md',new['log.md'].decode('utf-8').replace('核对112文件快照无漂移',f'复核阶段1的112文件时拦截并行写入；用户确认暂停后核对新增日志/辅助文件，补充为{len(old)}文件快照'))
put('memory/error_log.md','''# 公共错误记录\n\n只记录总规则、路径路由、全库结构或公共工具错误。研究判断纠错属于D/memory/error_log.md。迁移前完整记录见 [[directions/ceramic-corrosion/memory/error_log]]，不得在日常公共启动时预读全部研究错误。\n\n## 2026-09-09 | 单方向规则与多方向作用域不匹配（已修正）\n\n### 错误表现\n\n旧公共阅读流程夹带领域附加检查，根配置和上下文混合了身份、方向目标与科研进度；沿用到多个方向会混用规则和记录。\n\n### 原因\n\n既有成功实现针对单方向，尚未区分公共默认与方向扩展。\n\n### 修正规则\n\n阶段2已按归属表拆分；根AGENTS负责选择、D绑定、显式加载方向规则与写入边界。用户教授身份归公共user_profile，方向用途独立保存。\n\n### 影响范围\n\n公共入口、通用流程、方向配置与记录路径。未重新评估科学证据，原有checked与未决项保持。具体结果见 [[docs/migration-stage2-2026-09-09/report]]。\n\n### 以后避免方式\n\n新增领域要求只在所选方向登记；公共任务检查规则作用域，方向任务检查实际读写范围，不以目录存在代替隔离成立。\n''')
put('memory/decision_log.md','''# 公共结构与规则决定\n\n既有公共证据/阅读/综合/写作决定已落实到现行hard_memory、agents和templates；原决定及迁移前混合历史完整保存在 [[directions/ceramic-corrosion/memory/decision_log]]。历史完成状态不作为当前执行任务。\n\n## [2026-09-09] 公共规则与方向工作区分离\n\n- Decision：根规则与个人默认偏好共用；研究规则/原件/知识页/综合/记录归各方向。公共启动选择已有方向或新建，每个会话独立绑定D。\n- Reason：用户并行管理多个方向，需要明确借鉴且互不混写。\n- Impact：跨方向来源默认只读，接收方向独立评价；原件保护和公共证据标准保持；阶段2迁移原目录，后续隔离验收单列。\n- Status：active；实际执行/验证范围见 [[docs/migration-stage2-2026-09-09/report]]，不表示阶段3–5已完成。\n''')
put('memory/error_log.md',new['memory/error_log.md'].decode('utf-8')+'''\n## 2026-09-09 | 迁移预览的格式假设与路径遗漏（执行前已修正）\n\n### 错误表现\n\n首轮预览假定全部综合页都有YAML，遇到原组外登记表无frontmatter而停止；后续链接校验发现README仍指向将迁出的旧报告路径。\n\n### 原因\n\n既有页面允许无YAML，路径拆分既包含双链也包含公共文档中的Markdown链接。\n\n### 修正规则\n\n无YAML页面仅新增direction_id前置信息，保留原文；README的实际历史报告链接使用迁移目标。占位语法与真实链接分开检查，全部在切换入口前修复。\n\n### 影响范围\n\n预览生成与公共说明，未损坏工作区原件或科学内容。最终范围见阶段2报告。\n\n### 以后避免方式\n\n迁移前支持真实旧格式，先检查预览的文件内容及常见链接，再执行；不要将模板假设当作旧页面保证。\n''')
if drift_file.exists():
    put('memory/error_log.md',new['memory/error_log.md'].decode('utf-8')+'''\n## 2026-09-09 | 迁移快照期间出现并行写入\n\n### 错误表现\n\n第一次尝试切换时log.md哈希已变化，另新增筛选辅助文件与本机配置；旧112文件快照已不足以直接迁移。\n\n### 原因\n\n其他任务在准备期间写入同一工作区。\n\n### 修正规则\n\n漂移保护在任何研究文件写入前停止切换。核对新增内容、补充清单与完整执行前备份；保留方向日志新条目，本轮不重复执行其Zotero操作。\n\n### 影响范围\n\n以accepted-drift.json和execution.json记录的实际成员为准；历史阶段1快照不覆盖最新写入。\n\n### 以后避免方式\n\n目录切换期间暂停并行写入，并在预览、应用前分别检查成员/哈希；恢复后各会话按新入口定位方向，避免重新创建旧路径。\n''')
put(D+'log.md',new[D+'log.md'].decode('utf-8')+'''\n## [2026-09-09] update | 迁入独立陶瓷腐蚀工作区\n\n- 输入：用户授权多方向改造阶段2。\n- 操作：保留原研究内容，迁移至本方向目录，修复派生文件路径并添加direction_id；领域阅读规则独立，研究进度提炼至current_context。\n- 新建：本方向AGENTS、current_context及上下文历史归档。\n- 更新：本方向索引、引用路径与维护记录。\n- 发现：未新增论文；科学判断与核查状态不升级；原始笔记保留原文字节与旧链接，外部来源未移动。\n- 后续：继续遵守暂停扩写与选定候选后处理的研究约束。公共隔离验收见根级阶段2报告/后续阶段3，不作为本方向科研待办。\n''')
plan=text('docs/multi-direction-migration-plan.md')
plan=plan.replace('阶段 2–5 尚未实施。','阶段 2 已执行，校验结果见 [[docs/migration-stage2-2026-09-09/report]]；阶段 3–5 尚未实施。',1)
plan=plan.replace('本文中的目标路径、字段和启动流程是设计，尚未生效。当前研究资料继续使用原路径。','方向入口、目录与规则拆分现已生效；阶段1材料保留为迁移前快照。后文阶段0/1当时的边界描述是历史说明，不代表当前仍使用旧目录。',1)
plan=plan.replace('| 2：启用第一个独立方向 |','| 2：启用第一个独立方向（已执行） |')
plan=plan.replace('下一步进入阶段 2，先按 [[docs/migration-stage1-2026-09-09/report]] 核对快照漂移，再协调拆分规则与迁移当前方向。','下一步进入阶段 3隔离验收，阶段2执行结果见 [[docs/migration-stage2-2026-09-09/report]]。阶段1快照与旧路径映射继续保留用于溯源，不重做目录迁移。')
put('docs/multi-direction-migration-plan.md',plan)

# Full replacement files are prepared as UTF-8 text assets alongside this script.
assets=OUT/'content'
for p in assets.rglob('*.md.in'):
    put(p.relative_to(assets).as_posix().removesuffix('.in'),p.read_bytes())
registry = {'schema_version':1,'directions':[{'id':'ceramic-corrosion','name':'陶瓷腐蚀','path':D.rstrip('/'),'status':'active','last_used':None}]}
put('memory/direction_registry.yaml',json.dumps(registry,ensure_ascii=False,indent=2)+'\n')

# Metadata and research integrity gates before touching the working tree.
for p in scientific:
    expected=add_direction(translate(text(p))).encode('utf-8')
    assert new[mapping[p]] == expected, p
for p in protected: assert new[mapping[p]] == old[p],p
assert hard.split('## Evidence Rules',1)[1].split('## Maintenance Rules',1)[0] == text('memory/hard_memory.md').split('## Evidence Rules',1)[1].split('## Maintenance Rules',1)[0]
retired=sorted(p for p in old if p not in new and mapping[p] != p)
for p in retired: assert mapping[p] in new, p
for p in new:
    assert p in old or not (ROOT/p).exists(), 'Unexpected existing output: '+p
for p,b in new.items():
    if p.endswith('.json') or p=='memory/direction_registry.yaml': json.loads(b)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
backup=ROOT/'.migration-backups'/('stage2-preflight-'+stamp+'.zip')
preview=ROOT/'.migration-backups'/('stage2-preview-'+stamp+'.zip')
for dest, data in ((backup,old),(preview,new)):
    with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED) as z:
        for p,b in sorted(data.items()): z.writestr(p,b)
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        assert all(z.read(p)==b for p,b in data.items())
record={'mode':'apply' if '--apply' in sys.argv else 'preview','source_count':len(old),'output_count':len(new),'retired':retired,
        'backup':backup.relative_to(ROOT).as_posix(),'backup_sha256':sha(backup.read_bytes()),
        'preview':preview.relative_to(ROOT).as_posix(),'preview_sha256':sha(preview.read_bytes()),
        'protected_raw':protected,'scientific_pages':scientific,'mapping':mapping,
        'outputs':[{'path':p,'sha256':sha(b)} for p,b in sorted(new.items())]}
if '--apply' in sys.argv:
    # Every retirement is an enumerated file below ROOT; verified copy + ZIP already exists.
    for p,b in old.items(): assert (ROOT/p).read_bytes()==b, 'Changed before apply: '+p
    for p,b in new.items():
        dest=(ROOT/p).resolve(); assert dest.is_relative_to(ROOT)
        dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(b)
    for p,b in new.items(): assert (ROOT/p).read_bytes()==b,p
    for p in retired:
        source=(ROOT/p).resolve()
        assert source.is_relative_to(ROOT) and source != ROOT and source.is_file()
        assert source.read_bytes()==old[p] and (ROOT/mapping[p]).is_file()
        source.unlink()
    # Remove empty old directories only, no recursive delete or computed tree deletion.
    for prefix in ['raw','wiki','synthesis']:
        parent=(ROOT/prefix).resolve(); assert parent.parent==ROOT
        if parent.exists():
            for d in sorted((x for x in parent.rglob('*') if x.is_dir()),key=lambda x:len(x.parts),reverse=True):
                assert d.resolve().is_relative_to(parent)
                if not any(d.iterdir()): d.rmdir()
            if not any(parent.iterdir()): parent.rmdir()
    record['status']='applied-and-output-hashes-verified'
else: record['status']='preview-only'
(OUT/'execution.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k not in {'mapping','outputs','retired','protected_raw','scientific_pages'}},ensure_ascii=False,indent=2))
