#爬取豆瓣1热度前100名的电影

from urllib.request import urlopen,Request
from urllib.parse import urlencode
import simplejson

o_url = "http://movie.douban.com/j/search_subjects"
d = {"type":"mobie",
    "tag":"热门",
    "sort":"recommend",
    "page_limit":"100",
    "page_start":"0"}

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
req = Request("{}?{}".format(o_url,urlencode(d)),headers={"User-agent":ua})
with urlopen(req) as res:
    with open(r"C:\Users\Hasse\Desktop\电脑文件\pyproject\\13_python网络爬虫的设计与实现\douban.json","w+",encoding="utf8") as f:
        mov = simplejson.loads(res.read())
        print(mov)
        simplejson.dump(mov,f)  #编码入json文件中