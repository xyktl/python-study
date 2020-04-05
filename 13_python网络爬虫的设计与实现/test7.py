import requests

urls=["http://movie.douban.com/j/search_subjects","http://movie.douban.com/j/search_subjects"]
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
session = requests.Session()
for url in urls:
    with session:
        res = session.request("GET",url,headers={"User-agent":ua})
        with res:
            print(res.cookies)
            print(res.request.headers)#浏览器下一次访问就会使用服务器返回来的cookies