# coding:utf-8


# scheme    0   返回 URL 的 scheme scheme 参数
# netloc    1   网络位置部分（主机名＋端口）  空字符串
# path  2   资源路径    空字符串
# params    3   资源路径的附加参数   空字符串
# query 4   查询字符串   空字符串
# fragment  5   Fragment 标识符    空字符串
# username      用户名 None
# password      密码  None
# hostname      主机名 None
# port      端口  None
import urllib.parse


result = urllib.parse.urlparse("http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag")
print(result)
