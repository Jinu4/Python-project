import tkinter
import tkinter.messagebox
import pymysql
from PIL import ImageTk, Image
t = tkinter.Tk()
t.title('Profile')
t.geometry('500x500')
p = Image.open("C:\\Users\\Jinu Antony J\\Downloads\\bg.jpg")
p = p.resize((500, 500))
p = ImageTk.PhotoImage(p)
pic = tkinter.Label(t, image=p)
pic.place(x=0, y=0)
a = tkinter.Label(text="Profile creation", fg='indigo', bg='white', font=('bradley hand itc', 35, 'bold'))
a.place(x=90, y=0)
b = tkinter.Label(text="Name", fg='indigo', bg='white', font=('bradley hand itc', 25, 'bold'))
b.place(x=50, y=100)
c = tkinter.Entry(width=30)
c.place(x=180, y=115)
d = tkinter.Label(text="Place", fg='indigo', bg='white', font=('bradley hand itc', 25, 'bold'))
d.place(x=50, y=200)
e = tkinter.Entry(width=30)
e.place(x=180, y=220)


def abcd():
    name = c.get()
    place = e.get()
    if name == "" or place == "":
        tkinter.messagebox.showerror('Error', 'Please complete fields')
    else:
        x=pymysql.connect(host='localhost', user='root', password='root1', db='avodha')
        cur=x.cursor()
        cur.execute("insert into Profile values('"+name+"','"+place+"')")
        x.commit()
        x.close()
        tkinter.messagebox.showinfo('Thank You', 'Thanks for visiting')
        t.destroy()


f = tkinter.Button(text="Submit", command=abcd, bg='blue',fg='white', font=('bradley hand itc',25,'bold'))
f.place(x=150,y=310)

t.mainloop()