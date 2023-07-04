from abc import ABC,abstractmethod
import os
import math


### sort() method is for lists
students = list()
pupil = dict()
while True:
    name = input("Enter Name: ")
    if name == 'quit':
        break
    students.append(name)

#sorted(students)
#students.sort()
for i in students:
    print(i)
print("^^^^^^^^^^^^")
students.sort(reverse=True)
for i in students:
    print(i)


### sorted() function is for dictionary

dict = [(2,"two"),(8,"three"),(1,"one")]
str = lambda x:x[1]
so = sorted(dict,key=str)

for i in so:
    print(i)