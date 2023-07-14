import os
from abc import ABC,abstractmethod
import threading
import functools
from tkinter import *


window = Tk()

window.title("First Window")

icon = PhotoImage(file="img.png")
window.iconphoto(True,icon)

window.config(background="yellow")


window.mainloop()
