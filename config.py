from pydantic import BaseModel

class Config(BaseModel):
    """插件配置"""
    # 超级用户欢迎语配置
    welcome_messages: list[str] = [
        "欢迎回来，xiaoyao", 
        "Nonebot2 for Atri n_(づ︶ど) 已就绪",
        "哼哼~高性能机器人已就位~"
    ]
    
    # ping响应配置
    ping_replies: list[str] = [
        "pong", 
        "喵喵喵？",
        "Atri n_(づ︶ど)在呢~"
    ]
    
    # 超级用户触发词配置
    superuser_triggers: set[str] = {"entry", "登录", "login", "测试超管"}
