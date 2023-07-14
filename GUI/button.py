from tkinter import *

window = Tk()

def click():
    print("Button CLicked!")

icon = PhotoImage(file="img.png")

button = Button(window,text="Click Me!",command=click,image=icon,compound="top")

button.pack()

window.mainloop()