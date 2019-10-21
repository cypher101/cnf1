import random
from socket import *
from threading import Thread, Lock
client_info = {}
def listener(serverSocket):
	global client_info
	global recv_msg
	global name
	while flag:
		#print "started"
		recv_msg,address = serverSocket.recvfrom(1024)
		#print bool(client_info)
		if bool(client_info):
			if address in client_info.keys():
				msg = "\t\t"+client_info[address]+":"+recv_msg
				print msg
				for addr in client_info:
					'''Send data using sendto to addr'''
					serverSocket.sendto(msg,address)
			else:
				client_info[address] = recv_msg
				msg = "\n"+str(client_info[address])+" is online"
				print msg
				for addr in client_info:
					'''Send data using sendto to addr'''
					serverSocket.sendto(msg,address)
		else:
			client_info[address] = recv_msg
			msg = "\n"+str(client_info[address])+" is online"
			print msg
			for addr in client_info:
				'''Send data using sendto to addr'''
				serverSocket.sendto(msg,address)
flag = True
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 5500))
listener=Thread(target=listener,args=(serverSocket,))
listener.daemon=True
listener.start()
'''Create a thread and call listener'''
print "Server Started Listening.."
while flag:
	send_msg = raw_input()
	if send_msg == '*quit*':
		flag = False
		serverSocket.sendto(send_msg, address)
else:
	serverSocket.sendto(send_msg, address)
