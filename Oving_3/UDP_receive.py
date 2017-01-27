import socket

UDP_PORT = 20018 #30000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print ("Received message:", data)
