#coding:utf-8
import socket
from multiprocessing import Process

def handle_client(client_socket):
    '''处理客户端的请求'''
    request_data = client_socket.recv(1024)
    print(request_data)
    respond_head = "HTTP/1.1 200 OK\r\n"
    respond_heads = "my sever\r\n"
    respond_body = "<h1>my python</h1>"
    respond_data = respond_head + respond_heads + "\r\n" + respond_body
    print(respond_data)
    client_socket.send(bytes(respond_data.encode("utf-8")))
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 500))
    server_socket.listen(128)
    while True:
        client_socket,client_address = server_socket.accept()
        print(client_address)
        print("[%s,%s]用户连接上了"% client_address)
        handle_client_process = Process(target=handle_client,args=(client_socket,))
        handle_client_process.start()
        client_socket.close()