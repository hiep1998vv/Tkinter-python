#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:40:11 2022

@author: adveng
"""

from tkinter import *
from sys import exit
window = Tk()

# creatin input field
input1 = Entry(window, width = 50)
input1.pack()
input1.get() # nhan cac gia tri input
# input1.insert(0, "write your name: ")

    
# function for button1 
def click1():
    label1 = Label(window, text = "hello " + input1.get())
    label1.pack()
    return()
# creating button
button1 = Button(window, text = "click to say hello", padx = 20, pady = 10, command = click1, fg ="blue", bg= "red")
button1.pack()

window.mainloop()