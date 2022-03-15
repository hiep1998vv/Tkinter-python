#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:20:58 2022

@author: adveng
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()

# create a main frame
main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)

# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT, fill = BOTH, expand =1)



# create a scrollbar to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient= VERTICAL, command= my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)

my_scrollbar1 = ttk.Scrollbar(main_frame, orient= HORIZONTAL , command= my_canvas.xview)
my_scrollbar1.pack(side = BOTTOM, fill = X)

# configure the canvas
my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

my_canvas.configure(xscrollcommand = my_scrollbar1.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# create another frame into canvas
second_frame = Frame(my_canvas)

my_canvas1 = Canvas(second_frame)
my_canvas1.pack(side = LEFT, fill = BOTH, expand =1)
# add that new frame to a window in the canvas
my_canvas.create_window((0,0), window = second_frame, anchor="center")

frame_1 = LabelFrame(my_canvas1, text = "test1")
frame_2 = LabelFrame(my_canvas1, text = "test2")
frame_3 = LabelFrame(my_canvas1, text = "test3")

frame_1.grid(row = 0, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
frame_2.grid(row = 0, column=1, sticky=(tk.W, tk.E, tk.S, tk.N))
frame_3.grid(row = 1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))

e1 = Text(frame_1).pack()
e2 = Text(frame_2).pack()
e3 = Text(frame_3).pack()


root.mainloop()