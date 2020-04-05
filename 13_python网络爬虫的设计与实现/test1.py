
#urllib 中的request模块
from urllib.request import Request,urlopen
import random

url = "http://www.bing.com"
ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36","User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"]
ua = random.choice(ua_list)

req =  Request(url)     #生成一个请求文件头
req.add_header("User-agent",ua)

res = urlopen(req)     #返回一个请求结果

print(res.closed)
with res:
    print(res.status)
    print(res.geturl())
    print(res.info())
    print(req.get_header("User-agent"))

