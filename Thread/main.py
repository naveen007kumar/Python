import threading
import time

print(threading.active_count())
print(threading.enumerate())

def sum(x,y):
    time.sleep(2)
    print(x+y)


x =threading.Thread(target=sum,args=(5,7))
x.start()

#x.join()
print(threading.active_count())
print(threading.enumerate())