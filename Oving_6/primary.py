from socket import *
import time
import select

from subprocess import *
import sys
import os


def backup_does_things():
	print("I AM BACKUP\n")

	socket_receive = socket(AF_INET, SOCK_DGRAM)
	socket_receive.bind(('',20018))
	socket_receive.setblocking(0)
	last_i = 0

	while(True):
		m = "0"
		ready = select.select([socket_receive], [], [], 2)
		if ready[0]:		
			m = socket_receive.recvfrom(1024)
			#print("I am backup, I heard that %d" % (int(m[0])))
			last_i = int(m[0])
		if(m == "0"):
			socket_receive.close()	
			primary_does_things(last_i)



def primary_does_things(i):		

	os.system("gnome-terminal -x python primary.py ")

	socket_send = socket(AF_INET, SOCK_DGRAM)
	while(True):
		i += 1
		socket_send.sendto( str(i) , ("127.0.0.1" ,20018))
		print("I am primary, I say: %d" % (i))
		time.sleep(1)


def spawn_backup():
	os.system("gnome-terminal -x python primary.py ")


backup_does_things()

#"Popen(["gnome-terminal -x primary.py"])




