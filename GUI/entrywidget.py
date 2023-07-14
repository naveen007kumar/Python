from tkinter import *

window = Tk()

entry = Entry(window, font="Arial")
entry.insert(10,'Hello')
entry.pack()

str= entry.get()
print(str)
window.mainloop()