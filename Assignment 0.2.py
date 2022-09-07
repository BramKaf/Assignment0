from tkinter import *
from datetime import date
from datetime import datetime
from datetime import timedelta
import re

root = Tk()
root.geometry("500x350")

#get dates from file
filename = "Desktop\SDA\events.txt"

file = open(filename, 'r')

for line in file:
    if 'Birthday' in line:
        Birthday = re.search(r'\d{2}\D\d{2}\D\d{2}', line)

verjaardag = datetime.strptime(Birthday.group(), '%d/%m/%y').date()




#get date
today = date.today()
delta = today - verjaardag
res = delta.days
if res < 0 :
    res2 = res * -1
    verjaardag_label = Label(root, text=f'{res2} days until birthday')
    verjaardag_label.pack(pady=20)
if res > 0 :
    verjaardag_label2 = Label(root, text=f'{res} days until birthday')
    verjaardag_label2.pack(pady=20)



#f_today = date.strftime("%A - %B %d, %Y")

#output date
#today_label = Label(root, text=f'today is {f_today}')
#today_label.pack(pady=20)

#countdown
#days_in_year = 365
#Birthday_day_number = int(date.strftime("%j"))


#calculate days left in year
#days_left = days_in_year - todays_day_number

#countdown_label = Label(root, text=f'there are only {days_left} days left in 2022!')
#countdown_label.pack(pady=20)


root.mainloop()