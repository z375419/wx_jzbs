# -*- coding: utf-8 -*-
# # filename: handle.py
import hashlib
import web
import reply
import receive


class Handle(object):
    # 验证token是否是微信消息
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

    # 接收微信后台消息, 并进行处理
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            # 后台打日志
            recMsg = receive.parse_xml(webData)
            replyNone = reply.Msg()
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                
                if recMsg.MsgType == "text":
                    print(recMsg.Content.decode('utf-8'))
                    if recMsg.Content.decode("utf-8") == "bwg密码":
                        content = "KXmklljHJ"
                    else:
                        content = "欢迎关注!"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == "image":
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                    return replyMsg.send()
                else:
                    return replyNone.send()
            # 事件类型的处理程序
            elif isinstance(recMsg, receive.EventMsg): 
                print('event', recMsg.Event, recMsg.EventKey)
                if recMsg.Event == 'CLICK':
                    if recMsg.EventKey == 'mpGuide':
                        content = "编写中，尚未完成"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            else:
                print("暂且不处理")
                return replyNone.send() # 无匹配模式则返回success
        except Exception as e:
            return e
