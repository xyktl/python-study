import requests
from lxml import etree



url = "https://movie.douban.com/"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

res = requests.get(url,headers={"User-agent":ua})
print(type(res.content))
content = res.text
print(type(res.text))

html = etree.HTML(content)
print("*"*30)
print(type(html))
t = html.xpath("//div[@class='billboard-bd']//tr")
for i in t:
    txt = i.xpath(".//text()")
    print("".join(map(lambda x: x.strip(),txt)))



