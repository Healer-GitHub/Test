import itchat,re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('在吗|在不|在哪',msg['Text'])
    if match:
        itchat.send(('什么事？——【自动回复】'),msg['FromUserName'])


itchat.auto_login(enableCmdQR=True)
itchat.run()
