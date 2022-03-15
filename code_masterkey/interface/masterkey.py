from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from sys import exit
from time import sleep


# khoi tao cua so giao dien
window = Tk()
window.title("test")

a =0
def click2():
    global a
    a=1
    if a ==1:
        e.delete(0, END)
        e.insert(0, "start_status")
def click1():
    global a
    a=0
    if a == 0:
        e.delete(0, END)
        e.insert(0, "stop_status")
                    


    
button_stop = Button(window, text = "stop", command = click1)
button_stop.pack(side = LEFT)

button_start = Button(window, text = "start", command = click2)
button_start.pack(side = RIGHT)
e =Entry(window, width= 50)
e.pack()



window.mainloop()