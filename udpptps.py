import socket
from threading import Thread, Lock
import sys
def receiver(sock):
	global flag
	while flag:
		data = sock.recv(size)
	        '''Receive data from client'''
		if data == 'quit':
			sys.exit(0)
		print "\t\t"+data
		flag = True
		print "Thread Exiting"
host = '192.168.122.1'
port = 50020
backlog = 5
size = 1024
flag = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
	print "Waiting for Peer to Join..."
	client,address=s.accept()
	'''Accept a connection'''
	print "Client "+str(address)+"joined chat.\n"
	'''Create a thread'''
	recv_thread=Thread(target=receiver,args=(client,))
	recv_thread.daemon = True
	recv_thread.start()
	data = "random"
	while data != 'quit':
		data=raw_input()
		client.send(data)
		'''Send data to client'''
		flag = False
client.close()
