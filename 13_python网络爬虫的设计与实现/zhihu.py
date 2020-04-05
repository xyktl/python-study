import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import base64
import json
import hmac
from hashlib import sha1
import time
import requests


#为了防止ssl出现问题，加上下面一行代码
ssl._create_default_https_context = ssl._create_unverified_context
print("cookie处理中......")

#以下进行登录操作
#建立cookie处理
cjar = http.cookiejar.CookieJar()      #创建cookie 实例
cookie_handler = urllib.request.HTTPCookieProcessor(cjar)   #创建管理器
opener = urllib.request.build_opener(cookie_handler)    #创建请求管理器
urllib.request.install_opener(opener)             #发起请求
print("cookie处理完成，正在进行登录")

url1 ="https://www.zhihu.com"
req0 = urllib.request.Request(url1)
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
req0data = urllib.request.urlopen(req0).read().decode("utf-8","ignore")


#验证码处理
oauth = "c3cef7c66a1843f8b3a9e6a1e3160e20"
#oauth ="oauthEwAQA3l+BAAUvDBLmTCD21dGgKWS1TSPVrFoWQcAARtlXYy4X/SzVZ1eTh7HpzvirwsTi8XHvQRtiWL16O97pDhTgklJXy1JvT3ndDFKBEfEGUVx+u9i9faznwYXGpLusnkNAAsEG7yl1aF+4uQ3Bpsjctb605PGl/dz7NaFshQqsC/oeN11ZUHfJZbk8oSqUh5iLeUbpkTAgGDdLU/DtNyFhvE2BOvKob/TZcW+gpyezjEwEiS/oWPzhlSB+m+Y3uxazdJktm4ga2uzkev4dhkqyH9QDCS2ye77KoZS0rJ6oqsPWEU36oqreZBUlpZti5dX2/9Bydebx40Mmzu+BaOluJeA3FyHcBn9NkMBnjWR7sZi2ngFb2Ud/qsQ41EDZgAACPcCsAb9sLv+4AEWB1w6qoGgBVEObWClfLROeAESJ8W3jAPrYX7/Ctt1+BiD5wveDHUrHbpQBsc+64jP07w0eJiAWRWKXS3G1qLBE4c1I2tpOKTRKYMz3n3+v82Ugr4v+8AyZ5YrjhDysK+3qAkeLpmQ6jOc+rBv7t3Ko8bd540aM1rTbr2mgB78gjpnzFmXZXYrI3gVXnTifsAky9k2RPCMBA8qqyyQq3eAW8cfRwYjukKjMYHSwaLyFq8gZJ8noQYkwT/lqFL3etc0VJq1NV+rk93oL/kJw9pxucMD/OqeDIf5ARYdNFhlEP63NcSgp6b4mLoD9TMyLjWS1SYZ+7etEJXUYl3GDnarsWfKUJHjZWFH9uqBnG24DEztJZH7rxmolqX0mmjhXlYnrhm2dEZvojvYAcEeB6gO/r43e31D6851Wlhwi0dTNVZuwUIfB1+jC2e3Oy2tzCGYqkKdt+ifyeq2pitaiix2foE+P5hDjWbXQI4vuq4SBy6wCFgGOfeJrKImdMPFLnTLEJYxrQgIiJfpvV2HlsJ+qRrqepBGip6MSI8Ixe21uIqnIZS9TGJYbB5bSdjjvjY2AN7V0VgucOxeOeySdqynyWrsSTUUZlX84rZNEKavcHjX7/El3bKGREMOZeNAk60dAg=="
yzm1 = "https://www.zhihu.com/api/v3/oauth/captcha?lang=cn"  #get
req0 = urllib.request.Request(yzm1)
req0.add_header("User-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
#req0.add_header("authorization",oauth)
req0data = urllib.request.urlopen(req0).read().decode("utf8","ignore")
yzm1 = "https://www.zhihu.com/api/v3/oauth/captcha?lang=cn"  #put
req0 = urllib.request.Request(yzm1,method="PUT")
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
#req0.add_header("authorization",oauth)
req0data = urllib.request.urlopen(req0).read().decode("utf-8","ignore")
pat_yzm = '"img_base64":"(.*?)"'
yzm_data = re.compile(pat_yzm,re.S).findall(req0data)
if (len(yzm_data)>0):
    yzm_data = yzm_data[0]
    #------解码成图片------
    yzm_img = base64.b64decode(yzm_data.replace("\\n",""))
    with open("./知乎验证码.jpg","wb") as f:
        f.write(yzm_img)
else:
    yzm_data=""

yzm_type = input("请输入验证码类型：（1）倒立图片 （2）直接输入")
yzm_map = {1:[22.796875,22],
           2:[42.796875,22],
           3:[63.796875,21],
           4:[84.796875,20],
           5:[107.796875,20],
           6:[129.796875,22],
           7:[150.796875,22]
}
if(yzm_type=="1"):
    yzm_id = input("请输入倒立图片：")
    captcha = {"img_size":[200,44],
               "input_points":[],
    }
    yzm_id = eval(yzm_id)
    for num in yzm_id:
        captcha["input_points"].append(yzm_map[num])
    yzm_value = json.dumps(captcha)
else:
    yzm_value = input("请输入验证码的值：")

# #验证验证码   post
# yzmposturl = "https://www.zhihu.com/api/v3/oauth/captcha?lang=cn"
# yzmpostdata = urllib.parse.urlencode({"input_text":yzm_value}).encode("utf-8")
# req1 = urllib.request.Request(yzmposturl,yzmpostdata)
# req1.add_header("User-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
# req1data = urllib.request.urlopen(req1).read().decode("utf-8","ignore")

#签名处理

#获取加密的数据，用的是加sha1的hmac算法        详解见00_笔记
def get_signature(grantType,clientid,source,timestamp):
    hm = hmac.new(b'',None,sha1)    #new(key,message)
    hm.update(str.encode(grantType))   #数据量过大用  update（）方法
    hm.update(str.encode(clientid))
    hm.update(str.encode(source))
    hm.update(str.encode(str(timestamp)))
    return str(hm.hexdigest())
#账号密码登录
timestamp = int(time.time()*1000)
loginposturl = "https://www.zhihu.com/api/v3/oauth/sign_in"
loginpostdata = urllib.parse.urlencode({
    "client_id":"c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grantType":"password",
    "timestamp":timestamp,
    "signature":get_signature("password","c3cef7c66a1843f8b3a9e6a1e3160e20","com.zhihu.web",timestamp),
    "username":"+8613698466115",
    "password":"c1635976271",
    "captcha":yzm_value,
    "lang":"cn",
    "ref_source":"other_",
    "utm_source":""
}).encode("utf-8")
req2 = urllib.request.Request(loginposturl,loginpostdata)
req2.add_header("authorization",oauth)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
req2data = urllib.request.urlopen(req2).read().decode("utf-8","ignore")

#登录成功后爬取
url = "https://www.zhihu.com/"
req0 = urllib.request.Request(url)
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
req0data = urllib.request.urlopen(req0).read().decode("utf-8","ignore")
fh = open("./知乎网页1.html","w",encoding="utf-8")
fh.write(req0data)
fh.close()

url = "https://www.zhihu.com/question/264239372/answer/450790203"
req0 = urllib.request.Request(url)
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0")
req0data = urllib.request.urlopen(req0).read().decode("utf-8","ignore")
fh = open("./知乎网页1.html","w",encoding="utf-8")
fh.write(req0data)
fh.close()










