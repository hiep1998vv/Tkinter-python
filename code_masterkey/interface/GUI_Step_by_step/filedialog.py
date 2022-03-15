#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:17:58 2022

@author: adveng
"""

from tkinter import *
from PIL import *
from tkinter import filedialog

root = Tk()

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir = "images/", title= "select file", filetypes = (("jpeg file", "*.jpeg"), ("all files", "*.*")))
    Label(root, text = root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(image = img).pack()

Button(root, text = "open Files", command = open).pack()



root.mainloop()
