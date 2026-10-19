# DC 时代 Wiki

> 说明：本文为面向中文读者整理的「DC 时代」机种史 / 平台史概览，整理范围为世嘉（SEGA）第六世代家用游戏机 Dreamcast（日文名 ドリームキャスト，中文玩家通称 DC、世嘉 DC）从 1998 年 11 月 27 日日本首发，到 2001 年 3 月 31 日停止生产、世嘉退出家用主机硬件业务为止的平台史；内容覆盖硬件架构、内置联网、GD-ROM 载体、Visual Memory（VMU）周边、在线服务（SegaNet / Dreamarena / Dricas）以及代表性软件生态。软件部分按「它在当年做了什么新事」组织，不作作品清单。日本市场 2001 年后仍有零星软件发售，只在末章作为余波提及。主要依据世嘉官方硬件史专栏与 2001 年 1 月 31 日新闻稿、世嘉 2001 年度报告、当年 BBC 与日本经济新闻社系媒体报道、英文与日文维基百科、Sega Retro 的硬件与销量整理，以及机核、虎嗅等中文资料。全文把事实、推断与评价分开表述，检索未能确证者标注「待核实」。这是一个已经结束的时代，不做进行中判断。检索时间：2026 年 10 月。

:::epigraph
世纪末的秋夜，电话线第一次被牵进客厅，拨号音之后是一长串握手声。
街机厅里刚打完的那一关，回到家能在电视上按原样再打一遍。
光驱转起来像一台小风扇，记忆卡上有一块会发光的屏幕，装着旁人看不见的小游戏。
这样的日子只够两年多；后来的人把电话线换成了宽带，把下载换成了商店。
当年守着电视机的那批人，多数要在很多年后的回顾文章里，才想起自己曾短暂地站在未来那一侧。
:::

---

## 1. 时代概览

Dreamcast 是世嘉于 1998 年 11 月 27 日在日本发售的第六世代家用游戏机，也是世嘉历史上最后一台家用主机。它比索尼 PlayStation 2 早十五个月上市，比任天堂 GameCube 与微软 Xbox 早两年以上；在 1998 年末到 2000 年之间，它是市面上性能最强的一档机器，也是第一台把联网能力作为标准配置随主机一起交给玩家的家用游戏机——「家用游戏机首次标准搭载联网功能」是世嘉官方在纪念文案里的表述。它内置调制解调器，使用特制的大容量光盘 GD-ROM，配备带液晶屏的记忆卡 VMU，并把街机基板 NAOMI 的架构直接搬进客厅。

本篇要立的核心命题是：Dreamcast 是世嘉家用主机史上最后一次、也是超前的一次总攻。它提前把联网对战、可下载内容、街机级移植和一批实验性作品带进客厅；与此同时，它又是「历史地位高于大众记忆」的典型样本——方向看得足够远，平台寿命却不足以让这些优势沉淀成一代人的共同记忆。

关于寿命，日本首发到停产约两年四个月，西方市场从 1999 年 9 月 9 日算起只有约十八个月。世嘉官方口径的全球累计销量约 913 万台，另有约 1045 万台（含渠道库存）的说法，日本国内累计约 245 万台；同期 PlayStation 2 的全球销量约 1.55 亿台，两者相差十几倍。这个量级差，是理解本篇全部张力的起点。

把 Dreamcast 放回世嘉的硬件谱系，它接在 1994 年 11 月 22 日发售的 Saturn（土星）之后。世嘉的家用硬件从 1983 年的 SG-1000 起步，经 Mark III / Master System、Mega Drive（北美名 Genesis）、Game Gear、Saturn，到 Dreamcast 收尾。2001 年 1 月 31 日的停产宣布，同时也是世嘉从硬件商转为第三方软件商的转折点。

## 2. 时代时间线

### 2.1 1994–1998：土星失速与「Katana」立项

Saturn 在日本与 PlayStation 缠斗，在北美市场失利；双 CPU 的复杂架构抬高了开发门槛，世嘉在 1990 年代中后期承受连续亏损。世嘉随后启动后继机计划，研发代号 Katana。芯片方案一度摇摆：世嘉早期与美国 3Dfx 的 Voodoo 方案有过合作讨论，最终采用 NEC 与 VideoLogic 的 PowerVR2（3Dfx 相关的合作与诉讼细节，待核实）。

这代机器最关键的一项决策，是把街机新基板 NAOMI 与家用机做成同一套架构：同款日立 SH-4 CPU、同系山叶 AICA 音源、不同版本的 PowerVR2 GPU。NAOMI 甚至可以直接接 Dreamcast 的手柄与 VMU。这决定了 Dreamcast 后来的软件气质以街机移植见长。

1998 年 5 月 21 日，世嘉对外发表 Dreamcast，宣布 11 月 20 日发售，当天在各大报纸晨刊投放广告；实际发售日推后一周，定在 11 月 27 日，价格 29,800 日元。世嘉官方回顾里提到，为了抢在对手前面取得先手，1998 年内必须发售，这是赶工的背景。EA 一方后来也把「世嘉在是否内置调制解调器上态度反复」列为不支持该平台的理由之一。

### 2.2 1998 年 11 月：日本首发与第一年

1998 年 11 月 27 日，Dreamcast 在日本发售，定价 29,800 日元。首发阵容包括 AM2 从 Model 3 街机移植的《Virtua Fighter 3tb》，以及 Godzilla Generations、Pen Pen Triathlon、July 等；随后是《Sega Rally 2》（1999 年 1 月 28 日）与《House of the Dead 2》（1999 年 3 月 25 日）。秋叶原等地的店头活动与电视广告里的「湯川専務」角色成为当时的谈资，初回出货有限，市场出现缺货；有资料称发售当年的出货总量约 30 万台（待核实）。

1998 年 12 月 23 日，《Sonic Adventure》在日本发售。它是索尼克系列第一款 3D 正传，后来以约 250 万份成为 Dreamcast 全球最畅销游戏，其中日本约 44 万、北美约 127 万。日本市场第一年的另外两个亮点是 Vivarium 的《Seaman》（1999 年 7 月，配麦克风养成）与 Namco 的《Soulcalibur》（1999 年 8 月 5 日，销量超过 130 万份）。在线能力从第一年就开始铺：日本市场配发浏览器光盘 Dream Passport，世嘉运营网络服务（Dricas，上线时间待核实），玩家可以用主机收发邮件、浏览网页。

### 2.3 1999 年：9/9/99 与欧美登陆

1999 年 9 月 9 日，Dreamcast 在北美发售，价格 199 美元，宣传口号是「9/9/99 for $199」。首日售出 225,132 台、销售额约 9840 万美元（另有约 1 亿美元的说法），创下当时的纪录。首发阵容有《Sonic Adventure》《NFL 2K》《Ready 2 Rumble Boxing》《Hydro Thunder》《Mortal Kombat Gold》《TrickStyle》等，《NBA 2K》在 11 月跟进，《Soulcalibur》则在北美充当画面标杆。

北美市场最显著的缺口来自 EA。EA 要求体育类独占，世嘉已在 1999 年 3 月完成对 Visual Concepts 约 1000 万美元的收购、坚持自营体育品牌，谈判随之破裂。EA 的 Bing Gordon 对外留下「没有 EA，Dreamcast 不可能成功」这句话；世嘉一方（时任世嘉美国总裁 Bernie Stolar）的说法则是 EA 要的是没有竞争的体育品类。结果是 Dreamcast 在北美靠 2K 系列填补体育空缺：《NFL 2K》卖出约 113 万份，《NFL 2K1》在美国首周 139,000 份，超过同期《Madden NFL 2001》的 126,000 份。

1999 年 3 月 2 日，索尼已公布 PlayStation 2 的初步信息，消费者的等待情绪开始出现。多篇回顾（例如 Eurogamer 的 Dan Whitehead）认为，PS2 的公布对 Dreamcast 的打击大于硬件本身。欧洲方面，Dreamcast 于 1999 年 10 月 14 日发售，随机器提供免费的拨号服务 Dreamarena（同日上线，服务延续到 2003 年 3 月）；到 1999 年 11 月 24 日，欧洲售出约 40 万台。

1999 年 12 月 29 日，《Shenmue》第一章在日本发售，由铃木裕与 AM2 制作，开发加营销费用估计在 4700 万至 7000 万美元之间，是当时最贵的游戏之一；铃木裕拒绝把它归入既有类型，另给了一个类型名「FREE」。

### 2.4 2000 年：内容高峰、联网开局与 PS2 压境

2000 年 1 月 27 日，《Crazy Taxi》日版发售（街机版 1999 年在 NAOMI 上稼働，由 AM3 / Hitmaker 开发），美版在 2 月跟进；游戏里的真实品牌招牌与朋克配乐成为当时的话题。2 月 3 日，Capcom 的《Resident Evil – Code: Veronica》日版发售，约 114 万份，是 Dreamcast 上最有分量的第三方独占之一。

2000 年 3 月 4 日，PlayStation 2 在日本发售，定价 39,800 日元，带 DVD 播放与向下兼容。Dreamcast 相对 PS1 的画质优势不再构成代差防线，PS2 的 DVD 功能又把竞争拉进客厅影音这一层。同年 6 月 29 日，Smilebit 的《Jet Set Radio》在日本发售，把卡通渲染当作整套美术风格，舞台设定在虚构的东京都；美版于 10 月 31 日以《Jet Grind Radio》之名推出。

2000 年也是世嘉实验作最密集的一年：《Space Channel 5》（1999 年 12 月 16 日）之后，《Samba de Amigo》配沙锤控制器，《Roommania #203》观察公寓住户的日常，这批作品的商业成绩普遍平平。联网方面，美国 SegaNet 于 2000 年 9 月 7 日上线，月费 21.95 美元，签约十八个月可获 150 美元返还，主机同期降到 149 美元。早期的联网作品包括《ChuChu Rocket!》（1999 年，Dreamcast 上第一款在线多人游戏，最初被 Sonic Team 用来测试在线框架）与《NFL 2K1》（第一款支持联网的美式足球游戏）。2000 年 12 月 21 日，Sonic Team 的《Phantasy Star Online》在日本发售，是家用机上第一款实时在线 RPG，带符号聊天与按月收费；美版在 2001 年 1 月、欧版在 2001 年 2 月跟进。

盗版压力在同一年升级。Dreamcast 为兼容卡拉 OK 与音频 CD 而保留读取 MIL-CD 混合模式光盘的能力，世嘉在该启动路径上加过扰码，但机制被逆向；2000 年出现引导盘（Utopia Boot Disc），2001 年出现可直接启动的刻录镜像，GD-ROM 靠「普通光驱读不了」建立起来的物理防护由此失效。到年末商战，Dreamcast 的势头明显失速，世嘉 2001 年度报告写得很直接：Dreamcast 业务在最要紧的圣诞销售季失去动力。

### 2.5 2001 年：停产与转身

2001 年 1 月 31 日，世嘉召开「结构改革计划说明会」并发布新闻稿，宣布 2001 年 3 月 31 日停止 Dreamcast 生产，转为内容与街机事业并推进多平台战略，同时把全财年预期亏损从 236 亿日元下调到 583 亿日元。会上披露的库存为日本 28 万台、美国 120 万台、欧洲 46 万台、亚洲 9 万台；该财年（2000 年 4 月至 2001 年 3 月）主机销量合计 232 万台，其中日本 28 万、美国 135 万、欧洲 56 万、亚洲 13 万。

会长兼社长大川功捐出个人资产约 850 亿日元，包括约 1986 万股自有股与相关公司持股，世嘉据此确认约 779 亿日元的捐赠收益；大川功于 2001 年 3 月 16 日去世。世嘉 2001 财年净亏损 517 亿日元，消费事业营业亏损 692 亿日元，其中与 Dreamcast 硬件相关的库存减记与处置损失 524 亿日元。日本随后出现 9,900 日元的清仓价。

停产不等于停软。2001 年 Dreamcast 上仍有《Phantasy Star Online Ver.2》（6 月）、《Crazy Taxi 2》与《Sonic Adventure 2》（6 月 23 日）等作品；《Shenmue II》日版在 2001 年 9 月 6 日于 Dreamcast 发售，后来移植到 Xbox。日本市场的软件支持一直延续到 2004 年 2 月 24 日的《Puyo Puyo Fever》，这是世嘉一方在 Dreamcast 上的最后一款游戏。

与停产同时公布的第三方路线，是为 PlayStation 2 提供《Virtua Fighter 4》等五款、为 Game Boy Advance 提供《Sonic the Hedgehog Advance》等三款。世嘉从此成为软件商；2004 年与 Sammy 合并为 Sega Sammy，2005 年把 Visual Concepts 与 2K 品牌卖给 Take-Two。Dreamcast 由此成为世嘉家用硬件史的终点。

## 3. 基础信息速览

### 3.1 平台基本参数

| 项目 | 内容 |
| --- | --- |
| 平台名称 | Dreamcast（ドリームキャスト，中文通称 DC、世嘉 DC） |
| 讨论范围 | 世嘉第六世代家用主机本体、周边与在线服务；不含复刻周边与同人服务器的完整清单 |
| 时代跨度 | 1998 年 11 月 27 日日本首发；1999 年 9 月 9 日北美、10 月 14 日欧洲；2001 年 3 月 31 日停止生产；日本软件支持延续到 2004 年 2 月 |
| 平台属性 | 第六世代家用游戏机；首台以标准配置内置联网能力的家用主机（世嘉官方口径） |
| 主要载体 | GD-ROM（约 1.2GB）；兼容 CD 与 MIL-CD |
| 关键规格 | 日立 SH-4 200MHz；NEC / VideoLogic PowerVR2；主内存 16MB、显存 8MB、音效内存 2MB；山叶 AICA 音源；内置调制解调器（日本 33.6kbps，部分地区 56kbps，待核实）；可选宽带适配器 |
| 记忆卡 | Visual Memory Unit（VMU），128KB，带单色液晶屏与按键 |
| 官方销量口径 | 全球约 913 万台（世嘉口径）；另有约 1045 万台（含渠道库存）之说；日本累计约 245 万台。口径差异待核实 |
| 历史定位 | 世嘉最后一台家用主机；方向超前的短命平台 |

### 3.2 历史定位速写

| 维度 | 速写 |
| --- | --- |
| 技术印象 | 与街机基板同架构、画面干净、支持 VGA 输出、内置联网、VMU 充当第二屏 |
| 市场印象 | 北美首发创纪录，随后被 PS2 的公布与发售压制，两年多退场 |
| 软件印象 | 街机移植与实验作密集；大厂 RPG 与欧美体育大厂缺席，品类偏科 |
| 玩家文化 | 人数不占多数但黏性高的怀旧圈；同人服务器、模拟器与硬件改造延续至今 |
| 历史评价 | 普遍被描述为「超前」，历史地位明显高于大众普及记忆 |

### 3.3 关键词

Dreamcast；DC；世嘉；第六世代；SH-4；PowerVR2；GD-ROM；内置调制解调器；SegaNet；Dreamarena；Dricas；Visual Memory Unit（VMU）；Dream Passport；NAOMI；街机移植；9/9/99；Sega Sports 与 2K；Shenmue；Phantasy Star Online；Jet Set Radio；Crazy Taxi；Sonic Adventure；MIL-CD；Utopia；莎木；电软；模拟器。

## 4. 技术与硬件

### 4.1 核心架构

CPU 是日立 SH-4，主频 200MHz，带浮点单元与 SIMD 指令；GPU 是 NEC 与 VideoLogic 合作的 PowerVR2，采用分块延迟渲染，在当年以填充率与抗锯齿见长。内存配置为主内存 16MB、显存 8MB、音效内存 2MB，音源是山叶 AICA，最多 64 个声道。手柄为单摇杆、双扳机、两个 VMU 插槽，支持震动包。

在同期对手里，PS1 的规格已经老旧，Dreamcast 在 1998 到 1999 年的画面优势真实存在。VGA 输出盒能把画面推到 640×480 逐行，这在当年是相当干净的信号，也是 DC 老玩家至今念念不忘的一项。

### 4.2 GD-ROM 与反盗版

存储介质 GD-ROM 由世嘉与山叶共同开发，容量约 1.2GB，靠提高记录密度实现，普通 CD / DVD 光驱无法读取。世嘉没有采用加密芯片，而是把安全建立在「市面设备读不了」这一物理前提上。为兼容卡拉 OK 与音频 CD，主机保留了读取 MIL-CD 混合模式光盘的能力；世嘉在该启动路径上加了一道扰码，但机制被逆向。2000 年出现引导盘，2001 年出现可直接启动的刻录镜像，物理门槛随之失效。2000 到 2001 年间还出现过商业化的 PS1 模拟器 Bleemcast（细节待核实），可见当时围绕这台机器的技术尝试相当密集。GD-ROM 本身也有代价：1.2GB 在 1999 年够用，到 2001 年面对更大体量的游戏已经紧张。

### 4.3 联网与 VMU

内置调制解调器是 Dreamcast 的定位核心。日本首发机型为 33.6kbps，北美与欧洲机型规格更高，并另售宽带适配器。VMU 是 128KB 的记忆卡，正面有单色液晶屏与几枚按键，插在手柄上可以显示游戏提示，拔下来能当掌上小玩具玩迷你游戏，两个 VMU 还可以对接交换数据与对战；《Sonic Adventure》的 Chao 养育就把它当作随身设备使用。Dream Passport 是日本市场的浏览器光盘，让主机具备收发邮件、浏览网页的能力。这些设计合起来，是家用主机第一次把「网络」和「第二块屏幕」当作标配来做。

### 4.4 设计取舍

Dreamcast 没有内置 DVD 播放，这在 2000 年之后变成明显的比较劣势；16MB 主内存对于《Shenmue》这类开放场景已经吃紧；GD-ROM 与调制解调器的组合把成本压在 1999 年可接受的区间，却没有给后续扩容留下余地。芯片组的选择也留下争议，EA 曾以「非行业标准、缺少现成开发库」为由反对这一方案，这属于 EA 一方的立场性陈述。整体看，Dreamcast 把资源集中在画质与联网两项上，其他项目都做了让步。

## 5. 软件生态与平台气质

### 5.1 街机同架构的移植红利

NAOMI 与 Dreamcast 共用 SH-4、AICA 与 PowerVR2 系列架构，家用版与街机版的差距被压到很小。《Virtua Fighter 3tb》《Sega Rally 2》《House of the Dead 2》《Virtua Tennis》《Crazy Taxi》《18 Wheeler》，加上 Namco 的《Soulcalibur》、Capcom 的《Marvel vs. Capcom》系列、Tecmo 的《Dead or Alive 2》，让「街机厅里那一台，客厅里也有一台」在 1999 到 2000 年成了 Dreamcast 最具体的卖点。这种红利同时限制了软件结构：平台早期的口碑几乎由街机系与格斗系撑起。

### 5.2 联网服务与下载内容

Dreamcast 的在线棋盘是分区运营的：日本走世嘉的网络服务与 Dream Passport；欧洲用随主机附带的 Dreamarena（免费拨号，1999 年 10 月 14 日上线，2003 年 3 月停服）；美国用 2000 年 9 月 7 日上线的 SegaNet（月费 21.95 美元）。早期联网作品里，《ChuChu Rocket!》是这台主机第一款在线多人游戏，也是 Sonic Team 用来测试在线框架的试验品；《NFL 2K1》是第一款支持联网的美式足球游戏。真正把在线变成长期玩法的是《Phantasy Star Online》：舰队大厅、符号聊天、分期开放的下载任务，这套结构后来被整个家用机网络游戏沿用。世嘉还通过光盘与网络下发过追加内容与浏览内容，够得上「下载内容」的早期样本（具体项目待核实）。

### 5.3 实验作与世嘉内部工作室

Dreamcast 时代的世嘉内部是分权而活跃的：AM2 的铃木裕、Sonic Team 的中裕司、Smilebit 的《Jet Set Radio》、United Game Artists 的水口哲也（《Space Channel 5》《Rez》）、Hitmaker 的《Crazy Taxi》，各做各的方向。《Seaman》用麦克风与玩家对话，《Samba de Amigo》配沙锤控制器，《Typing of the Dead》把光枪换成键盘，《Roommania #203》观察一间公寓里住户的日常。这些作品的共同点是把生活里的某一种动作直接搬进来当玩法，与世嘉的街机血统一脉相承。它们大多商业成绩平平，却构成了 Dreamcast 最难被复制的平台气质。

### 5.4 VMU 与第二屏

VMU 是 Dreamcast 记忆里最具体的一件小东西：玩家在《Sonic Adventure》里养 Chao，把它带在身上继续照顾；在《Phantasy Star Online》里，VMU 会提示好友上线；一些游戏甚至把整场小游戏装进记忆卡。把「主机之外的屏幕」交给玩家随身携带，在家用机上这是第一次成规模地做。

### 5.5 偏科的软件结构

Dreamcast 的强项集中在街机、竞速、格斗与美式体育；弱项是大型 RPG 与欧美第三方。史克威尔与艾尼克斯把《最终幻想》《勇者斗恶龙》的下一代留给 PS2，Namco 除《Soulcalibur》外的主力资源转向 PS2，EA 完全缺席。世嘉用 Visual Concepts 的 2K 系列补上体育，用《Phantasy Star Online》《Grandia II》《Eternal Arcadia》零星填补 RPG，但整体厚度不足以覆盖一个平台的完整生命周期。一个平台的名作记忆通常由 RPG 与大众动作游戏承载，这一环恰好是 Dreamcast 最薄的。

### 5.6 中文圈的接触路径

中国大陆没有 Dreamcast 的正规行货渠道（官方引进记录待核实），中文世界里的官方软件集中在台湾与香港，官方繁体中文游戏很少。当年接触 DC 的路径主要有三条：水货主机与少量正版盘；2000 年后通过 MIL-CD 漏洞流出的刻录盘；以及杂志。《电子游戏软件》长期对世嘉系主机有偏爱，2001 年世嘉宣布停产后，该刊以《世嘉 DC 成绝响》为题做过报道，这句话后来常被中文玩家引用。GD-ROM 在 1990 年代末无法被普通光驱读取，使 DC 的盗版扩散比 PS 晚，也把相当一部分玩家挡在门外。到 2000 年代中期，Chankast、nullDC 等模拟器出现，很多人才第一次玩到《莎木》与《Jet Set Radio》，这段记忆因此带有明显的补课性质。哪些作品曾在包机房出现过、普及度如何，缺乏可核查数据，此处不展开。

## 6. 为什么它重要，以及它为什么退场

### 6.1 为什么重要

按「为什么重要」这一问，Dreamcast 的位置有三处无法绕开。第一，它把联网从外设变成主机的默认部分：内置调制解调器、随主机附带的浏览器与在线服务、按月收费的在线 RPG，这套组合在 1999 到 2000 年是行业里唯一成规模的实践。第二，它证明了街机与家用机的架构可以合并：NAOMI 与 Dreamcast 同源，使街机移植的完成度与速度都上一个台阶，此后多数街机系厂商都沿着类似方向思考。第三，它留下了一批方向明确的实验作品：卡通渲染、第二屏记忆卡、用生活动作当玩法的设计，都能在 Dreamcast 上找到早期样本。

按「玩家当时怎样体验」这一问：在北美，1999 年 9 月 9 日买下 Dreamcast 的人拿到的是一台比 PS1 明显更强、能直接拨号上线对战的机器，199 美元的价格与《Sonic Adventure》《NFL 2K》《Soulcalibur》的首发阵容构成了很强的即时满足；一年之后，同一批玩家开始面对 PS2 的广告与 DVD 播放能力。在欧洲，随机器附带的 Dreamarena 是很多人第一次用家用主机上网。

### 6.2 为什么退场

原因可以拆成四层，彼此叠加。

一，时间窗口。Dreamcast 在 1998 年末是唯一的新世代机器，但 1999 年 3 月 2 日索尼公布 PS2、2000 年 3 月 4 日 PS2 发售，把这段独家期压缩到一年出头。想买「下一代 PlayStation」的人会等，这个等待在北美尤其明显。

二，第三方结构。EA 缺席削弱了北美体育与大众市场的吸引力，史克威尔、艾尼克斯与 Namco 的主力资源流向 PS2，使 Dreamcast 的软件名录在 RPG 与大制作上偏薄。主机生命周期的后段决定销量曲线，Dreamcast 恰好在这一段最缺人。

三，世嘉的财务状况。土星时代的失利与 Dreamcast 的持续投入，让世嘉没有打价格战与长期补贴的余裕。2001 财年消费事业营业亏损 692 亿日元、库存减记 524 亿日元，最终需要大川功捐出约 850 亿日元的个人资产才稳住阵脚。硬件业务对世嘉而言已经无法与软件业务并存。

四，盗版与硬件设计的相互作用。MIL-CD 漏洞在 2000 至 2001 年被击穿，自启动镜像扩散；世嘉官方与多数回顾并不把盗版当作停产主因，但它确实削弱了软件收入的弹性。加上没有 DVD 播放、16MB 内存的容量天花板，Dreamcast 在 2001 年的货架上已经很难讲出新故事。

### 6.3 名作记忆不厚的几个原因

这是本篇要回答的核心张力。Dreamcast 的名作在核心玩家圈里地位很高，却很少进入大众游戏记忆，原因可以被具体列举。

其一，平台寿命太短。日本约两年四个月、西方约十八个月，装不进一代人的成长期。多数主机的集体记忆需要五到七年的软件积累与二手流通才能成型，Dreamcast 只走了不到一半。

其二，装机量太小。全球约 913 万台（另一口径约 1045 万台），与 PS2 的约 1.55 亿台相差十几倍。名作要被反复提起、在同学之间传阅、在二手市场持续流通，需要足够大的人群基数，Dreamcast 不具备这个基数。

其三，第三方撤退改变了品类结构。能被大众反复回忆的作品通常集中在 RPG、开放世界与大众动作类型，而 Dreamcast 在这些类型上最薄；它最出名的一批作品恰好是街机移植与实验作，天然更接近核心玩家而非大众。

其四，世嘉自身的财务处境。世嘉没有能力像索尼那样用长期营销与渠道把作品反复推到台前。平台退场后，世嘉把《Shenmue II》《Phantasy Star Online》等作品搬到 Xbox、GameCube 与 PC 上，这些作品的记忆于是被记到了别的平台名下。

其五，联网体验无法被复述。Dreamcast 的联网体验依赖拨号、Dream Passport、SegaNet 与 Dreamarena，以及世嘉的服务器；服务器在主机退场后陆续关闭，这套体验没有留下可以被后人继承的界面。等到宽带与在线商店成为常态，Dreamcast 当年的先行做法反而变成了没有实物的历史。

其六，中文圈的接触成本。没有行货、GD-ROM 难复制、官方中文软件稀少，使 Dreamcast 在中文玩家里的普及度明显低于 PS 系；很多人的 DC 记忆来自模拟器，属于私人的补课经验，缺少包机房与街机厅式的公共记忆场景。

其七，PS2 的记忆垄断。PS2 通过向下兼容与 DVD 播放占据了客厅的中心位置，也占据了那个世代的默认叙事。有了默认平台，边缘平台的超前尝试就更容易被记成后来者本来就会做的事。

把这七条合起来看，Dreamcast 的处境可以概括为：它把未来的做法提前演示了一遍，却没有活到这些做法变成常识的那一天。

## 7. 它留下了什么

### 7.1 成为行业标配的做法

内置联网、随主机附带的在线服务、按月订阅的在线 RPG、下载追加内容、卡通渲染、第二屏记忆卡——这些做法在 2000 年代中期之后陆续成为行业常态，Dreamcast 是最早把它们成规模放进客厅的那一台。Dreamcast 之后的 PS2 网络适配器、Xbox Live 与后来的在线商店，都建立在「家用主机必须能联网」这个前提上。

### 7.2 作品与制作人的去向

《Phantasy Star Online》延伸出系列，直到《PSO2》与《PSO2 New Genesis》；《Shenmue》在 2015 年靠 Kickstarter 筹得超过 600 万美元，《Shenmue III》于 2019 年发售，同一 IP 还推出了动画；《Jet Set Radio》的卡通渲染与音乐成为后续作品的标志；《Crazy Taxi》《Sonic Adventure》《Virtua Tennis》各有续作。铃木裕、中裕司、水口哲也这一批制作人此后或留在世嘉，或独立创业，Dreamcast 是他们在硬件红利最好的一段时间里的作品集合。

### 7.3 社区与硬件的延续

Dreamcast 的在线游戏并未随 SegaNet 一起彻底消失：社区运营的同人服务器让《Phantasy Star Online》在原始硬件上仍可连线，独立游戏与小型发行一直延续到 2000 年代后期，例如 2007 年在日本发售的《Trigger Heart Exelica》（具体发售记录待核实）。硬件层面，VMU 的改造版、光驱替换件与 SD 卡加载方案在近年仍有小规模生产。中文圈的延续方式更简单：一台二手机、几张刻录盘、一个模拟器，加上《电子游戏软件》上那句「世嘉 DC 成绝响」。

## 8. 一句话总结

Dreamcast 把联网、下载内容、街机级移植与实验作品提前带进客厅，却在两年多的平台寿命里没能把它们沉淀成一代人的共同记忆；它留下的是一份被广泛承认、却少有人真正经历过的答卷。

## 9. 参考资料

以下链接最后检索时间为 2026 年 10 月。

- 世嘉官方硬件史专栏《ゲームの未来を変えた先進的ハード『ドリームキャスト』》：https://www.sega.jp/history/hard/column/column_06.html
- 世嘉 2001 年 1 月 31 日新闻稿《家庭用ゲーム機の製造中止および通期業績予想の修正に関するお知らせ》（存档）：https://web.archive.org/web/20010607154729/http://www.sega.co.jp/sega/corp/news/nr010131_2.html
- SEGA Annual Report 2001（PDF）：https://segaretro.org/images/8/80/AnnualReport2001_English.pdf
- BBC News《Sega scraps the Dreamcast》：http://news.bbc.co.uk/1/hi/business/1145936.stm
- BBC News《Sega chief's $700m gift》：http://news.bbc.co.uk/2/hi/business/1159418.stm
- The Japan Times《Sega Corp. shuts down Dreamcast production》（2001-02-01）：https://www.japantimes.co.jp/news/2001/02/01/business/sega-corp-shuts-down-dreamcast-production/
- Game Watch《セガ、Dreamcast製造中止!》（2001-01-31）：https://game.watch.impress.co.jp/docs/20010131/sega2.htm
- Game Watch《セガ、ドリームキャストを発表》（1998-05-21）：https://game.watch.impress.co.jp/docs/kikaku/1589368.html
- Wikipedia（英）Dreamcast：https://en.wikipedia.org/wiki/Dreamcast
- Wikipedia（英）List of best-selling Dreamcast games：https://en.wikipedia.org/wiki/List_of_best-selling_Dreamcast_games
- Wikipedia（英）VMU：https://en.wikipedia.org/wiki/VMU
- Wikipedia（英）ChuChu Rocket!：https://en.wikipedia.org/wiki/ChuChu_Rocket!
- Wikipedia（英）Jet Set Radio：https://en.wikipedia.org/wiki/Jet_Set_Radio
- Wikipedia（英）Phantasy Star Online：https://en.wikipedia.org/wiki/Phantasy_Star_Online
- Wikipedia（英）Shenmue：https://en.wikipedia.org/wiki/Shenmue
- Wikipedia（英）Sonic Adventure：https://en.wikipedia.org/wiki/Sonic_Adventure
- Wikipedia（英）PlayStation 2：https://en.wikipedia.org/wiki/PlayStation_2
- Wikipedia（英）NFL 2K：https://en.wikipedia.org/wiki/NFL_2K_(video_game)
- Wikipedia（日）ドリームキャスト：https://ja.wikipedia.org/wiki/ドリームキャスト
- Wikipedia（中）Dreamcast：https://zh.wikipedia.org/zh-hans/Dreamcast
- Sega Retro《Sega NAOMI》：https://segaretro.org/Sega_NAOMI
- Sega Retro《Visual Memory Unit》：https://segaretro.org/Visual_Memory_Unit
- Sega Retro《History of the Sega Dreamcast/Internet》：https://segaretro.org/History_of_the_Sega_Dreamcast/Internet
- Sega Retro《Puyo Pop Fever》：https://segaretro.org/Puyo_Pop_Fever
- Fabien Sanglard《How the Dreamcast copy protection was defeated》：https://fabiensanglard.net/dreamcast_hacking/
- Retro Reversing《How the Dreamcast's Security was Hacked (MIL-CD)》：https://www.retroreversing.com/How-the-Dreamcast-Security-was-Hacked
- The New York Times《Sega Launches Online Game Network》（2000-09）：https://www.nytimes.com/library/tech/00/09/biztech/articles/05sega-debut.html
- GameSpot《SegaNet Launches》：https://www.gamespot.com/articles/seganet-launches/1100-2625699/
- SEGA Dreamcast Info《The History of Visual Concepts》系列：https://www.sega-dreamcast-info.com/en/visual-concepts-history-ea-war-dreamcast-prototypes-archive
- SEGAbits《EA not supporting the Dreamcast》：https://segabits.com/blog/2013/05/20/monday-memories-ea-not-supporting-the-dreamcast/
- Game Developer《Execs: Tech Changes, Visual Concepts Issues Behind EA's Lack Of Dreamcast Support》：https://www.gamedeveloper.com/game-platforms/execs-tech-changes-visual-concepts-issues-behind-ea-s-lack-of-dreamcast-support
- Inverse《25 Years Ago, Sega Dreamed Of Connecting The World》：https://www.inverse.com/gaming/phantasy-star-online-dreamcast-anniversary
- Video Game Console Library《The Day Two Legendary Consoles Launched》：https://www.videogameconsolelibrary.com/playstation-dreamcast-9-9/
- 机核《有关〈莎木〉：一个为了理想重生的游戏》：https://www.gcores.com/articles/115517
- 机核《大陆解除游戏机禁令之前，华人电视游戏市场一些鲜为人知的故事》：https://www.gcores.com/articles/99611
- 虎嗅《世嘉在中国：30 年、7 家公司，与一次新的归来》：https://m.huxiu.com/article/4882395.html
- 网易游戏《人间有情，莎花飘香——〈莎木 3〉评测》（文中引用《电子游戏软件》文章标题）：https://play.163.com/article/155356.html
