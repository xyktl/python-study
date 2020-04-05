
#urllib 中的request模块
from urllib.request import Request,urlopen
import random
import ssl

url = "https://www.12306.cn/mornhweb/"

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safarix"

context = ssl._create_unverified_context()  #生成数字认证
req =  Request(url)     #生成一个请求文件头
req.add_header("User-agent",ua)

res = urlopen(req,context=context)     #返回一个请求结果

print(res.closed)
with res:
    print(res.status)
    print(res.geturl())
    print(req.get_header("User-agent"))
    print(res._method)
    print(type(res.read()))

