from tkinter import *

def obtain_str_ticker(ticker):
    pass

def obtain_str_start(start):
    pass

def obtain_str_end(end):
    pass

def provide_values(ticker, start, end):
    pass

def get_entries(val_1, val_2, val_3):
    print(str(val_1.get()), str(val_2.get()), str(val_3.get()))


master = Tk()

sv = StringVar()
dv1 = StringVar()
dv2 = StringVar()

Label(master, text="Ticker Symbol").grid(row=0)
Label(master, text="Start (YYYY-MM-DD").grid(row=1)
Label(master, text="End (YYYY-MM-DD)").grid(row=2)

stock_entry = Entry(master, textvariable=sv).grid(row=0, column=1)
start_entry = Entry(master, textvariable=dv1).grid(row=1, column=1)
end_entry = Entry(master, textvariable=dv2).grid(row=2, column=1)

collectBtn = Button(master, text="Collect Data", padx=20, command=lambda: get_entries(sv, dt1, dt2)).grid(row=3)




master.mainloop()