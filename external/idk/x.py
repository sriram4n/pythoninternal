from tkinter import *

root = Tk()
root.title("Simple program")

canvas = Canvas(root,width=300,height=400,bg="white")
canvas.pack()

canvas.create_rectangle(50,50,180,100,fill="red")
canvas.create_oval(100,160,160,100,fill="pink")
root.mainloop()