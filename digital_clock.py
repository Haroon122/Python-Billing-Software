from tkinter import*
from tkinter.ttk import*
from time import strftime 
root=Tk()
root.geometry("500x300")
root.title("Clock")
def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1,time)
label=Label(root,font=("ds-digital 80 bold"),background="black",foreground="cyan")
label.pack(anchor="center")
time()


root.mainloop()