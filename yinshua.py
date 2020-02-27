#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
import os
#from urllib import parse
#  印刷文字多语种 webapi接口地址
URL = "https://webapi.xfyun.cn/v1/service/v1/ocr/recognize_document"
#  应用ID (必须为webapi类型应用，并印刷文字识别多语种服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481)
APPID = "5e5772cf"
#  接口密钥(webapi类型应用开通印刷文字识别多语种服务后，控制台--我的应用---印刷文字识别多语种---服务的apikey)
API_KEY = "e98d504f8c5bdbf78f9422a4dddf34f8"
def getHeader():
    curTime = str(int(time.time()))
    param = {"engine_type": "recognize_document"}
    param = json.dumps(param)
    paramBase64 = base64.b64encode(param.encode('utf-8'))
    m2 = hashlib.md5()
    str1 = API_KEY + curTime + str(paramBase64,'utf-8')
    m2.update(str1.encode('utf-8'))
    checkSum = m2.hexdigest()
#   组装http请求头
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header
path = 'E:\\you\\'
def piliang(chuantr):
   lunt=chuantr
   print("");
   print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
   print("文件名是："+chuantr);
   with open(chuantr, 'rb') as f:
       f1 = f.read()
       
       f1_base64 = str(base64.b64encode(f1), 'utf-8')    
       data = {
        'image': f1_base64
        }
       r = requests.post(URL, data=data, headers=getHeader())
       result = str(r.content, 'utf-8')

       body = json.loads(result, encoding='utf-8')
#print(body)

       for text_line in body['data']['document']['blocks']:
           word = text_line['lines'][0]['text']
        
           print(word)


for filename in os.listdir(path):
    piliang(os.path.join(path, filename))
#  上传图片路径，base64编码后大小不超过4m



 

