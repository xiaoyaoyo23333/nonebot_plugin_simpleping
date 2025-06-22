# nonebot_plugin_simpleping
向你的Nonebot发送ping以检查基础nonebot功能是否正常工作（
（偏个人用代码）

# 🚀 安装方法

# 方法1：直接复制代码
*可以通过 nb-cli 命令创建`你的插件名字`，也可以手动新建空白文件。

1. 在您的 `plugins` 目录下创建新的 Python 文件，如 `__init__.py`
2. 将插件代码复制到该文件中

# 方法2：复制到插件目录
1. 解压压缩包并将文件夹复制到您的 NoneBot2 项目的 `plugins` 目录下
2. 目录结构应该如下：
```
your_bot/
├── plugins/
│   └── nonebot_plugin_simpleping/
│       └── __init__.py
├── pyproject.toml
└── bot.py
```

# 配置项
配置方式: 请在nonebot的全局配置文件`.env` (或`.env.prod`)中添加如下超级用户配置项。
## SUPERUSERS
- 类型: List[str]
- 说明: 超级用户的列表
> SUPERSUSERS = ["your qq id"]

# 预期效果
## ping
发送`ping` 或` @bot ping `

机器人会：
1. 引用您的消息
2. 随机回复以下消息之一：
   - "pong"
   - "喵喵喵？"
   - "Atri n_(づ︶ど)在呢~"
   - #可在config.py中添加更多回复对话

## entry（超级用户项）
发送`entry`

机器人会：
1. 引用您的消息
2. 随机回复以下消息之一：
   - "欢迎回来，xiaoyao", 
   - "Nonebot2 for Atri n_(づ︶ど) 已就绪",
   - "哼哼~高性能机器人已就位~"
   - #可在config.py中添加更多回复对话

