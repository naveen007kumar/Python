import os

text = ". I code Python!!!"

with open('My_Details','a') as temp:
    temp.write(text)
    temp.write(" I learn to code Python###")

with open('My_Details', 'w') as temp:
    temp.write("I Naveen, learn and code Python!!!")



print(text[5])