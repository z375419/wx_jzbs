# -*- coding: utf-8 -*-
# filename: menu.py
import requests
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        urlResp = requests.post(url=postUrl, data=postData)
        print(urlResp.text)

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = requests.get(url=postUrl)
        print(urlResp.text)

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = requests.get(url=postUrl)
        print(urlResp.text)
        
    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = requests.get(url=postUrl)
        print(urlResp.text)

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "旅行",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
          ]
    }
    """
    # accessToken = Basic().get_access_token()
    accessToken = "28_xJAjCmDRKHgCLk1an8aIQ2mPQU0Q0hUlcKVIrUpSuqEu9ywaQj0SojRN0WcH4e--I_DgESdv0FJx_6Hnzm4hSTUrJt3050cve3OFcN2hO9RpEGPqALSNtj11vueEQGNUiPF3Xvs4jmYL69eMJUSeAIAUFD"
    # myMenu.delete(accessToken)
    postJson = postJson.encode('utf-8')
    myMenu.create(postJson, accessToken)