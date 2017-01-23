import socket

UDP_IP = "127.0.0.1" #"109.189.14.115"
UDP_PORT = 20016

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print ("received message:", data)
