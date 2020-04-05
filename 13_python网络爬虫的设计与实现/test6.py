import requests

urls=["http://movie.douban.com/j/search_subjects","http://movie.douban.com/j/search_subjects"]
d = {"type":"mobie",
    "tag":"热门",
    "sort":"recommend",
    "page_limit":"100",
    "page_start":"0"}

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
for url in urls:
    res = requests.request("GET",url,headers={"User-agent":ua})
    with res:
        print(res.url)
        print(res.text)
        print(res.cookies)#比较两次打印的cookies有什么不同
        print(res.request.headers)
        print(type(res.text))

        with open(r"C:\Users\Hasse\Desktop\电脑文件\pyproject\13_python网络爬虫的设计与实现\movie.html","w+",encoding="utf8") as f:
            f.write(res.text)