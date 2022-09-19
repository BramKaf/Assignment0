from genericpath import exists
from logging import captureWarnings
from struct import unpack
from tkinter import *
from datetime import date
from datetime import datetime
from datetime import timedelta
import re

root = Tk()
root.geometry("500x370")

filename = "Documents\GitHub\Assignment0\data_capital_city.txt"

#1. Vraag de user om een input -> het land
e = Entry(root, width=25)
e.pack()
e.get()
e.insert(0, "Insert country here")

Capitalstringvar = StringVar()
Capitalstringvar.set("Your answer here")
my_label = Label(root, textvariable= Capitalstringvar, font = "Helvetica 10 bold")
my_label.pack()

#2. ga door elke line heen van de file en check of het land in de line zit
def myClick():
    file = open(filename, "r")
    while True:
        line = file.readline()
        if e.get() in line:
            Capital = line.strip("\n").split("/")[1]
            Capitalstringvar.set("The Capital of " + e.get() + " is " + Capital)
            ACstringvar.set("Add capital to file, in this format: Country/Capital")
            e.delete(0, END)
            e.insert(0, "Insert country here")
            break;
        if line == "":
            Capitalstringvar.set("The Capital not known.")
            ACstringvar.set("Add capital to file, in this format: Country/Capital")
            e.delete(0, END)
            e.insert(0, "Insert country here")
            break;
    file.close()


#2a. Zo ja: haal de capital te voorschijn, display en exit.
#2b. Zo nee: ga naar de volgende line.
#3. Als ie nooit gevonden wordt, geef je aan dat ie niet bestond.   

button_city = Button(root, text="find capital", command=myClick, pady=10, padx=20)
button_city.pack(pady=20)

ACE = Entry(root, width=25)
ACE.pack()
ACE.get()
ACE.insert(0, "Country/Capital")

ACstringvar = StringVar()
ACstringvar.set("Add capital to file, in this format: Country/Capital")
AClabel = Label(root, textvariable= ACstringvar, font = "Helvetica 10 bold")
AClabel.pack()

def AC():
    file = open(filename, "r")
    while True:
        line = file.readline()
        if ACE.get() in line:
            ACstringvar.set("Already in file")
            ACE.delete(0, END)
            ACE.insert(0, "Country/Capital")
            break;
        if line == "":
            file = open(filename, "a")
            file.write("\n" + ACE.get())
            ACstringvar.set("Capital added")
            ACE.delete(0, END)
            ACE.insert(0, "Country/Capital")
            break;
    file.close()

button_city = Button(root, text="Add capital", command= AC, pady=10, padx=20)
button_city.pack(pady=20)

button_quit = Button(root, text="Exit", command=root.quit, pady=10, padx=20)
button_quit.pack(pady=20)

root.mainloop()