import socket
import time

UDP_IP = "127.0.0.255"
UDP_PORT = 20018
MESSAGE_1 = "Hei paa deg!"
MESSAGE_2 = "Det er meg!"

print ("Message 1 is: ", MESSAGE_1)
print ("Message 2 is: ", MESSAGE_2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	sock.sendto(MESSAGE_1, (UDP_IP, UDP_PORT))
	time.sleep(1)
	sock.sendto(MESSAGE_2, (UDP_IP, UDP_PORT))
	time.sleep(1)
