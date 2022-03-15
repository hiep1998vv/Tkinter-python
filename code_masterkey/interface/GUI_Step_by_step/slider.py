#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:04:56 2022

@author: adveng
"""

from tkinter import *

root = Tk()
root.geometry("800x800")
def click_scale():
    root.geometry(str(HORIZONTAL.get())+"x"+str(VERTICAL.get()))

VERTICAL = Scale(root, from_= 0, to = 800)
VERTICAL.pack()

HORIZONTAL = Scale(root, from_= 0, to = 800, orient= HORIZONTAL)
HORIZONTAL.pack()

button_scale = Button(root, text = "scale", command = click_scale).pack()


root.mainloop()