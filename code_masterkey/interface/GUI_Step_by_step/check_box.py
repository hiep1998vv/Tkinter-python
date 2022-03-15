#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:20:37 2022

@author: adveng
"""

from tkinter import *

root = Tk()
def click():
    if var.get() ==1:
        Label(root, text ="ok! Start nao").pack()
    else:
        Label(root, text ="Stop!").pack()

var = IntVar()
c = Checkbutton(root, text ="on or off", variable= var, command = click)
c.deselect()
c.pack()

if var.get() ==1:
    Label(root, text ="ok! Start nao").pack()
else:
    Label(root, text ="Stop!").pack()

root.mainloop()