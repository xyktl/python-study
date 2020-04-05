#!/usr/bin/python
# coding: utf-8
#面向对象（object oriented）开发
import socket
import re
from multiprocessing import Process
HTML_ROOT_DIR = "./"
 
 
class HttpServer(object):
 	"""docstring for Http_server"""
 	def __init__(self):
 		
 		self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 		self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


 	def start(self):
 		self.server_socket.listen(128)
 		while True:
 			client_socket,client_address = self.server_socket.accept()
 			print("[%s,%s 用户连接上了"%client_address)
 			handle_client_process = Process(target=handle_client,args=(client_socket,))
 			handle_client_process.start()
 			client_socket.close()



 	def hand_client(self,client_socket):
 		request_data = client_socket.recv(1024)
 		print("request_data:",request_data)
 		request_list = request_data.decode("utf-8").splitlines()
 		request_start_line = request_list[0]
 		file_name = re.match(r"\w+ +(/[^ ]*)",request_start_line).group(1)
 		print(file_name)
 		if re.match(r"/\w*",file_name):
 			file_name = "index.html"
 		file_root = HTML_ROOT_DIR + file_name

 		try:
 			file_open = open(file_root,"rb")		
 		except IOError:
 			response_start_line = "HTTP/1.1 404 Not Found\r\n"
 			response_head = "My Server\r\n"
 			response_body = "This file not found"	
 		else:
 			file_data = file_open.read()
 			file_open.close()
 			response_start_line = "HTTP/1.1 200 OK\r\n"
 			response_head = "My Server\r\n"
 			response_body = file_data.decode("utf-8")
 		response_data = response_start_line + response_head + response_body
 		client_socket.send(response_data.encode("utf-8"))
 		client_socket.close()

 		
 	def bind(self,port):
 		self.server_socket.bind(("",port))



if __name__ == "__main__":
	oo_web_server = HttpServer()
	oo_web_server.bind(400)
	oo_web_server.start()





