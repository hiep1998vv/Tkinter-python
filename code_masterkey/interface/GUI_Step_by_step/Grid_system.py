#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:08:49 2022

@author: adveng
"""

from tkinter import *

window = Tk()

# creating label
label1 = Label(window, text = 'label 1')
label2 = Label(window, text = 'label 2')

# grid like excel
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 1)

window.mainloop()