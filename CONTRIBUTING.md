# Contributing · 参与贡献

English · 简体中文见下方

## What fits

- A new photo pose: a portrait-shoot photo and a white model (faceless wooden or grey mannequin) that shows exactly the same pose, camera angle and framing.
- Fixes: a white model that does not match its photo, a wrong name, a broken link, a prompt that fails.
- Only AI-generated, fictional people, or people who gave written consent. No real person's likeness without consent, no minors in adult-styled looks, nothing sexualised, outfits opaque.

## How

1. Open an issue first for new poses or styles, with the two images and the prompt you used.
2. Data lives in `data/*.json`. `README.md`, `README.zh-CN.md` and `styles/*` are generated: do not edit them by hand.
3. After changing data, run:

   ```bash
   python3 scripts/build_readme.py
   python3 scripts/validate.py
   ```

4. Open a pull request. By contributing you agree your images and data are released under CC BY 4.0 and your code under MIT.

## 简体中文

- **欢迎的内容**：新的写真姿势（一张写真照 + 一张动作、机位、取景完全一致的无脸白模）；修正白模和照片对不上、名字写错、链接失效、提示词不好用等问题。
- **人物要求**：只用 AI 生成的虚构人物，或已书面同意的真人；不使用未经同意的真人肖像，不做低龄化的成人造型，不做性感化内容，服装不透。
- **步骤**：新姿势或新风格先开 issue，附上两张图和用到的提示词。数据在 `data/*.json`；`README.md`、`README.zh-CN.md` 和 `styles/*` 是生成文件，不要手改。改完数据后运行上面两个命令，再提 PR。贡献即表示同意图片和数据按 CC BY 4.0、代码按 MIT 开放。
