# DOS 世代 时代 Wiki

> 说明：本文为面向中文读者整理的「DOS 世代」平台史与时代概览。叙述主体为 IBM PC 兼容机与 MS-DOS 从 1981 年 IBM PC 问世到 1996 年前后的个人电脑游戏舞台，范围涵盖硬件与操作系统环境、现代游戏类型的奠基、shareware 发行模式、modding 文化的起点，以及中文玩家的具体经验。主要依据为维基百科、Computer History Museum、IBM 官方历史页、The Digital Antiquarian、PC Gamer、Creative 官方历史页与中文维基等。DOS 世代已经结束，不属于「进行中的平台」。检索时间为 2026-10-18；整理期间联网检索工具多次返回异常，凡未能二次核对者已在正文标注「待核实」。

:::epigraph
机房的风扇声比画面先一步响起，屏幕上只剩一列绿色的盘符。
软盘插进驱动器，读盘灯一闪一闪，几张盘换来一个下午。
有人把中断号和内存地址抄在纸片上，贴在显示器边框。
那是一个要先跟机器商量、才能开始游戏的年代。
:::

---

## 1. 时代概览

DOS 世代指 IBM PC 兼容机与 MS-DOS（Microsoft Disk Operating System）操作系统共同构成的个人电脑游戏舞台，时间上从 1981 年 8 月 IBM 发布 PC 起算，到 1996 年前后 Windows 95、DirectX 与 3D 加速卡把游戏主战场逐步移出纯 DOS 环境为止。它没有一台由单一厂商定义的主机，边界由「能不能跑同一份软件」这类兼容性来划定，硬件出自众多厂商，系统出自微软与 IBM 的分工。

核心命题是：这是个人电脑游戏的奠基时代。今天常见的几大类型在这里找到最早的可玩原型——第一人称射击（Wolfenstein 3D、DOOM）、即时战略（Dune II、Command & Conquer）、电脑角色扮演（Ultima 系列、Ultima Underworld）、图形冒险与解谜（King's Quest、Monkey Island、Myst）、模拟经营与 4X（SimCity、Civilization）。这些作品在当时就已经确立，后来的系列只是它们的后代。

它同时留下两套软性的制度。一是 shareware 发行模式：把游戏拆成段落，第一段免费发到 BBS 与软盘上，玩家尝过之后再邮寄支票购买其余部分，Apogee Software 与 id Software 把它做成了一门生意。二是 modding 文化的起点：DOOM 的数据文件 WAD 对外开放，玩家自制关卡、贴图与规则，最早的一批修改社区由此成形。

技术侧的关键词是从软盘到 CD-ROM 的跃迁。5.25 英寸与 3.5 英寸软盘、硬盘、光驱依次登场；CPU 从 8088 走到 486 与 Pentium；显卡从 CGA、EGA 走到 VGA、SVGA；声音从 PC speaker 的一声蜂鸣走到 AdLib、Sound Blaster 与 General MIDI。对当时的人来说，硬件参数不是宣传数字，而是能不能进入游戏的门槛：常规内存要凑够 640 KB，声卡要占对 IRQ 与 DMA 通道。

历史地位与市场结果在这里并不重合。IBM 原本想用 PC 卖办公机器，游戏是寄居其上的用途；整个 DOS 世代里，家用主机在客厅中仍是更大的娱乐市场。但这台「办公机器」把游戏类型的模板、发行方式与社区结构定了下来，此后二十年的 PC 游戏，以及数字商店与 mod 社区，都能追溯到这一段。

这套平台的气质与家用主机不同。主机买回家插卡即玩，PC 则要先攒机、装系统、调驱动，玩家往往同时是使用者与维护者；显卡型号、声卡参数、内存配置这些知识，成了进入游戏的常识。开发一侧也开放得多，一个人或几个人就能写出一款游戏并直接发行，Wolfenstein 3D 与 DOOM 都出自十几人的团队。分享、复制与自制的风气，从这个结构里自然生长出来，也决定了后来 PC 游戏社区的形态。

对中国玩家而言，DOS 世代既近又远。一方面，仙剑奇侠传（1995，大宇资讯）、轩辕剑、金庸群侠传等中文作品在这里出现；另一方面，正版价格与渠道稀缺，让杂志攻略、电脑房与盗版光盘合集成了更普遍的入口。这部分在第 7 章单独展开。

## 2. 时代时间线

### 2.1 1981–1983：IBM PC 与开放架构

1981 年 8 月 12 日，IBM 在纽约发布 IBM Personal Computer（型号 5150），采用 Intel 8088 处理器、主频 4.77 MHz，售价 1565 美元（约合 2025 年的 5540 美元），运行微软提供、IBM 以 PC DOS 名义销售的 MS-DOS。项目由 William C. Lowe 与 Philip Don Estridge 主持，在佛罗里达州博卡拉顿完成。这台机器的一个例外做法是采用开放架构，处理器、操作系统与扩展卡都允许来自外部厂商；IBM 在两年内卖出超过 75 万台，远超内部预期。开放也带来后果：1982 年起，兼容机（clone）陆续出现，它们复制同一套 BIOS 接口与总线，成为此后十几年「PC 兼容」一词的来源。1983 年 3 月推出的 PC XT（5160）首次标准配置内置硬盘。

对游戏来说，起步时的硬件很朴素。原版 5150 只有单声道 PC speaker，一张 CGA 彩色显卡或单色 MDA 文本卡，最多两条软驱与五个扩展槽。文字冒险、飞行模拟、早期策略游戏是这时期的主要内容形态。受限于显示与声音，这些游戏更依赖文本与规则，而不是画面。

### 2.2 1984–1987：图形冒险与磁盘杂志

1984 年，Sierra On-Line 的 Roberta Williams 设计了 King's Quest，最初为 IBM PCjr 开发，随后推出普通 PC 版本。它用自行开发的 AGI（Adventure Game Interpreter）引擎，把可操作角色放进彩色背景，让冒险游戏从纯文字走向手绘动画画面；Sierra 约在 1988 年前后用 SCI 引擎替代 AGI。1987 年，Lucasfilm Games 为 Maniac Mansion 开发 SCUMM（Script Creation Utility for Maniac Mansion）引擎，于当年 10 月在 Commodore 64 与 Apple II 上推出，用鼠标点选动词与物品，这套界面一直用到 1990 年的 The Secret of Monkey Island 与之后的系列。

发行渠道在这一阶段也有变化。1987 年，Scott Miller 以 Kingdom of Kroz 试验「第一段免费、其余邮寄购买」的做法，成立 Apogee Software；同一时期，Softdisk 这类「磁盘杂志」按月把若干游戏装进软盘寄给订户，成为 id Software 几位成员后来的工作处。音乐与音效上，AdLib 声卡与 Roland MT-32 音源在 1987 年出现，PC 游戏开始支持 FM 合成与 MIDI。

### 2.3 1988–1991：类型成形与声响革命

1989 年是 DOS 世代的一个转折点。Maxis 的 SimCity 由 Will Wright 设计（开发始于 1985 年），在多家发行商因看不出商业前景而拒绝后，由 Broderbund 代理发行，起初卖得不快，靠媒体口碑带动，到 1992 年底累计约一百万份（家用电脑与 SNES 各约五十万）。同一年，Creative Technology 推出 Sound Blaster 1.0（代号 Killer Kard），以 Yamaha YM3812（OPL2）芯片提供 FM 合成并兼容 AdLib，PC 游戏音频从此有了统一的事实标准。1991 年 9 月，MicroProse 发行 Sid Meier's Civilization，由 Sid Meier 与 Bruce Shelley 设计，开发费用约 17 万美元；它把探索、扩张、开发、征服（后来被概括为 4X）放进一盘棋里，1992 年获得 Origins Award 的最佳军事/策略电脑游戏奖。

硬件上，Intel 80386（1985）与 80486（1989）让保护模式、更大内存与更快图形成为可能，VGA 在 EGA 之后接替成为主流显示标准，256 色与更高分辨率逐渐普及。IBM PC 兼容机在办公室与家庭同步铺开，PC 游戏的消费群体随之扩大。

### 2.4 1992–1993：shareware 爆发与 3D 起跑

1992 年 5 月，id Software 的 Wolfenstein 3D 由 Apogee 以 shareware 发行，第一段免费、后两段邮购，另由 FormGen 在 1992 年 9 月推出盒装的 Spear of Destiny。它在此后约一年半里为 Apogee 带来平均每月约 20 万美元收入，到 1993 年底 Apogee 版本与 Spear of Destiny 合计超过十万份，1995 年达到 25 万份、收入 250 万美元；到 1994 年年中，注册量约 15 万份，盒装 Spear of Destiny 另售出约 15 万份，id 估计全球分发出去的 shareware 拷贝约有一百万份，其中超过两成销量来自美国之外。PC Zone 引述的 shareware 经销商称，Wolfenstein 3D 是 1992 年最畅销的 shareware 作品。同年，Westwood Studios 的 Dune II 由 Virgin Games 发行，把资源采集、基地建设、迷雾与鼠标微操组合成即时战略的标准模板；Blue Sky Productions（后为 Looking Glass）与 Origin Systems 在 1992 年 3 月推出 Ultima Underworld: The Stygian Abyss，被吉尼斯世界纪录列为第一款全 3D 环境 RPG，也是「沉浸式模拟」一类作品的最早源头之一。法国 Infogrames 在 1992 年发行 Alone in the Dark，被广泛认为是最早的 3D 生存恐怖游戏。

1993 年 12 月，id Software 推出 DOOM，仍以 shareware 发布，第一段免费传播。它在两年内被估计安装到超过一千万台电脑上，注册版销量超过一百万份，发售即盈利，单日收入曾达 10 万美元，一天之内卖出了 Wolfenstein 3D 一个月的量；到 1999 年各版本合计约 350 万份，2002 年有估计认为玩过 shareware 版的人达 600 万，另有口径称发售两年内玩家人数在 1000 万至 2000 万之间。DOOM 也用 Novell 的 IPX/SPX 协议做局域网对战，让「死亡竞赛」在办公室与宿舍的局域网里流行起来；id 甚至向 IANA 申请把 666 端口登记给 DOOM。开发工具与 WAD 文件的开放，使玩家自制关卡成为风气。同年，Trilobyte 的 The 7th Guest 与 Cyan 的 Myst 把 CD-ROM 推成卖点，Myst 后来售出六百万份以上，成为 2002 年之前最畅销的电脑游戏。

### 2.5 1994–1995：RTS 与 FPS 主流化、光驱普及

1994 年 11 月，Blizzard 的 Warcraft: Orcs & Humans 发售，接着在 1995 年 12 月推出 Warcraft II: Tides of Darkness，把即时战略带进奇幻题材；Westwood 则在 1995 年 8 月 31 日推出 Command & Conquer，以 GDI 与 Nod、泰伯利亚资源为设定，到 1996 年 4 月销量 50 万份、9 月超过 100 万份，累计超过 300 万份。两家在这一年的竞争，把 RTS 从一个小众类型做成主流品类。id Software 的 DOOM II 在 1994 年以盒装零售方式发售，不再走 shareware，成为 1990 年代最畅销的盒装电脑游戏之一。

1995 年 8 月 24 日，微软发布 Windows 95，DirectX 开发套件同年推出，为游戏提供 AutoPlay、DirectPlay、Direct3D 等接口，PC 游戏开始向 Windows 迁移。CD-ROM 光驱在多媒体个人电脑（MPC）规格的推动下进入家庭，盒装游戏从几张软盘换成一张光盘，全动态视频与预渲染画面成为新的卖点。

### 2.6 1996：DOS 尾声与加速卡登场

1996 年是承前启后的一年。id Software 的 Quake、3D Realms 的 Duke Nukem 3D 与 Blizzard 的 Diablo 都在这一年推出，前两者把真 3D 与联网对战往前推，后者把动作角色扮演与随机装备带进新框架（三者的确切发售日期待核实）。微软在 1996 年 8 月 20 日推出 DOOM95，作为第一款 DirectX 游戏，证明了 Windows 可以顺畅地跑游戏。3dfx 在 1996 年底推出 Voodoo 3D 加速卡，Direct3D 在同年加入硬件加速，PC 游戏的画面竞争进入显卡时代，纯 DOS 环境则逐渐退居兼容模式。

## 3. 基础信息速览

### 3.1 平台基本参数

| 项目 | 内容 |
| --- | --- |
| 平台名称 | DOS 世代（IBM PC 兼容机 + MS-DOS） |
| 讨论范围 | IBM PC 兼容机硬件、MS-DOS 系统，以及在其上发行的电脑游戏 |
| 时代跨度 | 约 1981—1996 |
| 平台属性 | 开放架构个人电脑 + 命令行操作系统，非封闭游戏机 |
| 主要载体 | 5.25 英寸软盘、3.5 英寸软盘、硬盘、CD-ROM |
| 关键规格 | CPU 8088→80286→80386→80486→Pentium；显卡 CGA/EGA/VGA/SVGA；声音 PC speaker→AdLib/Sound Blaster/General MIDI |
| 官方销量口径 | IBM 5150 两年售出逾 75 万台（IBM 官方历史页）；PC 兼容机总装机量没有统一官方口径，第三方统计标准不一 |
| 历史定位 | 个人电脑游戏的奠基平台，现代游戏类型与发行模式的源头 |

### 3.2 历史定位速写

| 维度 | 速写 |
| --- | --- |
| 技术印象 | 命令行、640 KB 常规内存、手动配置 IRQ/DMA、软盘换盘 |
| 市场印象 | 办公机器的副产品，客厅主机之外的第二市场 |
| 软件印象 | 类型齐全、原创作密集、画面与音效迭代快 |
| 玩家文化 | 抄密码、看攻略本、局域网死亡竞赛、电脑城淘碟 |
| 历史评价 | 类型与发行方式的源头，历史地位远高于同期商业规模 |

### 3.3 关键词

IBM PC、MS-DOS、PC 兼容机、shareware、Apogee Software、id Software、Wolfenstein 3D、DOOM、DOOM II、WAD、Dune II、Command & Conquer、Warcraft、Ultima、Ultima Underworld、King's Quest、SCUMM、SimCity、Civilization、Myst、CD-ROM、Sound Blaster、AdLib、General MIDI、config.sys、autoexec.bat、HIMEM.SYS、EMM386、BBS、Computer Gaming World、大众软件、藏经阁。

## 4. 技术演进与硬件环境

### 4.1 处理器与整机

IBM PC 起步用 Intel 8088，一条 8 位外部总线跑 16 位内部运算，主频 4.77 MHz。1984 年的 IBM PC AT 换用 80286，1985 年的 80386 与 1989 年的 80486 依次带来 32 位运算、保护模式与浮点性能提升，1993 年的 Pentium 再上一层。同一时期，兼容机厂商把整机价格拉开，组装机（clone）成为主流购机方式。游戏对 CPU 的需求集中在整数运算与内存寻址，飞行模拟、实时策略与 3D 射击最先把 CPU 吃满。

值得注意的是，PC 在诞生时并没有为游戏设计专用图形与音频芯片，声音与画面的能力靠扩展卡一层层补上。这种「通用机器 + 外插板卡」的结构，既造成了配置门槛，也给了厂商与玩家自行升级的空间。

### 4.2 内存：640 KB 的战场

MS-DOS 运行在实模式下，程序能直接使用的常规内存只有 640 KB，640 KB 到 1 MB 之间的上位内存区留给显卡与系统 BIOS。随着 TSR（常驻内存程序）、鼠标驱动、光驱驱动与声卡驱动越装越多，留给游戏的空间被不断挤占，「内存不足」成为最常见的故障。

解决办法分两路。扩充内存（EMS）通过分页把 640 KB 之外的内存映射进常规内存窗口，早期由板卡实现，后来由 EMM386.EXE 用 80386 的虚拟 86 模式模拟；扩展内存（XMS）则由 HIMEM.SYS 管理 1 MB 以上的线性内存。玩家在 CONFIG.SYS 里写 DEVICE=HIMEM.SYS、DEVICE=EMM386.EXE、DOS=HIGH,UMB，在 AUTOEXEC.BAT 里放入鼠标与声卡驱动，再用 DEVICEHIGH/LOADHIGH 把驱动塞进上位内存块。第三方内存管理器 QEMM 也在这一时期流行。这些文件因此成了玩家最常手工编辑的文件，改错一行就开不了机。

### 4.3 显示：从 CGA 到 SVGA

IBM PC 最初的显示标准是单色文本的 MDA 与四色的 CGA，1980 年代中期的 EGA 提升到 16 色，IBM 在 1987 年的 PS/2 上引入 VGA，提供 256 色与 640×480 文本/图形模式。此后 SVGA 出现，分辨率与色彩进一步拉开，但缺少像 VGA 那样统一的模式定义，游戏往往要在安装时选择显卡型号，或依赖厂商提供的驱动。画面在这十年里从块状色块走到手绘背景、预渲染场景与早期真 3D，Myst 的 2500 多张预渲染图与 Ultima Underworld 的贴图 3D 是两端代表。

### 4.4 声音：从蜂鸣到声卡

最初的 PC 只有一枚 1 位 PC speaker，能发出单一频率的蜂鸣，早期游戏用它挤出声效与简单旋律。1987 年，AdLib 声卡以 Yamaha YM3812（OPL2）芯片提供 FM 合成，Roland MT-32 提供更高质量的音源，两者成为 PC 游戏音频最早的两种标准。1989 年，Creative Technology 的 Sound Blaster 在 AdLib 兼容的基础上加入数字采样播放，成为此后十余年 PC 游戏默认支持的声卡；1992 年的 Sound Blaster 16 带来 16 位、CD 音质输出，Gravis Ultrasound 与 General MIDI 也在同一时期推广。

声卡要占用中断（IRQ）与直接内存访问（DMA）通道，Sound Blaster 常见的默认设置为端口 220h、IRQ 7、DMA 1，一旦与其它板卡冲突，轻则没声音，重则游戏无法启动。玩家要在安装程序里手选这些参数，或改 AUTOEXEC.BAT 里的 SET BLASTER 环境变量。

### 4.5 存储：软盘、硬盘与 CD-ROM

DOS 世代的前半段靠软盘分发。5.25 英寸软盘常见容量为 360 KB 与 1.2 MB，3.5 英寸软盘为 720 KB 与 1.44 MB，大型游戏往往要三五张盘，安装与读盘成为体验的一部分。硬盘在 1980 年代末逐步进入家用机，减少了换盘。1990 年代上半段，CD-ROM 光驱随多媒体电脑规格进入家庭，一张光盘容量约 650 MB，足以容纳全动态视频与大量音轨，Myst 与 The 7th Guest 正是借它成名的作品。到 1996 年，盒装游戏的主流载体已从软盘转向光盘。

## 5. 游戏类型的奠基

### 5.1 第一人称射击与沉浸式模拟

第一人称视角并非 DOS 世代首创，但把它做成商品类型的正是这一代。id Software 的 Wolfenstein 3D（1992）用贴图墙面与快节奏射击，把「第一人称射击」变成可复制的玩法；DOOM（1993）在此之上加入更强的关卡设计、网络对战与开放数据文件，最终确定了 FPS 的基本结构。另一条路径是 Ultima Underworld（1992），它在真 3D 环境里融合角色扮演数值、物理互动与多解谜题，被追认为「沉浸式模拟」的鼻祖。此后 The Elder Scrolls、System Shock、Deus Ex 等作品，都能看出这两条线的延伸。

### 5.2 即时战略

Westwood 的 Dune II（1992）把资源采集、基地建设、战争迷雾与鼠标微操合成一套循环，成为后来所有即时战略的模板；它的欧洲名为 Dune II: Battle for Arrakis，Blizzard 的开发者事后直言 Warcraft 是在反复玩 Dune II 之后做出来的。Blizzard 的 Warcraft: Orcs & Humans（1994）与 Westwood 自己的 Command & Conquer（1995）把这一类型推向主流，两家的竞争在 1995 至 1996 年把 RTS 做成重要的电脑游戏品类。Warcraft II（1995）加入海军、空军与石油资源，Beyond the Dark Portal 资料片在 1996 年推出；Command & Conquer 到 1996 年 4 月销量 50 万份、9 月超过 100 万份，系列累计超过 300 万份。Age of Empires 等后续系列都明确以 Dune II 为起点。RTS 的鼠标操作与「指挥者视角」，也反过来影响了 PC 游戏界面设计。

### 5.3 电脑角色扮演

从 1980 年代初的 Wizardry、Ultima 与 Might and Magic 起，电脑 RPG 在 DOS 世代完成了数次转向。Richard Garriott（Lord British）在 1979 年以 Akalabeth 起步，1981 年的 Ultima I 奠定俯视探索加第一人称地牢的结构，1983 年成立的 Origin Systems 把系列做成公司招牌，公司口号是「We create worlds」。Ultima IV（1985）用诚实、慈悲、勇武等八德系统把道德选择写进主线，改变了 RPG 的叙事重心；1992 年的 Ultima VII 与 Ultima Underworld 分别代表俯视世界与第一人称 3D 两条路线。Ultima Underworld 由 Paul Neurath 设计、Warren Spector 制作，Origin 1992 年 7 月的内部通讯显示当时 Ultima VII 出货 7.1 万份、Underworld 出货 4.1 万份，此后 Underworld 靠口碑持续长卖，Neurath 称全球累计超过 50 万份，超过此前任何一部 Ultima。Interplay 的 Wasteland 把废土世界观带进 RPG，它影响了后来由部分原班人马参与的 Fallout。RPG 的存档、属性面板与装备系统，也在这一代定型。

### 5.4 图形冒险与解谜

Sierra 与 Lucasfilm Games 是两台发动机。Sierra 的 AGI/SCI 引擎产出 King's Quest、Space Quest、Leisure Suit Larry 等系列，走的是「输入指令、容易死亡」的路线；King's Quest 最初的开发平台是 IBM PCjr，销售目标之一是帮这台机器打开家用市场。Lucasfilm 的 SCUMM 引擎由 Aric Wilmunder、Chip Morningstar、Ron Gilbert 与 Brad Taylor 设计，从 Maniac Mansion（1987）到 Monkey Island（1990）再到 1990 年代中期，用点选界面与更宽容的设计降低了门槛；Maniac Mansion 开发约 18 至 24 个月，1987 年在芝加哥消费电子展亮相，由公司自办发行，成为此后作品惯例。1993 年，Myst 用 CD-ROM 上的 2500 多张预渲染图与第一人称解谜，把冒险游戏推向更广的非传统玩家群体，成为很长一段时间里最畅销的电脑游戏。

### 5.5 模拟经营与 4X

Maxis 的 SimCity（1989）提出没有固定胜负、以系统运转为核心的「软件玩具」，Will Wright 从 1985 年起开发，因缺少动作与关卡元素，多家发行商担心卖不动而拒收，最后由 Broderbund 代理，上市初期销售平淡，靠媒体评价与口碑翻盘，到 1992 年底累计约一百万份（家用电脑与 SNES 版各约五十万），SNES 版全球约 198 万份、其中日本约 90 万份。Will Wright 后来据此发展出 The Sims。MicroProse 的 Civilization（1991）把历史进程压缩成一局回合制棋，由 Sid Meier 与 Bruce Shelley 设计，开发费用约 17 万美元，上市时因公司管理层对 Meier 作品的态度而几乎没有宣传，全靠口耳相传，1992 年拿下 Origins Award 的最佳军事/策略电脑游戏奖，1995 年推出可七人对战的 CivNet；到 2016 年系列累计约 3300 万份、66 个版本。同一家公司还产出 Railroad Tycoon、Pirates!、Silent Service 等策略与模拟作品。飞行模拟方面，subLOGIC 的作品被微软引入 IBM PC，成为持续数十年的微软飞行模拟系列的起点（早期版本年份待核实）。模拟经营与策略在这一代成长为电脑最擅长的题材。

### 5.6 modding 与工具文化的起点

DOOM 的关卡数据打包在 WAD 文件里，id 在发售时就附带或放任关卡编辑器流出，玩家据此制作自制地图、替换贴图与声音，形成最早的规模性修改社区。这种「引擎与内容分离」的结构，让非开发者也能参与创作；后来 Duke Nukem 3D、Quake 沿用并扩展了这条路。id 还把引擎授权给其他厂商，Quake 引擎后来被多款射击游戏使用，其中一个授权产物最终成长为《半条命》。mod 与引擎授权的商业模式，源头都在这一代。

## 6. 发行与传播：shareware、BBS、杂志与光盘

### 6.1 shareware 与 Apogee 模式

shareware 的核心做法是把完整游戏切出一部分免费传播，靠口碑换来付费注册。Scott Miller 在 1987 年用 Kingdom of Kroz 试验这一套，方法是他自称的「三部曲」结构：第一段无条件免费，后两段需付费；这套做法被后来者统称为 shareware 或「Apogee 模式」。1989 年 Apogee 成为第一家专门发行他人 shareware 作品的公司，1991 年 Epic MegaGames 跟进采用同一模式。1990 年 12 月，Apogee 发行 id Software 的 Commander Keen，第一段免费、其余邮购，作者当月即拿到约一万美元版税，次年 1 月第二张版税支票为 2.5 万美元。Wolfenstein 3D 与 DOOM 沿用了这条路，也把 shareware 与 FPS 牢牢绑定。这套模式把发行成本压到极低，作者与发行商几乎不需要印刷与渠道，只要一条电话线、一间堆满软盘与邮包的房间，加上愿意寄支票的玩家。

### 6.2 BBS、邮购与盒装零售

在互联网普及之前，shareware 靠 BBS（电子公告板）与软盘传播。Apogee 运营自家的 Software Creations BBS，高峰期接入的分发网络覆盖五千多个 BBS，还连续两年被 Boardwatch 杂志读者评为最佳 BBS。玩家从 BBS 下载第一段，往出版商的信箱寄支票，换来软盘与说明书。Apogee 早期更接近一家接单公司，邮局甚至为它派过空卡车来装包裹。盒装零售则留给后期作品与大型发行商，id 在 DOOM II 时期才转向传统盒装渠道。

### 6.3 杂志、磁盘杂志与封面光盘

Computer Gaming World 等刊物在 1980 年代为电脑游戏提供评测与攻略，Softdisk 之类的磁盘杂志按月把游戏装进软盘寄给订户，本身就是发行渠道，其订阅制把一年若干款原创游戏打包收费（PC Gamer 记载的费用是全年 12 款共 89.95 美元）。进入 1990 年代，随刊附赠的演示光盘（covermount CD）成为新游戏的重要曝光方式，试玩版与 shareware 互相补充。媒体评价对销量影响显著，SimCity 靠口碑起量、Ultima Underworld 靠评测长卖，都是例子。

### 6.4 中文世界的传播渠道

中文地区的正版渠道狭窄，传播更多依赖杂志与线下。1994 至 1995 年，电子游戏软件（前身《GAME集中营》，1993 年夏推出，1994 年 5 月以现名正式创刊）、家用电脑与游戏机（1994 年 6 月创刊，双月刊，2001 年更名《家用电脑与游戏》）与大众软件（1995 年创刊）相继出现，构成中国大陆第一代游戏媒体；大众软件由北京前导软件有限公司参与创办并支持，社长边晓春、总编辑刘贫和，创刊号发行十万册，到 1998 年 5 月单期发行达 30 万册，最高单期约 38 万册。《电子游戏软件》在 1995 年 7 月曾被停刊处分，同年 10 月复刊并改副刊名。这些刊物的读者从杂志获取前瞻、攻略与评论，杂志也承担了作品在大陆的第一波传播：大众软件第三期刊出仙剑奇侠传攻略，当期销量随即上升。同一时期，前导软件自身也在做游戏，1994 年成立，开发了《官渡》《赤壁》等早期国产作品。线下则靠电脑城、软件市场与后来出现的电脑房，1999 年起流行的「藏经阁」系列合集光盘把这些作品成批带给玩家（该系列主体在 1999—2004 年，已略出本文时间范围，但属于这一代玩家的共同记忆）。

### 6.5 玩家当时怎样进入游戏

在 DOS 下启动游戏通常是一条命令。先进入安装程序，选择显卡型号与声卡参数，再调整内存配置；装完可能要重新编辑 CONFIG.SYS 与 AUTOEXEC.BAT，重启后再试。配色、音量、鼠标灵敏度写进各自的配置文件，出错就回到命令行重新来过。借软盘、换盘、抄下一串安装口令，以及为腾出几百 KB 常规内存反复重启，构成了那个时代的日常。

## 7. 为什么它重要，留下了什么

### 7.1 开放架构如何胜出

DOS 世代能够成立，前提是 IBM 没有把 PC 做成封闭系统。5150 允许使用外部处理器、外部操作系统与第三方扩展卡，兼容机厂商随即复制这一套接口。IBM 后来在 PS/2 上试图收回控制权，把输入输出集成到主板，但标准已经扩散，兼容机阵营与微软的操作系统共同定义了「PC」这个词。就游戏而言，这意味着开发者只为一个大体统一的软硬件平台写一次代码，就能覆盖尽可能多的机器，规模效应由此产生。

### 7.2 历史地位与市场结果的错位

在整个 DOS 世代，家用主机占据客厅，PC 游戏更集中在办公室与书房，商业规模并不占优。shareware 的转化率也低，id 曾估计只有约 1% 的下载者购买完整版，绝大多数人玩的是免费那一段。与此同时，PC 游戏的成本在 1990 年代上半段快速上涨，手绘背景与全动态视频都要逐帧制作，到 1993 年销售虽然稳步增长，增速却跟不上开发开支，连 Sierra 这样的大厂也开始出现亏损。影响并不随收入走：FPS、RTS、CRPG、冒险解谜、模拟经营乃至 modding 社区与引擎授权，都在这个「第二市场」里定型。留下的多，赚到的相对少，是这一代最明显的一组反差。

### 7.3 留下的东西

首先是一整套游戏类型模板，今天的 FPS、RTS、4X、点击式冒险、城市模拟仍能追溯到这一代的原作。其次是发行方式的雏形，shareware 的「免费试玩 + 付费解锁」逻辑，被后来的数字商店与免费游戏继承。第三是 modding 与引擎授权文化，WAD 与 id 引擎授权开了先例，后来采用 id 引擎授权的作品中成长出《半条命》。第四是「配置」这件事本身，显卡型号、声卡参数、内存管理成为玩家的常识，设置菜单与兼容选项也从这里起源。最后是联网对战的早期形态，IPX/SPX 局域网死亡竞赛是后来在线竞技的前身，id 为 DOOM 申请的 666 端口一直留在 IANA 的登记表里。CD-ROM 带来的多媒体演示与配乐，也让电脑第一次成为家庭影音设备的一种，这条脉络延伸到后来的 Windows 娱乐中心。

### 7.4 中文世界的 DOS 记忆

中文玩家的 DOS 记忆由几样东西组成：组装兼容机与 486、586 的攒机经验；UCDOS 等中文 DOS 环境；为声卡与内存反复改 CONFIG.SYS 的夜晚；以及一批中文作品——大宇资讯的仙剑奇侠传（1995 年 7 月在台湾上市，定价 720 新台币起，大陆正版约 160 元人民币）、轩辕剑系列，智冠科技的金庸群侠传（1996 年，确切日期待核实）等。传播上，盗版光盘合集、电脑房与杂志攻略是最常见的入口。这些经验让 DOS 世代在中国玩家那里不是一段技术史，而是一整代人的共同起点。

## 8. 一句话总结

DOS 世代没有赢下客厅，却用一台开放的办公机器和一套邮寄解锁的发行方式，把现代游戏的主要类型、mod 文化与 PC 游戏的基本规矩一并定了下来。

## 9. 参考资料

- IBM Personal Computer — Wikipedia：https://en.wikipedia.org/wiki/IBM_Personal_Computer（检索于 2026-10-18）
- The IBM PC — IBM 官方历史页：https://www.ibm.com/history/personal-computer（检索于 2026-10-18）
- Timeline of Computer History（1981）— Computer History Museum：https://www.computerhistory.org/timeline/1981（检索于 2026-10-18）
- id Software — Wikipedia：https://en.wikipedia.org/wiki/Id_Software（检索于 2026-10-18）
- Wolfenstein 3D — Wikipedia：https://en.wikipedia.org/wiki/Wolfenstein_3D（检索于 2026-10-18）
- Doom (1993 video game) — Wikipedia：https://en.wikipedia.org/wiki/Doom_(1993_video_game)（检索于 2026-10-18）
- The Shareware Scene, Part 4: DOOM — The Digital Antiquarian：https://www.filfre.net/2020/06/the-shareware-scene-part-4-doom（检索于 2026-10-18）
- Mail trucks and millions of dollars: how shareware transformed PC gaming forever — PC Gamer：https://www.pcgamer.com/mail-trucks-and-millions-of-dollars-how-shareware-transformed-pc-gaming-forever/（检索于 2026-10-18）
- 3D Realms / Apogee 官方历史页：https://legacy.3drealms.com/history2.html（检索于 2026-10-18）
- Apogee: Where Wolfenstein got its start — Polygon：https://www.polygon.com/features/2017/10/26/16511514/wolfenstein-origins-apogee/（检索于 2026-10-18）
- Dune II — Wikipedia：https://en.wikipedia.org/wiki/Dune_II（检索于 2026-10-18）
- Command & Conquer (1995 video game) — Wikipedia：https://en.wikipedia.org/wiki/Command_%26_Conquer_(1995_video_game)（检索于 2026-10-18）
- Warcraft: Orcs & Humans — Wikipedia：https://en.wikipedia.org/wiki/Warcraft:_Orcs_%26_Humans（检索于 2026-10-18）
- King's Quest I — Wikipedia：https://en.wikipedia.org/wiki/King%27s_Quest_I（检索于 2026-10-18）
- SCUMM — Wikipedia：https://en.wikipedia.org/wiki/SCUMM（检索于 2026-10-18）
- Maniac Mansion — Wikipedia：https://en.wikipedia.org/wiki/Maniac_Mansion（检索于 2026-10-18）
- Ultima IV: Quest of the Avatar — Wikipedia：https://en.wikipedia.org/wiki/Ultima_IV:_Quest_of_the_Avatar（检索于 2026-10-18）
- Ultima Underworld: The Stygian Abyss — Wikipedia：https://en.wikipedia.org/wiki/Ultima_Underworld:_The_Stygian_Abyss（检索于 2026-10-18）
- Civilization (video game) — Wikipedia：https://en.wikipedia.org/wiki/Civilization_(video_game)（检索于 2026-10-18）
- SimCity (1989 video game) — Wikipedia：https://en.wikipedia.org/wiki/SimCity_(1989_video_game)（检索于 2026-10-18）
- Will Wright — Computer History Museum：https://computerhistory.org/profile/will-wright（检索于 2026-10-18）
- Sound Blaster — Wikipedia：https://en.wikipedia.org/wiki/Sound_Blaster（检索于 2026-10-18）
- Sound Blaster: Our Story — Creative 官方页：https://us.creative.com/soundblaster/ourstory（检索于 2026-10-18）
- Myst — Wikipedia：https://en.wikipedia.org/wiki/Myst（检索于 2026-10-18）
- Unparalleled Industry Support for Gaming on Windows 95 — Microsoft 新闻稿（1996-05-16）：https://news.microsoft.com/source/1996/05/16/unparalleled-industry-support-for-gaming-on-windows-95-makes-it-the-gaming-platform-of-choice-for-1996（检索于 2026-10-18）
- 大众软件 — 中文维基百科：https://zh.wikipedia.org/zh-hans/大众软件（检索于 2026-10-18）
- 家用电脑与游戏 — 中文维基百科：https://zh.wikipedia.org/wiki/家用电脑与游戏（检索于 2026-10-18）
- 电子游戏软件 — 中文维基百科：https://zh.wikipedia.org/wiki/电子游戏软件（检索于 2026-10-18）
- 游戏档案参考（第一、二期）— gamearchive.cn：http://gamearchive.cn/game_archive_journal_vol1/section_4_3（检索于 2026-10-18）
- 普罗米修斯消亡史 — 界面新闻：https://www.jiemian.com/article/1044575.html（检索于 2026-10-18）
- 哎哟！要盘吗？！关于《藏经阁》— 机核 GCORES：https://www.gcores.com/articles/115433（检索于 2026-10-18）
