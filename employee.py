import tkinter
import tkinter.messagebox
from tkinter import RIGHT, Y, END, INSERT

import pymysql
from PIL import ImageTk, Image

t = tkinter.Tk()
t.title('Profile')
t.geometry('800x500')
p = Image.open("C:\\Users\\Jinu Antony J\\Downloads\\bg.jpg")
p = p.resize((800, 500))
p = ImageTk.PhotoImage(p)
pic = tkinter.Label(t, image=p)
pic.place(x=0, y=0)
a = tkinter.Label(text="Employee list", fg='indigo', bg='white', font=('bradley hand itc', 35, 'bold'))
a.place(x=90, y=0)
b = tkinter.Label(text="Name", fg='indigo', bg='white', font=('bradley hand itc', 15, 'bold'))
b.place(x=50, y=100)
c = tkinter.Entry(width=30)
c.place(x=180, y=100)
d = tkinter.Label(text="Age", fg='indigo', bg='white', font=('bradley hand itc', 15, 'bold'))
d.place(x=50, y=150)
e = tkinter.Entry(width=30)
e.place(x=180, y=150)
f = tkinter.Label(text="Employee ID", fg='indigo', bg='white', font=('bradley hand itc', 15, 'bold'))
f.place(x=50, y=200)
g = tkinter.Entry(width=30)
g.place(x=180, y=200)
h = tkinter.Label(text="Place", fg='indigo', bg='white', font=('bradley hand itc', 15, 'bold'))
h.place(x=50, y=250)
i = tkinter.Entry(width=30)
i.place(x=180, y=250)


def abcd():
    name = c.get()
    age = e.get()
    employee_id = g.get()
    place = i.get()
    if name == "" or place == "" or age == "" or employee_id == "":
        tkinter.messagebox.showerror('Error', 'Please complete fields')
    else:
        x = pymysql.connect(host='localhost', user='root', password='root1', db='avodha')
        cur = x.cursor()
        cur.execute("insert into Employees values('" + name + "','" + age + "','" + employee_id + "','" + place + "')")
        x.commit()
        x.close()
        tkinter.messagebox.showinfo('Thank You', 'Thanks for visiting')
        t.destroy()


x = pymysql.connect(host='localhost', user='root', password='root1', db='avodha')
cur = x.cursor()
sc = tkinter.Scrollbar()
sc.pack(side=RIGHT, fill=Y)
tx = tkinter.Text(height=10, width=25, yscrollcommand=sc.set)
tx.place(x=500, y=100)
cur.execute('select * from Employees')
v = cur.fetchall()
vn = [','.join(map(str, xd)) for xd in v]


def efgh():
    sc.config(command=tx.yview())
    tx.delete('1.0', END)
    for j in vn:
        tx.insert(INSERT, ('%s\n\n' % j))


l = tkinter.Button(text='View', command=efgh, bg='blue', fg='white', font=('bradley hand itc', 20, 'bold'))
l.place(x=300, y=310)
k = tkinter.Button(text="Submit", command=abcd, bg='blue', fg='white', font=('bradley hand itc', 20, 'bold'))
k.place(x=150, y=310)

t.mainloop()
