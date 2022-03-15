# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:45:19 2022

@author: adveng
"""
"""
import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showwarning("this is my message box!", "Hello Guys :v" )
    Label(root, text = response).pack()

button = Button(root, text= "click", command= popup)
button.pack()
root.mainloop()
"""
from tkinter import Tk
from tkinter.messagebox import Message 
from _tkinter import TclError

TIME_TO_WAIT = 2000 # in milliseconds 
root = Tk() 
root.withdraw()
try:
    root.after(TIME_TO_WAIT, root.destroy) 
    Message(title="your title", message="your message", master=root).show()
except TclError:
    pass
