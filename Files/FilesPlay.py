###

import os


path1 = "C:\\Users\\Saketh Gondela\\Desktop\\Python\\Files\\My_Details"
#path2 = "C:\\Users\\Saketh Gondela\\Desktop\\Python\\Files\\Personal"

if os.path.exists:
    print("File exists in the location")

if os.path.exists:
    print("Directory exists in the location")


if os.path.isfile(path1):
    print("It is a file!")
elif os.path.isdir(path1):
    print("It is a Directory!!!")


