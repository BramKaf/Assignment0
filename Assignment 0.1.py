from tkinter import *


root = Tk()
root.geometry("455x400")
canvas1 = Canvas(width=150, height=150,)
canvas2 = Canvas(width=150, height=150,)
canvas3 = Canvas(width=150, height=150,)
canvas4 = Canvas(width=150, height=150,)
canvas5 = Canvas(width=150, height=150,)
canvas6 = Canvas(width=150, height=150,)
root.title('Assignment 0.1')


Label1 = Label(root, text="What has to be assembled?") 
Label1.grid(row=0, column=0)

canvas1.create_oval(5,5,140,140, outline ="Blue", fill="Blue", width = 2)
canvas1.grid(row=1, column=0)
canvas2.create_oval(5,5,140,140,outline ="Yellow", fill="Yellow", width = 2)
canvas2.grid(row=1, column=1)
canvas3.create_oval(5,5,140,140,outline ="Red", fill="Red", width = 2)
canvas3.grid(row=1, column=2)
canvas4.create_rectangle(5,5,140,140, outline ="Blue", fill="Blue", width = 2)
canvas4.grid(row=2, column=0)
canvas5.create_rectangle(5,5,140,140,outline ="Yellow", fill="Yellow", width = 2)
canvas5.grid(row=2, column=1)
canvas6.create_rectangle(5,5,140,140,outline ="Red", fill="Red", width = 2)
canvas6.grid(row=2, column=2)

button_quit = Button(root, text="Exit", command=root.quit, pady=20, padx=50)
button_quit.grid(row=3, column=1)

root.mainloop()


