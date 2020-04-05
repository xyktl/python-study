# -*- coding: utf-8 -*-


from wsgiref.simple_server import make_server
import webob
print(webob.__file__)


def simple_app(environ, start_response):

    request = webob.Request(environ)
    res = webob.Response()  # 因为要求res 要是可迭代对象
    res.body = "<h1>hello world</h1>".encode()

    return res(environ,start_response)  # 返回要求可迭代对象，正文就是这个列表的元素，

http1 = make_server("127.0.0.1", 8000, simple_app)
print("hello,8000")
http1.serve_forever()
