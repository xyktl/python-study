# 网站登录要有签名认证：对 客户端发送给服务端的数据进行加密：
# 通常用     hmac的加 MD5（信息摘要法）或sha1(安全哈希算法) 加密
# hmac: hex-based message authentication code    哈希消息认证码
# hashlib 模块就包括了 md5 和 sha1 算法

import hmac


#    hmac.new(key,message)   需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
secret_key1 = b'This is my secret key'
message1 = b'Hello world'
hex_res1 = hmac.new(secret_key1, message1, digestmod="MD5").hexdigest()
print(hex_res1)  # b8908a20bd70f465330b434e18441d3b

content = "hello world"
content_bytes = content.encode("utf-8")
content_bytes_upper = content_bytes.upper()  # 今天才知道,还可以对bytes进行upper    大写转换
print(content_bytes_upper.decode("utf-8"))  # HELLO WORLD

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用  h.update(msg)
print(h.hexdigest())
print("\n")





import hashlib


# MD5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
print("\n")





#sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())