#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:24:46 2022

@author: adveng
"""


from tkinter import *
from sys import exit
window = Tk()

# function for button1 
def click1():
    label1 = Label(window, text = "click successfully")
    label1.pack()
    return()
# creating button
button1 = Button(window, text = "click to shutdown", padx = 20, pady = 10, command = click1, fg ="blue", bg= "red")
button1.pack()

window.mainloop()