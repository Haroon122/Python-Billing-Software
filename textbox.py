from tkinter import *

win = Tk()
win.geometry("600x800+300+20")
global a,b,c,d
a=StringVar()
b=StringVar()
Entry(win,textvariable=a).place(x=500,y=50)
Entry(win,textvariable=b).place(x=500,y=100)


tx=Text(win,width=30,height=20)
def add():
    global total
    total = int()
    c=int(a.get())
    d=int(b.get())
    total = c*d
Button(win,command=add,text="total").place(x=500,y=150)
tx.place(x=20,y=20)
tx.insert(END,"\t          ------ Welcome\n")
tx.insert(END,"\t =================================\t")

tx.insert(END,f"a:   {a.get()}\n")
tx.insert(END,f"b:   {b.get()}\n")
# tx.insert(END,f'total:    total')
tx.config(font=("poppins 20 bold"))
win.mainloop()