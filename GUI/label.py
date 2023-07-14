from tkinter import *


window = Tk()

label = Label(window,text="Hello!",relief=RAISED,bd=10,padx=20,pady=20,font=('Arial',50,'bold'),
              bg="Yellow",fg="Red")

label.pack()
label.place(x=30,y=50)

window.mainloop()