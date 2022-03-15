#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:36:21 2022

@author: adveng
"""

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x500")
def click():
    global img
    top = tk.Toplevel()
    img = ImageTk.PhotoImage(Image.open("1x.jpeg"))
    label = Label(top, text=img).pack()
    button_2 = Button(top, text= "close", command= top.destroy).pack()
    
button = Button(root, text = "open img", command = click).pack()



root.mainloop()