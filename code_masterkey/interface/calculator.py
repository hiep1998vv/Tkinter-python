#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:06:46 2022

@author: adveng
"""

from tkinter import *
import tkinter

window = Tk()

class calculator:

    # function
    def button_click(self, numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)
        
    def clear(self):
        self.entry.delete(0, END)
        self.operator = ""
        
    def evaluate(self):
        self.answer = eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)
        
    def __init__(self,master):
    
        self.operator = ""
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=45 )
        frame_s.grid(row=0, column=0, columnspan=3)
        self.entry = Entry(frame_s ,textvariable=self.var,bg='grey',bd=10,insertwidth=4,justify="right",font=('arial',10,'bold')) 
        self.entry.grid(row=0, column=0, columnspan=3)
        self.t = Text(self.entry,height=40)
        
            # creat button
        button1= Button(window, text = "1", padx = 20, pady=20, command = lambda: self.button_click(1))
        button1.grid(row=1, column=0)
        button2= Button(window, text = "2", padx = 20, pady=20, command = lambda: self.button_click(2))
        button2.grid(row=1, column=1)
        button3= Button(window, text = "3", padx = 20, pady=20, command = lambda: self.button_click(3))
        button3.grid(row=1, column=2)
        button4= Button(window, text = "4", padx = 20, pady=20, command = lambda: self.button_click(4))
        button4.grid(row=2, column=0)
        button5= Button(window, text = "5", padx = 20, pady=20, command = lambda: self.button_click(5))
        button5.grid(row=2, column=1)
        button6= Button(window, text = "6", padx = 20, pady=20, command = lambda: self.button_click(6))
        button6.grid(row=2, column=2)
        button7= Button(window, text = "7", padx = 20, pady=20, command = lambda: self.button_click(7))
        button7.grid(row=3, column=0)
        button8= Button(window, text = "8", padx = 20, pady=20, command = lambda: self.button_click(8))
        button8.grid(row=3, column=1)
        button9= Button(window, text = "9", padx = 20, pady=20, command = lambda: self.button_click(9))
        button9.grid(row=3, column=2)
        button0= Button(window, text = "0", padx = 20, pady=20, command = lambda: self.button_click(0))
        button0.grid(row=4, column=0)
        
        button_dot= Button(window, text = ".", padx = 20, pady=20, command = lambda: self.button_click("."))
        button_dot.grid(row=4, column=1)
        
        button_C= Button(window, text = "C", padx = 20, pady=20, command = self.clear)
        button_C.grid(row=0, column=4)
        button_add= Button(window, text = "+", padx = 20, pady=20, command = lambda: self.button_click("+"))
        button_add.grid(row=1, column=4)
        button_subtract= Button(window, text = "-", padx = 20, pady=20, command = lambda: self.button_click("-") )
        button_subtract.grid(row=2, column=4)
        button_multiply= Button(window, text = "*", padx = 20, pady=20, command = lambda: self.button_click("*"))
        button_multiply.grid(row=3, column=4)
        button_divide= Button(window, text = "/", padx = 20, pady=20, command = lambda: self.button_click("/"))
        button_divide.grid(row=4, column=4)
        
        
        button_equal= Button(window, text = "=", padx = 20, pady=20, command= self.evaluate)
        button_equal.grid(row=4, column=2)
    



c = calculator(window)
window.title("Calculator")
window.mainloop()