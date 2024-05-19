from tkinter import*
class Nishaf():
    def __init__( self,root):
        global menubar
        self.root=root
        self.root.geometry("700x500")
        menubar=Menu(self.root)
        filemenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="file",menu=filemenu)
        filemenu.add_command(label="new_file")
        filemenu.add_command(label="open_file")
        filemenu.add_command(label="save")
        filemenu.add_separator()
        filemenu.add_command(label="save as")
        filemenu.add_separator()
        filemenu.add_command(label="exit",command=self.root.quit)
        # filemenu.add_command(label="file",menu=filemenu)
        self.root.config(menu=menubar)
        





if __name__=="__main__":
    root=Tk()
    obj=Nishaf(root)
    root.mainloop()

