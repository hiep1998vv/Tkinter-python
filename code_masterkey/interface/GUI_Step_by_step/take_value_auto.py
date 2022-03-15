#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:51:11 2022

@author: adveng
"""

import tkinter
from tkinter import *
from sys import exit


root = Tk()

# funtion
def e_change(a=0):
    e.config(e.insert(0, "1") if a&1 else e.insert(0, "0"))
    e.after(1000, e_change, a^1)
    
def e_stop():
    e.delete(0, END)

def click_start():
    e_change()

def click_stop():
    root.quit()



# button 
button_start = Button(root, text = "start", command = click_start, padx = 20, pady =20)
button_start.pack(side = LEFT)

button_stop = Button(root, text = "stop", command = click_stop, padx = 20, pady =20)
button_stop.pack(side = RIGHT)

e = Entry(root, width =50, bd =10)
e.pack()




root.mainloop()