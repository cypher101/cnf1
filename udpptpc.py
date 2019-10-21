import socket
from threading import Thread, Lock
import sys
def receiver(sock):
	while flag:
		data = sock.recv(1024)
		if data == 'quit':
			sys.exit(0)
		print "\t\t"+data
host = '192.168.122.1'
port = 50020
size = 1024
flag = True
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))
hop = Thread(target=receiver, args=(sock,))
hop.daemon = True
hop.start()
data = "random"
while data != 'quit':
	data = raw_input()
	sock.send(data)
	'''Send data to server'''
sock.close()

