---
name: photo-pose-match
description: Match portrait poses to a user photo — look at the photo, pick suitable poses from 200 photo poses in 20 styles (sample photo + white model), explain why, then generate the portrait from "user photo + white model". Use when a user sends their own photo and asks for portrait or photo-shoot poses, pose ideas, or "make photos of me in this style". 看用户上传的照片，从 200 组写真姿势（20 种风格，写真照 + 白模）里挑出适合这个人的姿势，说明理由，再用「用户照片 + 白模」生成同款写真。用户发来自己的照片并说「帮我拍写真」「推荐几个姿势」「我适合什么姿势」「用这张照片出几张写真」「照着这个风格给我拍」时使用。
---

# 照片配姿势

这个技能所在仓库（[ai-photo-poses](https://github.com/leisure-cat/ai-photo-poses)）的 `data/photo-poses.json` 有 200 组写真姿势：20 种风格各 10 组，每组一张示例写真（`photo`）和照着它画的木头白模（`pose`）。生成时，用户照片作为图 1，白模作为图 2：人像来自图 1，动作照抄图 2。

`recommend.py` 负责按条件筛选姿势并拼好提示词；看照片、做判断由你来。

```bash
python3 skills/photo-pose-match/recommend.py --list-styles
python3 skills/photo-pose-match/recommend.py --style street,hkretro --group stand,lean --limit 6
python3 skills/photo-pose-match/recommend.py --id sp101 --keep-outfit
```

作为 Claude Code 插件安装时，脚本路径是 `${CLAUDE_PLUGIN_ROOT}/skills/photo-pose-match/recommend.py`。如果只装了这个技能、没有克隆整个仓库，加 `--remote`：数据和图片都从 GitHub 读取，图片路径是可以直接下载的链接。

## 怎么做

1. **看照片**。确认照片里只有一个人、看得清脸。看不清，或者有好几个人时，请用户换一张或指定是谁，不要猜。然后记下：
   - 照片是全身还是半身、自拍；
   - 穿的什么（街头、通勤、礼服、运动、汉服……）；
   - 整体气质和照片本身的风格（明亮、清新、酷、复古、文艺、暗黑……）。

   不要根据照片推断或说出性别、年龄、种族、身材，也不要评价长相。
2. **定风格**。用户点名了风格就用它（`--list-styles` 里找对应的 id）。没点名就按照片推荐 2–3 种并说明理由，例如：
   - 穿风衣、在城市里 → 街拍时尚、港风复古、老钱风；
   - 针织衫、在室内 → 咖啡馆文艺、居家慵懒；
   - 黑衣、气质冷 → 情绪棚拍、暗黑哥特、赛博霓虹；
   - 浅色、阳光 → 日系清新、森系花田、海边度假。
3. **定动作**。用户说了想要的动作（站、坐、靠、走、回眸、蹲跪、躺、半身、动态）就用 `--group` 筛选。没说就混着挑，让几张之间有变化。只有用户只要半身特写时才加 `--framing half`。
4. **决定服装**。用户想保留自己的衣服，或者照片里的衣服跟风格很搭，就加 `--keep-outfit`。否则用风格自带的服装，并告诉用户会换成什么衣服（看输出 prompt 里的 `wearing …`）。服装只按风格和用户的意愿选，不按你对用户性别的猜测选。
5. **运行脚本并挑选**。从输出里挑 3 组（用户要更多就多给）。每组告诉用户：姿势名、风格、为什么适合这张照片（一句话），附上示例写真和白模，方便对比。
6. **生成**。
   - 你有生图工具（GPT Image、Nano Banana、Seedream 等能传参考图的）：按顺序传两张参考图，图 1 是用户照片，图 2 是这组的白模（`white_model`），提示词用输出里的 `prompt`，原样使用，不要删掉保脸和得体的要求。
   - 没有生图工具：把每组的 `page` 链接给用户，在 Promicat 页面上传照片就能一键生成；同时给出 `prompt` 和白模，方便用户拿去别的工具用。
7. **看结果**。人脸不像、动作和白模差很多、出现木头关节或者灰色皮肤，就再生成一次，或者换一组姿势。告诉用户哪里不对、你做了什么调整。

## 规矩

- 只用用户本人或已经同意的人的照片。用户说照片是别人的（明星、网图、陌生人），就停下来说明不能这样做。
- 只做得体的写真：不做裸露、性感化、低龄化的内容。照片里的人看起来未成年时，只做日常生活照风格，不用暗黑哥特、Y2K 这类成人向造型。
- 不改脸型，不美颜到认不出来，不换人。
- 用到图片时注明素材来自 Promicat（CC BY 4.0）。
