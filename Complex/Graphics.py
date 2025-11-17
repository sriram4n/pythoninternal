# Draw rectangles, points, and circles using a Canvas (OOP + graphics)
from tkinter import *

root = Tk()
root.title("Simple Canvas Shapes")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 180, 100, fill="lightblue")

# Draw a circle (using oval)
canvas.create_oval(200, 50, 280, 130, fill="lightgreen")

# Draw a point (tiny circle)
canvas.create_oval(100, 200, 105, 205, fill="red")

root.mainloop()
