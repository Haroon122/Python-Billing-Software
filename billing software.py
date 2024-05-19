from tkinter import *
import random
from tkinter import messagebox, Text, END

class Bill():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x670+0+0")
        self.root.title("Billing Software")

        # =======================bill detail variables===============================
        customer_name = StringVar()
        customer_phone = StringVar()
        item = StringVar()
        rate = IntVar()
        quantity = IntVar()
        bill_no = StringVar()
        genrate_bill = StringVar()
        x = random.randint(1000, 9999)
        bill_no.set(str(x))
        global l
        l = []

        # ==========================welcome function======================
        def welcome():
            if "Welcome Haroon Retails" not in textarea.get("1.0", "end-1c"):

                textarea.delete(1.0,"end-1c")
                #textarea.delete(1.0, END)
                textarea.insert(END, "\t Welcome Haroon Retails")
                textarea.insert(END, f"\n\n Bill Number:\t\t{bill_no.get()}")
                textarea.insert(END, f"\n Customer Name:\t\t{customer_name.get()}")
                textarea.insert(END, f"\n Phone Number:\t\t {customer_phone.get()}")
                textarea.insert(END, f"\n===========================================")
                textarea.insert(END, "\n Product \t\t QTY \t\t price")
                textarea.insert(END, f"\n===========================================\n")
                textarea.configure(font="arial 13 bold")

        # ===========================Add item function==========================
        def add_item():
            welcome()
            n = rate.get()
            m = quantity.get() * n
            l.append(m)
            if item.get() == "":
                messagebox.showerror("Error", "Please Enter The Item ")
            else:
                textarea.insert((10.0 + float(len(l) - 1)), f"{item.get()}\t\t{quantity.get()}\t\t{m}\n\n")
                
                
                item.set("")
                rate.set(0)
                quantity.set(0)
        # ===========================generate bill function==========================
        def generate_bill():
            if customer_name.get() == "" or customer_phone.get() == "":
                messagebox.showwarning("Error", "Customer Name & Phone number required")
            elif customer_name.get() == "":
                messagebox.showerror("Error", "Please enter name")
            else:
                
                tex = textarea.get(1.0,END)

                #tex = textarea.get(9.0, (9.0 + float(len(l))))
                welcome()
                textarea.delete(1.0, END)

                textarea.insert(END, tex)
                textarea.insert(END, f"\n\n===========================================")
                textarea.insert(END, f"\nTotal Paybill Amount:\t\t\t{sum(l)}")
                textarea.insert(END, f"\n===========================================")
                save_bill()

        # ===========================save function==========================
        def save_bill():
            op = messagebox.askyesno("Save Bill", "Do you want save the bill",parent=self.root)
            if op > 0:
                bill_detail = textarea.get(1.0, END)
                #f1 = open(r"D:\python projects\billing software\Bills" + str(bill_no.get()) + ".txt", "w")
                f1 = open(r"D:\python projects\billing software\Billing Details\Bills" + str(bill_no.get()) + ".txt", "w")

                f1.write(bill_detail)
                f1.close()
                messagebox.showinfo("Save", f"Bill no:{bill_no.get()} save successfully",parent=self.root)
            else:
                return

        # ===========================clear function==========================
        def clear():
            customer_name.set("")
            customer_phone.set("")
            item.set("")
            rate.set(0)
            quantity.set(0)
            welcome()

        # ===========================exit function==========================
        def exit():
            op = messagebox.askyesno("Exit", "Do you really want to exit")
            if op > 0:
                self.root.destroy()

        # Header Label Frame
        lbl1 = LabelFrame(self.root, bg="#dd677b", relief=GROOVE, bd=7, width=1350, height=70)
        lbl1.pack()

        # customer detail frame
        lbl2 = LabelFrame(self.root, text="Customer Details", font="arial 13 bold", fg="white", bg="#dd677b",
                          relief=GROOVE, bd=7, width=1350, height=100)
        lbl2.place(x=0, y=80)

        # product detail frame
        lbl3 = LabelFrame(self.root, text="Product Details", font="arial 13 bold", fg="white", bg="#dd677b",
                          width=570, height=400)
        lbl3.place(x=20, y=200)

        # main billing label
        lbl_e1 = Label(lbl1, text="Billing Software", font="arial 25 bold", fg="white", bg="#dd677b")
        lbl_e1.place(x=570, y=0)

        # customer detail label customer name
        lbl_e2 = Label(lbl2, text="Customer Name:", font="arial 15 bold", fg="white", bg="#dd677b")
        lbl_e2.place(x=30, y=20)

        # customer detail label customer phone no
        lbl_e2 = Label(lbl2, text="Phone No:", font="arial 15 bold", fg="white", bg="#dd677b")
        lbl_e2.place(x=700, y=20)

        # customer detail entry of name
        ent1 = Entry(lbl2, width=25, font=20, relief=GROOVE, bd=5, textvariable=customer_name)
        ent1.place(x=300, y=20)

        # customer detail entry of phone
        ent2 = Entry(lbl2, width=25, font=20, relief=GROOVE, bd=5, textvariable=customer_phone)
        ent2.place(x=900, y=20)

        # product detail frame in label of product name
        lbl_e3 = Label(lbl3, text="Product Name", font="arial 15 bold", fg="white", bg="#dd677b")
        lbl_e3.place(x=30, y=30)

        # product detail frame in label of product rate
        lbl_e3 = Label(lbl3, text="Product Rate", font="arial 15 bold", fg="white", bg="#dd677b")
        lbl_e3.place(x=30, y=90)

        # product detail frame in label of product quantity
        lbl_e3 = Label(lbl3, text="Product Quantity", font="arial 15 bold", fg="white", bg="#dd677b")
        lbl_e3.place(x=30, y=150)

        # product detail frame in entry of product name
        ent3 = Entry(lbl3, width=25, font=20, relief=GROOVE, bd=5, textvariable=item)
        ent3.place(x=250, y=30)

        # product detail frame in entry of product rate
        ent3 = Entry(lbl3, width=25, font=20, relief=GROOVE, bd=5, textvariable=rate)
        ent3.place(x=250, y=90)

        # product detail frame in entry of product quantity
        ent3 = Entry(lbl3, width=25, font=20, relief=GROOVE, bd=5, textvariable=quantity)
        ent3.place(x=250, y=150)

        # =======================bill area=========================
        bill_frame = Frame(self.root, relief=GROOVE, bd=10)
        bill_frame.place(x=680, y=200, width=630, height=410)
        # ======================title frame========================
        bill_title = Label(bill_frame, text="Bill Area", font="arial 15 bold", relief=GROOVE, bd=7).pack(fill=X)
        # =====================scroll bar===========================
        scroll_y = Scrollbar(bill_frame, orient=VERTICAL)
        textarea = Text(bill_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack()
        welcome()

        # ========================buttons===========================
        # Add item button
        btn = Button(lbl3, text="Add item", height=1, width=15, font="arial 15 bold", bg="#7bb3ad", relief=GROOVE,
                     bd=4, command=add_item)
        btn.place(x=100, y=220)

        # Generate bill button
        btn = Button(lbl3, text="Generate Bill", height=1, width=15, font="arial 15 bold", bg="#7bb3ad", relief=GROOVE,
                     bd=4, command=generate_bill)
        btn.place(x=330, y=220)

        # Clear button
        btn = Button(lbl3, text="Clear", height=1, width=15, font="arial 15 bold", bg="#7bb3ad", relief=GROOVE, bd=4,
                     command=clear)
        btn.place(x=100, y=300)

        # Exit button
        btn = Button(lbl3, text="Exit", height=1, width=15, font="arial 15 bold", bg="#7bb3ad", relief=GROOVE, bd=4,
                     command=exit)
        btn.place(x=330, y=300)





if __name__ == "__main__":
    root = Tk()
    obj = Bill(root)
    root.mainloop()
