#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:56:25 2022

@author: adveng
"""

import tkinter
from tkinter import *

root = Tk()


frame = LabelFrame(root, text = "1st frame", bg = "blue", padx = 100, pady = 100)
frame.pack(side = LEFT, padx =5, pady =5)

frame_2 = LabelFrame(root, text = "2nd frame", bg = "red", padx = 100, pady = 100)
frame_2.pack(side = RIGHT, padx =5, pady =5)

button_1 = Button(frame, text ="button1", bg = "white")
button_1.grid(row= 0, column = 0)

button_2 = Button(frame_2, text ="button1", bg = "white")
button_2.grid(row= 0, column = 0)

root.mainloop()