import socket

TCP_IP = "129.241.187.151" 
TCP_PORT = 34933

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

conn,addr = s.accept()
print 'Connection address:', addr

while 1:
	data = conn.recv(20)
	print ("received datra: ", data)
	conn.send(data)

conn.close()
