from tkinter import *

root = Tk()
root.title("Simple input taker")

Label(root,text="Enter name").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0,column=1)

Label(root,text="Enter phone number").grid(row=1, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=1,column=1)

def Submit():
    print(name_entry.get())
    print(phone_entry.get())

def Reset():
    name_entry.delete(0,END)
    phone_entry.delete(0,END)

Button(root,text="submit",command=Submit).grid(row = 2, column= 0)
Button(root,text="REset",command=Reset).grid(row = 2, column= 1)

root.mainloop()