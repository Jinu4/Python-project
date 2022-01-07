from tkinter import *

root = Tk()
f = Frame(root)
f.pack()


def login():
    x = e.get()
    y = e1.get()
    if x == "Jinu" and y == 123:
        print("Welcome")
    else:
        print("Incorrect username and password")


def cancel():
    f = Frame(root)
    print("Come again")
    f.quit()


Label(f, text="Username", fg="red").grid(row=0, column=0)
Label(f, text="Password", fg="red").grid(row=1, column=0)
e = Entry(f)
e.grid(row=0, column=1)
e1 = Entry(f)
e1.grid(row=1, column=1)
Button(f, text="Login", command=login).grid(row=3, column=1)
Button(f, text="Cancel", command=cancel).grid(row=3, column=0)
root.mainloop()
