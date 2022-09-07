from tkinter import *
from datetime import date
from datetime import datetime
from datetime import timedelta
import re

root = Tk()
root.geometry("500x220")
root.configure(bg="Black")

#get dates from file
filename = "Documents\GitHub\Assignment0\events.txt"

file = open(filename, 'r')

for line in file:
    if 'Birthday' in line:
        Birthday = re.search(r'\d{2}\D\d{2}\D\d{2}', line)
Bday = datetime.strptime(Birthday.group(), '%d/%m/%y').date()

file = open(filename, 'r')
for line in file:
    if 'Begin' in line:
        BA = re.search(r'\d{2}\D\d{2}\D\d{2}', line)
BAdate = datetime.strptime(BA.group(), '%d/%m/%y').date()

file = open(filename, 'r')
for line in file:
    if 'Hand in' in line:
        EA = re.search(r'\d{2}\D\d{2}\D\d{2}', line)
EAdate = datetime.strptime(EA.group(), '%d/%m/%y').date()


#Calculate difference between today and dates
today = date.today()
delta = Bday - today
res = delta.days

delta2 = BAdate - today
BAres = delta2.days  

delta3 = EAdate - today
EAres = delta3.days

#Labeling and putting text on the screen
text1_label = Label(root, text="My countdown calender.",
    fg="Orange",
    bg="Black",
    font = "Helvetica 12 bold italic underline")
text1_label.pack(anchor=W,padx=50,pady=20) 

Bday_label2 = Label(root, text=f'It is {res} days until birthday.',
    fg= "LightBlue",
    bg="Black",
    font = "Helvetica 12 bold italic underline")
Bday_label2.pack(anchor=W, padx=50)

EA_label2 = Label(root, text=f'It is {EAres} days until hand in final assignment.',
    fg= "LightBlue",
    bg="Black",
    font = "Helvetica 12 bold italic underline")
EA_label2.pack(anchor=W, padx=50)

BA_label2 = Label(root, text=f'It is {BAres} days until start of final assignment.',
    fg= "LightBlue",
    bg="Black",
    font = "Helvetica 12 bold italic underline")
BA_label2.pack(anchor=W, padx=50)

button_quit = Button(root, text="Exit", command=root.quit, pady=10, padx=20)
button_quit.pack(pady=20)

root.mainloop()