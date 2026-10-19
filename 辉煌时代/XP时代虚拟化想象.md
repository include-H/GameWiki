# XP 时代的虚拟化想象：随身化、便携化与网吧化

> 说明：本文为面向中文读者整理的虚拟化技术史辨析专题。讨论范围以 2003—2010 年为主，即 Windows XP 作为事实上的公共桌面的时期，并把它与 2010 年以后以服务器虚拟化、容器、隔离与安全为主线的路线并置对照。整理内容包括 U 盘上的便携工作区（U3、Ceedo、MojoPac、PortableApps）、中文语境的"绿色软件"、网吧与学校机房的使用条件、还原卡与沙盒类工具，以及后来被倒灌回这段历史的概念（KVM、Hyper-V、容器、Kubernetes、VBS、TEE）。主要依据为可公开检索的英文报道、厂商公告与百科条目，检索时间为 2026 年 10 月。写作期间检索接口只在一个短窗口内可用，凡未能独立复核的具体年份、数字与产品细节，已在正文与文末标注「待核实」。本文区分事实、推断与评价三类陈述，不作产品优劣判断。

:::epigraph
那几年，一块 128MB 的 U 盘别在钥匙串上，插进哪台机器，哪台机器就短暂地成了自己的。
壳是别人的，字是自己打的；桌面弹出来，拔走以后什么都不留。
同一间网吧里，几十台机器轮流做过几十个人的桌面，
而每个人真正想带走的，其实只是自己那份习惯。
:::

---

## 一、先把"虚拟化"这个词的两种用法分开

在 2020 年代谈"虚拟化"，第一反应通常是 KVM、Hyper-V、容器、Kubernetes、虚拟化安全（Virtualization-Based Security，VBS）与可信执行环境（Trusted Execution Environment，TEE）。这套语汇的服务对象是数据中心、开发流水线与攻击者模型。本文要讨论的却是另一件事：在 Windows XP 当家的那几年，普通用户对"虚拟化"的想象，是以"把自己的数字环境带走"为中心的——把桌面、软件、设置、存档和聊天记录装进一块 U 盘，插到任意一台公用电脑上继续用。

两种想象共用"虚拟化"这个词，动机与工程路径都不相同。前者要解决的是"一台物理服务器怎么切成许多台逻辑服务器""如何在不互信的前提下共享资源"；后者要解决的是"只借这台机器坐一会儿，怎么让桌面还是我的"。用今天的云、容器与零信任去解释 2000 年代中期的 U 盘便携软件，是把后来的需求倒灌回过去。

当年中文电脑语汇里的"虚拟"，有它自己的常见搭配。"虚拟光驱"是把光盘镜像挂成盘符，用来免去换盘与保护光驱；"虚拟内存"是用硬盘上的页面文件补足物理内存；"虚拟桌面"在很多工具里指同一台机器上的多个工作区；"虚拟机"则指用 VMware Workstation 或 Virtual PC 在 XP 里再装一个系统，多用来试装 Linux 或测试新软件。这些用法里，"虚拟"大体带着"临时的、替代的、不占实物的"意味。而"把我的环境带走"这件事，当年更常出现在"便携""绿色""随身"这些词下面，未必挂"虚拟化"的招牌。

本文的命题是：XP 时代对虚拟化的想象，重心在随身化、便携化与网吧化；今天虚拟化的主角变成了云、容器、隔离与安全。两种想象的差别，可以概括为"借机器"与"借资源"的差别，也是两种社会技术条件的差别。

## 二、XP 时代的使用条件

要理解那套想象，先要理解它的前提：一台机器、一个本地账户、一次安装。

Windows XP 的账户体系是本机的。登录窗口核对的是这台硬盘上的账户与密码，用户配置文件放在本机的 `C:\Documents and Settings` 下。跨机器延续身份的做法，主要出现在装了域的企业里，靠漫游用户配置文件和文件夹重定向实现，由域控制器在登录时把个人配置投放到本机。对绝大多数家庭与网吧用户，换一台机器意味着重新配置一遍：桌面壁纸、输入法、浏览器书签、聊天软件好友列表、游戏按键与存档，一样都不会跟着走。

那几年正是移动存储换代的时点。软盘与刻录光盘逐步让位给 U 盘（USB 闪存盘）。U 盘没有机械部件，容量从几十兆升到几吉字节，插到任何一台带 USB 口的机器上都会作为一个盘符出现，不需要驱动。2005 年 9 月，SanDisk 随首批 U3 智能盘公布的售价是 512MB 54.99 美元、1GB 99.99 美元，容量与价格已经进入普通用户能接受的范围。硬件条件具备了，"把东西随身带"从数据层面（文档、照片）向环境层面（软件、设置）延伸。

公用电脑是这套想象最真实的舞台。学校机房、公司前台机、图书馆检索机、街边网吧，装的是同一代 Windows XP，却几乎不给管理员权限，也几乎都装了某种保护或还原机制。用户能在这些机器上做的事被压到很窄：能上网、能编辑、能玩，但装不了自己的软件，重启之后一切归零，上一次用完留下的浏览记录还留在机器上。

最后一层条件是 XP 时代软件的"安装"成本。一个程序要能正常运行，往往要把文件写进 `C:\Program Files`，把配置写进注册表，把用户数据写进 `%APPDATA%` 或"我的文档"，还要登记组件对象模型（Component Object Model，COM）之类的系统级组件。个人状态散落在系统的好几处，任何一处搬不走，程序在别的机器上就可能报错或恢复成默认值。要"带着环境走"，必须先解决两个工程问题：程序怎么在不安装的情况下运行，以及它的状态该写到哪里。

## 三、把桌面装进 U 盘：四条产品线

围绕上面两个问题，2004 到 2008 年间出现了几条互不相同的技术路线。它们的目标一致——让"自己的桌面"跟着 U 盘走——但对"虚拟化层放在哪里"给出了不同答案。

### 3.1 U3：把 U 盘变成应用平台

U3 由闪存厂商 SanDisk 与 M-Systems 共同发起。两家公司在 2004 年 9 月 7 日宣布战略合作与专利交叉授权，要把标准 U 盘从"存储设备"升级为"软件分发平台"；2005 年 1 月的国际消费电子展（CES）上，U3 作为独立公司正式亮相。同年 3 月，Kingston、Verbatim 与 Memorex 成为首批硬件伙伴，分别把 U3 放进 DataTraveler、Store 'n' Go 与 TravelDrives 产品线；9 月 19 日的 DEMOfall 上，Verbatim 与 Memorex 首批出货，Kingston 与 SanDisk 随后跟进，设备于 10 月 15 日上市。

U3 的形态是一套装在盘上的启动器（Launchpad）。插上盘后，启动器自动弹出菜单，列出盘上已安装的 U3 程序，并提供下载、添加与移除功能。U3 系统软件本身占约 6MB，插上后约 30 秒加载完成。用它运行的程序必须为 U3 改造过，写完的数据与设置留在盘上；拔盘时，系统会关掉正在运行的程序并清掉残留，浏览器 Cookie 之类的东西存在盘上而非宿主机。U3 官方口径把它描述为"个人工作区"：文件、程序、密码与设置都在一块口香糖大小的设备里，插到任意一台 Windows XP 或 2000 机器上，用完走人，宿主机不留个人数据。

U3 的约束也在这里。它要求硬件带 U3 标识、软件为 U3 适配，两边都被锁进同一套授权体系；它只支持 Windows，Linux 版本长期停留在"开发中"；因为要在盘上跑完整应用，USB 接口的读写速度直接决定体验。U3 后来停止运营（时间待核实），这套"平台 + 授权"的路线没能成为通用标准。

### 3.2 Ceedo：在用户态重定向

Ceedo 由以色列公司 Ceedo Technologies（2005）Ltd. 于 2005 年推出，创始人 Dror Wettenstein，总部在内坦亚。它的思路与 U3 相反：不要求特殊硬件，也不要求应用改造，而是在宿主 Windows 上装一层用户态的重定向机制，把程序对文件与注册表的读写改写到 U 盘上，从而让未改造的常见 Windows 程序也能"带着走"。2006 年 1 月的 CES 上，Lexar 用它做成了 PowerToGo，预装在 Platinum 系列 U 盘上，1GB 型号 53 美元。Ceedo Personal 定价约 40 美元，占用约 2 到 3MB。

Ceedo 的技术要点是"截获再改写"。Verbatim 捆绑产品的测评把它描述为：软件截获程序试图写入宿主机的注册表项，把它们改道到 Ceedo 盘上，让程序据此正常运行。代价是隔离并不彻底：有用户报告，把 Firefox 装到 Ceedo 盘上、换一台电脑运行时，它会读到宿主机自己那份 Firefox 的书签，新存的书签也会出现在宿主机版本里。Ceedo 后来推出面向企业的 Ceedo Enterprise（2008 年），并在同年与 Citrix 合作，为 XenApp 做便携客户端；公司此后经历多年停滞后于 2016 年转向网络安全产品。

### 3.3 MojoPac：把第二张桌面借来

MojoPac 出自美国 RingCube Technologies，2006 年 9 月在 DEMO 展会上作为消费产品发布，并被评为展会最受关注的产品之一。它与前两者的差别在于隔离层次更深：被称为内核态虚拟化，会在宿主机上启动第二个 Windows 桌面，有自己的壁纸、图标与外壳，屏幕顶端留一条 MojoBar 用来在宿主桌面与 MojoPac 桌面之间切换。盘里的 `C:` 是一个虚拟硬盘，宿主机的盘符在 MojoPac 环境里不可见；用户可以在其中照常运行安装程序，把 Office、Photoshop、Firefox 装进盘里，而这些操作不会落到宿主机的文件系统。

MojoPac 刻意不带操作系统副本，它借的是宿主机的 Windows XP。RingCube 的首席执行官 Shan Appajodu 用体积说明这种取舍：MojoPac 的虚拟化文件只有 26 到 28MB，而 VMware ESX Server 或微软 Virtual Server 搭出的虚拟机往往要 250MB 左右，因为后者把操作系统一起装了进去。2006 年的评测提到，一块 128MB 的 U 盘就够装一套 MojoPac 环境；也有玩家把魔兽世界、半条命 2 这类游戏装进盘上运行。2007 年 10 月 2 日，RingCube 追加了免费版 MojoPac Freedom；2008 年 12 月 5 日发布 2.0 版；企业线衍生出 MojoDrive（把虚拟桌面放进盘里，99 美元）、MojoNet（放在公司服务器供下载）与 MojoStation（在公司网站下载，49 美元）。

MojoPac 的最大门槛是权限。1.0 版要求宿主机上的管理员权限，否则连启动都不行；这恰好挡住了它最想服务的人——在公司与学校用受限账户的用户。官方为此提供了 MojoPac Usher，需要在受限制环境里由管理员先登录一次；面向普通受限用户的版本一直在开发中却没如期交付。它也只支持 32 位 Windows XP Home／Pro／Media Center／Tablet PC，Windows 2000 不支持，Vista 的支持计划最终没有实现。MojoPac 的隔离强度弱于完整机器虚拟化：有资料指出，用户对 MojoPac 系统文件的改动可能反映到宿主机的同名文件上，公司称这是已知缺陷。RingCube 后来被 Citrix 收购（时间待核实），MojoPac 官网一度跳转到 Citrix。

### 3.4 PortableApps.com：不改系统，改程序

与上述三条"加一层"的路线并列，还有一条"改程序本身"的免费路线。2004 年 3 月，John T. Haller 在 mozillaZine 论坛上做了一个便携版 Firefox：Firefox 0.7 以后提供了 `-profile` 参数，可以把用户配置目录指到别处，于是他写了一个批处理，把浏览器与配置打包，之后陆续扩展到 Thunderbird、NVU、Sunbird 与 OpenOffice.org。2005 年 11 月起他接受捐赠，同年 12 月把项目搬到一个社区站点，PortableApps.com 上线。

PortableApps 的做法是把程序"绿色化"：让启动器在运行时修正路径、临时生成需要的注册表项、在退出时清理，让程序把设置写在自身目录里。它不提供跨机器的隔离层，也不接管整个桌面，但免去了 U3 的硬件绑定与 Ceedo 的授权费用。到 2009 年，这套集合已包含 Skype 与 Google Chrome 的便携版，其平台格式发布 1.0 版本；PortableApps.com 后来累积的下载量以十亿计。

### 3.5 两条技术路线的分野

把四条产品线并排看，分野清楚。U3、Ceedo、MojoPac 属于"虚拟化"路线：在宿主系统与程序之间加一层，截获并改写文件与注册表访问，代价是需要权限、需要适配、隔离程度有限。PortableApps 属于"便携化"路线：不动系统，只改程序的路径与存储习惯，代价是并非所有程序都能这么改，功能受限的程序尤其难办。两条路线共享同一个目标——让程序不安装也能运行、让状态跟着盘走——却走向了不同的工程折中。XP 时代对"虚拟化"的民间想象，正是长在这两条路线上。

## 四、绿色软件：中文语境里的便携

在中文互联网里，"便携软件"有个更早、更本土的名字——绿色软件。

中文维基的条目把绿色软件定义为：多数免费、无需安装即可使用、可存放在可移除式存储媒体（如 U 盘）上、移除后不在本机留下注册表记录的小型软件。条目还记下了命名的来由：起初指"不会在使用者的电脑上留下难以清除的冗余信息的软件"，和环保里"不弃置污染物"的联想有关，命名背景与中国当时恶意软件泛滥的环境直接相关。这个来由很能说明问题——在中文语境里，"绿色"首先是一种对系统洁净的诉求，其次才是便携。

围绕这个诉求，形成了整条检索与下载生态。"绿色软件联盟"这类站点按类别罗列免安装程序并标注更新时间，例如 2005 年 5 月的更新列表里就有局域网共享工具、BitComet 绿色版等条目。2005 年前后，还流行过整张"绿色软件光盘"：一位用户在网上贴出的目录长达数百项，从 AutoCAD 2002、Photoshop CS、Microsoft Office 组件，到千千静听、金山词霸、QQ2005，几乎都做成"绿色汉化版""精简免安装版"，再以 BT 方式分发。这些盘里既包含开放源代码软件的正规绿化，也包含把商业软件改造成免安装并免费散发的"绿化版"，后者在版权上是明确的灰色地带，中文维基条目也点明了这类侵权情形。

绿色软件在公用电脑场景里的实际用途很清楚：既然改不了机器，那就改软件。把 QQ、输入法、播放器、下载工具做成免安装版塞进 U 盘，插到网吧或机房的机器上直接运行，走的时候连设置一起带走。腾讯 QQ 在那些年里是这套做法的核心标的：QQ 的账号体系在服务器上，任何时候在任意一台机器登录都能找回好友列表，真正留在本机、需要随身带的，是聊天记录与本地设置。U 盘里的"随身 QQ"，把云端身份与本机桌面之间那道缝，用一块移动存储暂时补上。

## 五、网吧、学校机房与公用电脑

公用电脑在中国的最典型形态是网吧。2000 年代中期的网吧是清一色的 Windows XP，几十台同型号机器排成两排，收银台用一套网管软件计费、限时、锁定桌面，机器上普遍装还原卡或还原类软件——关机重启后系统盘回到初始状态，玩家装的东西一律消失。学校机房、办公前台机用的是同类思路，只是换成保护卡或域策略。这套配置的出发点是把机器变成"公用设施"：谁都能用，用完即净，运维成本低。

这种配置制造了本文关注的那个具体需求。玩家在网吧把游戏装到本机，下次换一台机器就得重装；存档在本地，换机就丢；想用自己习惯的输入法与聊天记录，得随身带。对这批人，"把自己的环境装进 U 盘"不是抽象的技术兴趣，是每天要解决的现实问题。也有一部分人选择了另一条路——直接玩网吧里已经装好的游戏，用服务器上的账号登录，让存档留在服务端。这两条路线的消长，后来决定了便携桌面的命运。

网吧的普及也带来监管。2002 年北京发生"蓝极速"网吧火灾，随后国务院于当年出台《互联网上网服务营业场所管理条例》，将网吧纳入许可与实名管理（具体日期待核实）。监管与经营压力推高了网吧的规范化程度，也让"机器一律还原、一律统一"的运维方式更加普遍。

## 六、并行的一条线：沙盒、还原与"试用"

U 盘路线之外，XP 时代还有一组共享"不留痕"动机、方向却相反的技术：它们保护的不是"带走的我"，而是"被借用的机器"。

最朴素的是系统还原。Windows Me 与 Windows XP 内置的系统还原会定期拍摄系统快照，出问题时回滚。网吧与机房用的还原卡、还原精灵、冰点还原（Deep Freeze）把这件事做得更彻底：把系统盘置于写保护或重定向状态，重启即恢复（各家产品名称与首发年份待核实）。对用户而言，效果与沙盒相近：怎么折腾都不怕，重启就好。

个人机上，Sandboxie 是这条线里最有代表性的工具。它在 XP 上把程序的文件与注册表写操作重定向到一个沙盒目录，程序以为自己在正常读写，实际改动被关在沙盒里，可以随时清空（作者与首发年份待核实）。影子系统、PowerShadow 一类工具的思路类似，把整块系统盘变成可回滚的影子（待核实）。

虚拟机在个人机上的早期用途也属于这一类。用 VMware Workstation 或 Virtual PC 在 XP 里再装一个系统，主要目的是"试装"：试试 Linux 发行版，试试来路不明的软件，出了问题直接删掉虚拟机文件。在中文电脑杂志的语境里，这时的"虚拟机"就是一个安全的试验场，而不是数据中心的基础设施。

这批工具共享一套直觉：让改动可以被撤销，让"用过"不留痕迹。把它和 U 盘路线放在一起看，会发现两者其实是同一需求的两面——都想要"这台机器不是我的，我的东西必须能干净地进出"，只是一个选择把环境带走，一个选择把环境就地关进笼子。

## 七、倒灌一：服务器虚拟化的谱系

把话头从 U 盘转开，来看今天被称为"虚拟化"的那条主线。它比 XP 早得多，服务对象也完全不同。

虚拟化的起点在大型机。IBM 在 1960 年代就在大型机上做分时共享，1972 年的 VM/370 能把一台机器切成多台逻辑机器。个人机时代，Connectix 于 1997 年推出 Virtual PC（2003 年被微软收购），VMware 由 Diane Greene、Mendel Rosenblum 等人在 1998 年创立、1999 年推出 Workstation，2001 年推出不依赖宿主操作系统的 ESX Server，把虚拟化监控器（hypervisor）直接架到服务器硬件上。2003 年，Fabrice Bellard 发布 QEMU，Xen 从剑桥大学的研究项目成形；2006 年，Avi Kivity 在 Qumranet 启动 KVM，次年并入 Linux 内核；2008 年，微软随 Windows Server 推出 Hyper-V。2003 年 Windows 服务器版还出现过 Virtual Server 产品线（时间待核实）。

这条线的动机一贯而清楚：把一台物理服务器的算力切给多个工作负载，提高利用率，靠隔离让互不信任的租户与业务共存，把运维从"修机器"变成"管镜像"。它的客户是数据中心与软件团队，不是别着 U 盘的个人。把它写成 XP 时代虚拟化想象的主角，是时间顺序与动机的双重错位。

需要认清一处容易混淆的相似：MojoPac 在宣传里借用了"虚拟机"的类比（虚拟硬盘、第二个桌面），技术上却不模拟硬件、也不运行独立的操作系统内核，它借的就是宿主机那份 XP。它和 ESX、KVM 的差别，正是"借机器"与"借资源"的差别。

## 八、倒灌二：容器与云

今天大众语境里的"虚拟化"，很大一部分其实是容器，而不是虚拟机。

容器这条路线的根更早：Unix 的 `chroot` 从 1979 年前后就有了，把进程的文件系统视图锁在一棵子树里；FreeBSD 在 2000 年推出 jail（时间待核实）；Solaris 在 2004 年推出 Zones（时间待核实）。2000 年代中后期，Google 的工程师（Paul Menage、Rohit Seth 等人）把进程分组与资源限额做进 Linux 内核，形成 cgroups（时间待核实）；2008 年出现了 LXC；2013 年，Solomon Hykes 所在的 dotCloud 把容器工具以 Docker 之名公开，2014 年 Google 发布容器编排系统 Kubernetes。

容器要解决的是"同一个内核上，怎么让许多进程彼此看见的世界不同、资源配额不同"。它不启动第二个内核，也不借宿主的 Windows，而是让进程共享操作系统内核、隔离命名空间与文件系统。这与"把桌面装进 U 盘"在工程上几乎不相干。云则把"借"推到了资源层：算力、存储、网络、数据库都从别处租，用户端退化为浏览器或瘦客户端。XP 时代那句"插到哪台机器上都是我的桌面"，在今天被改写成"登录哪个账号都到我的工作区"——环境被做成了镜像与账号，放进了数据中心，而不是塞进一块 U 盘。

## 九、倒灌三：隔离、安全与身份

虚拟化在 2000 年代中后期还多了一层用途：隔离与安全。这一层后来成为今天"虚拟化"叙事里最显眼的成分。

先是恶意软件用上了虚拟化。2006 年，研究人员演示了把恶意程序藏进轻量虚拟监控器、让操作系统以为自己独占硬件的做法（"蓝色药丸"与 SubVirt 一类研究，细节待核实）。虚拟化第一次被明确地当成"制造看不见的隔离层"的工具，而不只是"多跑几个系统"的手段。

接着是硬件与系统把隔离做进底座。ARM 在 2004 年前后引入 TrustZone，把处理器分成安全与非安全两个世界；Intel 在 2015 年的 Skylake 世代推出软件保护扩展（Software Guard Extensions，SGX），让程序在处理器内划出受保护的飞地；AMD 在 2016 到 2017 年间推出加密虚拟化（Secure Encrypted Virtualization，SEV）。系统侧，Windows 10 在 2015 年起用基于虚拟化的安全（VBS）支撑凭据保护（Credential Guard）与设备保护（Device Guard），把一部分系统状态放进由 hypervisor 隔离的环境；2019 年的 Windows 10 1903 又带来了基于 Hyper-V 的 Windows Sandbox，让普通用户也能一键开一个用完即弃的隔离桌面。

与之并行的是身份与访问控制的转向。"零信任"这个概念由 Forrester 的 John Kindervag 在 2010 年前后提出，Google 的 BeyondCorp 在 2014 年公开，主张不再以"在不在内网"作为信任依据，而按每次请求做验证。它让"隔离"从机器的属性变成了身份与流量的属性。

这一路的服务对象是攻击者模型与合规要求，不是"我要在网吧用我的输入法"。不过，把 VBS 与 Windows Sandbox 拿来和 MojoPac 对照，会发现一种奇特的呼应：同样是"在别人给的系统里开一块自己的地盘"，两个时代的实现方向完全相反——一个把地盘建在随身的盘上、借宿主的硬件，一个把地盘建在宿主的处理器与内核里、由硬件强制隔离。前者服务于"借用公用电脑的人"，后者服务于"保护企业数据不被内鬼与恶意软件碰"。这正是"借机器"与"借资源"的差别在安全层的投影。

## 十、借机器与借资源

把两条线索并到一处，差别可以落到一句话上。

XP 时代的便携桌面，本质是"借机器"。U 盘里装的是"我的状态"——桌面布局、软件、设置、存档；运行所需的处理器、显卡、内存、网络、甚至 Windows 本身，全部来自当场那台公用电脑。它成立的前提是一组物理条件：能摸到机器、插得上 USB、拿得到管理员权限、宿主是兼容的那一代 Windows。它的失败点也全在这里——权限不够就跑不起来，换一代系统就未必兼容，宿主机上的一枚键盘记录器就能把密码拿走。

今天的虚拟化主角，本质是"借资源"。算力、存储、网络都在别处，用户端退化成浏览器或客户端；"我的环境"以镜像、容器、账户与策略的形式存在，由别处的编排系统调度。它成立的前提换成了另一组条件：网络可达、身份可信、计费成立。物理接触、管理员权限、硬件兼容，这一组旧前提在新路线里几乎不再重要。

"桌面"这个词的迁移最能说明问题。XP 时代说"虚拟桌面"，多指同一台机器上的多个工作区（微软在 XP 时代提供过虚拟桌面管理器，第三方有 Dexpot、VirtuaWin 一类工具，细节待核实）。同一个词到了 2010 年代，指的却是把桌面放进数据中心、以远程协议流式送给瘦客户端的"桌面虚拟化"（Virtual Desktop Infrastructure，VDI）。VMware 在 2006 年前后推出桌面虚拟化产品，Citrix 在 2008 年推出 XenDesktop（时间待核实）。值得注意的是，做 MojoPac 的 RingCube 最终被 Citrix 收购（时间待核实）——那家把"随身桌面"做成生意的公司，最后并入了把桌面搬进数据中心的那条线路。"桌面带走"这件事还在，只是方向掉了个头：过去从公用电脑带回家，今天从数据中心送到任意终端。

## 十一、中国的特殊性与今天的回望

如果只看英文报道，U 盘便携软件更像一类面向差旅者与校园用户的工具：路透社 2008 年的报道把它描述成"在公用电脑上不留痕迹"的手段，纽约时报 2006 年的专栏把 Lexar PowerToGo 推介给需要在多台机器间切换的人，工程师社区则把它当作"在任何别人的机器上继续编码"的便利。中国的情况有几处不同。

其一，公用电脑的密度更高。网吧、学校机房、单位前台机在 2000 年代中期的中国市场里比许多地区更常见，且制式高度统一（清一色 XP、清一色还原）。这让"随身桌面"从一种小众便利变成一批人的日常刚需。

其二，移动存储的普及有其本地的产业背景。U 盘启蒙在中国与本土厂商的专利与品牌高度绑定（朗科等厂商的闪存盘专利与"优盘"品牌，细节待核实），价格下行与普及速度快，U 盘很快成为学生与网吧用户的标配。

其三，中文互联网长出了一套围绕"免安装"的内容生态：绿色软件联盟式的下载站、"绿色软件光盘"式的 BT 合集、汉化与绿化改造。这套生态既满足了"在公用电脑上用我的软件"的真实需求，也在商业软件版权上留下了大面积灰色地带，并在此后演变成捆绑安装等更受诟病的形式。

其四，乡村与城镇网吧里的"随身 QQ"是许多人对"账号跟着人走"的最早体验。网友在网吧登录 QQ，好友在服务器上；下一次换台机器，只要账号密码对，人就回来了。这是中国用户最早接触到的"云端身份"，而它旁边的桌面仍然是彻底本地的。身份云化、桌面本地化，这种错位正是 XP 时代中国互联网体验的一个缩影。

今天回望，随身化、便携化、网吧化的那套想象并没有消失，只是换了载体。浏览器取代了安装包，"登录即可"取代了"插盘即可"，云盘与同步取代了 U 盘里的 `My Documents`。真正被保留下来的，是那句朴素的直觉：换一台机器，我也应该还是我。XP 时代用一块 U 盘去兑现它，今天用一个账号去兑现它；两种兑现方式背后的社会技术条件不同，想象的内核却惊人地一致。

## 参考资料

以下为本文检索与核对时实际返回的来源，检索时间为 2026 年 10 月。本次写作期间检索接口仅在短窗口内可用，标注「待核实」的条目为未能独立复核者。

U 盘便携工作区（U3、Ceedo、MojoPac、PortableApps）：

- Reuters，《PluggedIn: Virtual PCs add new layer of security》（2008-01-03，含 MojoPac 借宿主 XP 资源、不留痕的描述）：https://www.reuters.com/article/marketsNews/idUKN0322939520080103/
- Engadget，《Take your PC anywhere with RingCube's MojoPac software》（2006-09-26，MojoPac 试用与定价）：https://www.engadget.com/2006-09-26-take-your-pc-anywhere-with-ringcubes-mojopac-software.html
- VMblog，《Virtualize Your Desktop On Any PC With MojoPac》（2007-08-22，MojoPac 体积、企业线与权限要求）：https://vmblog.com/archive/2007/08/22/virtualize-your-desktop-on-any-pc-with-mojopac.aspx
- Wikipedia，《MojoPac》（产品机制、版本、Windows XP 依赖与隔离局限）：https://en.wikipedia.org/wiki/MojoPac
- ITmedia（＠IT），《ポータブル仮想デスクトップ環境「MojoPac」が無償版を公開》（2007-10-04，MojoPac Freedom 与 U3、Ceedo 的比较）：https://atmarkit.itmedia.co.jp/news/200710/04/mojopac.html
- MCPmag，《Windows XP To Go》（2006-10-24，MojoPac 安装步骤与 128MB 盘可行性）：https://mcpmag.com/articles/2006/10/24/windows-xp--to-go
- Engadget，《U3 launches platform for flash drives》（2005-09-19/20，U3 设备上市时间与价格）：https://www.engadget.com/2005-09-19-u3-launches-platform-for-flash-drives.html
- The Register，《U3 launches USB drive-hosted app 'standard'》（2005-01-07，U3 由 SanDisk 与 M-Systems 成立、CES 正式发布）：https://www.theregister.com/on-prem/2005/01/07/u3-launches-usb-drive-hosted-app-standard/440015
- SanDisk 新闻（phys.org 转载），《SanDisk to ship units of its first 'U3 smart' flash drive》（2005-09-19，Cruzer Micro 规格与售价、Launchpad）：https://phys.org/news/2005-09-sandisk-ship-u3-smart.html
- U.S. SEC，M-Systems 6-K（2004-09-07，SanDisk 与 M-Systems 合作与专利交叉授权）：https://www.sec.gov/Archives/edgar/data/895361/000089536104000039/msystems6k04october2004.htm
- TWICE，《U3 Partners With Kingston, Verbatim, Memorex》（2005-04-04）：https://www.twice.com/news/u3-partners-kingston-verbatim-memorex-28191
- The Register，《U3 signs first USB Flash drive makers》（2005-03-22）：https://www.theregister.com/off-prem/2005/03/22/u3-signs-first-usb-flash-drive-makers/1033026
- ITWorld Canada，《U3, partners add intelligence to USB drives》（2005-09-20，CEO Kate Purmal 口径、系统软件体积与加载时间）：https://www.itworldcanada.com/article/u3-partners-add-intelligence-to-usb-drives/13551
- The New York Times，David Pogue，《A Flash Drive That Holds Your Computer》（2006-06-15，Lexar PowerToGo 即 Ceedo Personal 授权版）：https://www.nytimes.com/2006/06/15/technology/15pogue.html
- StorageMojo，《USB Thumb Drive Working Environment From Lexar》（2006-05-25，Ceedo 定位与安全提醒）：https://storagemojo.com/2006/05/25/usb-thumb-drive-working-environment-from-lexar/
- EE Times，《STORAGE: Thumb drives launch apps, media players》（2006-01-09，CES 2006 上 Lexar 与 Ceedo 合作）：https://www.eetimes.com/storage-thumb-drives-launch-apps-media-players/
- Network World，《A PDF reader, more portable apps》（2006-05-01，Ceedo 与 U3 的竞争、Ceedo 定价与重定向机制）：https://www.networkworld.com/article/849813/computers-a-pdf-reader-more-portable-apps.html
- Wikipedia，《Ceedo》（公司沿革、OEM 授权、与 U3 的比较）：https://en.wikipedia.org/wiki/Ceedo
- PortabApps.com 社区讨论，《My Take on Ceedo and StickyDrive》（2006-06-25，Ceedo 隔离不彻底的实例）：https://portableapps.com/node/2225
- Linux.com，《Interview: PortableApps brings open source to USB》（2006-08-07，John T. Haller 自述 Portable Firefox 起点与站点上线）：https://www.linux.com/news/interview-portableapps-brings-open-source-usb/
- PortableApps.com，《PortableApps.com Launches!》（2005-12-09）：https://portableapps.com/news/2005-08-12-portableapps.com_launches
- PortableApps.com，《About》（项目起始时间与规模）：https://portableapps.com/about
- Wikipedia，《PortableApps.com》《Firefox Portable》（首发日期与特性）：https://en.wikipedia.org/wiki/PortableApps.com https://en.wikipedia.org/wiki/Portable_Firefox

绿色软件与中文语境：

- 中文维基百科，《绿色软件》（定义、命名由来与绿化侵权问题）：https://zh.wikipedia.org/zh-cn/%E5%85%8D%E5%AE%89%E8%A3%85%E7%89%88
- 绿色软件联盟（xdowns）分类页（免安装软件与更新时间，社区下载站，仅作线索）：https://www.xdowns.com/view_soft/2/29/list_65_2.html
- 网上读书园地论坛，《绿色软件光盘》（2005-05-03，绿色软件合集的目录样例，社区来源仅作线索）：https://www.readfree.net/bbs/thread-63646-1-1.html
- Loose Wire Blog，《A Directory Of Programs Designed For USB Drives》（2005-03-15，英文侧便携软件目录）：https://www.loosewireblog.com/2005/03/a_directory_of_-7.html
- TechEnclave 转载，《The Portable Freeware Collection》（2005-04-24，便携软件定义）：https://techenclave.com/t/the-portable-freeware-collection/46927
- Wikipedia，《winPenPack》（X-Launcher 重定向机制与项目起始）：https://en.wikipedia.org/wiki/WinPenPack

未能在本次写作期间独立复核、正文中标注「待核实」的事项：U3 停止运营的年份；RingCube 被 Citrix 收购与 MojoPac 官网跳转的确切年份与月份；Ceedo 转向安全业务的年份；Daemon Tools 与 Alcohol 120% 的首次发布年份；Sandboxie 的作者与首发年份；影子系统／PowerShadow、还原精灵、冰点还原（Deep Freeze）的产品首发年份；2002 年北京"蓝极速"网吧火灾的确切日期与《互联网上网服务营业场所管理条例》的施行日期；网吧网管软件（万象、美萍等）的名称与年份；无盘系统厂商与产品年份；联想保护卡／增霸卡一类机房产保护卡的确切型号与年份；朗科闪存盘专利与"优盘"品牌的申请与上市年份；BartPE、WinPE 的首次发布年份；Windows XP 虚拟桌面管理器（Virtual Desktop Manager）与 Dexpot、VirtuaWin 的首发年份；微软 Virtual Server 产品线的年份；IBM VM/370（1972）、Connectix Virtual PC（1997）、VMware 创立（1998）与 Workstation／ESX 首发（1999／2001）、QEMU（2003）、Xen（2003）、KVM（2006／2007 并入内核）、Hyper-V（2008）等服务器虚拟化节点；`chroot`（1979 前后）、FreeBSD jail（2000）、Solaris Zones（2004）、cgroups（2006／2007）、LXC（2008）、Docker（2013）、Kubernetes（2014）等容器节点；ARM TrustZone（2004 前后）、Intel SGX（Skylake，2015）、AMD SEV（2016／2017）、Windows VBS／Credential Guard（2015）、Windows Sandbox（1903，2019）等安全与隔离节点；"蓝色药丸"与 SubVirt（2006）等虚拟化恶意软件研究的细节；"零信任"（John Kindervag，2010 前后）与 Google BeyondCorp（2014）的提出年份；VMware VDI（2006 前后）与 Citrix XenDesktop（2008）的首发年份。上述条目在正文中均按标准公开口径概述，未在本环境取得独立可核查来源。
