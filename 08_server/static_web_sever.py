# coding:utf-8
import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "."
def handle_client(client_socket):
    #处理请求数据
    request_data = client_socket.recv(1024)
    print(request_data)
    request_list = request_data.decode("utf-8").splitlines()
    #从请求数据中提取文件名得到文件路径   re匹配
    file_name = re.match(r"\w+ +(/[^ ]*) ",request_list[0]).group(1)
    if re.match(r"/\w*",file_name):
        file_name = "/index.html"
    file_root = HTML_ROOT_DIR + file_name
    print(file_root)
    #根据文件路径构造返回数据 并且构造异常情况（文件打不开）
    try:
        file = open(file_root,"rb")
    except IOError:
        response_head_line = "HTTP/1.1 404 Not Found\r\n"
        response_head = "my sever\r\n"
        response_body = "The file is not found"
    else:
        file_data = file.read()
        file.close()
        response_head_line = "HTTP/1.1 200 OK\r\n"
        response_head = "my sever\r\n"
        response_body = file_data.decode("utf-8")
    # 将返回数据发送给客户端
    response_data = response_head_line + response_head + "\r\n" +response_body
    print(type(response_data))
    print("response_data:",response_data)
    ''' 
    bytes()  str.encode()   将str 类型转换为 bytes
    str()    str.decode()   将bytes 类型转换为 str
    '''
    #client_socket.send(response_data.encode("utf-8"))
    client_socket.send(bytes(response_data,"utf-8"))
    print(type(response_data))
    client_socket.close()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("",1000))
    server_socket.listen(128)
    while True:
        client_socket,client_address = server_socket.accept()
        print("%s:%s 用户连接上了"%client_address)
        handle_client_process = Process(target=handle_client,args=(client_socket,))
        handle_client_process.start()
        client_socket.close()