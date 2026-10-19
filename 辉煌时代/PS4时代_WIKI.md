# PS4 时代 Wiki

> 说明：本文为面向中文读者整理的「PS4 时代」机种史 / 平台史概览。整理范围为索尼互动娱乐（SIE）的 PlayStation 4 主机家族——初代 PS4、PS4 Slim、PS4 Pro，以及同代配套的 PlayStation VR——从 2013 年 2 月公布、同年 11 月首发，到 2020 年 11 月 PlayStation 5 上市、2022 年索尼停止单独公布 PS4 出货量的这段历史；同时涉及第一方工作室群在这一代成形的内容体系、PlayStation Store 与 PlayStation Plus 的运作方式、以 SHARE 键为中心的分享与直播功能，以及中国大陆自 2014 年解除游戏机禁令之后的国行与港版经验。主要依据为 SIE 官方新闻稿、PlayStation.Blog、Sony 投资者关系业务数据页，以及 Digital Foundry、Ars Technica、Polygon、GameSpot、Famitsu 等媒体的公开记录。PS4 作为主力销售机型已经退场，本世代已经结束，本文按已结束的时代书写，不作前瞻判断。检索时间：2026 年 10 月。

:::epigraph
十一月中旬的夜里，客厅的电视被一根 HDMI 线整整齐齐地连上，墙脚那根网线不再只属于电脑。
手柄正中间多出一颗按键，按下去，刚才的几分钟被存成一段可以发出去的录像。
新光盘塞进光驱，安装条走一遍，补丁再走一遍，之后才轮到标题画面。
商店里那排打折的绿色数字，比货架上的塑料盒更快地告诉人这一年游戏是怎么被卖出去的。
到这一代的末尾，同一台机器已经换过两副身板，旧机器里的每一次通关，都随着一个账号搬进了新机器。
:::

---

## 1. 时代概览

PlayStation 4 在 2013 年 11 月 15 日于北美首发，2013 年 11 月 29 日进入欧洲、拉丁美洲与澳大利亚，2014 年 2 月 22 日才在日本上市。它的官方生命周期总量停在了 1.172 亿台（索尼 2022 年 3 月口径，之后不再单独公布），是 PlayStation 2 之后销量最高的家用主机，也是同代对手 Xbox One 约 5800 万台的两倍量级。索尼财报里的年度出货曲线能看出这台机器的节奏：2013 财年出货 760 万台，随后三个财年分别为 1480 万、1770 万、2000 万台，2016 财年是峰值；2017 财年起回落，到 2020 财年只剩 570 万台，2021 财年 100 万台。数字本身只说明结果。这一代值得单独成篇的地方在于：主机平台作为一门生意、一套开发者基础设施、一个社交与直播入口、一条数字发行渠道的整套做法，在 PS4 这七年里第一次被完整地跑顺，并被后来的机器逐条继承。

PS4 要处理的第一件事发生在 2007 年前后。PlayStation 3 的 Cell 处理器性能强悍，代价是开发者要花大量精力去研究一套非常规的多核编程模型，跨平台移植格外吃力。PS4 的首席架构师 Mark Cerny 在多次受访中给出的说法很直接：这一代的目标是不让硬件变成开发者必须解开的谜题。最终方案是 AMD 定制的单芯片 APU，八个 x86-64「Jaguar」核心加一颗 1.84 TFLOPS 的 Radeon 图形核心，8GB GDDR5 统一内存，CPU 与 GPU 共用同一块内存池。这套结构在纸面上就是一台被强化过的 PC，跨平台移植的成本被压到这一代三台主机里最低的水平。

第二件事发生在 2013 年 E3。微软为 Xbox One 设计了强制联网与二手游戏限制，舆论反弹剧烈。索尼在 6 月 10 日的发布会上由时任 SCEA 总裁 Jack Tretton 宣布 PS4 不对二手游戏设限、不要求定时联网，定价 399 美元，比 Xbox One 低 100 美元；现场还放了一条 21 秒的「如何借游戏给朋友」教学短片——把光盘递给对方。微软在 6 月 19 日撤回了这套 DRM 方案。价格与政策在这次交锋里把两家的起跑线拉开了距离，而这段距离此后基本没有再被抹平。

第三处变化来自功能层面。DualShock 4 在方向键与功能键之间加了一颗 SHARE 键，把录制、截图、上传、直播收进一个按键；系统内置的社交功能把 Twitch、Ustream、YouTube 的直播入口直接做进主机；PlayStation Plus 从这一代起成为联机对战的付费前提；PlayStation Store 成为与实体零售并列的主渠道；2016 年一年之内，同一代主机先出了更薄更便宜的 Slim，再出了性能翻倍的 Pro，这是 PlayStation 历史上第一次在生命周期中段推出更高端机型。直播、订阅、数字商店、同代分层，这四件事此后成了行业默认配置。

## 2. 时代时间线

### 2.1 2007–2013：从 PS3 复盘到押注 x86

Cerny 把 PS4 的起点追到 2007 年年底。那段时间索尼电脑娱乐内部对 PS3 做复盘，他在感恩节假期读了一本讲 x86 架构历史的书，判断到 PS4 上市时 x86 已经足够强。2013 年 2 月 20 日，索尼在纽约举行「PlayStation Meeting 2013」，正式公布 PS4：x86-64 八核 CPU、1.84 TFLOPS 的 Radeon GPU、8GB GDDR5 统一内存，内置硬盘与 Blu-ray 光驱，DualShock 4 手柄带触摸板、光条与 SHARE 键。原定 4GB 内存的传闻最终被 8GB 取代，据当时报道，不少在做 PS4 项目的开发者事先并不知情。同场还谈到 Gaikai 的云游戏方向，并公布了由 Cerny 参与制作的《Knack》。

### 2.2 2013–2014：首发、政策交锋与第一年

2013 年 6 月 10 日的 E3 发布会上，索尼确认 PS4 售价 399 美元、不限制二手游戏、不要求定期联网，并播放了那条 21 秒的借盘教学短片。微软于 6 月 19 日宣布放弃 Xbox One 的强制联网与二手限制方案。11 月 15 日，PS4 在北美开卖，24 小时内售出超过 100 万台，创下当时家用主机首发最快纪录；11 月 29 日进入欧洲等地。首发阵容里，索尼自家独占只有《Killzone Shadow Fall》（Guerrilla Games）与《Knack》（日本工作室），外加数字发行的《Resogun》（Housemarque），其余靠《Assassin's Creed IV: Black Flag》《Battlefield 4》《Call of Duty: Ghosts》《FIFA 14》等第三方跨平台作品撑场面。

主机在上市同日还需要一个约 300MB 的首日补丁（系统软件 1.50）才能补齐部分功能，这件事本身成了这一代「机器不联网就不完整」的开端。同期确认的信息是：PS4 联机对战需要 PlayStation Plus 订阅，索尼自此把上一代免费的网络对战改成付费项，同时继续以每月免费游戏维持订阅吸引力。2014 年 2 月 22 日 PS4 进入日本，售价 39980 日元（不含税）/41979 日元（含税）。同年前后，索尼公布 PlayStation Now 云游戏服务，用串流方式让 PS4 运行 PS3 作品。这一年的大作还包括《inFamous Second Son》（Sucker Punch）与《Driveclub》（Evolution Studios），年底《Grand Theft Auto V》登陆 PS4。

### 2.3 2015–2016：内容补齐与同代分层

2015 年 3 月的系统更新 2.50「Yukimura」加入挂起/恢复功能，玩家把正在进行的游戏存进 Rest Mode，开机即回到原位，这一代主机「随开随玩」的体验由此定型。同年发售的作品包括《Bloodborne》（FromSoftware 与日本工作室合作，2015 年 3 月 24 日）、《The Order: 1886》、《Until Dawn》；2016 年则是《Uncharted 4: A Thief's End》（5 月 10 日，Naughty Dog）、《Ratchet & Clank》（Insomniac）与《The Last Guardian》（12 月，日本工作室）的一年。

硬件层面，2016 年 9 月 7 日的「PlayStation Meeting 2016」发布两款新机型。PS4 Slim（型号 CUH-2000）9 月 15 日上市，299 美元 / 29980 日元 / 299 欧元 / 259 英镑，取消光纤音频口，机身与功耗下降但性能与初代一致，成为新的标准机型。PS4 Pro（型号 CUH-7000）11 月 10 日上市，399 美元 / 44980 日元，CPU 提升到约 2.1GHz、GPU 4.2 TFLOPS（36 个 GCN 计算单元）、内存带宽约 218GB/s 并额外加 1GB DDR3 供系统使用，主推 4K 输出与 HDR，索尼官方称这是 PlayStation 历史上第一次在生命周期中段推出更高端主机。10 月 13 日，PlayStation VR 以 399 美元发售，需配合 PS4 与 PlayStation Camera 使用。

### 2.4 2017–2020：第一方工业化与世代收尾

2017 年起，索尼第一方的产出密度进入高点：《Horizon Zero Dawn》（Guerrilla）2 月发售，一年内销量突破 760 万；《Persona 5》（Atlus）、《NieR: Automata》（白金工作室 / Square Enix）、《Yakuza》系列新作等日式作品也集中在 PS4 上。2018 年 4 月 20 日《God of War》（Santa Monica Studio）发售，三天售出约 310 万套；9 月 7 日《Marvel's Spider-Man》（Insomniac）三天售出 330 万套，成为当时索尼第一方的最快销售纪录。2019 年 8 月，索尼宣布收购 Insomniac Games，交易金额约 2.29 亿美元，这家长期为 PlayStation 做独占的工作室正式并入 SIE 全球工作室体系。

2020 年 6 月 19 日《The Last of Us Part II》（Naughty Dog）发售，三天售出 400 万套；7 月《Ghost of Tsushima》（Sucker Punch）发售。索尼在 2020 年 1 月公布，PlayStation Network 的月活跃用户达到 1.03 亿，其中超过三分之一订阅 PlayStation Plus。2020 年 11 月 PlayStation 5 上市，向下兼容 PS4 游戏与存档，世代完成交接。2022 年 8 月，索尼在财报中给出 PS4 的最终出货口径 1.172 亿台，并停止单独披露，这台机器的生命周期到此收束。

## 3. 基础信息速览

### 3.1 平台基本参数

| 项目 | 内容 |
| --- | --- |
| 平台名称 | PlayStation 4（PS4） |
| 讨论范围 | 初代 PS4 / PS4 Slim（CUH-2000）/ PS4 Pro（CUH-7000）/ PlayStation VR |
| 时代跨度 | 2013 年 2 月公布，2013 年 11 月首发，2020 年 PS5 接棒，2022 年停止单独披露出货量 |
| 平台属性 | 第八世代家用游戏机；x86-64 架构、AMD 定制 APU |
| 主要载体 | Blu-ray 光盘（BD 6x CAV）、内置硬盘（首发 500GB，Slim 500GB、Pro 1TB）、PlayStation Store 数字发行 |
| 关键规格 | 8 核 x86-64 AMD「Jaguar」CPU（初代约 1.6GHz）；GPU 1.84 TFLOPS / 18 个计算单元；8GB GDDR5 统一内存，176GB/s；Pro 为 4.2 TFLOPS / 36 单元、约 2.1GHz CPU、218GB/s |
| 官方销量口径 | 1.172 亿台（Sony IR，截至 2022 年 3 月，之后不再单独公布） |
| 历史定位 | 把数字商店、订阅制、社交分享与同代分层整理成行业默认配置的一代；PlayStation 品牌由 PS3 的被动转为压倒性领先 |

### 3.2 历史定位速写

| 维度 | 印象 |
| --- | --- |
| 技术印象 | 放弃 PS3 的 Cell 转向 x86-64 与统一内存，开发门槛降低，跨平台移植成本在这次三台主机中最低 |
| 市场印象 | 依靠 399 美元定价、不限制二手与不强制联网，在 2013 年与 Xbox One 的交锋中占先，并保持到世代结束 |
| 软件印象 | 第一方工业化产出稳定，Naughty Dog、Santa Monica、Guerrilla、Insomniac、Sucker Punch 各有代表作；日式与欧美第三方覆盖面广 |
| 玩家文化 | SHARE 键把录屏、截图、直播变成日常动作；数字商店打折、会免游戏与奖杯体系构成新的消费与社交习惯 |
| 历史评价 | 索尼在主机业务上的强势回归代；平台模板被后续机器沿用，争议集中在付费联机、首日补丁与中后期数字发行挤压实体渠道 |

### 3.3 关键词

x86-64、AMD Jaguar、8GB GDDR5 统一内存、Mark Cerny、DualShock 4、SHARE 键、Share Play、PlayStation Plus、PlayStation Store、Twitch 直播、PlayStation VR、PS4 Slim、PS4 Pro、4K 与 HDR、棋盘渲染、向下兼容、1.172 亿台、国行、锁区、备份还原、港服。

## 4. 技术与硬件

PS4 的核心是一颗 AMD 定制的单芯片 APU，由台积电 28nm 工艺制造，CPU、GPU、内存控制器与视频编解码单元集成在同一块硅片上。CPU 是两组四核的 AMD「Jaguar」模块，共八核，初代主频约 1.6GHz，每组共享 2MB 二级缓存，理论峰值约 102.4 GFLOPS。GPU 属于 AMD Radeon 的 GCN 架构，18 个计算单元、1152 个流处理器，800MHz，理论峰值 1.84 TFLOPS，可由开发者自由分配给图形、物理模拟或二者混合。内存是 8GB GDDR5，256 位总线，带宽 176GB/s，CPU 与 GPU 共用同一地址空间，无需在两块独立内存之间搬运数据。

把这套规格与 PS3 对照，能看清这一代的设计取舍。PS3 的 Cell 是一颗性能可观但结构特殊的处理器，开发者要投入额外精力才能榨出性能；PS3 的内存是 256MB XDR 系统内存加 256MB GDDR3 显存，合计 512MB，且两块分开。PS4 把内存扩到 8GB 并合并为一块统一池，Cerny 的说法是，PC 上即便有 8GB 内存，单帧内 CPU 与 GPU 能共享的比例也受 PCIe 速度限制，主机上的统一内存让开发者「上手第一天」就能拿到好处。他还提到，团队曾考虑过把总线压到 128 位、换取片上 eDRAM 的方案，最终因会给开发者增加复杂度而放弃。这种把「不让开发者解谜」写进架构的做法，是 PS4 软件开发成本下降的直接原因，也解释了为什么这一代跨平台作品在 PS4 上的移植质量普遍稳定。

除主芯片外，PS4 里还有若干颗次要定制芯片，专门负责下载、上传与社交功能的后台处理。这带来两个具体能力：数字版游戏可以在下载未完成时先行游玩；主机处于 Rest Mode 时也能在后台完成下载与上传。DualShock 4 相对 DualShock 3 增加了触摸板、后部光条与 SHARE 键，光条配合 PlayStation Camera 做体感追踪。初代 PS4 的接口包括 SuperSpeed USB 3.0、HDMI、光纤数字音频输出与以太网口；Blu-ray 光驱为 6x CAV，DVD 为 8x CAV。

两款同代机型的差异集中在性能与形态。PS4 Slim 沿用初代的计算规格，机身更小、功耗更低，去掉光纤音频口，作为新的标准机型压低入门价格。PS4 Pro 把 GPU 计算单元翻倍到 36 个、频率提到 911MHz，浮点算力 4.2 TFLOPS（16 位半精度运算下可达约 8.4 TFLOPS），CPU 频率提升到约 2.1GHz，内存带宽约 218GB/s，并额外加入 1GB DDR3 用于把非游戏应用从 GDDR5 中换出。运行普通 PS4 游戏时，Pro 会关闭一半计算单元并回落到初代频率以保持兼容。4K 输出方面，原生 2160p、几何渲染与棋盘渲染三种路线并存，其中棋盘渲染用半量像素着色配合前后帧信息重建接近 4K 的画面，是当时最主流的一种做法。Pro 支持 4K 视频串流，Netflix、YouTube 等应用随之上线 4K。

PlayStation VR 是这一代的配套设备，采用 5.7 英寸 1920×1080 OLED 显示，刷新率 120Hz 与 90Hz，配合 PlayStation Camera 与 Move 手柄使用，需连接 PS4 本体。它的定价低于同期 PC 端 VR 头显，但依赖 PS4 的算力，画面与追踪精度受限。PS4 Pro 针对 VR 增加了多分辨率渲染等优化。

## 5. 软件生态与平台气质

### 5.1 数字商店、订阅制与发行方式

PS4 的发行结构里，PlayStation Store 与实体零售并列成为主渠道。2013 年主机首发时，完整游戏销量中数字版占比不到一成；到这一代后期，索尼财报口径下数字版已占 PlayStation 完整游戏销量的八成上下，实体渠道被明显压缩。数字商店改变了价格节奏：定期折扣、会员专享价、预购与预载成为常规手段，一款游戏的生命周期从「首发定价、缓慢降价」变成「频繁打折、长期在线」。

PlayStation Plus 在这一代发生变化：联机对战需要订阅，索尼把上一代免费的网络对战改为付费项。与此同时，会员每月可领取若干款免费游戏，云存档、折扣等权益继续加码。到 2020 年，PSN 月活跃用户达到 1.03 亿，超过三分之一为 PS Plus 订阅者；索尼也靠这一订阅获得了稳定现金流。这一模式后来被 Xbox Live Gold、Nintendo Switch Online 不同程度地参照。数字发行的另一面是首日补丁与强制安装：光盘插进去后，先安装、再下补丁，成为这一代玩家的共同体验，游戏的「完整形态」不再只存在于那张盘里。

### 5.2 SHARE 键、直播与分享

SHARE 键是 PS4 手柄上最具时代标志的一处改动。单击可截图、长按可进入分享菜单、双击可开始/结束录制，玩家能把最近一段游玩录像直接发到 Twitch、Ustream 或 YouTube，或分享到社交平台。索尼把 Twitch 等直播服务做进了系统层，直播不再是需要外接采集卡和电脑的额外步骤。Share Play（2014 年系统更新加入）进一步允许把游戏画面串给好友观看，甚至在一小时内把操作权交给对方，联机合作与「看别人玩」被做成系统功能。

由此形成的传播链条值得单列。此前主机游戏的曝光主要靠广告、杂志与评测；PS4 时代，主播与视频创作者成为作品扩散的关键节点，一段直播切片或一次高难度通关录像，能在商业宣传之外带来源源不断的曝光。对玩家群体来说，录屏、截图、发帖、看播成为日常动作，游戏体验被拆分成可分享的片段。这条链条也让一些玩法难度高、画面有辨识度的作品在社交平台上获得了与其宣传预算不相称的传播量。

### 5.3 第一方工业化体系

PS4 第一方的特点在于产出稳定、品类互补、且每条线都有明确的代表作。Naughty Dog 在这一代交付《The Last of Us Remastered》（2014）、《Uncharted 4: A Thief's End》（2016）、《Uncharted: The Lost Legacy》（2017）与《The Last of Us Part II》（2020）；作品强调电影化叙事、动作表演与线性关卡，成为 PS4 独占内容最直观的门面。Santa Monica Studio 在 2018 年重启《God of War》，改用一镜到底的连续镜头与北欧题材；Guerrilla Games 从《Killzone Shadow Fall》的射击线转向《Horizon Zero Dawn》（2017）的开放世界，一年内销量突破 760 万。Insomniac Games 交付了《Ratchet & Clank》（2016）与《Marvel's Spider-Man》（2018），后者三天 330 万套，促成 2019 年索尼以约 2.29 亿美元将其收购。Sucker Punch 有《inFamous Second Son》（2014）与《Ghost of Tsushima》（2020）。日本工作室与 FromSoftware 合作的《Bloodborne》（2015）在发售后一个月内销量破百万；Polyphony Digital 的《Gran Turismo Sport》（2017）、Media Molecule 的《Dreams》（2020）、Bend Studio 的《Days Gone》（2019）覆盖竞速、创作工具与开放世界不同方向。

这套体系的运作逻辑是：单个工作室不必每款都做全品类爆款，而是在各自擅长的方向上持续产出，以独占作品为硬件提供购买理由。与 PS3 时代相比，PS4 第一方的开发节奏更规律，作品在发售前的宣传周期也更标准化。这种「工业化」不必然等于每款都是精品，但确实让 PlayStation 平台在中后期很少有长时间的内容空窗。

### 5.4 第三方与日本市场

PS4 的第三方覆盖面是它能拉开与对手差距的另一半原因。欧美方向有《Grand Theft Auto V》（2014 年登陆 PS4）、《The Witcher 3: Wild Hunt》（2015）、《Red Dead Redemption 2》（2018）、《Call of Duty》与《FIFA》系列等年货级跨平台作品；日本方向则汇集了《Persona 5》（2016 年日版）、《NieR: Automata》（2017）、《Yakuza》系列、《Final Fantasy》系列新作以及大量中小体量作品。以 x86-64 为共同基础的架构让这些跨平台作品的移植成本下降，PC 与主机共享开发流程也更加顺畅。对日本市场而言，PS4 承接了 PS3 之后大部分日式家用机作品的发行，日本厂商在 PS4 与 PC 之间的同步发行也变得更常见。

### 5.5 中国玩家的 PS4 经验

中国大陆的主机市场与这一代几乎同步重启。2000 年起实施的电子游戏机禁售政策在 2014 年 1 月 6 日先行于上海自贸区松绑，国务院允许外资企业从事游戏游艺设备的生产和销售，通过文化部门内容审查的产品可面向国内市场；此后禁售范围逐步扩大到全国。索尼方面的动作是推出国行机型：2015 年 3 月 20 日，PS4 国行以 2899 元（单手柄）、3299 元（含摄像头与底座套装）上市，PS Vita 为 1299 元。原定 2015 年 1 月 11 日的首发因为「不锁区」争议被延期，一位玩家以实名向主管部门反映国行 PS4 未锁区，事件在玩家社区引发激烈争论，成为国行主机早期最具代表性的插曲。

国行主机在区域限制上的处理方式，直接塑造了大陆玩家的购买习惯。由于官方渠道以国行区服为主，不少玩家选择港版、日版或美版机器，或在国行主机上通过备份还原的方式使用港服账号——这套社区流传的变通办法延续了这一代的大部分时间。同一时期，淘宝等平台上的实体光盘、二手盘交易活跃，主机游戏的流通靠线下与电商并行。直播与视频平台在中国玩家群体里的热度也在这一代上升，主机区主播与解说视频成为不少人了解新作的主要渠道，其播放量常常超过传统媒体评测。国行与港版并行、审核与「曲线登录」并存，是这一代中国主机玩家区别于海外玩家的具体经验。

## 6. 为什么它重要 / 为什么它赢·输

### 6.1 为什么它是平台模板的成熟样本

PS4 的价值不在于单纯卖得多，而在于它把四件事同时做成了行业标准：一是以 x86-64 与统一内存降低开发门槛，让第三方跨平台作品能低成本、高质量地登陆；二是把 PlayStation Store 做成与实体并行的主渠道，并通过订阅与折扣维持长期收入；三是把录制、截图、直播、Share Play 收进手柄的一颗按键，重塑作品的传播路径；四是以 Slim / Pro 实现同代内的机型分层，回应 4K 与 HDR 等显示技术的更新。这四点单独看并非 PS4 首创，但被它整合成一套可复制的体系，此后的 PS5、Xbox Series、乃至 PC 平台的客户端，都在不同程度上沿用其中要素。

### 6.2 为什么它赢下同代竞争

胜负在 2013 年就被几件事定下。价格上，PS4 首发 399 美元比 Xbox One 低 100 美元；政策上，PS4 不限制二手、不强制联网，而对手的相关限制在舆论压力下才被撤回；性能上，8GB GDDR5 统一内存与 1.84 TFLOPS 的 GPU 让同代跨平台作品在 PS4 上常有更好的分辨率或帧率表现；内容上，中后期第一方与日式第三方的产出稳定，硬件因此持续有购买理由。这几点叠加的结果是 PS4 与 Xbox One 在世代结束时形成约 1.172 亿对约 5800 万的差距。需要注意，这一差距的成因里，价格与政策属于可被一次发布会改变的因素，而第一方内容体系与开发者友好度则是需要数年积累的结构性优势。PS4 能保持领先，依靠的是后一类优势。

### 6.3 争议与代价

PS4 时代同时留下几项争议。联机对战被改为必须订阅 PlayStation Plus，被部分玩家视为把上一代免费的东西重新收费。首日补丁与强制安装让实体光盘不再等于「插上即玩」，游戏的完整形态依赖厂商的服务器长期在线，这一代之后的收藏与保存问题由此浮现。数字发行比例持续攀升，实体零售与二手渠道的空间被压缩，围绕商店定价权与玩家权益的讨论随之出现。PlayStation VR 虽然以更低价格打开了主机 VR 的入口，但受限于 PS4 的算力与追踪方案，实际普及度有限。在中国大陆，国行机型长期存在区域与账号限制，玩家需要在官方渠道与曲线登录之间做出选择，这套摩擦一直延续到这一代退场。

## 7. 它留下了什么

PS4 留下的第一样东西是「向下兼容 + 同代升级」这一套硬件节奏。PS4 Pro 证明了在生命周期中段推出加强机型可以做到兼容旧作、不分裂玩家基础，这条路线被 PS5 时代的 PS5 Pro 继续采用；PS5 对 PS4 游戏的向下兼容，也让这一代主机的软件库得以整体延续，玩家积累的数字游戏与存档没有随换代作废。

第二样东西是数字发行与订阅制的商业结构。PS4 把 PlayStation Store 做成与实体并列的主渠道，把 PS Plus 从「送游戏」的服务变成联机与权益的付费入口，索尼由此获得了硬件之外的稳定收入。这一结构在 PS5 时代被进一步细化成多档订阅，成为 PlayStation 业务的核心组成。

第三样东西是分享与直播的传播逻辑。SHARE 键把「记录并分享一段游玩」变成了系统级能力，主播与视频创作者从边缘角色变成作品扩散的关键节点。这套逻辑此后被所有平台吸收，直播切片与短视频成为游戏营销的常规组成部分。

第四样东西是 x86-64 架构带来的跨平台便利。与 PS3 时代截然不同的架构选择，让主机、PC 甚至移动端之间的移植成本大幅下降。这一便利的直接后果，是索尼在 PS4 世代后期开始把部分原独占作品带到 PC，包括《Horizon Zero Dawn》（2020）、《Days Gone》（2021）与《God of War》（2022）等；主机独占作品不再天然地与 PC 隔绝。

最后，PS4 也是中国大陆主机市场重启后的第一台主流机器。国行渠道的建立、审查与区域限制带来的摩擦、港版与备份还原并行的消费方式，共同构成了一代中国主机玩家的具体记忆。与海外玩家的差异，恰恰体现在这些制度与渠道细节上，而不只是游戏本身。

## 8. 一句话总结

PS4 卖出了 PlayStation 2 之后最高的主机销量，更重要的是它把数字商店、订阅制、社交直播与同代机型分层整理成一套可复制的平台模板，让「现代主机」这套做法在它这七年里第一次完整跑顺。

## 9. 参考资料

- Sony Interactive Entertainment, Business Data & Sales（PS4 累计出货、PSN 月活、PS Plus 订阅与软件销量口径）https://sonyinteractive.com/en/our-company/business-data-sales/
- Sony Interactive Entertainment 新闻稿《「プレイステーション 4」(PS4™) 北米で11月15日に、欧州…》（2013-08-21，首发日期与价格）https://sonyinteractive.com/jp/press-releases/2013/130821a/
- Sony Interactive Entertainment 新闻稿《PlayStation®4 Sales Surpass 1 Million Units in North America in 24 Hours》（2013-11-17）https://sonyinteractive.com/en/press-releases/2013/playstation4-sales-surpass-1-million-units-in-north-america-in-24-hours/
- Sony Interactive Entertainment 新闻稿《Sony Interactive Entertainment Unveils PlayStation®4 Pro…》（2016-09-08，Pro 规格、价格与「生命周期中段首推高端机型」表述）https://sonyinteractive.com/en/press-releases/2016/sony-interactive-entertainment-unveils-playstation4-pro-delivering-enhanced-ps4-experience/
- Sony Interactive Entertainment 新闻稿《…Slimmer and Lighter PlayStation®4 in September, Available at 29,980yen, $299, €299 and £259》（2016）https://sonyinteractive.com/en/press-releases/2016/sony-interactive-entertainment-to-launch-slimmer-and-lighter-playstation4-in-september-available-at-29980yen-299-299-and-259/
- Sony Interactive Entertainment 新闻稿《PlayStation®VR Launches October 2016 Available Globally at 44,980 Yen, $399 USD, €399 and £349》（2016-03）https://sonyinteractive.com/en/press-releases/2016/playstationvr-launches-october-2016-available-globally-at-44980-yen-399-usd-399-and-349/
- Sony Interactive Entertainment 新闻稿《Sales of PlayStation®4 (PS4™) Exclusive Bloodborne™ Surpass 1 Million Units Worldwide》（2015-04）https://sonyinteractive.com/en/press-releases/2015/sales-of-playstation4-ps4-exclusive-bloodborne-surpass-1-million-units-worldwide/
- Sony Interactive Entertainment 新闻稿《UNCHARTED 4: A Thief's End First Week Sales Surpass 2.7 Million Units Worldwide》（2016-05）https://sonyinteractive.com/en/press-releases/2016/uncharted-4-a-thiefs-end-first-week-sales-surpass-27-million-units-worldwide/
- Sony Interactive Entertainment 新闻稿《Sony Interactive Entertainment to Acquire Insomniac Games…》（2019-08）https://sonyinteractive.com/en/press-releases/2019/sony-interactive-entertainment-to-acquire-insomniac-games-developer-of-playstation4-top-selling-marvels-spider-man-ratchet-clank/
- Sony Interactive Entertainment 新闻稿《PlayStation™Network Monthly Active Users Reaches 103 Million》（2020-01）https://sonyinteractive.com/en/press-releases/2020/playstationnetwork-monthly-active-users-reaches-103-million/
- PlayStation.Blog《PS4 Launch Games: The Complete List》（2013-11-15）https://blog.playstation.com/2013/11/15/ps4-launch-games-the-complete-list/
- PlayStation.Blog《PS4 Update 2.50 "Yukimura" Preview: Suspend/Resume and More》（2015-03-11）https://blog.playstation.com/2015/03/11/ps4-update-2-50-yukimura-preview-suspendresume-and-more/
- PlayStation.Blog《PS4 Pro: The Ultimate FAQ》（2016-09-08，棋盘渲染、分辨率与价格）https://blog.playstation.com/2016/09/08/ps4-pro-the-ultimate-faq/
- PlayStation.Blog《The Last of Us Part II sells more than 4 million copies》（2020-06-26）https://blog.playstation.com/2020/06/26/the-last-of-us-part-ii-sells-more-than-4-million-copies/
- PlayStation 日本官方《PlayStation の歴史年表 2013 - PS4 / PS VR》（首发地区日期）https://www.playstation.com/ja-jp/playstation-history/2013-ps4-ps-vr/
- Digital Foundry《Spec Analysis: PlayStation 4》（2013-02-21，官方规格与 8GB GDDR5）https://www.digitalfoundry.net/articles/df-hardware-spec-analysis-playstation-4
- Digital Foundry《Inside PlayStation 4 Pro: How Sony made the first 4K games console》（2016-10-20，Pro 架构与棋盘渲染）https://www.digitalfoundry.net/articles/digitalfoundry-2016-inside-playstation-4-pro-how-sony-made-a-4k-games-machine
- Polygon《PS4 tech specs: 'supercharged PC architecture,' x86 CPU, 8 GB memory》（2013-02-20）https://www.polygon.com/2013/2/20/4009940/playstation-4-tech-specs-hardware-details/
- Ars Technica《Sony reveals the PlayStation 4 ahead of holiday 2013 launch》（2013-02-20）https://arstechnica.com/gaming/2013/02/sony-reveals-the-first-official-details-of-the-playstation-4/
- Ars Technica《PS4 owners will need PlayStation Plus subscription for online multiplayer》（2013-06）https://arstechnica.com/gaming/2013/06/ps4-owners-will-need-playstation-plus-subscription-for-online-multiplayer/
- Gamasutra / Game Developer《Inside the PlayStation 4 With Mark Cerny》（2013-04-24，统一内存与「不为开发者制造谜题」）https://www.gamedeveloper.com/business/inside-the-playstation-4-with-mark-cerny
- The Verge《PlayStation 4 lead architect reveals secrets behind Sony's next console》（2013-04-25）https://www.theverge.com/2013/4/25/4264222/mark-cerny-interview-ps4-technical-details
- Polygon《PlayStation's one-step tutorial on sharing used games》（2013-06-10）https://www.polygon.com/2013/6/10/4417490/playstations-one-step-tutorial-on-sharing-used-games/
- CNET《Microsoft pulls a 180, reverses Xbox One always-on DRM and used games policy》（2013-06-19）https://www.cnet.com/tech/tech-industry/microsoft-pulls-a-180-reverses-xbox-one-always-on-drm-and-used-games-policy/
- GameSpot《PS4 Sales Reach 117.2 Million Units As Production Winds Down》（2022-08-10）https://www.gamespot.com/articles/ps4-sales-reach-117-2-million-units-as-production-winds-down/1100-6506319/
- GameSpot《PlayStation 4 Pro: Everything You Need to Know》（2016-11-07，Pro 详细参数）https://www.gamespot.com/articles/playstation-4-pro-everything-you-need-to-know/1100-6444653/
- Wikipedia《PlayStation 4 technical specifications》（APU、CPU/GPU 与内存参数）https://en.wikipedia.org/wiki/PlayStation_4_technical_specifications
- Wikipedia《Eighth generation of video game consoles》（PS4 约 1.17 亿、Xbox One 约 5800 万）https://en.wikipedia.org/wiki/Eighth_generation_of_video_game_consoles
- Wikipedia《PlayStation Now》（云游戏服务范围）https://en.wikipedia.org/wiki/PlayStation_Now
- Famitsu《プレイステーション4 日本での発売日は2014年2月22日》（2013-09-09，日本价格）https://www.famitsu.com/news/201309/09039687.html
- Variety《'Spider-Man' Dethrones 'God of War' as Sony's Fastest-Selling PS4 Game》（2018-09，三天 330 万套）https://variety.com/2018/gaming/news/spider-man-fastest-selling-ps4-game-1202951072/
- Kotaku《God of War Comes To PC Next Year As Sony Continues Porting Exclusives》（2021，PC 移植）https://kotaku.com/sony-continues-bringing-playstation-exclusives-to-pc-wi-1847900565
- ExtremeTech《PS4 will ship without many core features, requires 300MB day-one patch》（2013-11，首日补丁）https://www.extremetech.com/gaming/169594-ps4-will-ship-without-a-number-of-core-features-requires-300mb-day-one-patch
- 索尼（中国）新闻稿《"一切为了玩家" — 索尼 PlayStation 中国版正式发布》（国行价格与套装）https://www.sony.com.cn/newscenter/corporate/2083.htm
- 人民网《我国正式解除长达13年游戏机禁令 允许外资企业进入》（2014-01-06）http://politics.people.com.cn/n/2014/0106/c1001-24038455.html
- 维基百科《中国大陆 PlayStation 系列延迟发售事件》（延期与锁区争议）https://zh.wikipedia.org/zh-hans/中国大陆PlayStation系列延迟发售事件
- 爱范儿《国行 PS4 Pro 终于来了：售价 2999 元将于 6 月 7 日发售》（2017）https://www.ifanr.com/842598
- 游民星空《PS4 国行备份还原解锁教程》（备份还原使用港服账号的社区做法）https://www.gamersky.com/handbook/201803/1021671_3.shtml

（以上链接均为检索时可直接访问的公开页面；检索时间：2026 年 10 月。）
