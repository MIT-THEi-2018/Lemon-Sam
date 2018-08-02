from tkinter import *

def show_entry_fields():
   print("Route Number: %s\nStops: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Route Number").grid(row=0)
Label(master, text="Stops").grid(row=1)
Label(master, text="YAY").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='test', command=show_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

mainloop( )