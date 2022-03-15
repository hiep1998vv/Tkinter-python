#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:44:01 2022

@author: adveng
"""

try:
    from Tkinter import *
except:
    from tkinter import *

def change(a=0):
    color_label.config(bg = "blue" if a & 1 else "purple")
    color_label.after(400,change, a ^ 1 )

if __name__ == '__main__':
    win = Tk() 
    win.geometry("500x300")
    win.title('Demonstrating after event')
    color_label = Label(win)
    color_label.pack(expand=YES, fill=BOTH)
    change()
    
    win.mainloop()