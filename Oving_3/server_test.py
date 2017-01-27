import socket
from thread import *

REMOTE_IP = '129.241.187.43'
MY_IP = '129.241.187.151'
TCP_PORT = 33546

s_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_connect.connect((REMOTE_IP, TCP_PORT))

data = s_connect.recv(1024)
print(data)

s_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_listen.bind((MY_IP, TCP_PORT))


s_listen.listen(10)

def clientthread(conn):
	conn.send('Server says hi once more!\n\0')
	
	while True:
		min_data = conn.recv(1024)
		reply = 'Message received at the server!\n'
		print min_data
		if not min_data:
			break
		
		conn.sendall(reply)

	conn.close()

while True:
	conn, addr = s_listen.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	start_new_thread(clientthread,(conn,))

s_listen.close()
s_connect.close()
