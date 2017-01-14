from threading import Thread, Lock

def someThreadFunction1():
    global i, lock

    lock.acquire()
    try:
        for x in range (0,1000000):
            i = i + 1
    finally:
        lock.release()

def someThreadFunction2():
    global i,lock

    lock.acquire()
    try:
        for x in range (0,1000001):
            i = i - 1
    finally:
        lock.release()

def main():

    global i,lock
    i = 0   
    lock = Lock()  

    someThread1 = Thread(target = someThreadFunction1)
    someThread2 = Thread(target = someThreadFunction2)

    someThread1.start()
    someThread2.start()

    someThread1.join()
    someThread2.join()
    
    print("i: ", i)


main()
