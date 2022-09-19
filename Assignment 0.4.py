from genericpath import exists
from logging import captureWarnings
from struct import unpack
from tkinter import *
from datetime import date
from datetime import datetime
from datetime import timedelta
import re

root = Tk()
root.geometry("250x200")


Capitalstringvar = StringVar()
Capitalstringvar.set("Do you want to code or DeCode?")
my_label = Label(root, textvariable= Capitalstringvar, font = "Helvetica 10 bold")
my_label.pack()

e = Entry(root, width=25,)
e.pack()
e.get()
e.insert(0, "")

#def myClick():


f1=Frame(root)
f1.pack(pady=5)
b1=Button(f1,text="enter", command=root.quit, pady=5, padx=15, bd=4)
b1.pack(expand=True,side=LEFT)
b2=Button(f1,text="Exit", command=root.quit, pady=5, padx=15, bd=4)
b2.pack(expand=True,side=LEFT)





root.mainloop()