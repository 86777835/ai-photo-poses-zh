---
name: ai-photo-poses
description: 用开源人像摄影库按风格找写真姿势（200 组写真照 + 白模，20 种风格：街拍、港风、哥特、老钱风、Y2K、新中式……），或套用、组装 AI 写真配方：从组件（光影、场景、胶片质感、服装、姿势、景别、机位、镜头）拼出整套 9 张的写真提示词，并给出姿势参考图（白模图）。用户说「找个港风/哥特/街拍的姿势」「给我一套写真提示词」「做一组人像写真」「找个拍照姿势」「这张照片换个姿势」「什么光好看」「AI 写真姿势参考」时使用。
---

# AI 人像摄影库

这个技能所在的仓库里有：

- `data/photo-poses.json`：写真姿势，20 种风格各 10 组。每组有 `style`/`style_name`、姿势名 `name.zh`、分类 `group`（stand 站 / sit 坐 / lean 靠 / walk 走 / look 回眸 / crouch 蹲跪 / lie 躺 / upper 半身 / move 动态）、`photo`（写真照）、`pose`（照着写真照画的木头白模，用作姿势参考图）、`prompt`（虚构模特示例）和 `prompt_with_your_photo`（附图 1 用户照片、附图 2 白模）。`styles/<style>.md` 是每个风格的图文页。
- `data/portrait-recipes.json`：现成的人像写真配方，每套 9 张，`set` 是整组共用的组件 id，`shots` 是每张的组件 id、样片、`prompt`（虚构模特）和 `prompt_with_your_photo`（用户照片）。
- `data/components.json`：人像组件库，按槽位分组（look、skin、light、light_mod、scene、outfit、hair、makeup、motion、props、negative、gaze_rule、pose、action、expression、shot_size、angle、placement、foreground、camera）。每个组件有 `id`、`zh`、`en`、`text`；姿势组件还有 `image`（白模图）和 `pose_ref`（不为空时生图要带白模图）。
- `scripts/assemble.py`：把配方拼成提示词。`--list` 列配方；`<配方id> [--shot N] [--with-photo]`；`--recipe 自己的.json`。会同时打印要附带的参考图。
- `data/poses.json`：摄影姿势。每个有中英文名、分类（stand 站 / sit 坐 / kneel 跪 / lie 卧 / crouch 蹲 / upper 半身）、各机位白模图路径（`views`）、在线页面 `url`。
- `data/lights.json`：光影。`prompt` 是可直接放进提示词的一句话。
- `data/scenes.json`：场景。
- `data/cases.json`：示例写真，带完整提示词，可以当范例。
- `data/templates.json`：`prompt_with_your_photo`，「用户照片 + 白模图」的通用提示词。

路径都相对仓库根目录（本文件往上两级）。

## 怎么做：按风格找写真姿势

1. 弄清风格（不确定就给用户看 `style_name` 列表）和想要的动作类型（站、坐、靠、走、回眸、蹲、躺、半身、动态）。
2. 在 `photo-poses.json` 里按 `style` 和 `group` 挑 1–3 组，给出姿势名、写真照路径和白模路径。
3. 用户有照片：给 `prompt_with_your_photo`，参考图顺序是用户照片在前、白模在后；没有照片：给 `prompt`。
4. 想换风格只换风格描述，白模可以跨风格复用。

## 怎么做：要一整套写真

1. 先问清（或从对话里判断）：主题和氛围、在哪拍、什么光、男女和大致样貌、有没有用户自己的照片。
2. 在 `portrait-recipes.json` 里找最接近的配方。能直接用就用；差一点就复制它，只换几个组件 id（比如换 `scene`、`light`、`outfit`），存成新的 JSON。组件只能用 `components.json` 里已有的 id，不要自己编。
3. 运行 `python3 scripts/assemble.py --recipe <文件>`（用户有照片就加 `--with-photo`），把 9 条提示词和每条的参考图交给用户。
4. 整组槽位一套只选一个值，保证 9 张像同一场拍摄；逐张槽位让 9 张覆盖远景、全身、中景、特写、细节和一张创意机位。表情要符合 `gaze_rule`。

## 怎么做：只要一个姿势

1. 弄清用户要什么：人数（这里都是单人）、站坐卧、情绪（自信、慵懒、俏皮、安静）、在哪拍、什么光。
2. 在 `poses.json` 里按分类和名字挑 1–3 个姿势，告诉用户每个的中文名，并给出白模图路径（优先 `front`，没有就用第一个机位）。
3. 从 `lights.json`、`scenes.json` 各挑一个合适的，或者照用户的要求自己写。
4. 拼提示词：
   - 用户有自己的照片：用 `templates.json` 的 `prompt_with_your_photo`，在末尾加上「Scene: <场景>. Lighting: <光影名> — <光影 prompt>. Wearing <服装>.」。参考图顺序是用户照片在前，白模图在后。
   - 没有照片：参照 `cases.json` 里的 `prompt` 写，把人物描述换成用户要的人。
5. 告诉用户：如果白模不完全合适，可以打开该姿势的 `url`，在 3D 里拖动白模微调，再直接用自己的照片生成。

## 规矩

- 只做得体的写真：不做裸露、性感化、低龄化的内容。
- 不要用这些素材冒充真实的人。
- 图片和数据是 CC BY 4.0，转发或商用时注明「来自 Promicat（promicat.app）」。
