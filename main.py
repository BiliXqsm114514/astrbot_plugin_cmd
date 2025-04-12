import os
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.core.provider.register import llm_tools


@register("astrbot_plugin_cmd", "BiliXqsm114514", "让ai调用本地cmd", "0.0.1", "repo url")
class CmdUsing(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @llm_tools(name="cmd_using")
    async def cmd_using(self, event: AstrMessageEvent,content:str):
        '''使用本地 cmd 指令'''  # 这是 handler 的描述，将会被解析方便用户了解插件内容。非常建议填写。
        exit_code = os.system(content)
        '''
        user_name = event.get_sender_name()
        message_str = event.message_str  # 获取消息的纯文本内容
        yield event.plain_result(f"Hello, {user_name}!")  # 发送一条纯文本消息
        '''
        return "指令成功" if exit_code == 0 else "出现报错"

    async def terminate(self):
        '''可选择实现 terminate 函数，当插件被卸载/停用时会调用。'''