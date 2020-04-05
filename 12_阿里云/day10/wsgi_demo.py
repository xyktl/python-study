# -*- coding: utf-8 -*-
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app


# def simple_app(environ, start_response):
#     print(environ) #打印请求
#     status = "200 OK"
#     headers = [("Content-type", "text/plain;charset=utf-8")]
#     start_response(status, headers)
#     ret = [("%s:%s" % (key, value)).encode("utf-8") for key, value in environ.items()]
#     return ret  # 返回要求可迭代对象，正文就是这个列表的元素，


# httpd = make_server("0.0.0.0", 8000, simple_app)
# print("Serveing on port 8000 .....")
# httpd.serve_forever()
http = make_server("0.0.0.0", 8000, demo_app)  # 内置模块中有一个demo_app函数
print("hello")
http.serve_forever()

# def demo_app(environ,start_response):
#     from io import StringIO
#     stdout = StringIO()
#     print("Hello world!", file=stdout)
#     print(file=stdout)
#     h = sorted(environ.items())
#     for k,v in h:
#         print(k,'=',repr(v), file=stdout)
#     start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
#     return [stdout.getvalue().encode("utf-8")]
