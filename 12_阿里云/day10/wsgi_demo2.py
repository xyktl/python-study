# -*- coding: utf-8 -*-
# 创建可迭代对象的三种方法

from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    print(environ)
    status = "200 OK"
    headers = [("Content-Type", "Text/plain;charset=utf-8")]
    start_response(status, headers)
    ret = [("%s:%s\n" % (key, value)).encode("utf-8") for key, value in environ.items()]
    return ret  # 返回要求可迭代对象，正文就是这个列表的元素，


# class A:
#     def __init__(self):
#         pass
#     def __call__(self, environ, start_response):
#         print(self.environ)
#         status = "200 OK"

#         headers = [("Content-Type", "Text/plain;charset=utf-8")]
#         self.start_response(status, headers)
#         self.ret = [("%s:%s\n" % (key, value)).encode("utf-8") for key, value in self.environ.items()]
#         return self.ret


class B:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        print(self.environ)
        status = "200 OK"
        headers = [("Content-Type", "Text/plain;charset=utf-8")]
        self.start_response(status, headers)
        self.ret = [("%s:%s\n" % (key, value)).encode("utf-8") for key, value in self.environ.items()]

    def __iter__(self):
        yield from self.ret


http1 = make_server("0.0.0.0", 6000, simple_app)
print("hello,6000")
http1.serve_forever()

# http2 = make_server("0.0.0.0", 7000, A())
# print("hello, 7000")
# http2.serve_forever()
http3 = make_server("0.0.0.0", 8000, B)
print("hello,8000")
http3.serve_forever()
