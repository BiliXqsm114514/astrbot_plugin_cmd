from astrbot.api.event import AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.event.filter import command,PermissionType
import os
from astrbot.api import llm_tool, logger
from astrbot.api.event import filter, AstrMessageEvent


@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class Main(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @command("cmd_use_help")
    async def help(self,event: AstrMessageEvent):
        yield event.plain_result("ai会自动调用cmd")
        ...
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @command("cmd_use")
    async def cmd_use(self, event: AstrMessageEvent):
        """简陋的cmd调用插件"""
        ...


    @filter.permission_type(PermissionType.ADMIN)
    @llm_tool(name="cmd_use")  # 如果 name 不填，将使用函数名
    async def cmd_use(self, event: AstrMessageEvent, command: str) -> MessageEventResult:
        '''使用本地cmd命令行。

        Args:
            command(string): 命令
        '''
        if os.system(command) == 0:
            resp = "成功"
        else:
            resp = "失败"
        return "指令" + resp
        #yield event.plain_result("指令: " + resp)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        ...
