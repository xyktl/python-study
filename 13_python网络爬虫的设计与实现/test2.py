from urllib.request import Request,urlopen
from urllib.parse import urlencode
import simplejson

Baseurl = "http://www.bing.com/search"
d = {"age":26,"name":"张三？/"}
url = "{}?{}".format(Baseurl,urlencode(d))
print(url)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
req = Request(url,headers={"User-agent":ua})

with urlopen(req) as f:
    with open(r"C:\Users\Hasse\Desktop\电脑文件\pyproject\\13_python网络爬虫的设计与实现\test.html","wb+") as b: #将请求回来的数据打印到test.html 文件上
        b.write(f.read())
        b.flush()
    