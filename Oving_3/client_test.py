import socket
import time

TCP_PORT = 33546
BUFFER_SIZE = 1024

s_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_1.connect(("gmail.com",80))
MY_IP = s_1.getsockname()[0]
print 'Connect from: ', MY_IP, ':', TCP_PORT, '\0'
s_1.close()

MESSAGE = 'Hello World\0!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((MY_IP, TCP_PORT))
s.send(MESSAGE)
s.close()

while True:
	print 'Our message: ', MESSAGE
	time.sleep(1)
