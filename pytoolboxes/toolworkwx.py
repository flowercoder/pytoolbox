# corpwechat send message

from corpwechatbot import AppMsgSender

class WorkWX():
    def appMsgSender(self, corpid,corpsecret,agentid,content):
        app = AppMsgSender(corpid=corpid,  # 你的企业id
                           corpsecret=corpsecret,  # 你的应用凭证密钥
                           agentid=agentid)  # 你的应用id
        app.send_text(content)