from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ticket Sales")
root.geometry("1000x1000")


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
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(master)
        self.frame2.pack(side=BOTTOM)

        # Labels
        self.cellnumber = Label(self.frame1, text="Enter CellNumber: ")
        self.cellnumber.pack()
        self.tk_cat = Label(self.frame1, text="Select Ticket Category: ")
        self.tk_cat.pack()
        self.tk_number = Label(self.frame1, text="Number of Tickets Bought: ")
        self.tk_number.pack()
        self.lab4 = Label(self.frame2, text="Amount Payable: ")
        self.lab4.pack()
        self.lab5 = Label(self.frame2, text="Reservation for: ")
        self.lab5.pack()
        self.lab6 = Label(self.frame2, text="was done by: ")
        self.lab6.pack()
        self.result = Label(self.frame2, text="", textvariable=self.myresult)
        self.result.pack()
        self.result2 = Label(self.frame2, text="", textvariable=self.line1)
        self.result2.pack()
        self.result3 = Label(self.frame2, text="", textvariable=self.line2)
        self.result3.pack()

        # Entries
        self.myentry = Entry(self.frame1)
        self.myentry.pack()
        self.mychoice = ttk.Combobox(self.frame1, values=self.tickets)
        self.mychoice.pack()
        self.mytickets = Entry(self.frame1)
        self.mytickets.pack()

        # Buttons
        self.btn_calc = Button(self.frame1, text="Calculate Ticket", command=self.calc_payment)
        self.btn_calc.pack()
        self.btn_clear = Button(self.frame1, text="Clear Entries", command=self.clear_btn)
        self.btn_clear.pack()

    def calc_payment(self):
        if self.mychoice.get() == "Soccer":
            result = int(self.mytickets.get()) * self.moviepr
            self.myresult.set(result)
            self.line1.set(self.mytickets.get())
            self.line2.set(self.cellnumber.get())
        elif self.mychoice.get() == "Movie":
            result = int(self.mytickets.get()) * self.soccerpr
            self.myresult.set(result)
            self.line1.set(self.mytickets.get())
            self.line2.set(self.cellnumber.get())
        elif self.mychoice.get() == "Theater":
            result = int(self.mytickets.get()) * self.theaterpr
            self.myresult.set(result)
            self.line1.set(self.mytickets.get())
            self.line2.set(self.cellnumber.get())

    def clear_btn(self):
        self.myentry.delete(0, END)
        self.mytickets.delete(0, END)
        self.mychoice.set("Select")



x = clsTicketSales(root)
root.mainloop()
