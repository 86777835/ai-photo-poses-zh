# AI 人像摄影库 · 姿势大全 + 写真配方组装

**200 组写真姿势（20 种风格，每组一张写真照 + 一张照着它画的白模）、24 套人像写真配方（216 张样片）、62 个摄影姿势（39 个带多机位白模图和 3D 数据）、436 个可自由组合的人像元素（光影、场景、胶片质感、服装、景别、机位、镜头……），每张图都有可复制的提示词。** 图片和数据按 CC BY 4.0 开放，可以免费商用，注明来自 [Promicat](https://promicat.app?ref=github) 即可。

这个库的核心是一套**人像提示词组件**：把一张写真拆成「质感 + 光 + 场景 + 服装 + 姿势 + 表情 + 景别 + 机位 + 镜头」等 20 个槽位，每个槽位都有一批写好的英文短句。挑几个组件一拼，就是一条完整的写真提示词；换掉其中一个，就是一套新写真。下面 24 套配方全部是这样拼出来的。

由 [Promicat](https://promicat.app?ref=github) 制作和维护。在线浏览姿势、**在 3D 里微调姿势**、上传自己的照片一键生成同款写真：<https://promicat.app/zh/poses?ref=github>

## 能用来做什么

- **按风格找写真姿势**：20 种写真风格（街拍、港风、哥特、老钱风、Y2K、新中式……）各 10 组自然不僵的姿势，每组都有写真照和对应白模，白模直接拿来当姿势参考图。
- **直接套用写真配方**：24 套主题写真，每套 9 张（远景、全身、中景、特写、细节都有），每张都有两版提示词：虚构模特版，以及「用你的照片」版。
- **自己组装人像配方**：从 436 个组件里挑，几行 JSON 就是一套新配方，脚本帮你拼成提示词。
- **给 AI 生图当姿势参考**：你的照片作为第一张参考图，白模图作为第二张。GPT Image、Nano Banana、Seedream、即梦等都能用。
- **拍照前找姿势、学光影**：姿势按站、坐、跪、卧、蹲、半身分类；每种光都有示例照和一句能直接用的描述。
- **给 Agent 用**：自带两个 Agent Skill（`skills/`），其中「照片配姿势」能看用户的照片自动推荐姿势并生成写真；另有结构化 JSON（`data/`）和组装脚本（`scripts/`）。

## 写真姿势

200 组，20 种风格。每组是一张写真照和一张照着它画的木头白模：白模当姿势参考图，配上你的照片和风格描述，就能拍出同款。点风格名看这个风格的全部 10 组和提示词。

| 风格 | 写真照（点风格名看全部 10 组） |
|---|---|
| [**街拍时尚**](styles/street.md)<br><sub>Street fashion</sub> | <img src="thumbs/photo-poses/street/sp001-photo.webp" width="96" alt="迎面走来提衣领"> <img src="thumbs/photo-poses/street/sp002-photo.webp" width="96" alt="靠墙低头看墨镜"> <img src="thumbs/photo-poses/street/sp003-photo.webp" width="96" alt="过马路回头"> <img src="thumbs/photo-poses/street/sp004-photo.webp" width="96" alt="坐台阶看街"> <img src="thumbs/photo-poses/street/sp005-photo.webp" width="96" alt="整理袖口"> <img src="thumbs/photo-poses/street/sp006-photo.webp" width="96" alt="拎包侧身"> |
| [**咖啡馆文艺**](styles/cafe.md)<br><sub>Cafe & bookshop</sub> | <img src="thumbs/photo-poses/cafe/sp011-photo.webp" width="96" alt="托腮望窗"> <img src="thumbs/photo-poses/cafe/sp012-photo.webp" width="96" alt="书架抽书"> <img src="thumbs/photo-poses/cafe/sp013-photo.webp" width="96" alt="捧杯吹气"> <img src="thumbs/photo-poses/cafe/sp014-photo.webp" width="96" alt="翻书低笑"> <img src="thumbs/photo-poses/cafe/sp015-photo.webp" width="96" alt="趴桌侧脸"> <img src="thumbs/photo-poses/cafe/sp016-photo.webp" width="96" alt="吧台倚靠"> |
| [**海边度假**](styles/beach.md)<br><sub>Seaside holiday</sub> | <img src="thumbs/photo-poses/beach/sp021-photo.webp" width="96" alt="提裙回眸"> <img src="thumbs/photo-poses/beach/sp022-photo.webp" width="96" alt="赤脚踢水"> <img src="thumbs/photo-poses/beach/sp023-photo.webp" width="96" alt="坐沙抱膝"> <img src="thumbs/photo-poses/beach/sp024-photo.webp" width="96" alt="按帽子"> <img src="thumbs/photo-poses/beach/sp025-photo.webp" width="96" alt="拎鞋走"> <img src="thumbs/photo-poses/beach/sp026-photo.webp" width="96" alt="侧躺沙滩"> |
| [**森系花田**](styles/flower.md)<br><sub>Forest & flower field</sub> | <img src="thumbs/photo-poses/flower/sp031-photo.webp" width="96" alt="蹲着闻花"> <img src="thumbs/photo-poses/flower/sp032-photo.webp" width="96" alt="花中转身"> <img src="thumbs/photo-poses/flower/sp033-photo.webp" width="96" alt="躺花丛"> <img src="thumbs/photo-poses/flower/sp034-photo.webp" width="96" alt="跪坐编花环"> <img src="thumbs/photo-poses/flower/sp035-photo.webp" width="96" alt="倚树干"> <img src="thumbs/photo-poses/flower/sp036-photo.webp" width="96" alt="捧花半身"> |
| [**日系清新**](styles/jfilm.md)<br><sub>Japanese fresh film</sub> | <img src="thumbs/photo-poses/jfilm/sp041-photo.webp" width="96" alt="扶车撩发"> <img src="thumbs/photo-poses/jfilm/sp042-photo.webp" width="96" alt="骑车回头"> <img src="thumbs/photo-poses/jfilm/sp043-photo.webp" width="96" alt="坐路边"> <img src="thumbs/photo-poses/jfilm/sp044-photo.webp" width="96" alt="电车站等车"> <img src="thumbs/photo-poses/jfilm/sp045-photo.webp" width="96" alt="靠自动售货机"> <img src="thumbs/photo-poses/jfilm/sp046-photo.webp" width="96" alt="伸手挡光"> |
| [**港风复古**](styles/hkretro.md)<br><sub>HK retro neon</sub> | <img src="thumbs/photo-poses/hkretro/sp051-photo.webp" width="96" alt="靠霓虹墙"> <img src="thumbs/photo-poses/hkretro/sp052-photo.webp" width="96" alt="外套搭肩走"> <img src="thumbs/photo-poses/hkretro/sp053-photo.webp" width="96" alt="电话亭打电话"> <img src="thumbs/photo-poses/hkretro/sp054-photo.webp" width="96" alt="茶餐厅托腮"> <img src="thumbs/photo-poses/hkretro/sp055-photo.webp" width="96" alt="回头望镜"> <img src="thumbs/photo-poses/hkretro/sp056-photo.webp" width="96" alt="点烟姿势无烟"> |
| [**居家慵懒**](styles/home.md)<br><sub>Cosy at home</sub> | <img src="thumbs/photo-poses/home/sp061-photo.webp" width="96" alt="靠沙发抱膝笑"> <img src="thumbs/photo-poses/home/sp062-photo.webp" width="96" alt="窗边伸懒腰"> <img src="thumbs/photo-poses/home/sp063-photo.webp" width="96" alt="床边看书"> <img src="thumbs/photo-poses/home/sp064-photo.webp" width="96" alt="厨房倚台"> <img src="thumbs/photo-poses/home/sp065-photo.webp" width="96" alt="地毯趴着"> <img src="thumbs/photo-poses/home/sp066-photo.webp" width="96" alt="抱枕窝沙发"> |
| [**校园青春**](styles/campus.md)<br><sub>Campus youth</sub> | <img src="thumbs/photo-poses/campus/sp071-photo.webp" width="96" alt="台阶抬头"> <img src="thumbs/photo-poses/campus/sp072-photo.webp" width="96" alt="抱书走"> <img src="thumbs/photo-poses/campus/sp073-photo.webp" width="96" alt="靠树看书"> <img src="thumbs/photo-poses/campus/sp074-photo.webp" width="96" alt="草坪躺"> <img src="thumbs/photo-poses/campus/sp075-photo.webp" width="96" alt="黑板前"> <img src="thumbs/photo-poses/campus/sp076-photo.webp" width="96" alt="骑车过"> |
| [**情绪棚拍**](styles/mood.md)<br><sub>Moody studio</sub> | <img src="thumbs/photo-poses/mood/sp081-photo.webp" width="96" alt="抚肩低眸"> <img src="thumbs/photo-poses/mood/sp082-photo.webp" width="96" alt="双手捧脸"> <img src="thumbs/photo-poses/mood/sp083-photo.webp" width="96" alt="坐凳侧身"> <img src="thumbs/photo-poses/mood/sp084-photo.webp" width="96" alt="背影回头"> <img src="thumbs/photo-poses/mood/sp085-photo.webp" width="96" alt="蹲坐抱膝"> <img src="thumbs/photo-poses/mood/sp086-photo.webp" width="96" alt="手扶后颈"> |
| [**新中式**](styles/chinese.md)<br><sub>New Chinese style</sub> | <img src="thumbs/photo-poses/chinese/sp091-photo.webp" width="96" alt="月洞门回眸"> <img src="thumbs/photo-poses/chinese/sp092-photo.webp" width="96" alt="执扇半遮"> <img src="thumbs/photo-poses/chinese/sp093-photo.webp" width="96" alt="廊下坐栏"> <img src="thumbs/photo-poses/chinese/sp094-photo.webp" width="96" alt="撑油纸伞"> <img src="thumbs/photo-poses/chinese/sp095-photo.webp" width="96" alt="倚窗格"> <img src="thumbs/photo-poses/chinese/sp096-photo.webp" width="96" alt="拾阶而上"> |
| [**暗黑哥特**](styles/gothic.md)<br><sub>Gothic</sub> | <img src="thumbs/photo-poses/gothic/sp101-photo.webp" width="96" alt="回廊回眸"> <img src="thumbs/photo-poses/gothic/sp102-photo.webp" width="96" alt="烛台前"> <img src="thumbs/photo-poses/gothic/sp103-photo.webp" width="96" alt="王座侧坐"> <img src="thumbs/photo-poses/gothic/sp104-photo.webp" width="96" alt="倚石柱"> <img src="thumbs/photo-poses/gothic/sp105-photo.webp" width="96" alt="手捧玫瑰"> <img src="thumbs/photo-poses/gothic/sp106-photo.webp" width="96" alt="楼梯下行"> |
| [**学院风**](styles/darkacad.md)<br><sub>Dark academia</sub> | <img src="thumbs/photo-poses/darkacad/sp111-photo.webp" width="96" alt="书梯上"> <img src="thumbs/photo-poses/darkacad/sp112-photo.webp" width="96" alt="台灯下读"> <img src="thumbs/photo-poses/darkacad/sp113-photo.webp" width="96" alt="抱书倚架"> <img src="thumbs/photo-poses/darkacad/sp114-photo.webp" width="96" alt="地毯坐书堆"> <img src="thumbs/photo-poses/darkacad/sp115-photo.webp" width="96" alt="走廊快走"> <img src="thumbs/photo-poses/darkacad/sp116-photo.webp" width="96" alt="窗边写信"> |
| [**老钱风**](styles/oldmoney.md)<br><sub>Old money</sub> | <img src="thumbs/photo-poses/oldmoney/sp121-photo.webp" width="96" alt="网球场扛拍"> <img src="thumbs/photo-poses/oldmoney/sp122-photo.webp" width="96" alt="露台倚栏"> <img src="thumbs/photo-poses/oldmoney/sp123-photo.webp" width="96" alt="毛衣搭肩走"> <img src="thumbs/photo-poses/oldmoney/sp124-photo.webp" width="96" alt="藤椅坐"> <img src="thumbs/photo-poses/oldmoney/sp125-photo.webp" width="96" alt="戴帽回头"> <img src="thumbs/photo-poses/oldmoney/sp126-photo.webp" width="96" alt="车门旁"> |
| [**西部牛仔**](styles/western.md)<br><sub>Western cowboy</sub> | <img src="thumbs/photo-poses/western/sp131-photo.webp" width="96" alt="坐围栏"> <img src="thumbs/photo-poses/western/sp132-photo.webp" width="96" alt="压帽檐"> <img src="thumbs/photo-poses/western/sp133-photo.webp" width="96" alt="靠谷仓"> <img src="thumbs/photo-poses/western/sp134-photo.webp" width="96" alt="夕阳走来"> <img src="thumbs/photo-poses/western/sp135-photo.webp" width="96" alt="蹲地看远"> <img src="thumbs/photo-poses/western/sp136-photo.webp" width="96" alt="甩绳套"> |
| [**波西米亚**](styles/boho.md)<br><sub>Boho desert</sub> | <img src="thumbs/photo-poses/boho/sp141-photo.webp" width="96" alt="沙丘张臂"> <img src="thumbs/photo-poses/boho/sp142-photo.webp" width="96" alt="坐地毯"> <img src="thumbs/photo-poses/boho/sp143-photo.webp" width="96" alt="沙中走"> <img src="thumbs/photo-poses/boho/sp144-photo.webp" width="96" alt="倚枯树"> <img src="thumbs/photo-poses/boho/sp145-photo.webp" width="96" alt="转圈裙摆"> <img src="thumbs/photo-poses/boho/sp146-photo.webp" width="96" alt="压帽回头"> |
| [**Y2K 千禧辣妹**](styles/y2k.md)<br><sub>Y2K flash</sub> | <img src="thumbs/photo-poses/y2k/sp151-photo.webp" width="96" alt="便利店门口蹲"> <img src="thumbs/photo-poses/y2k/sp152-photo.webp" width="96" alt="翻盖手机"> <img src="thumbs/photo-poses/y2k/sp153-photo.webp" width="96" alt="扶门回头"> <img src="thumbs/photo-poses/y2k/sp154-photo.webp" width="96" alt="坐路沿"> <img src="thumbs/photo-poses/y2k/sp155-photo.webp" width="96" alt="靠贩卖机"> <img src="thumbs/photo-poses/y2k/sp156-photo.webp" width="96" alt="甩发"> |
| [**街头朋克**](styles/punk.md)<br><sub>Street punk</sub> | <img src="thumbs/photo-poses/punk/sp161-photo.webp" width="96" alt="涂鸦墙蹲"> <img src="thumbs/photo-poses/punk/sp162-photo.webp" width="96" alt="扛吉他"> <img src="thumbs/photo-poses/punk/sp163-photo.webp" width="96" alt="靠铁门"> <img src="thumbs/photo-poses/punk/sp164-photo.webp" width="96" alt="坐音箱"> <img src="thumbs/photo-poses/punk/sp165-photo.webp" width="96" alt="拉外套"> <img src="thumbs/photo-poses/punk/sp166-photo.webp" width="96" alt="跳起"> |
| [**赛博霓虹**](styles/cyber.md)<br><sub>Cyberpunk neon</sub> | <img src="thumbs/photo-poses/cyber/sp171-photo.webp" width="96" alt="雨中回头"> <img src="thumbs/photo-poses/cyber/sp172-photo.webp" width="96" alt="靠广告牌"> <img src="thumbs/photo-poses/cyber/sp173-photo.webp" width="96" alt="蹲屋顶"> <img src="thumbs/photo-poses/cyber/sp174-photo.webp" width="96" alt="拉拉链"> <img src="thumbs/photo-poses/cyber/sp175-photo.webp" width="96" alt="站地铁口"> <img src="thumbs/photo-poses/cyber/sp176-photo.webp" width="96" alt="快步过街"> |
| [**好莱坞复古**](styles/hollywood.md)<br><sub>1950s Hollywood</sub> | <img src="thumbs/photo-poses/hollywood/sp181-photo.webp" width="96" alt="楼梯扶手"> <img src="thumbs/photo-poses/hollywood/sp182-photo.webp" width="96" alt="化妆镜前"> <img src="thumbs/photo-poses/hollywood/sp183-photo.webp" width="96" alt="回眸肩头"> <img src="thumbs/photo-poses/hollywood/sp184-photo.webp" width="96" alt="倚钢琴"> <img src="thumbs/photo-poses/hollywood/sp185-photo.webp" width="96" alt="躺贵妃椅"> <img src="thumbs/photo-poses/hollywood/sp186-photo.webp" width="96" alt="手托下巴"> |
| [**北欧极简**](styles/nordic.md)<br><sub>Nordic minimal</sub> | <img src="thumbs/photo-poses/nordic/sp191-photo.webp" width="96" alt="窗前站"> <img src="thumbs/photo-poses/nordic/sp192-photo.webp" width="96" alt="坐地靠墙"> <img src="thumbs/photo-poses/nordic/sp193-photo.webp" width="96" alt="走过空间"> <img src="thumbs/photo-poses/nordic/sp194-photo.webp" width="96" alt="倚窗框"> <img src="thumbs/photo-poses/nordic/sp195-photo.webp" width="96" alt="椅子反坐"> <img src="thumbs/photo-poses/nordic/sp196-photo.webp" width="96" alt="仰头闭眼"> |

## 人像写真配方（24 套）

每套 9 张共用同一组质感、光影、场景、服装和人物，只换姿势、表情、景别、机位和镜头。完整提示词在 `data/portrait-recipes.json`，也可以用脚本生成：

```bash
python3 scripts/assemble.py --list                       # 列出全部配方
python3 scripts/assemble.py tokyo-rain-night             # 9 张的提示词（虚构模特）
python3 scripts/assemble.py tokyo-rain-night --shot 3 --with-photo   # 第 3 张，用你的照片
```

带 `--with-photo` 时，参考图顺序是：你的照片在前，脚本列出的白模图在后。

|  |  |  |
|---|---|---|
| <img src="images/portrait-recipes/tokyo-rain-night/grid.webp" width="240" alt="东京雨夜·霓虹小巷"><br><b>东京雨夜·霓虹小巷</b><br><code>tokyo-rain-night</code><br><sub>霓虹夜景 · 东京雨夜小巷 · CineStill 800T 夜景胶片</sub> | <img src="images/portrait-recipes/paris-cafe-morning/grid.webp" width="240" alt="巴黎咖啡馆·清晨露台"><br><b>巴黎咖啡馆·清晨露台</b><br><code>paris-cafe-morning</code><br><sub>清晨斜阳 · 巴黎咖啡馆露台 · 胶片 Portra 400 随拍</sub> | <img src="images/portrait-recipes/snowy-cabin-fireside/grid.webp" width="240" alt="雪夜木屋·壁炉边"><br><b>雪夜木屋·壁炉边</b><br><code>snowy-cabin-fireside</code><br><sub>壁炉火光 · 雪夜木屋 · 胶片 Portra 400 随拍</sub> |
| <img src="images/portrait-recipes/beach-sunset-wind/grid.webp" width="240" alt="海边日落·风中白裙"><br><b>海边日落·风中白裙</b><br><code>beach-sunset-wind</code><br><sub>黄金时刻 · 海边沙滩 · 褪色逆光胶片</sub> | <img src="images/portrait-recipes/old-library-dust-beam/grid.webp" width="240" alt="老图书馆·光柱浮尘"><br><b>老图书馆·光柱浮尘</b><br><code>old-library-dust-beam</code><br><sub>窗口硬光斑 · 老图书馆 · 中画幅艺术肖像</sub> | <img src="images/portrait-recipes/black-studio-strobe-menswear/grid.webp" width="240" alt="黑棚硬闪·男士礼服"><br><b>黑棚硬闪·男士礼服</b><br><code>black-studio-strobe-menswear</code><br><sub>棚拍硬闪 · 纯黑背景 · 清透杂志感</sub> |
| <img src="images/portrait-recipes/film-noir-blinds/grid.webp" width="240" alt="黑色电影·百叶窗"><br><b>黑色电影·百叶窗</b><br><code>film-noir-blinds</code><br><sub>百叶窗光影 · 旧式侦探办公室 · 黑色电影</sub> | <img src="images/portrait-recipes/wheat-field-backlight/grid.webp" width="240" alt="金色麦田·逆光剪影"><br><b>金色麦田·逆光剪影</b><br><code>wheat-field-backlight</code><br><sub>逆光剪影 · 金色麦田 · 日系青春电影</sub> | <img src="images/portrait-recipes/subway-platform-bw/grid.webp" width="240" alt="深夜地铁站台·黑白"><br><b>深夜地铁站台·黑白</b><br><code>subway-platform-bw</code><br><sub>顶部荧光灯 · 地铁站台 · 黑白 Tri-X 颗粒</sub> |
| <img src="images/portrait-recipes/rooftop-blue-hour-suit/grid.webp" width="240" alt="天台蓝调·廓形西装"><br><b>天台蓝调·廓形西装</b><br><code>rooftop-blue-hour-suit</code><br><sub>蓝调时刻 · 城市天台 · 35mm 电影级时尚</sub> | <img src="images/portrait-recipes/greenhouse-pastel/grid.webp" width="240" alt="玻璃温室·植物午后"><br><b>玻璃温室·植物午后</b><br><code>greenhouse-pastel</code><br><sub>阴天散射光 · 玻璃温室 · 宝丽来拍立得</sub> | <img src="images/portrait-recipes/vintage-convertible-road-trip/grid.webp" width="240" alt="复古敞篷车·海岸公路"><br><b>复古敞篷车·海岸公路</b><br><code>vintage-convertible-road-trip</code><br><sub>金色逆光加环境补 · 复古敞篷车公路 · Ektachrome 反转片</sub> |
| <img src="images/portrait-recipes/rainy-bookshop-afternoon/grid.webp" width="240" alt="雨天旧书店·午后"><br><b>雨天旧书店·午后</b><br><code>rainy-bookshop-afternoon</code><br><sub>窗边柔光 · 旧书店 · 居家纪实胶片</sub> | <img src="images/portrait-recipes/lakeside-dock-mist/grid.webp" width="240" alt="湖边栈道·清晨薄雾"><br><b>湖边栈道·清晨薄雾</b><br><code>lakeside-dock-mist</code><br><sub>清晨薄雾光 · 湖边木栈道 · 北欧冷淡哑光</sub> | <img src="images/portrait-recipes/sculpture-museum/grid.webp" width="240" alt="古典雕塑馆·天窗光"><br><b>古典雕塑馆·天窗光</b><br><code>sculpture-museum</code><br><sub>天窗顶光 · 古典雕塑馆 · 杂志美妆大片</sub> |
| <img src="images/portrait-recipes/snowy-pine-forest/grid.webp" width="240" alt="雪地松林·红大衣"><br><b>雪地松林·红大衣</b><br><code>snowy-pine-forest</code><br><sub>雪地漫反射 · 雪地松林 · 富士 400H 淡彩</sub> | <img src="images/portrait-recipes/retro-diner-night/grid.webp" width="240" alt="美式复古餐厅·深夜"><br><b>美式复古餐厅·深夜</b><br><code>retro-diner-night</code><br><sub>室内暖钨丝灯 · 美式复古餐厅 · 港风电影色调</sub> | <img src="images/portrait-recipes/old-town-sodium-night/grid.webp" width="240" alt="老城夜巷·钠灯"><br><b>老城夜巷·钠灯</b><br><code>old-town-sodium-night</code><br><sub>钠灯路灯 · 老城夜巷 · CineStill 800T 夜景胶片</sub> |
| <img src="images/portrait-recipes/autumn-park-dappled/grid.webp" width="240" alt="秋日公园·落叶树影"><br><b>秋日公园·落叶树影</b><br><code>autumn-park-dappled</code><br><sub>树影斑驳光 · 秋日公园 · 胶片 Portra 400 随拍</sub> | <img src="images/portrait-recipes/desert-dunes-linen/grid.webp" width="240" alt="沙漠沙丘·亚麻长袍"><br><b>沙漠沙丘·亚麻长袍</b><br><code>desert-dunes-linen</code><br><sub>低角度侧硬光 · 沙漠沙丘 · 清透杂志感</sub> | <img src="images/portrait-recipes/night-train-compartment/grid.webp" width="240" alt="夜行列车·卧铺车厢"><br><b>夜行列车·卧铺车厢</b><br><code>night-train-compartment</code><br><sub>室内暖钨丝灯 · 夜行列车 · 港风电影色调</sub> |
| <img src="images/portrait-recipes/vintage-tennis-court/grid.webp" width="240" alt="老式网球场·夏日正午"><br><b>老式网球场·夏日正午</b><br><code>vintage-tennis-court</code><br><sub>正午硬光 · 老式网球场 · Ektachrome 反转片</sub> | <img src="images/portrait-recipes/candlelit-manor-hall/grid.webp" width="240" alt="古堡烛光·丝绒长裙"><br><b>古堡烛光·丝绒长裙</b><br><code>candlelit-manor-hall</code><br><sub>烛光 · 古堡烛光大厅 · 35mm 电影级时尚</sub> | <img src="images/portrait-recipes/rembrandt-plaster-portrait/grid.webp" width="240" alt="伦勃朗光·素墙经典肖像"><br><b>伦勃朗光·素墙经典肖像</b><br><code>rembrandt-plaster-portrait</code><br><sub>伦勃朗光 · 暖色素墙影棚 · 中画幅艺术肖像</sub> |

## 自己组装人像配方

`data/components.json` 是全部组件，按槽位分组；每个组件有 `id`、中英文名和真正拼进提示词的 `text`。一套配方只写组件 id：

| 槽位 | 中文 | 层级 | 内容 | 数量 |
|---|---|---|---|---|
| `look` | 质感 | 整组 | 胶片型号、调色、颗粒 | 17 |
| `skin` | 皮肤 | 整组 | 皮肤真实感 | 5 |
| `light` | 主光 | 整组 | 一套只用一种主光 | 34 |
| `light_mod` | 光的细节 | 整组·多选 | 投影、眩光、高光晕染、金边 | 26 |
| `scene` | 场景 | 整组 | 地点，只写环境 | 45 |
| `outfit` | 服装 | 整组 | 全部得体不透 | 39 |
| `hair` | 发型 | 整组 | 发型和状态 | 17 |
| `makeup` | 妆容 | 整组 | 妆容程度和唇色 | 9 |
| `motion` | 动态 | 整组·可空 | 风、动作中、拖影 | 5 |
| `props` | 道具 | 整组·多选 | 伞、书、胶片相机、老爷车…… | 27 |
| `negative` | 避免项 | 整组·多选 | 无文字、手部正常、得体、拒绝塑料皮 | 15 |
| `gaze_rule` | 看镜规则 | 整组 | 九张里几张看镜头（只用来排片） | 3 |
| `pose` | 姿势 | 逐张 | 身体姿势，带白模参考图 | 62 |
| `action` | 动作 | 逐张·可空 | 手在做什么 | 39 |
| `expression` | 表情 | 逐张 | 表情和视线 | 30 |
| `shot_size` | 景别 | 逐张 | 大远景到微距 | 11 |
| `angle` | 机位 | 逐张 | 平视、仰拍、顶拍、过肩…… | 12 |
| `placement` | 构图位置 | 逐张·可空 | 三分、居中、留白 | 8 |
| `foreground` | 前景 | 逐张·可空 | 虚化的花、雨滴玻璃、书架边 | 16 |
| `camera` | 镜头 | 逐张 | 焦段、光圈、拍法 | 16 |

「整组」的槽位一套配方只选一次，9 张共用，保证整套像同一场拍摄；「逐张」的槽位每张单独选。一个最小的配方长这样（以「东京雨夜·霓虹小巷」的第 2 张为例）：

```json
{
 "id": "my-recipe",
 "subject": "a young East Asian woman in her late twenties with long straight black hair",
 "set": {
  "look": "cinestill-800t-night",
  "skin": "real-skin-full",
  "light": "neon",
  "light_mod": [
   "wet-reflections",
   "neon-spill",
   "backlit-rain",
   "halation"
  ],
  "scene": "tokyo-rain-alley",
  "outfit": "belted-trench",
  "hair": "damp-from-rain",
  "makeup": "natural-editorial",
  "gaze_rule": "two-of-nine-glance",
  "motion": "none-sharp",
  "props": [
   "black-umbrella"
  ],
  "negative": [
   "no-text",
   "hands-ok",
   "modest",
   "anti-plastic",
   "anti-ai-illustration",
   "no-extra-people"
  ]
 },
 "shots": [
  {
   "pose": "classic-contrapposto",
   "action": "hold-umbrella",
   "expression": "gaze-out-of-frame",
   "shot_size": "full-body",
   "angle": "low-angle",
   "placement": "right-third",
   "foreground": null,
   "camera": "35mm-f2.8"
  }
 ]
}
```

存成 `my-recipe.json` 后运行 `python3 scripts/assemble.py --recipe my-recipe.json`。想换一套：把 `scene` 换成 `rooftop`、`light` 换成 `blue-hour`，同样的 9 个镜头就变成了天台蓝调时刻。写错 id 会直接报错并告诉你去 `data/components.json` 里查。

小技巧：

- 姿势里有 `pose_ref` 的会自动带上白模参考图，姿势最稳；补充姿势只有一张正面白模图，靠文字描述。
- 一套 9 张建议覆盖：1 张远景、2 张不同机位的全身、2 张中景（其中一张正侧面）、1 张中近景、1 张特写、1 张手部或道具细节、1 张过肩或遮挡的创意镜头。
- `gaze_rule` 不进提示词，只提醒你九张里安排几张看镜头。

## 姿势大全（39）

点图片打开在线页面，可以看所有机位、在 3D 里微调、直接生成。

### 站姿（9）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/classic-contrapposto?ref=github"><img src="thumbs/poses/classic-contrapposto.webp" width="140" alt="经典站姿"></a><br>经典站姿 | <a href="https://promicat.app/zh/poses/both-hands-in-hair?ref=github"><img src="thumbs/poses/both-hands-in-hair.webp" width="140" alt="双手撩发"></a><br>双手撩发 | <a href="https://promicat.app/zh/poses/hand-behind-head?ref=github"><img src="thumbs/poses/hand-behind-head.webp" width="140" alt="扶头站"></a><br>扶头站 | <a href="https://promicat.app/zh/poses/hand-to-brow-gaze-away?ref=github"><img src="thumbs/poses/hand-to-brow-gaze-away.webp" width="140" alt="抚额远望"></a><br>抚额远望 | <a href="https://promicat.app/zh/poses/arm-up-hip-out?ref=github"><img src="thumbs/poses/arm-up-hip-out.webp" width="140" alt="扬臂扭腰"></a><br>扬臂扭腰 | <a href="https://promicat.app/zh/poses/mid-step-hand-to-hair?ref=github"><img src="thumbs/poses/mid-step-hand-to-hair.webp" width="140" alt="迈步抚发"></a><br>迈步抚发 |
| <a href="https://promicat.app/zh/poses/both-arms-high?ref=github"><img src="thumbs/poses/both-arms-high.webp" width="140" alt="双臂高举"></a><br>双臂高举 | <a href="https://promicat.app/zh/poses/arms-spread-wide?ref=github"><img src="thumbs/poses/arms-spread-wide.webp" width="140" alt="双臂舒展"></a><br>双臂舒展 | <a href="https://promicat.app/zh/poses/playful-forward-lean?ref=github"><img src="thumbs/poses/playful-forward-lean.webp" width="140" alt="前倾俏皮"></a><br>前倾俏皮 |  |  |  |

### 坐姿（12）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/relaxed-lean-back-sit?ref=github"><img src="thumbs/poses/relaxed-lean-back-sit.webp" width="140" alt="慵懒后仰坐"></a><br>慵懒后仰坐 | <a href="https://promicat.app/zh/poses/side-lean-on-one-hand?ref=github"><img src="thumbs/poses/side-lean-on-one-hand.webp" width="140" alt="侧身撑手坐"></a><br>侧身撑手坐 | <a href="https://promicat.app/zh/poses/knee-up-hand-to-hair?ref=github"><img src="thumbs/poses/knee-up-hand-to-hair.webp" width="140" alt="屈膝抚发"></a><br>屈膝抚发 | <a href="https://promicat.app/zh/poses/legs-swept-to-one-side?ref=github"><img src="thumbs/poses/legs-swept-to-one-side.webp" width="140" alt="斜伸长腿"></a><br>斜伸长腿 | <a href="https://promicat.app/zh/poses/folded-forward-hand-at-ankle?ref=github"><img src="thumbs/poses/folded-forward-hand-at-ankle.webp" width="140" alt="低头抱踝"></a><br>低头抱踝 | <a href="https://promicat.app/zh/poses/chin-on-hand-thinking?ref=github"><img src="thumbs/poses/chin-on-hand-thinking.webp" width="140" alt="托腮沉思"></a><br>托腮沉思 |
| <a href="https://promicat.app/zh/poses/leaning-back-knees-to-one-side?ref=github"><img src="thumbs/poses/leaning-back-knees-to-one-side.webp" width="140" alt="侧身仰坐"></a><br>侧身仰坐 | <a href="https://promicat.app/zh/poses/knees-drawn-side-sit?ref=github"><img src="thumbs/poses/knees-drawn-side-sit.webp" width="140" alt="抱膝侧坐"></a><br>抱膝侧坐 | <a href="https://promicat.app/zh/poses/side-sit-cheek-in-hand?ref=github"><img src="thumbs/poses/side-sit-cheek-in-hand.webp" width="140" alt="侧坐托腮"></a><br>侧坐托腮 | <a href="https://promicat.app/zh/poses/seated-one-arm-raised?ref=github"><img src="thumbs/poses/seated-one-arm-raised.webp" width="140" alt="坐姿扬臂"></a><br>坐姿扬臂 | <a href="https://promicat.app/zh/poses/cross-legged-hand-at-neck?ref=github"><img src="thumbs/poses/cross-legged-hand-at-neck.webp" width="140" alt="盘坐抚颈"></a><br>盘坐抚颈 | <a href="https://promicat.app/zh/poses/seated-twist-hand-on-floor?ref=github"><img src="thumbs/poses/seated-twist-hand-on-floor.webp" width="140" alt="撑地回身"></a><br>撑地回身 |

### 跪姿（6）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/half-kneel-hand-on-knee?ref=github"><img src="thumbs/poses/half-kneel-hand-on-knee.webp" width="140" alt="单膝跪"></a><br>单膝跪 | <a href="https://promicat.app/zh/poses/kneeling-arms-raised?ref=github"><img src="thumbs/poses/kneeling-arms-raised.webp" width="140" alt="跪姿举臂"></a><br>跪姿举臂 | <a href="https://promicat.app/zh/poses/kneeling-hand-to-brow?ref=github"><img src="thumbs/poses/kneeling-hand-to-brow.webp" width="140" alt="跪姿抚额"></a><br>跪姿抚额 | <a href="https://promicat.app/zh/poses/kneeling-one-arm-up?ref=github"><img src="thumbs/poses/kneeling-one-arm-up.webp" width="140" alt="跪姿扬臂"></a><br>跪姿扬臂 | <a href="https://promicat.app/zh/poses/quiet-kneel?ref=github"><img src="thumbs/poses/quiet-kneel.webp" width="140" alt="静坐"></a><br>静坐 | <a href="https://promicat.app/zh/poses/kneeling-twist?ref=github"><img src="thumbs/poses/kneeling-twist.webp" width="140" alt="跪坐回身"></a><br>跪坐回身 |

### 卧姿（2）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/reclining-on-one-elbow?ref=github"><img src="thumbs/poses/reclining-on-one-elbow.webp" width="140" alt="侧卧倚肘"></a><br>侧卧倚肘 | <a href="https://promicat.app/zh/poses/lying-stretched-on-one-side?ref=github"><img src="thumbs/poses/lying-stretched-on-one-side.webp" width="140" alt="侧卧舒展"></a><br>侧卧舒展 |  |  |  |  |

### 蹲姿（2）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/crouch-chin-on-hand?ref=github"><img src="thumbs/poses/crouch-chin-on-hand.webp" width="140" alt="蹲坐托腮"></a><br>蹲坐托腮 | <a href="https://promicat.app/zh/poses/street-style-crouch?ref=github"><img src="thumbs/poses/street-style-crouch.webp" width="140" alt="街拍蹲姿"></a><br>街拍蹲姿 |  |  |  |  |

### 半身（8）

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/finger-to-lips?ref=github"><img src="thumbs/poses/finger-to-lips.webp" width="140" alt="竖指轻嘘"></a><br>竖指轻嘘 | <a href="https://promicat.app/zh/poses/reaching-out?ref=github"><img src="thumbs/poses/reaching-out.webp" width="140" alt="伸手邀请"></a><br>伸手邀请 | <a href="https://promicat.app/zh/poses/chin-in-cupped-hands?ref=github"><img src="thumbs/poses/chin-in-cupped-hands.webp" width="140" alt="花朵托腮"></a><br>花朵托腮 | <a href="https://promicat.app/zh/poses/self-embrace?ref=github"><img src="thumbs/poses/self-embrace.webp" width="140" alt="交叠环抱"></a><br>交叠环抱 | <a href="https://promicat.app/zh/poses/hand-to-hair-at-the-ear?ref=github"><img src="thumbs/poses/hand-to-hair-at-the-ear.webp" width="140" alt="抚发侧颜"></a><br>抚发侧颜 | <a href="https://promicat.app/zh/poses/cheeks-in-both-hands?ref=github"><img src="thumbs/poses/cheeks-in-both-hands.webp" width="140" alt="双手捧脸"></a><br>双手捧脸 |
| <a href="https://promicat.app/zh/poses/shading-eyes-arm-out?ref=github"><img src="thumbs/poses/shading-eyes-arm-out.webp" width="140" alt="遮光伸展"></a><br>遮光伸展 | <a href="https://promicat.app/zh/poses/peeking-through-fingers?ref=github"><img src="thumbs/poses/peeking-through-fingers.webp" width="140" alt="指缝偷看"></a><br>指缝偷看 |  |  |  |  |

### 补充姿势（23）

配方里常用、但还没有 3D 数据的姿势：靠墙、坐椅子、坐台阶、走路、倚栏杆、捧杯……每个只有一张正面白模图（`images/poses-extra/`），用法和上面一样。

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <img src="thumbs/poses-extra/look-back-over-shoulder.webp" width="140" alt="过肩回眸"><br>过肩回眸 | <img src="thumbs/poses-extra/back-turned-stand.webp" width="140" alt="背影站立"><br>背影站立 | <img src="thumbs/poses-extra/lean-back-wall.webp" width="140" alt="靠墙站"><br>靠墙站 | <img src="thumbs/poses-extra/lean-shoulder-wall.webp" width="140" alt="侧肩倚墙"><br>侧肩倚墙 | <img src="thumbs/poses-extra/sit-on-chair.webp" width="140" alt="端坐椅上"><br>端坐椅上 | <img src="thumbs/poses-extra/sit-chair-backwards.webp" width="140" alt="反坐椅子"><br>反坐椅子 |
| <img src="thumbs/poses-extra/sit-bed-edge.webp" width="140" alt="坐床边"><br>坐床边 | <img src="thumbs/poses-extra/sit-on-steps.webp" width="140" alt="坐台阶"><br>坐台阶 | <img src="thumbs/poses-extra/sit-at-table.webp" width="140" alt="倚桌而坐"><br>倚桌而坐 | <img src="thumbs/poses-extra/sit-window-sill.webp" width="140" alt="坐窗台"><br>坐窗台 | <img src="thumbs/poses-extra/sit-floor-against-wall.webp" width="140" alt="靠墙席地坐"><br>靠墙席地坐 | <img src="thumbs/poses-extra/walk-toward-camera.webp" width="140" alt="迎面走来"><br>迎面走来 |
| <img src="thumbs/poses-extra/walk-away.webp" width="140" alt="背身走远"><br>背身走远 | <img src="thumbs/poses-extra/walk-hand-in-pocket.webp" width="140" alt="插兜漫步"><br>插兜漫步 | <img src="thumbs/poses-extra/lying-on-back.webp" width="140" alt="平躺仰卧"><br>平躺仰卧 | <img src="thumbs/poses-extra/hands-in-pockets-stand.webp" width="140" alt="插兜站"><br>插兜站 | <img src="thumbs/poses-extra/arms-crossed-stand.webp" width="140" alt="抱臂站"><br>抱臂站 | <img src="thumbs/poses-extra/lean-on-railing.webp" width="140" alt="倚栏杆"><br>倚栏杆 |
| <img src="thumbs/poses-extra/hold-cup-standing.webp" width="140" alt="捧杯站"><br>捧杯站 | <img src="thumbs/poses-extra/lean-on-car.webp" width="140" alt="倚车"><br>倚车 | <img src="thumbs/poses-extra/standing-profile.webp" width="140" alt="侧身站立"><br>侧身站立 | <img src="thumbs/poses-extra/spin-in-place.webp" width="140" alt="原地转圈"><br>原地转圈 | <img src="thumbs/poses-extra/stairs-look-back.webp" width="140" alt="上楼回眸"><br>上楼回眸 |  |

### 只用一个姿势：你的照片 + 白模图

不想拼整套配方的话，挑一个姿势，参考图顺序是你的照片在前、白模图在后，提示词：

```text
Image 1 is the person. Image 2 is a faceless grey mannequin that shows only the pose. Make a photograph of the person from image 1: keep their exact face, facial features, skin tone, hairstyle and any distinctive features. Copy the body pose from image 2 exactly: the same position of the head, torso, arms, hands, legs and feet, and the same camera angle. Do not copy the mannequin itself: no grey skin, no bald head, no mannequin joints. They wear an elegant, modest, fully opaque ivory silk dress with long flowing fabric. Fine-art portrait photography, soft window light from the left, warm neutral plaster studio backdrop, 85 mm lens, natural skin texture, calm and graceful mood. Tasteful and fully clothed, no sheer or see-through fabric, no nudity, no text, no logo.
```

觉得白模不完全合适？到 [Promicat 姿势库](https://promicat.app/zh/poses?ref=github) 点「在 3D 里微调这个姿势」，直接拖动白模的手臂和腿，调好后一键用你的照片生成。

## 示例写真（78）

每张都用对应的白模图作为姿势参考生成，完整提示词在 `data/cases.json` 的 `prompt` 字段。

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/poses/relaxed-lean-back-sit?ref=github"><img src="thumbs/cases/relaxed-lean-back-sit-1.webp" width="140" alt="慵懒后仰坐"></a><br>慵懒后仰坐<br><sub>环形光 · 森林空地</sub> | <a href="https://promicat.app/zh/poses/relaxed-lean-back-sit?ref=github"><img src="thumbs/cases/relaxed-lean-back-sit-2.webp" width="140" alt="慵懒后仰坐"></a><br>慵懒后仰坐<br><sub>黄金时刻 · 老图书馆</sub> | <a href="https://promicat.app/zh/poses/side-lean-on-one-hand?ref=github"><img src="thumbs/cases/side-lean-on-one-hand-1.webp" width="140" alt="侧身撑手坐"></a><br>侧身撑手坐<br><sub>霓虹夜景 · 美术馆</sub> | <a href="https://promicat.app/zh/poses/side-lean-on-one-hand?ref=github"><img src="thumbs/cases/side-lean-on-one-hand-2.webp" width="140" alt="侧身撑手坐"></a><br>侧身撑手坐<br><sub>百叶窗光影 · 大理石楼梯</sub> | <a href="https://promicat.app/zh/poses/knee-up-hand-to-hair?ref=github"><img src="thumbs/cases/knee-up-hand-to-hair-1.webp" width="140" alt="屈膝抚发"></a><br>屈膝抚发<br><sub>蝴蝶光 · 暖色素墙影棚</sub> | <a href="https://promicat.app/zh/poses/knee-up-hand-to-hair?ref=github"><img src="thumbs/cases/knee-up-hand-to-hair-2.webp" width="140" alt="屈膝抚发"></a><br>屈膝抚发<br><sub>轮廓逆光 · 森林空地</sub> |
| <a href="https://promicat.app/zh/poses/legs-swept-to-one-side?ref=github"><img src="thumbs/cases/legs-swept-to-one-side-1.webp" width="140" alt="斜伸长腿"></a><br>斜伸长腿<br><sub>阴天散射光 · 城市天台</sub> | <a href="https://promicat.app/zh/poses/legs-swept-to-one-side?ref=github"><img src="thumbs/cases/legs-swept-to-one-side-2.webp" width="140" alt="斜伸长腿"></a><br>斜伸长腿<br><sub>烛光 · 美术馆</sub> | <a href="https://promicat.app/zh/poses/folded-forward-hand-at-ankle?ref=github"><img src="thumbs/cases/folded-forward-hand-at-ankle-1.webp" width="140" alt="低头抱踝"></a><br>低头抱踝<br><sub>低调暗光 · 沙漠沙丘</sub> | <a href="https://promicat.app/zh/poses/folded-forward-hand-at-ankle?ref=github"><img src="thumbs/cases/folded-forward-hand-at-ankle-2.webp" width="140" alt="低头抱踝"></a><br>低头抱踝<br><sub>分割光 · 暖色素墙影棚</sub> | <a href="https://promicat.app/zh/poses/chin-on-hand-thinking?ref=github"><img src="thumbs/cases/chin-on-hand-thinking-1.webp" width="140" alt="托腮沉思"></a><br>托腮沉思<br><sub>黄金时刻 · 海边沙滩</sub> | <a href="https://promicat.app/zh/poses/chin-on-hand-thinking?ref=github"><img src="thumbs/cases/chin-on-hand-thinking-2.webp" width="140" alt="托腮沉思"></a><br>托腮沉思<br><sub>正午硬光 · 城市天台</sub> |
| <a href="https://promicat.app/zh/poses/leaning-back-knees-to-one-side?ref=github"><img src="thumbs/cases/leaning-back-knees-to-one-side-1.webp" width="140" alt="侧身仰坐"></a><br>侧身仰坐<br><sub>百叶窗光影 · 花田</sub> | <a href="https://promicat.app/zh/poses/leaning-back-knees-to-one-side?ref=github"><img src="thumbs/cases/leaning-back-knees-to-one-side-2.webp" width="140" alt="侧身仰坐"></a><br>侧身仰坐<br><sub>伦勃朗光 · 沙漠沙丘</sub> | <a href="https://promicat.app/zh/poses/knees-drawn-side-sit?ref=github"><img src="thumbs/cases/knees-drawn-side-sit-1.webp" width="140" alt="抱膝侧坐"></a><br>抱膝侧坐<br><sub>轮廓逆光 · 雨夜街头</sub> | <a href="https://promicat.app/zh/poses/knees-drawn-side-sit?ref=github"><img src="thumbs/cases/knees-drawn-side-sit-2.webp" width="140" alt="抱膝侧坐"></a><br>抱膝侧坐<br><sub>蓝调时刻 · 海边沙滩</sub> | <a href="https://promicat.app/zh/poses/side-sit-cheek-in-hand?ref=github"><img src="thumbs/cases/side-sit-cheek-in-hand-1.webp" width="140" alt="侧坐托腮"></a><br>侧坐托腮<br><sub>烛光 · 城市街道</sub> | <a href="https://promicat.app/zh/poses/side-sit-cheek-in-hand?ref=github"><img src="thumbs/cases/side-sit-cheek-in-hand-2.webp" width="140" alt="侧坐托腮"></a><br>侧坐托腮<br><sub>高调白光 · 花田</sub> |
| <a href="https://promicat.app/zh/poses/seated-one-arm-raised?ref=github"><img src="thumbs/cases/seated-one-arm-raised-1.webp" width="140" alt="坐姿扬臂"></a><br>坐姿扬臂<br><sub>分割光 · 极简公寓</sub> | <a href="https://promicat.app/zh/poses/seated-one-arm-raised?ref=github"><img src="thumbs/cases/seated-one-arm-raised-2.webp" width="140" alt="坐姿扬臂"></a><br>坐姿扬臂<br><sub>窗边柔光 · 雨夜街头</sub> | <a href="https://promicat.app/zh/poses/cross-legged-hand-at-neck?ref=github"><img src="thumbs/cases/cross-legged-hand-at-neck-1.webp" width="140" alt="盘坐抚颈"></a><br>盘坐抚颈<br><sub>正午硬光 · 庭院花园</sub> | <a href="https://promicat.app/zh/poses/cross-legged-hand-at-neck?ref=github"><img src="thumbs/cases/cross-legged-hand-at-neck-2.webp" width="140" alt="盘坐抚颈"></a><br>盘坐抚颈<br><sub>树影斑驳光 · 城市街道</sub> | <a href="https://promicat.app/zh/poses/seated-twist-hand-on-floor?ref=github"><img src="thumbs/cases/seated-twist-hand-on-floor-1.webp" width="140" alt="撑地回身"></a><br>撑地回身<br><sub>伦勃朗光 · 咖啡馆窗边</sub> | <a href="https://promicat.app/zh/poses/seated-twist-hand-on-floor?ref=github"><img src="thumbs/cases/seated-twist-hand-on-floor-2.webp" width="140" alt="撑地回身"></a><br>撑地回身<br><sub>环形光 · 极简公寓</sub> |
| <a href="https://promicat.app/zh/poses/half-kneel-hand-on-knee?ref=github"><img src="thumbs/cases/half-kneel-hand-on-knee-1.webp" width="140" alt="单膝跪"></a><br>单膝跪<br><sub>蓝调时刻 · 老图书馆</sub> | <a href="https://promicat.app/zh/poses/half-kneel-hand-on-knee?ref=github"><img src="thumbs/cases/half-kneel-hand-on-knee-2.webp" width="140" alt="单膝跪"></a><br>单膝跪<br><sub>霓虹夜景 · 庭院花园</sub> | <a href="https://promicat.app/zh/poses/kneeling-arms-raised?ref=github"><img src="thumbs/cases/kneeling-arms-raised-1.webp" width="140" alt="跪姿举臂"></a><br>跪姿举臂<br><sub>高调白光 · 大理石楼梯</sub> | <a href="https://promicat.app/zh/poses/kneeling-arms-raised?ref=github"><img src="thumbs/cases/kneeling-arms-raised-2.webp" width="140" alt="跪姿举臂"></a><br>跪姿举臂<br><sub>蝴蝶光 · 咖啡馆窗边</sub> | <a href="https://promicat.app/zh/poses/kneeling-hand-to-brow?ref=github"><img src="thumbs/cases/kneeling-hand-to-brow-1.webp" width="140" alt="跪姿抚额"></a><br>跪姿抚额<br><sub>窗边柔光 · 森林空地</sub> | <a href="https://promicat.app/zh/poses/kneeling-hand-to-brow?ref=github"><img src="thumbs/cases/kneeling-hand-to-brow-2.webp" width="140" alt="跪姿抚额"></a><br>跪姿抚额<br><sub>阴天散射光 · 老图书馆</sub> |
| <a href="https://promicat.app/zh/poses/kneeling-one-arm-up?ref=github"><img src="thumbs/cases/kneeling-one-arm-up-1.webp" width="140" alt="跪姿扬臂"></a><br>跪姿扬臂<br><sub>树影斑驳光 · 美术馆</sub> | <a href="https://promicat.app/zh/poses/kneeling-one-arm-up?ref=github"><img src="thumbs/cases/kneeling-one-arm-up-2.webp" width="140" alt="跪姿扬臂"></a><br>跪姿扬臂<br><sub>低调暗光 · 大理石楼梯</sub> | <a href="https://promicat.app/zh/poses/quiet-kneel?ref=github"><img src="thumbs/cases/quiet-kneel-1.webp" width="140" alt="静坐"></a><br>静坐<br><sub>环形光 · 暖色素墙影棚</sub> | <a href="https://promicat.app/zh/poses/quiet-kneel?ref=github"><img src="thumbs/cases/quiet-kneel-2.webp" width="140" alt="静坐"></a><br>静坐<br><sub>黄金时刻 · 森林空地</sub> | <a href="https://promicat.app/zh/poses/kneeling-twist?ref=github"><img src="thumbs/cases/kneeling-twist-1.webp" width="140" alt="跪坐回身"></a><br>跪坐回身<br><sub>霓虹夜景 · 城市天台</sub> | <a href="https://promicat.app/zh/poses/kneeling-twist?ref=github"><img src="thumbs/cases/kneeling-twist-2.webp" width="140" alt="跪坐回身"></a><br>跪坐回身<br><sub>百叶窗光影 · 美术馆</sub> |
| <a href="https://promicat.app/zh/poses/classic-contrapposto?ref=github"><img src="thumbs/cases/classic-contrapposto-1.webp" width="140" alt="经典站姿"></a><br>经典站姿<br><sub>蝴蝶光 · 沙漠沙丘</sub> | <a href="https://promicat.app/zh/poses/classic-contrapposto?ref=github"><img src="thumbs/cases/classic-contrapposto-2.webp" width="140" alt="经典站姿"></a><br>经典站姿<br><sub>轮廓逆光 · 暖色素墙影棚</sub> | <a href="https://promicat.app/zh/poses/both-hands-in-hair?ref=github"><img src="thumbs/cases/both-hands-in-hair-1.webp" width="140" alt="双手撩发"></a><br>双手撩发<br><sub>阴天散射光 · 海边沙滩</sub> | <a href="https://promicat.app/zh/poses/both-hands-in-hair?ref=github"><img src="thumbs/cases/both-hands-in-hair-2.webp" width="140" alt="双手撩发"></a><br>双手撩发<br><sub>烛光 · 城市天台</sub> | <a href="https://promicat.app/zh/poses/hand-behind-head?ref=github"><img src="thumbs/cases/hand-behind-head-1.webp" width="140" alt="扶头站"></a><br>扶头站<br><sub>低调暗光 · 花田</sub> | <a href="https://promicat.app/zh/poses/hand-behind-head?ref=github"><img src="thumbs/cases/hand-behind-head-2.webp" width="140" alt="扶头站"></a><br>扶头站<br><sub>分割光 · 沙漠沙丘</sub> |
| <a href="https://promicat.app/zh/poses/hand-to-brow-gaze-away?ref=github"><img src="thumbs/cases/hand-to-brow-gaze-away-1.webp" width="140" alt="抚额远望"></a><br>抚额远望<br><sub>黄金时刻 · 雨夜街头</sub> | <a href="https://promicat.app/zh/poses/hand-to-brow-gaze-away?ref=github"><img src="thumbs/cases/hand-to-brow-gaze-away-2.webp" width="140" alt="抚额远望"></a><br>抚额远望<br><sub>正午硬光 · 海边沙滩</sub> | <a href="https://promicat.app/zh/poses/arm-up-hip-out?ref=github"><img src="thumbs/cases/arm-up-hip-out-1.webp" width="140" alt="扬臂扭腰"></a><br>扬臂扭腰<br><sub>百叶窗光影 · 城市街道</sub> | <a href="https://promicat.app/zh/poses/arm-up-hip-out?ref=github"><img src="thumbs/cases/arm-up-hip-out-2.webp" width="140" alt="扬臂扭腰"></a><br>扬臂扭腰<br><sub>伦勃朗光 · 花田</sub> | <a href="https://promicat.app/zh/poses/mid-step-hand-to-hair?ref=github"><img src="thumbs/cases/mid-step-hand-to-hair-1.webp" width="140" alt="迈步抚发"></a><br>迈步抚发<br><sub>轮廓逆光 · 极简公寓</sub> | <a href="https://promicat.app/zh/poses/mid-step-hand-to-hair?ref=github"><img src="thumbs/cases/mid-step-hand-to-hair-2.webp" width="140" alt="迈步抚发"></a><br>迈步抚发<br><sub>蓝调时刻 · 雨夜街头</sub> |
| <a href="https://promicat.app/zh/poses/both-arms-high?ref=github"><img src="thumbs/cases/both-arms-high-1.webp" width="140" alt="双臂高举"></a><br>双臂高举<br><sub>烛光 · 庭院花园</sub> | <a href="https://promicat.app/zh/poses/both-arms-high?ref=github"><img src="thumbs/cases/both-arms-high-2.webp" width="140" alt="双臂高举"></a><br>双臂高举<br><sub>高调白光 · 城市街道</sub> | <a href="https://promicat.app/zh/poses/arms-spread-wide?ref=github"><img src="thumbs/cases/arms-spread-wide-1.webp" width="140" alt="双臂舒展"></a><br>双臂舒展<br><sub>分割光 · 咖啡馆窗边</sub> | <a href="https://promicat.app/zh/poses/arms-spread-wide?ref=github"><img src="thumbs/cases/arms-spread-wide-2.webp" width="140" alt="双臂舒展"></a><br>双臂舒展<br><sub>窗边柔光 · 极简公寓</sub> | <a href="https://promicat.app/zh/poses/playful-forward-lean?ref=github"><img src="thumbs/cases/playful-forward-lean-1.webp" width="140" alt="前倾俏皮"></a><br>前倾俏皮<br><sub>正午硬光 · 老图书馆</sub> | <a href="https://promicat.app/zh/poses/playful-forward-lean?ref=github"><img src="thumbs/cases/playful-forward-lean-2.webp" width="140" alt="前倾俏皮"></a><br>前倾俏皮<br><sub>树影斑驳光 · 庭院花园</sub> |
| <a href="https://promicat.app/zh/poses/reclining-on-one-elbow?ref=github"><img src="thumbs/cases/reclining-on-one-elbow-1.webp" width="140" alt="侧卧倚肘"></a><br>侧卧倚肘<br><sub>伦勃朗光 · 大理石楼梯</sub> | <a href="https://promicat.app/zh/poses/reclining-on-one-elbow?ref=github"><img src="thumbs/cases/reclining-on-one-elbow-2.webp" width="140" alt="侧卧倚肘"></a><br>侧卧倚肘<br><sub>环形光 · 咖啡馆窗边</sub> | <a href="https://promicat.app/zh/poses/lying-stretched-on-one-side?ref=github"><img src="thumbs/cases/lying-stretched-on-one-side-1.webp" width="140" alt="侧卧舒展"></a><br>侧卧舒展<br><sub>蓝调时刻 · 森林空地</sub> | <a href="https://promicat.app/zh/poses/lying-stretched-on-one-side?ref=github"><img src="thumbs/cases/lying-stretched-on-one-side-2.webp" width="140" alt="侧卧舒展"></a><br>侧卧舒展<br><sub>霓虹夜景 · 老图书馆</sub> | <a href="https://promicat.app/zh/poses/crouch-chin-on-hand?ref=github"><img src="thumbs/cases/crouch-chin-on-hand-1.webp" width="140" alt="蹲坐托腮"></a><br>蹲坐托腮<br><sub>高调白光 · 美术馆</sub> | <a href="https://promicat.app/zh/poses/crouch-chin-on-hand?ref=github"><img src="thumbs/cases/crouch-chin-on-hand-2.webp" width="140" alt="蹲坐托腮"></a><br>蹲坐托腮<br><sub>蝴蝶光 · 大理石楼梯</sub> |
| <a href="https://promicat.app/zh/poses/street-style-crouch?ref=github"><img src="thumbs/cases/street-style-crouch-1.webp" width="140" alt="街拍蹲姿"></a><br>街拍蹲姿<br><sub>窗边柔光 · 暖色素墙影棚</sub> | <a href="https://promicat.app/zh/poses/street-style-crouch?ref=github"><img src="thumbs/cases/street-style-crouch-2.webp" width="140" alt="街拍蹲姿"></a><br>街拍蹲姿<br><sub>阴天散射光 · 森林空地</sub> | <a href="https://promicat.app/zh/poses/finger-to-lips?ref=github"><img src="thumbs/cases/finger-to-lips-1.webp" width="140" alt="竖指轻嘘"></a><br>竖指轻嘘<br><sub>树影斑驳光 · 城市天台</sub> | <a href="https://promicat.app/zh/poses/finger-to-lips?ref=github"><img src="thumbs/cases/finger-to-lips-2.webp" width="140" alt="竖指轻嘘"></a><br>竖指轻嘘<br><sub>低调暗光 · 美术馆</sub> | <a href="https://promicat.app/zh/poses/reaching-out?ref=github"><img src="thumbs/cases/reaching-out-1.webp" width="140" alt="伸手邀请"></a><br>伸手邀请<br><sub>环形光 · 沙漠沙丘</sub> | <a href="https://promicat.app/zh/poses/reaching-out?ref=github"><img src="thumbs/cases/reaching-out-2.webp" width="140" alt="伸手邀请"></a><br>伸手邀请<br><sub>黄金时刻 · 暖色素墙影棚</sub> |
| <a href="https://promicat.app/zh/poses/chin-in-cupped-hands?ref=github"><img src="thumbs/cases/chin-in-cupped-hands-1.webp" width="140" alt="花朵托腮"></a><br>花朵托腮<br><sub>霓虹夜景 · 海边沙滩</sub> | <a href="https://promicat.app/zh/poses/chin-in-cupped-hands?ref=github"><img src="thumbs/cases/chin-in-cupped-hands-2.webp" width="140" alt="花朵托腮"></a><br>花朵托腮<br><sub>百叶窗光影 · 城市天台</sub> | <a href="https://promicat.app/zh/poses/self-embrace?ref=github"><img src="thumbs/cases/self-embrace-1.webp" width="140" alt="交叠环抱"></a><br>交叠环抱<br><sub>蝴蝶光 · 花田</sub> | <a href="https://promicat.app/zh/poses/self-embrace?ref=github"><img src="thumbs/cases/self-embrace-2.webp" width="140" alt="交叠环抱"></a><br>交叠环抱<br><sub>轮廓逆光 · 沙漠沙丘</sub> | <a href="https://promicat.app/zh/poses/hand-to-hair-at-the-ear?ref=github"><img src="thumbs/cases/hand-to-hair-at-the-ear-1.webp" width="140" alt="抚发侧颜"></a><br>抚发侧颜<br><sub>阴天散射光 · 雨夜街头</sub> | <a href="https://promicat.app/zh/poses/hand-to-hair-at-the-ear?ref=github"><img src="thumbs/cases/hand-to-hair-at-the-ear-2.webp" width="140" alt="抚发侧颜"></a><br>抚发侧颜<br><sub>烛光 · 海边沙滩</sub> |
| <a href="https://promicat.app/zh/poses/cheeks-in-both-hands?ref=github"><img src="thumbs/cases/cheeks-in-both-hands-1.webp" width="140" alt="双手捧脸"></a><br>双手捧脸<br><sub>低调暗光 · 城市街道</sub> | <a href="https://promicat.app/zh/poses/cheeks-in-both-hands?ref=github"><img src="thumbs/cases/cheeks-in-both-hands-2.webp" width="140" alt="双手捧脸"></a><br>双手捧脸<br><sub>分割光 · 花田</sub> | <a href="https://promicat.app/zh/poses/shading-eyes-arm-out?ref=github"><img src="thumbs/cases/shading-eyes-arm-out-1.webp" width="140" alt="遮光伸展"></a><br>遮光伸展<br><sub>黄金时刻 · 极简公寓</sub> | <a href="https://promicat.app/zh/poses/shading-eyes-arm-out?ref=github"><img src="thumbs/cases/shading-eyes-arm-out-2.webp" width="140" alt="遮光伸展"></a><br>遮光伸展<br><sub>正午硬光 · 雨夜街头</sub> | <a href="https://promicat.app/zh/poses/peeking-through-fingers?ref=github"><img src="thumbs/cases/peeking-through-fingers-1.webp" width="140" alt="指缝偷看"></a><br>指缝偷看<br><sub>百叶窗光影 · 庭院花园</sub> | <a href="https://promicat.app/zh/poses/peeking-through-fingers?ref=github"><img src="thumbs/cases/peeking-through-fingers-2.webp" width="140" alt="指缝偷看"></a><br>指缝偷看<br><sub>伦勃朗光 · 城市街道</sub> |

## 光影（16）

把「提示词」一栏直接放进你的提示词。

| 示例 | 光影 | 提示词 |
|---|---|---|
| <img src="thumbs/lights/rembrandt.webp" width="110"> | **伦勃朗光**<br>Rembrandt light | `one soft key light high at 45 degrees to the side, a small triangle of light on the shadow-side cheek, dark moody background` |
| <img src="thumbs/lights/butterfly.webp" width="110"> | **蝴蝶光**<br>Butterfly light | `key light high and straight in front of the face, a small butterfly-shaped shadow under the nose, even glamorous light` |
| <img src="thumbs/lights/split.webp" width="110"> | **分割光**<br>Split light | `hard light from exactly 90 degrees to one side, half of the face lit and half in shadow, dramatic` |
| <img src="thumbs/lights/loop.webp" width="110"> | **环形光**<br>Loop light | `key light slightly above and 30 degrees to the side, a small loop shadow from the nose on the cheek, natural flattering light` |
| <img src="thumbs/lights/rim.webp" width="110"> | **轮廓逆光**<br>Rim backlight | `strong light from behind outlining the hair and shoulders with a glowing rim, face softly filled, dark background` |
| <img src="thumbs/lights/window.webp" width="110"> | **窗边柔光**<br>Window light | `large soft daylight from a window on one side, gentle falloff into shadow, calm indoor mood` |
| <img src="thumbs/lights/golden-hour.webp" width="110"> | **黄金时刻**<br>Golden hour | `low warm sunset sun from behind and to the side, golden glow and lens flare, warm outdoor mood` |
| <img src="thumbs/lights/blue-hour.webp" width="110"> | **蓝调时刻**<br>Blue hour | `deep blue twilight sky after sunset, cool ambient light with warm city lights in the background` |
| <img src="thumbs/lights/overcast.webp" width="110"> | **阴天散射光**<br>Overcast soft light | `soft shadowless light from a cloudy sky, natural muted colours, outdoors` |
| <img src="thumbs/lights/hard-sun.webp" width="110"> | **正午硬光**<br>Hard midday sun | `bright high midday sun, crisp hard shadows, saturated summer colours, outdoors` |
| <img src="thumbs/lights/neon.webp" width="110"> | **霓虹夜景**<br>Neon night | `magenta and cyan neon signs lighting her from both sides at night, wet reflective street, cinematic` |
| <img src="thumbs/lights/candle.webp" width="110"> | **烛光**<br>Candlelight | `warm flickering candlelight from below and in front, deep dark surroundings, intimate mood` |
| <img src="thumbs/lights/dappled.webp" width="110"> | **树影斑驳光**<br>Dappled light | `sunlight through tree leaves making dappled spots of light and shadow on her and the ground` |
| <img src="thumbs/lights/blinds.webp" width="110"> | **百叶窗光影**<br>Venetian blind shadows | `hard sunlight through venetian blinds casting striped shadows across her and the wall` |
| <img src="thumbs/lights/high-key.webp" width="110"> | **高调白光**<br>High key | `bright, even, almost shadowless light on a pure white background, airy and clean` |
| <img src="thumbs/lights/low-key.webp" width="110"> | **低调暗光**<br>Low key | `a single narrow light on a black background, most of the frame in deep shadow, chiaroscuro` |

## 场景（14）

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| <img src="thumbs/scenes/plaster-studio.webp" width="140" alt="暖色素墙影棚"><br>暖色素墙影棚<br><sub>warm neutral plaster studio backdrop</sub> | <img src="thumbs/scenes/beach.webp" width="140" alt="海边沙滩"><br>海边沙滩<br><sub>an empty sunlit beach with soft waves</sub> | <img src="thumbs/scenes/city-street.webp" width="140" alt="城市街道"><br>城市街道<br><sub>a quiet European city street</sub> | <img src="thumbs/scenes/cafe.webp" width="140" alt="咖啡馆窗边"><br>咖啡馆窗边<br><sub>a cosy café by the window</sub> | <img src="thumbs/scenes/forest.webp" width="140" alt="森林空地"><br>森林空地<br><sub>a green forest clearing</sub> | <img src="thumbs/scenes/rooftop.webp" width="140" alt="城市天台"><br>城市天台<br><sub>a city rooftop with a skyline view</sub> | <img src="thumbs/scenes/flower-field.webp" width="140" alt="花田"><br>花田<br><sub>a wide field of wildflowers</sub> |
| <img src="thumbs/scenes/apartment.webp" width="140" alt="极简公寓"><br>极简公寓<br><sub>a minimal bright apartment with linen curtains</sub> | <img src="thumbs/scenes/library.webp" width="140" alt="老图书馆"><br>老图书馆<br><sub>an old library with tall wooden bookshelves</sub> | <img src="thumbs/scenes/gallery.webp" width="140" alt="美术馆"><br>美术馆<br><sub>a white art gallery with large paintings</sub> | <img src="thumbs/scenes/desert.webp" width="140" alt="沙漠沙丘"><br>沙漠沙丘<br><sub>golden sand dunes in a desert</sub> | <img src="thumbs/scenes/rainy-street.webp" width="140" alt="雨夜街头"><br>雨夜街头<br><sub>a rainy street with reflections on the pavement</sub> | <img src="thumbs/scenes/garden.webp" width="140" alt="庭院花园"><br>庭院花园<br><sub>a formal garden with stone paths and hedges</sub> | <img src="thumbs/scenes/staircase.webp" width="140" alt="大理石楼梯"><br>大理石楼梯<br><sub>a sweeping marble staircase</sub> |

## Promicat 配方案例

这些写真玩法在 Promicat 上有现成的配方，上传照片就能做。

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| <a href="https://promicat.app/zh/recipes/professional-headshot?ref=github"><img src="https://promicat.app/api/media/recipe/professional-headshot-sample-01?w=640" width="140" alt="自拍变职业头像"></a><br>自拍变职业头像 | <a href="https://promicat.app/zh/recipes/lifestyle-profile-photo?ref=github"><img src="https://promicat.app/api/media/recipe/lifestyle-profile-photo-sample-01?w=640" width="140" alt="生活感头像照"></a><br>生活感头像照 | <a href="https://promicat.app/zh/recipes/animated-family-portrait?ref=github"><img src="https://promicat.app/api/media/recipe/animated-family-portrait-sample-01?w=640" width="140" alt="3D 动画全家福"></a><br>3D 动画全家福 | <a href="https://promicat.app/zh/recipes/royal-pet-portrait?ref=github"><img src="https://promicat.app/api/media/recipe/royal-pet-portrait-sample-01?w=640" width="140" alt="皇家宠物肖像"></a><br>皇家宠物肖像 | <a href="https://promicat.app/zh/recipes/holiday-pet-photo?ref=github"><img src="https://promicat.app/api/media/recipe/holiday-pet-photo-sample-01?w=640" width="140" alt="节日宠物照"></a><br>节日宠物照 | <a href="https://promicat.app/zh/recipes/product-lifestyle-scene?ref=github"><img src="https://promicat.app/api/media/recipe/product-lifestyle-scene-sample-01?w=640" width="140" alt="产品生活场景图"></a><br>产品生活场景图 |

## Promi 特别篇

Promicat 的吉祥物 Promi 也把这些姿势和光影拍了一遍（55 张），在 `images/promi/`。

## 数据格式

| 文件 | 内容 |
| --- | --- |
| `data/photo-poses.json` | 200 组写真姿势：风格、姿势名和分类、动作描述（`pose_text`）、全身或半身（`framing`）、写真照（`photo`）、白模（`pose`）、在线页面（`url`）、示例提示词、「用你的照片」提示词 |
| `data/portrait-recipes.json` | 24 套人像写真配方：用了哪些组件、每张的组件 id、样片、两版完整提示词、姿势参考图 |
| `data/components.json` | 人像组件库：20 个槽位、436 个组件，姿势组件带白模图 |
| `data/poses.json` | 姿势：中英文名、分类、各机位白模图、3D 姿势数据（`pose3d`）、在线页面 |
| `data/lights.json` | 光影：中英文名、提示词描述、示例图和示例提示词 |
| `data/scenes.json` | 场景：中英文名、示例图和示例提示词 |
| `data/cases.json` | 示例写真：用了哪个姿势、光影、场景、服装，完整提示词和姿势参考图 |
| `data/recipes.json` | Promicat 上相关的配方 |
| `data/templates.json` | 「你的照片 + 白模图」通用提示词 |

`pose3d` 是 Promicat 3D 白模的姿势格式 v1：`{"v": 1, "rot": {"关节": [x, y, z]}}`，单位是度，XYZ 顺序，相对站立静止姿势；没写的关节保持静止。

## Agent Skill

两个技能，复制到你的 Agent（Claude Code、Codex 等）的技能目录即可：

- **`skills/photo-pose-match`：照片配姿势**。用户发来自己的照片，Agent 看照片的穿着、气质和画面风格，从 200 组写真姿势里挑出适合的几组并说明理由，再用「用户照片 + 白模」直接生成写真；没有生图工具时给出 Promicat 页面链接，可以一键生成。只装这个技能、不克隆仓库也能用（`recommend.py --remote` 会从 GitHub 读取数据）。

  <img src="images/skill-demo.webp" width="540" alt="照片配姿势示例：用户照片、白模、生成结果">

  <sub>左：用户照片（示例人物为 AI 生成的虚构人物）　中：技能挑出的白模　右：生成结果。上面一组换成了港风复古的服装，下面一组用 `--keep-outfit` 保留了原来的衣服。</sub>

  ```bash
  python3 skills/photo-pose-match/recommend.py --list-styles
  python3 skills/photo-pose-match/recommend.py --style street,hkretro --group stand,lean --limit 6
  python3 skills/photo-pose-match/recommend.py --id sp101 --keep-outfit   # 保留用户自己的衣服
  ```
- **`skills/ai-photo-poses`：写真配方和姿势大全**。按需求套用或组装整套写真配方、挑姿势、拼好提示词，并给出参考图路径。

## 协议与来源

- 代码（`scripts/`、Skill）：MIT。
- 图片和数据：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans)。使用时请注明「来自 Promicat（promicat.app）」。
- 白模姿势图大部分来自 [Shisei](https://github.com/wquguru/shisei) 的 CC0 素材，部分机位由 Promicat 重绘；写真姿势的写真照和白模、补充姿势白模图、配方样片、示例写真、光影和场景图由 Promicat 用 AI 生成，人物均为虚构。
- 请不要用这些素材冒充他人或制作误导性内容。

## 关于 Promicat

[Promicat](https://promicat.app?ref=github) 是 AI 创作配方平台：把好看的 AI 作品做成能一键复刻的配方。姿势库、3D 微调、写真生成都在这里。
