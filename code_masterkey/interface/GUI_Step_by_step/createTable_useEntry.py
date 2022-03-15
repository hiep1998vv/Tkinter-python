#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:52:48 2022

@author: adveng
"""

# Python program to create a table
   
from tkinter import *

class Table:
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial',10))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


 
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
   
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
   
# create root window
root = Tk()
t = Table(root)
root.mainloop()