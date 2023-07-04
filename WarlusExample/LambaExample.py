from abc import ABC,abstractmethod
import math
import os

def multiply_10(x):
    return x*10

print(multiply_10(5))

##### Using lamba

mul = lambda x:x*10
print(mul(3))
