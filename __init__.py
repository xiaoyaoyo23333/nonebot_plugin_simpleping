from nonebot import on_command, on_keyword, on_regex
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from nonebot.rule import to_me
from random import choice
from .config import Config

# 获取配置实例
config = Config()

# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="超级用户响应插件",
    description="超级用户登录欢迎语和防误触发ping响应功能",
    usage="""
    超级用户命令:
    - 发送: entry/登录/login/测试超管 (需超级用户权限)
    
    通用命令:
    - 发送: /ping (命令格式，推荐)
    - 私聊或@机器人时发送: ping (精确匹配)
    
    ✨ 防误触发设计：
    - "我在ping服务器" ❌ 不会触发
    - "/ping" ✅ 会触发
    - "@机器人 ping" ✅ 会触发
    """,
    config=Config,
    extra={
        "author": "xiaoyaoyo23333",
        "supported_adapters": ["nonebot.adapters.onebot.v11"]
    }
)

# 超级用户登录命令
superuser_cmd = on_keyword(
    config.superuser_triggers,
    permission=SUPERUSER,
    priority=10,
    block=True
)

# 主ping命令：标准命令格式（最安全）
ping_cmd = on_command(
    "ping",
    priority=20,
    block=True
)

# 辅助ping命令：@机器人或私聊时的精确匹配
ping_cmd_direct = on_regex(
    r"^ping$",  # 只匹配单独的"ping"
    rule=to_me(),  # 只在@机器人或私聊时生效
    priority=21,
    block=True
)

@superuser_cmd.handle()
async def handle_superuser(bot: Bot, event: MessageEvent):
    """处理超级用户登录命令"""
    welcome_msg = choice(config.welcome_messages)
    reply_message = MessageSegment.reply(event.message_id) + welcome_msg
    await bot.send(event, reply_message)

@ping_cmd.handle()
async def handle_ping(bot: Bot, event: MessageEvent):
    """处理ping命令 - 标准格式 (/ping)"""
    reply_msg = choice(config.ping_replies)
    reply_message = MessageSegment.reply(event.message_id) + reply_msg
    await bot.send(event, reply_message)

@ping_cmd_direct.handle()
async def handle_ping_direct(bot: Bot, event: MessageEvent):
    """处理ping命令 - 直接格式 (仅@或私聊)"""
    reply_msg = choice(config.ping_replies)
    reply_message = MessageSegment.reply(event.message_id) + reply_msg
    await bot.send(event, reply_message)
