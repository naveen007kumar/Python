from abc import ABC,abstractmethod #for abstract implementation
import os  #for file implemetation
import math


#print(value = True) #throes error
print(value := True)

#EXAMPLE

foods = list()
# while True:
#     food = input("Enter food item: ")
#     if food == "quit":
#         break
#     foods.append(food)
#
# print(list)

while food := input("Enter Food Item: ") != "quit":
    print(food)
    foods.append(food)

for item in foods:
    print(item)
