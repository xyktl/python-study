#爬取腾讯视频评论  100页
#动态网页，抓包分析

import requests
import re

cid = 6383130973265682326
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

for i in range(0,5):
    print("第" + str(i + 1) + "页的评论数据" + "\n")
    url = "https://video.coral.qq.com/varticle/2369303789/comment/v2?callback=_varticle2369303789commentv2&orinum=10&oriorder=o&pageflag=1&"+str(cid)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1585487346895"
    res = requests.get(url,headers={"User-agent":ua})
    pattern1 = re.compile(r'"content":"(.*?)"',re.S)
    # re.I
    # 使匹配对大小写不敏感
    # re.L
    # 做本地化识别（locale - aware）匹配
    # re.M
    # 多行匹配，影响 ^ 和 $
    # re.S
    # 使.匹配包括换行在内的所有字符
    # re.U
    # 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    # re.X
    # 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    comment = pattern1.findall(res.text)

    #将评论数据写入到文件中
    with open(r"C:\Users\Hasse\Desktop\电脑文件\pyproject\13_python网络爬虫的设计与实现\comment.txt","a+",encoding="utf-8") as f:
        f.write("第" + str(i + 1) + "页的评论数据" + "\n")
        for data in comment:
            f.write(data+"\n")
        f.write("\n")

    for data in comment:
        print(data)
        #print(eval('u"'+str(data)+'"'))  eval() 函数来执行字符串表达式，并返回表达式的值
    print("\n")

    pattern2 = re.compile(r'"last":"(.*?)"')  #正则
    cid = pattern2.findall(res.text)[0]    #findall()  匹配所有的内容

