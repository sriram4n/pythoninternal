from tkinter import *

root = Tk()
root.title("Simple shapes")

canvas = Canvas(root,width = 300,height = 400, bg= "White")
canvas.pack()

canvas.create_rectangle(0,0,100,150,fill="Black")
canvas.create_oval()

root.mainloop()