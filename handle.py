# -*- coding: utf-8 -*-
# # filename: handle.py
import hashlib
import web
import reply
import receive


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "zld"  # 请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            # map(sha1.update, list)
            sha1.update(list[0].encode('utf-8'))
            sha1.update(list[1].encode('utf-8'))
            sha1.update(list[2].encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            # 后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Content == "bwg密码":
                    content = "KXmklljHJ"
                else:
                    content = "欢迎关注!"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as e:
            return e
