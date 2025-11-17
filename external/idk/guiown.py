import tkinter as tk
from tkinter import messagebox

def submit_command():
    name = inputname.get().strip()
    age = inputage.get().strip()
    if name and age:
        messagebox.showinfo(f"Submitted {name} & {age}")
    else:
        messagebox.showwarning("Input error","Fill all fields")

def reset_command():
    inputname.delete(0,tk.END)
    inputage.delete(0,tk.END)

root = tk.Tk()
root.geometry("300x150")
root.title("User info")
root.resizable(False,False)

tk.Label(root,text="Name: ").grid(row=0,column=0)
inputname = tk.Entry(root)
inputname.grid(row=0,column=1)

tk.Label(root,text="Enter Age: ").grid(row=1,column=0)
inputage = tk.Entry(root)
inputage.grid(row=1,column=1)

tk.Button(root,text="Submit",command=submit_command).grid(row=2,column=0)
tk.Button(root,text="Reset",command=reset_command).grid(row=2,column=1)

root.mainloop()