import threading
import time

def mul(x,y,z):
    time.sleep(3)
    print(x*y*z)

def mult(x,y,z):
    time.sleep(3)
    print(x*y*z)

x=threading.Thread(target=mul,args=(3,5,6))
x.start()
print("")
y=threading.Thread(target=mult(5,6,7),daemon=True)
y.start()