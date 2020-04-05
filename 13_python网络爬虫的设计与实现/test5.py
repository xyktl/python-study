import urllib3
from urllib.request import Request

url = "http://www.bing.com"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"


with urllib3.PoolManager() as http:
    res = http.request("GET",url,headers={"User-agent":ua})
    print(res.data)
    print(type(res.data))