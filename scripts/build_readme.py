#!/usr/bin/env python3
"""Generate README.md (English), README.zh-CN.md (Simplified Chinese) and one
page per photo-pose style in both languages (styles/<id>.md, styles/<id>.zh-CN.md)
from data/*.json and CHANGELOG.md. These files are generated: edit the data or
this script, then run

    python3 scripts/build_readme.py && python3 scripts/validate.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'https://github.com/leisure-cat/ai-photo-poses'
UTM = '?utm_source=github&utm_medium=readme&utm_campaign=ai-photo-poses'
SITE = 'https://promicat.app'
NAMES = ('poses', 'lights', 'scenes', 'cases', 'promi', 'recipes', 'components', 'portrait-recipes', 'photo-poses')
d = {k: json.load(open(os.path.join(ROOT, 'data', k + '.json'), encoding='utf-8')) for k in NAMES}
TPL = json.load(open(os.path.join(ROOT, 'data', 'templates.json'), encoding='utf-8'))['prompt_with_your_photo']
PP, PR = d['photo-poses'], d['portrait-recipes']
STYLES = list(dict.fromkeys(r['style'] for r in PP))
STYLE_NAME = {r['style']: r['style_name'] for r in PP}
EXTRA = [v for v in d['components']['pose'] if not v['pose_ref']]
NCOMP = sum(len(v) for v in d['components'].values())
NSHOTS = sum(len(r['shots']) for r in PR)
NCASES = sum(len(r.get('cases', [])) for r in PP)
POSE = {p['id']: p for p in d['poses']}
COMP = {slot: {v['id']: v for v in vals} for slot, vals in d['components'].items()}

# Latest update: the first "## YYYY-MM-DD" entry of CHANGELOG.md, with its first bullet in each language.
log = open(os.path.join(ROOT, 'CHANGELOG.md'), encoding='utf-8').read()
m = re.search(r'^## (\d{4}-\d{2}-\d{2})\n+- (.+)\n- (.+)\n', log, re.M)
if not m:
    raise SystemExit('CHANGELOG.md needs a "## YYYY-MM-DD" entry with an English bullet, then a Chinese bullet')
LATEST = {'date': m.group(1), 'en': m.group(2), 'zh': m.group(3)}

SLOTS = [  # slot, en, zh, level en, level zh
    ('look', 'Look & film stock', '质感', 'set', '整组'), ('skin', 'Skin realism', '皮肤', 'set', '整组'),
    ('light', 'Key light', '主光', 'set', '整组'), ('light_mod', 'Light details', '光的细节', 'set, multi', '整组·多选'),
    ('scene', 'Scene', '场景', 'set', '整组'), ('outfit', 'Outfit', '服装', 'set', '整组'),
    ('hair', 'Hair', '发型', 'set', '整组'), ('makeup', 'Makeup', '妆容', 'set', '整组'),
    ('motion', 'Motion', '动态', 'set, optional', '整组·可空'), ('props', 'Props', '道具', 'set, multi', '整组·多选'),
    ('negative', 'Avoid', '避免项', 'set, multi', '整组·多选'), ('gaze_rule', 'Gaze rule', '看镜规则', 'set', '整组'),
    ('pose', 'Pose', '姿势', 'per shot', '逐张'), ('action', 'Action', '动作', 'per shot, optional', '逐张·可空'),
    ('expression', 'Expression', '表情', 'per shot', '逐张'), ('shot_size', 'Shot size', '景别', 'per shot', '逐张'),
    ('angle', 'Camera angle', '机位', 'per shot', '逐张'), ('placement', 'Placement', '构图位置', 'per shot, optional', '逐张·可空'),
    ('foreground', 'Foreground', '前景', 'per shot, optional', '逐张·可空'), ('camera', 'Lens & camera', '镜头', 'per shot', '逐张'),
]
missing = set(d['components']) - {s[0] for s in SLOTS}
if missing:
    raise SystemExit(f'component slots without a README row: {missing}')
GROUP = {'stand': ('Standing', '站姿'), 'sit': ('Sitting', '坐姿'), 'kneel': ('Kneeling', '跪姿'),
         'lie': ('Lying', '卧姿'), 'crouch': ('Crouching', '蹲姿'), 'upper': ('Upper body', '半身')}
unknown = {p['group'] for p in d['poses']} - set(GROUP)
if unknown:
    raise SystemExit(f'pose groups without a heading: {unknown}')


def site(url, lang):
    """A promicat.app link in the reader's language: English pages have no /zh prefix."""
    url = url.split('?')[0]
    if lang == 'en':
        url = url.replace(SITE + '/zh/', SITE + '/').replace(SITE + '/zh?', SITE + '?')
    elif not url.startswith(SITE + '/zh'):
        url = url.replace(SITE + '/', SITE + '/zh/', 1)
    return url + UTM


def thumb_url(r):
    """Photo-pose thumbnails are served by promicat.app, so the README loads fast."""
    return f"{SITE}/promicat/photo-poses/{r['id']}-thumb.webp"


def grid(cells, cols=6):
    rows = ['| ' + ' | '.join([''] * cols) + ' |', '|' + '---|' * cols]
    for i in range(0, len(cells), cols):
        chunk = cells[i:i + cols] + [''] * (cols - len(cells[i:i + cols]))
        rows.append('| ' + ' | '.join(chunk) + ' |')
    return '\n'.join(rows)


def cell(img, caption, link=None, width=140):
    alt = re.sub(r'<[^>]+>', ' ', caption).split('  ')[0].strip()
    pic = f'<img src="{img}" width="{width}" alt="{alt}">'
    return f'<a href="{link}">{pic}</a><br>{caption}' if link else f'{pic}<br>{caption}'


def T(lang, en, zh):
    return en if lang == 'en' else zh


def readme(lang):
    L = lambda en, zh: T(lang, en, zh)
    n = lambda x: x[0] if lang == 'en' else x[1]
    nm = lambda o: o['en'] if lang == 'en' else o['zh']
    poses_url = site(f'{SITE}/zh/poses', lang)
    other = L('[简体中文](README.zh-CN.md)', '[English](README.md)')
    me = L('English', '简体中文')
    out = [f"# {L('AI Photo Poses: portrait poses, white models and prompts', 'AI 写真姿势库 · 白模 + 写真配方 + 提示词')}", '',
           f"{me} · {other}" if lang == 'en' else f"[English](README.md) · 简体中文", '',
           f'<a href="{poses_url}"><img src="images/readme/mosaic.webp" alt="'
           + L('Portrait photos in 18 styles, each shot from a white-model pose in this library',
               '18 种风格的写真，每张都照着这个库里的白模姿势拍') + '" width="100%"></a>', '',
           L(f"**{len(PP)} white models for natural portrait poses, in {len(STYLES)} styles**, with {len(PP) + NCASES} portraits shot from them: "
             "every white model comes with 4 photos in different styles, so you can see the pose works anywhere. "
             "Give an AI image model your own photo and a white model, and it shoots you in that exact pose.",
             f"**{len(PP)} 个自然不僵的写真白模，{len(STYLES)} 种风格**，以及用它们拍出的 {len(PP) + NCASES} 张写真："
             "每个白模配 4 张不同风格的案例，一眼看出这个姿势放到哪里都好看。"
             "把你的照片和白模一起交给 AI 生图模型，就能拍出同一个姿势的你。"), '',
           f"**[{L('▶ Try any pose with your own photo on Promicat', '▶ 在 Promicat 上传照片，一键生成同款')}]({poses_url})**", '',
           f'<a href="{poses_url}"><img src="images/readme/demo-{lang}.gif" alt="'
           + L('Pick a white-model pose, add one photo: your photo sets the face, the white model sets the pose',
               '选一个白模，放一张照片：照片管脸，白模管动作')
           + '" width="100%"></a>', '']
    out += [L(f'- **{len(PP)} white models** in {len(STYLES)} styles, from street fashion and HK retro to gothic, Y2K and new Chinese style, with **{len(PP) + NCASES} portraits** shot from them',
              f'- **{len(PP)} 个写真白模**，{len(STYLES)} 种风格：街拍、港风、哥特、Y2K、新中式……共 **{len(PP) + NCASES} 张**用它们拍出的写真'),
            L(f'- **{len(d["poses"])} white models with 3D data** you can fine-tune in the browser, plus {len(EXTRA)} extra pose references',
              f'- **{len(d["poses"])} 个带 3D 数据的白模**，可以在浏览器里拖动微调；另有 {len(EXTRA)} 个补充姿势'),
            L(f'- **{len(PR)} portrait recipes** ({NSHOTS} sample shots) assembled from {NCOMP} prompt components',
              f'- **{len(PR)} 套写真配方**（{NSHOTS} 张样片），由 {NCOMP} 个提示词组件拼成'),
            L('- **2 Agent Skills**: one looks at a user photo, recommends poses and generates the portrait',
              '- **2 个 Agent Skill**：其中一个能看用户的照片、推荐姿势并直接生成写真'),
            L('- Images and data under CC BY 4.0, code under MIT. All people are AI-generated and fictional.',
              '- 图片和数据 CC BY 4.0，代码 MIT。所有人物都由 AI 生成，均为虚构。'),
            f"- {L('Latest update', '最近更新')} ({LATEST['date']}): {LATEST[lang]} · [{L('Changelog', '更新记录')}](CHANGELOG.md)", '',
            L('If this library saves you time, a ⭐ Star helps other people find it.',
              '如果这个库帮你省了时间，点个 ⭐ Star，能让更多人找到它。'), '']
    toc = [('photo-poses', L('Photo poses by style', '写真姿势（按风格）'), len(PP)),
           ('skills', L('Agent Skills', 'Agent Skill'), 2),
           ('recipes', L('Portrait recipes', '写真配方'), len(PR)),
           ('build', L('Build your own recipe', '自己组装写真配方'), NCOMP),
           ('white-models', L('3D white models', '3D 白模姿势'), len(d['poses']) + len(EXTRA)),
           ('lights', L('Lighting', '光影'), len(d['lights'])),
           ('scenes', L('Scenes', '场景'), len(d['scenes']))]
    out += [f"## {L('Contents', '目录')}", '']
    out += [f'- [{t}](#{a}) ({c})' for a, t, c in toc]
    out += [f"- [{L('Data format', '数据格式')}](#data) · [{L('License', '协议')}](#license)", '']

    # Photo poses
    out += ['<a id="photo-poses"></a>', f"## {L('Photo poses by style', '写真姿势（按风格）')}", '',
            L('Each pose is a sample photo and a white model drawn from it. The white model is the pose reference: '
              'attach your photo first and the white model second, then use the prompt on the style page. '
              'Open a style for all 10 poses with both prompts.',
              '每组是一张示例写真和照着它画的白模。白模就是姿势参考：参考图顺序是你的照片在前、白模在后，再配上风格页里的提示词。'
              '点风格名看这个风格的全部 10 组和两版提示词。'), '',
            f"| {L('Style', '风格')} | {L('Photos (open the style for white models and prompts)', '写真照（点风格名看白模和提示词）')} |", '|---|---|']
    for st in STYLES:
        rs = [r for r in PP if r['style'] == st]
        pics = ' '.join(f'<img src="{thumb_url(r)}" width="92" alt="{nm(r["name"])}">' for r in rs[:6])
        page = f'styles/{st}.md' if lang == 'en' else f'styles/{st}.zh-CN.md'
        sub = STYLE_NAME[st]['zh'] if lang == 'en' else STYLE_NAME[st]['en']
        out.append(f"| [**{nm(STYLE_NAME[st])}**]({page})<br><sub>{sub}</sub> | {pics} |")
    out.append('')

    # Skills
    out += ['<a id="skills"></a>', '## Agent Skills', '',
            L('**Install in Claude Code** (both skills, one plugin):', '**在 Claude Code 里安装**（两个技能打包成一个插件）：'), '',
            '```text',
            '/plugin install ai-photo-poses --marketplace leisure-cat/ai-photo-poses',
            '```', '',
            L('On older Claude Code versions:', '旧版本 Claude Code：'), '',
            '```text',
            '/plugin marketplace add leisure-cat/ai-photo-poses',
            '/plugin install ai-photo-poses@ai-photo-poses',
            '```', '',
            L('**Codex and other agents**: copy a folder from `skills/` into `~/.agents/skills/` (or your agent\'s skills directory). '
              'Without the rest of the repo, run the script with `--remote`.',
              '**Codex 等其他 Agent**：把 `skills/` 下的文件夹复制到 `~/.agents/skills/`（或你的 Agent 的技能目录）。只复制技能、没有整个仓库时，脚本加 `--remote`。'), '',
            L('**`skills/photo-pose-match`: match poses to a photo.** The user sends a photo; the agent reads the outfit, mood and setting, '
              f'picks a few of the {len(PP)} photo poses with a reason for each, then generates the portrait from "user photo + white model". '
              'Without an image tool it hands over the Promicat link instead. Works without cloning: `recommend.py --remote` reads the data from GitHub.',
              f'**`skills/photo-pose-match`：照片配姿势。** 用户发来照片，Agent 看穿着、气质和画面风格，从 {len(PP)} 组写真姿势里挑几组并说明理由，'
              '再用「用户照片 + 白模」直接生成写真；没有生图工具时给出 Promicat 页面链接。不克隆仓库也能用：`recommend.py --remote` 会从 GitHub 读取数据。'), '',
            '<img src="images/skill-demo.webp" width="540" alt="'
            + L('User photo, chosen white model, generated portrait', '用户照片、挑中的白模、生成的写真') + '">', '',
            '<sub>' + L('Left: the user photo (an AI-generated, fictional person). Middle: the white model the skill picked. Right: the result. '
                        'The top row switches to the HK retro outfit; the bottom row keeps the original clothes with `--keep-outfit`.',
                        '左：用户照片（AI 生成的虚构人物）　中：技能挑出的白模　右：生成结果。上面一组换成了港风复古的服装，下面一组用 `--keep-outfit` 保留了原来的衣服。') + '</sub>', '',
            '```bash',
            'python3 skills/photo-pose-match/recommend.py --list-styles',
            'python3 skills/photo-pose-match/recommend.py --style street,hkretro --group stand,lean --limit 6',
            'python3 skills/photo-pose-match/recommend.py --id sp101 --keep-outfit',
            '```', '',
            L('**`skills/ai-photo-poses`: portrait recipes and the pose library.** Apply or assemble a full 9-shot recipe, pick poses, '
              'and get finished prompts with the reference images to attach.',
              '**`skills/ai-photo-poses`：写真配方和姿势大全。** 套用或组装整套 9 张的写真配方、挑姿势，拼好提示词并给出要附带的参考图。'), '']

    # Recipes
    out += ['<a id="recipes"></a>', f"## {L('Portrait recipes', '写真配方')} ({len(PR)})", '',
            L('Each recipe is 9 shots that share one look, light, scene, outfit and model, and change only pose, expression, framing, angle and lens. '
              'Full prompts are in `data/portrait-recipes.json`, or print them with the script:',
              '每套 9 张共用同一组质感、光影、场景、服装和人物，只换姿势、表情、景别、机位和镜头。完整提示词在 `data/portrait-recipes.json`，也可以用脚本生成：'), '',
            '```bash',
            'python3 scripts/assemble.py --list',
            'python3 scripts/assemble.py tokyo-rain-night',
            'python3 scripts/assemble.py tokyo-rain-night --shot 3 --with-photo',
            '```', '',
            L('With `--with-photo`, attach your photo first and the listed white model second.',
              '带 `--with-photo` 时，参考图顺序是：你的照片在前，脚本列出的白模图在后。'), '']
    cells = []
    for r in PR:
        s = r['set']
        tags = ' · '.join(nm(COMP[k][s[k]]) for k in ('light', 'scene', 'look'))
        cells.append(f'<img src="{r["grid"]}" width="240" alt="{nm(r["name"])}"><br><b>{nm(r["name"])}</b><br>'
                     f'<code>{r["id"]}</code><br><sub>{tags}</sub>')
    out += [grid(cells, 3), '']

    # Build your own
    r0 = PR[0]
    example = {'id': 'my-recipe', 'subject': r0['subject'], 'set': r0['set'],
               'shots': [{k: v for k, v in r0['shots'][1].items()
                          if k in ('pose', 'action', 'expression', 'shot_size', 'angle', 'placement', 'foreground', 'camera')}]}
    out += ['<a id="build"></a>', f"## {L('Build your own recipe', '自己组装写真配方')}", '',
            L('`data/components.json` holds every component, grouped by slot; each has an `id`, English and Chinese names, and the `text` that goes into the prompt. A recipe only lists component ids:',
              '`data/components.json` 是全部组件，按槽位分组；每个组件有 `id`、中英文名和真正拼进提示词的 `text`。一套配方只写组件 id：'), '',
            f"| {L('Slot', '槽位')} | {L('Name', '名称')} | {L('Level', '层级')} | {L('Count', '数量')} |", '|---|---|---|---|']
    out += [f"| `{k}` | {L(en, zh)} | {L(le, lz)} | {len(d['components'][k])} |" for k, en, zh, le, lz in SLOTS]
    out += ['', L(f'"Set" slots are chosen once and shared by all 9 shots; "per shot" slots change shot by shot. A minimal recipe (shot 2 of "{r0["name"]["en"]}"):',
                  f'「整组」的槽位一套只选一次，9 张共用；「逐张」的槽位每张单独选。一个最小的配方（以「{r0["name"]["zh"]}」的第 2 张为例）：'), '',
            '```json', json.dumps(example, ensure_ascii=False, indent=1), '```', '',
            L('Save it as `my-recipe.json` and run `python3 scripts/assemble.py --recipe my-recipe.json`. An unknown id is an error that tells you where to look.',
              '存成 `my-recipe.json` 后运行 `python3 scripts/assemble.py --recipe my-recipe.json`。写错 id 会直接报错并告诉你去哪里查。'), '']

    # White models
    out += ['<a id="white-models"></a>', f"## {L('3D white models', '3D 白模姿势')} ({len(d['poses'])} + {len(EXTRA)})", '',
            L('Open one on Promicat to see every camera angle, drag its arms and legs in 3D, and generate with your photo. `pose3d` in `data/poses.json` holds the 3D pose.',
              '点图片打开 Promicat 页面，可以看所有机位、在 3D 里拖动手臂和腿微调、上传照片生成。3D 姿势数据在 `data/poses.json` 的 `pose3d` 字段。'), '']
    for g, names in GROUP.items():
        ps = [p for p in d['poses'] if p['group'] == g]
        if ps:
            out += [f"### {n(names)} ({len(ps)})", '', grid([cell(p['thumb'], nm(p['name']), site(p['url'], lang)) for p in ps]), '']
    out += [f"### {L('Extra pose references', '补充姿势')} ({len(EXTRA)})", '',
            L('Common poses without 3D data yet, one front view each, in `images/poses-extra/`.',
              '配方里常用、但还没有 3D 数据的姿势，每个只有一张正面白模图，在 `images/poses-extra/`。'), '',
            grid([cell(v['thumb'], nm(v)) for v in EXTRA]), '',
            f"### {L('One pose with your photo', '只用一个姿势：你的照片 + 白模')}", '',
            L('Attach your photo first and the white model second, with this prompt:', '参考图顺序是你的照片在前、白模在后，提示词：'), '',
            '```text', TPL, '```', '']
    out += [f"### {L('Sample portraits', '示例写真')} ({len(d['cases'])})", '',
            grid([cell(c['thumb'], f"{nm(POSE[c['pose']]['name'])}<br><sub>{nm(c['light_name'])} · {nm(c['scene_name'])}</sub>",
                       site(POSE[c['pose']]['url'], lang)) for c in d['cases']]), '']

    # Lights and scenes
    out += ['<a id="lights"></a>', f"## {L('Lighting', '光影')} ({len(d['lights'])})", '',
            L('Paste the prompt column straight into your prompt.', '把「提示词」一栏直接放进你的提示词。'), '',
            f"| {L('Example', '示例')} | {L('Light', '光影')} | {L('Prompt', '提示词')} |", '|---|---|---|']
    out += [f"| <img src=\"{l['thumb']}\" width=\"110\" alt=\"{nm(l['name'])}\"> | **{nm(l['name'])}** | `{l['prompt']}` |" for l in d['lights']]
    out += ['', '<a id="scenes"></a>', f"## {L('Scenes', '场景')} ({len(d['scenes'])})", '',
            grid([cell(s['thumb'], nm(s['name'])) for s in d['scenes']], 7), '',
            f"## {L('More on Promicat', 'Promicat 上的相关配方')}", '',
            grid([cell(r['image'], nm(r['name']), site(r['url'], lang)) for r in d['recipes']]), '',
            f"## {L('Promi edition', 'Promi 特别篇')}", '',
            L(f"Promi, the Promicat mascot, shot these poses and lights too ({len(d['promi'])} images in `images/promi/`).",
              f"Promicat 的吉祥物 Promi 也把这些姿势和光影拍了一遍（{len(d['promi'])} 张，在 `images/promi/`）。"), '']

    # Data, license
    out += ['<a id="data"></a>', f"## {L('Data format', '数据格式')}", '',
            f"| {L('File', '文件')} | {L('Contents', '内容')} |", '|---|---|',
            L(f'| `data/photo-poses.json` | {len(PP)} white models: style, pose name, group, `pose_text`, `framing`, `photo`, white model (`pose`), `cases` ({NCASES} more portraits with their prompts), `url`, sample prompt, `prompt_with_your_photo` |',
              f'| `data/photo-poses.json` | {len(PP)} 个白模：风格、姿势名、分类、动作描述 `pose_text`、全身或半身 `framing`、写真照 `photo`、白模 `pose`、案例 `cases`（另外 {NCASES} 张写真和各自的提示词）、在线页面 `url`、示例提示词、「用你的照片」提示词 |'),
            L(f'| `data/portrait-recipes.json` | {len(PR)} recipes: component ids, shots, samples, both prompts, pose references |',
              f'| `data/portrait-recipes.json` | {len(PR)} 套写真配方：组件 id、每张的设置、样片、两版提示词、姿势参考图 |'),
            L(f'| `data/components.json` | {len(SLOTS)} slots, {NCOMP} components |', f'| `data/components.json` | {len(SLOTS)} 个槽位、{NCOMP} 个组件 |'),
            L('| `data/poses.json` | 3D white models: names, group, views, `pose3d`, page |', '| `data/poses.json` | 3D 白模：名字、分类、各机位图、`pose3d`、在线页面 |'),
            L('| `data/lights.json`, `data/scenes.json`, `data/cases.json` | lights, scenes and sample portraits with prompts |',
              '| `data/lights.json`、`data/scenes.json`、`data/cases.json` | 光影、场景和示例写真，带提示词 |'),
            L('| `data/templates.json` | the generic "your photo + white model" prompt |', '| `data/templates.json` | 「你的照片 + 白模」通用提示词 |'), '',
            L('`pose3d` is the Promicat white-model format v1: `{"v": 1, "rot": {"joint": [x, y, z]}}`, degrees, XYZ order, relative to standing at rest.',
              '`pose3d` 是 Promicat 3D 白模格式 v1：`{"v": 1, "rot": {"关节": [x, y, z]}}`，单位是度，XYZ 顺序，相对站立静止姿势。'), '',
            '<a id="license"></a>', f"## {L('License and credits', '协议与来源')}", '',
            L('- Code (`scripts/`, `skills/`): MIT. Images and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); credit "Promicat (promicat.app)".',
              '- 代码（`scripts/`、`skills/`）：MIT。图片和数据：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans)，使用时注明「来自 Promicat（promicat.app）」。'),
            L('- Most 3D white-model views come from the CC0 [Shisei](https://github.com/wquguru/shisei) library; every other image was generated by Promicat with AI, and every person is fictional.',
              '- 3D 白模的大部分机位图来自 CC0 的 [Shisei](https://github.com/wquguru/shisei)；其余图片都由 Promicat 用 AI 生成，人物均为虚构。'),
            L('- Do not use these images to impersonate anyone or to make misleading content. See [MEDIA-RIGHTS.md](MEDIA-RIGHTS.md); to contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).',
              '- 请不要用这些素材冒充他人或制作误导性内容。详见 [MEDIA-RIGHTS.md](MEDIA-RIGHTS.md)；想参与贡献请看 [CONTRIBUTING.md](CONTRIBUTING.md)。'), '',
            f"## {L('About Promicat', '关于 Promicat')}", '',
            L(f'[Promicat]({site(SITE, lang)}) turns good AI work into recipes anyone can remake in one click: the pose library, 3D fine-tuning and portrait generation all live there. '
              f'If this library helps, a ⭐ on [GitHub]({REPO}) helps others find it.',
              f'[Promicat]({site(SITE, lang)}) 是 AI 创作配方平台：把好看的 AI 作品做成能一键复刻的配方，姿势库、3D 微调、写真生成都在这里。'
              f'觉得有用的话，在 [GitHub]({REPO}) 点个 ⭐，能让更多人找到它。'), '']
    name = 'README.md' if lang == 'en' else 'README.zh-CN.md'
    open(os.path.join(ROOT, name), 'w', encoding='utf-8').write('\n'.join(out))
    return name


def style_pages(lang):
    L = lambda en, zh: T(lang, en, zh)
    nm = lambda o: o['en'] if lang == 'en' else o['zh']
    os.makedirs(os.path.join(ROOT, 'styles'), exist_ok=True)
    for st in STYLES:
        rows = [r for r in PP if r['style'] == st]
        other = f'[简体中文]({st}.zh-CN.md)' if lang == 'en' else f'[English]({st}.md)'
        back = '../README.md#photo-poses' if lang == 'en' else '../README.zh-CN.md#photo-poses'
        md = [f"# {nm(STYLE_NAME[st])}", '', (f'English · {other}' if lang == 'en' else f'{other} · 简体中文'), '',
              L(f'{len(rows)} white models, each with 4 portraits shot from it in different styles. Attach your photo first and the white model second. '
                f'Try them with your own photo on [Promicat]({site(SITE + "/zh/poses", lang)}).',
                f'{len(rows)} 个白模，每个配 4 张用它拍出的不同风格写真。参考图顺序是你的照片在前、白模在后。'
                f'也可以在 [Promicat]({site(SITE + "/zh/poses", lang)}) 上传照片直接生成。'), '',
              f"[{L('← Back to all styles', '← 返回全部风格')}]({back})", '']
        for r in rows:
            shots = [(r['photo_thumb'], nm(r['style_name']))] + [(c['thumb'], nm(c['style_name'])) for c in r.get('cases', [])]
            md += [f"## {nm(r['name'])} ({nm(r['group_name'])})", '',
                   '| ' + ' | '.join([L('White model', '白模')] + [lab for _, lab in shots]) + ' |',
                   '|' + '---|' * (len(shots) + 1),
                   f'| <img src="../{r["pose_thumb"]}" width="150" alt="{L("White model", "白模")}"> | '
                   + ' | '.join(f'<a href="{site(r["url"], lang)}"><img src="../{t}" width="150" alt="{nm(r["name"])} · {lab}"></a>' for t, lab in shots) + ' |', '',
                   f"{L('Full size', '大图')}: [{L('photo', '写真照')}](../{r['photo']}) · [{L('white model', '白模')}](../{r['pose']}) · "
                   f"[{L('try it on Promicat', '在 Promicat 生成')}]({site(r['url'], lang)})", '',
                   f"<details><summary>{L('Prompt with your photo (image 1: your photo, image 2: white model)', '提示词：用你的照片（图 1 你的照片，图 2 白模）')}</summary>", '',
                   '```text', r['prompt_with_your_photo'], '```', '', '</details>', '',
                   f"<details><summary>{L('Prompt for the sample (fictional model)', '提示词：生成示例图（虚构模特）')}</summary>", '',
                   '```text', r['prompt'], '```', '', '</details>', '']
        name = f'{st}.md' if lang == 'en' else f'{st}.zh-CN.md'
        open(os.path.join(ROOT, 'styles', name), 'w', encoding='utf-8').write('\n'.join(md))


for lang in ('en', 'zh'):
    print('wrote', readme(lang))
    style_pages(lang)
print('wrote', len(STYLES) * 2, 'style pages')
