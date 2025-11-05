from tkinter import *

root = Tk()
root.title("Simple Form")

# Labels and Text Fields
Label(root, text="Name:").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Email:").grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)

# Button Functions
def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())

def reset():
    name_entry.delete(0, END)
    email_entry.delete(0, END)

# Buttons
Button(root, text="Submit", command=submit).grid(row=2, column=0)
Button(root, text="Reset", command=reset).grid(row=2, column=1)

root.mainloop()
