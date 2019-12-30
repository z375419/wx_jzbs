# -*- coding: utf-8 -*-
# filename: basic.py
import requests
import time
import json

class Basic(object):    
    def __init__(self):        
        self.__accessToken = ''        
        self.__leftTime = 0    
        
    def __real_get_access_token(self):   
        with open('setting.txt','r',encoding='utf-8') as f:
            appinfo = json.load(f)     
        appId = appinfo['appId']  
        appSecret = appinfo['appSecret']   
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="               
                "client_credential&appid=%s&secret=%s" % (appId, appSecret))    
        urlResp = requests.get(postUrl)   
        print(urlResp.text)    
        urlResp = json.loads(urlResp.text)       
        self.__accessToken = urlResp['access_token']        
        self.__leftTime = urlResp['expires_in']    
        
    def get_access_token(self):        
        if self.__leftTime < 10:            
            self.__real_get_access_token()
            return self.__accessToken    
            
        def run(self):        
            while(True):            
                if self.__leftTime > 10:                
                    time.sleep(2)                
                    self.__leftTime -= 2            
                else:                
                    self.__real_get_access_token()

if __name__ == "__main__":
    r = Basic()
    a = r.get_access_token()
    print(a)
