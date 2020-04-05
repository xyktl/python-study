# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    print(environ)
    status = "200 OK"
    headers = [("Content-Type", "Text/plain;charset=utf-8")]
    start_response(status, headers)
    ret = [("%s:%s\n" % (key, value)).encode("utf-8") for key, value in environ.items()]
    return ret  # 返回要求可迭代对象，正文就是这个列表的元素，


http = make_server("0.0.0.0", 8000, simple_app)

try:
    print("sever is in port 8000")
    http.serve_forever()
except KeyboardInterrupt:
    print("stop")
    http.server_close()
except Exception as e:
    print(e)
