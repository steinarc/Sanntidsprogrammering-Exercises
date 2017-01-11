import threading
import time


i = 0

def someThreadFunction1():
    global i
    for x in range (0,1000000):
        i = i + 1

def someThreadFunction2():
    global i
    for x in range (0, 1000000):
        i = i - 1


def main():
    global i
    someThread1 = threading.Thread(target = someThreadFunction1)
    someThread2 = threading.Thread(target = someThreadFunction2)

    someThread1.start()
    someThread2.start()

    someThread1.join()
    someThread2.join()
    
    print(i)


main()
