# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
import urllib.parse
import webob


def simple_app(environ, start_response):

    request = webob.Request(environ)
    query_string = request.query_string

    #query_string = environ.get("QUERY_STRING")
    print(query_string)
    # 将查询字符串解析并插入一个字典中
    # dic = {}
    # for item in query_string.split("&"):
    #     k, _, v = item.partition("=")
    #     dic[k] = v
    # print(dic)

    # d = {i: j for i, _, j in map(lambda x: x.partition("="), query_string.split("&"))}
    # print(d)

    # print(urllib.parse.parse_qs(query_string))

    print(request.method)
    print(request.GET)
    print(request.POST)

    status = "200 OK"
    headers = [("Content-Type", "Text/plain;charset=utf-8")]
    start_response(status, headers)
    ret = [query_string.encode()]
    return ret  # 返回要求可迭代对象，正文就是这个列表的元素，


http1 = make_server("127.0.0.1", 8000, simple_app)
print("hello,8000")
http1.serve_forever()
