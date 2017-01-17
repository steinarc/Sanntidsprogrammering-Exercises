from threading import Thread, Lock
import time


i = 0
mutex = Lock()

def someThreadFunction1():
    global i, mutex
    for x in range (0,1000000):
        mutex.acquire()
        try:
            i = i + 1
        finally:
            mutex.release()

def someThreadFunction2():
    global i, mutex
    for x in range (0, 1000001):
        mutex.acquire()
        try:
            i = i - 1
        finally:
            mutex.release()


def main():

    someThread1 = Thread(target = someThreadFunction1)
    someThread2 = Thread(target = someThreadFunction2)

    someThread1.start()
    someThread2.start()

    someThread1.join()
    someThread2.join()
    
    print(i)


main()
