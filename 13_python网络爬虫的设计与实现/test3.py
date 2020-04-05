from urllib.request import Request,urlopen
from urllib.parse import urlencode
import simplejson

url = "http://www.httpbin.org/post"
d = {"age":26,"name":"张三？/"}
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
req = Request(url,headers={"User-agent":ua})

#post  请求data不能为空
with urlopen(req,data=urlencode(d).encode()) as res:
    text = res.read()
    print(text)
    print(type(text))
    dic = simplejson.loads(text)
    print(dic)
    print(type(dic))

