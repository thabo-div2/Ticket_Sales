from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Ticket Sales")
root.geometry("1000x1000")
root.config(bg="#222222")


class clsTicketSales:

    myresult = StringVar()
    tickets = ["Soccer", "Movie", "Theater"]
    moviepr = 40
    soccerpr = 75
    theaterpr = 100
    line1 = StringVar()
    line2 = StringVar()
    line3 = StringVar()

    def __init__(self, master):
        # Frames
        self.frame1 = Frame(master)
        self.frame1.place(x=50, y=50, width=500, height=500)
        self.frame2 = Frame(master)
        self.frame2.place(x=50, y=500, width=500, height=500)

        # Labels
        self.cellnumber = Label(self.frame1, text="Enter CellNumber: ")
        self.cellnumber.place(x=50, y=100)
        self.tk_cat = Label(self.frame1, text="Select Ticket Category: ")
        self.tk_cat.place(x=50, y=150)
        self.tk_number = Label(self.frame1, text="Number of Tickets Bought: ")
        self.tk_number.place(x=50, y=200)
        self.myline1 = Label(self.frame2, text="-------------------------")
        self.myline1.pack()
        self.result = Label(self.frame2, text="", textvariable=self.myresult)
        self.result.pack()
        self.result2 = Label(self.frame2, text="", textvariable=self.line1)
        self.result2.pack()
        self.result3 = Label(self.frame2, text="", textvariable=self.line2)
        self.result3.pack()
        self.myline2 = Label(self.frame2, text="------------------------")
        self.myline2.pack()

        # Entries
        self.myentry = Entry(self.frame1)
        self.myentry.place(x=200, y=100)
        self.mychoice = ttk.Combobox(self.frame1, values=self.tickets, state="readonly")
        self.mychoice.place(x=200, y=150)
        self.mytickets = Entry(self.frame1)
        self.mytickets.place(x=250, y=200)

        # Buttons
        self.btn_calc = Button(self.frame1, text="Calculate Ticket", command=self.calc_payment)
        self.btn_calc.place(x=50, y=300)
        self.btn_clear = Button(self.frame1, text="Clear Entries", command=self.clear_btn)
        self.btn_clear.place(x=200, y=300)

    def calc_payment(self):
        try:
            if self.mychoice.get() == "Soccer":
                vat = self.moviepr % 14
                result1 = int(self.mytickets.get()) * self.moviepr + vat
                result2 = self.mytickets.get()
                result3 = self.mychoice.get()
                result4 = int(self.myentry.get())
                self.myresult.set("Amount Payable: " + str(result1))
                self.line1.set("Reservation for " + str(result3) + " for " + str(result2))
                self.line2.set("was done by " + str(result4))
            elif self.mychoice.get() == "Movie":
                vat = self.soccerpr % 14
                result1 = int(self.mytickets.get()) * self.soccerpr + vat
                result2 = self.mytickets.get()
                result3 = self.mychoice.get()
                result4 = int(self.myentry.get())
                self.myresult.set("Amount Payable: " + str(result1))
                self.line1.set("Reservation for " + str(result3) + " for " + str(result2))
                self.line2.set("was done by " + str(result4))
            elif self.mychoice.get() == "Theater":
                vat = self.theaterpr % 14
                result1 = int(self.mytickets.get()) * self.theaterpr + vat
                result2 = self.mytickets.get()
                result3 = self.mychoice.get()
                result4 = int(self.myentry.get())
                self.myresult.set("Amount Payable: " + str(result1))
                self.line1.set("Reservation for " + str(result3) + " for " + str(result2))
                self.line2.set("was done by " + str(result4))
        except ValueError:
            if self.mytickets.get() != int:
                self.myresult.set(messagebox.showerror(title="Error", message="Not appropriate value"))
            elif self.myentry.get() != int:
                self.myresult.set(messagebox.showerror(title="Error", message="Not appropriate value"))
            elif self.mytickets.get() < 0:
                self.myresult.set(messagebox.showerror(title="Error", message="Not appropriate value"))

    def clear_btn(self):
        self.myentry.delete(0, END)
        self.mytickets.delete(0, END)
        self.mychoice.set("Select")


x = clsTicketSales(root)
root.mainloop()
