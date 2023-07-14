from abc import ABC,abstractmethod
import os
import threading

num = range(1,100)

fil = lambda x:(x%9)

result = filter(fil,num)

for i in result:
    print(i)

print(threading.enumerate())
print(threading.current_thread())