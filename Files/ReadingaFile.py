import os


with open('My_Details') as text:
    print(text.closed)
    print(text.read())

print(text.closed)