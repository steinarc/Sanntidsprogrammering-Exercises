import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 20016
MESSAGE = b"Hei paa deg!"

print ("message: ", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(1)
