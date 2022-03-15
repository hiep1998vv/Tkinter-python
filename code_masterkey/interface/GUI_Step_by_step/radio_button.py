#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:24:45 2022

@author: adveng
"""

import tkinter
from tkinter import *

root = Tk()

# mode
MODES = [
         ("option1", "\noption1"),
         ("option2", "\noption2"),
         ("option3", "\noption3"),
         ("option4", "\noption4"),
         ("option5", "\noption5"),
        ]
i = IntVar()

def click(value):
    global i
    i=1
    e.insert("1.0", value)
    i+=1
    return i
# set first value
r= StringVar()
r.set("\noption1")

# create radio radio button
for text, mode in MODES:
    Radiobutton(root, text = text, variable = r, value = mode).pack()


# creat entry area
e = Text(root, height= 8, width = 30)
e.pack()

# create button
button = Button(root, text = "choose 1", command = lambda: click(r.get()))
button.pack()


root.mainloop()