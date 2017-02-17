from socket import *
import time
from multiprocessing import Process

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE
import sys
from queue import *

REMOTE_IP = "127.0.0.1"         
PORT = 30000  

backup = socket(AF_INET, SOCK_DGRAM)
backup.bind(('',PORT))

def make_backup():                   
	Popen([sys.executable, 'primary.py'], creationflags = CREATE_NEW_CONSOLE) #shell = True

#backup
def receive_put(port):

	s = socket(AF_INET, SOCK_DGRAM)
		
	try :
		s.bind(('',port))
	except (socket.error, msg):
		print ('Failed to bind a socket. Error Code : '.encode() + str(msg[0]) + ' Message '.encode() + msg[1])
		sys.exit()
		
	m = s.recvfrom(1024)

	if (m != "I am alive"):
		q = queue()
		q.put(m)
	#return (m[0])


#primary should broadcast: i am alive
def broadcast_alive(port):
	main = socket(AF_INET, SOCK_DGRAM)
	main.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	main.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	
	while(True):
		#print("Er vi her?")
		main.sendto("I am alive".encode(),('255.255.255.255',port))
		time.sleep(1)

def counter(i):

	main = socket(AF_INET, SOCK_DGRAM)
	while(True):
		i += 1
		main.sendto(str(i).encode(), ("127.0.0.1" ,30000))
		print(i)
		time.sleep(1)
	



def run_primary(i):
	print("---- MASTER -----\n")
	Popen([sys.executable, 'primary.py'], creationflags = CREATE_NEW_CONSOLE) #åpner backup



#def run_backup():


def main():
	p1 = Process(target = broadcast_alive, args = (PORT,))
	p1.start()


	p2 = Process(target = counter, args = (0,))
	p2.start()




if __name__ == '__main__':
	main()
