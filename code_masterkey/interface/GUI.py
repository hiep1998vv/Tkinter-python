#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:38:05 2022

@author: adveng
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import tksheet



root = Tk()
root.title("Master Key GUI")
root.geometry("800x600")
root["bg"] = "white"


# function control
def click_start():
    button_start["bg"]= "green"
    button_stop["bg"] = "white"
    e.delete("1.0", END)
    e.insert("1.0", "\n Welcome to Master Key!")

def update_time():
    time_string = time.strftime('%H:%M:%S')
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
   
    label_time.config(text = hour+":" +minute+":"+second)
    label_time.after(1000, update_time)
    
def click_stop():
    button_start["bg"]= "white"
    button_stop["bg"] = "red"  
    e.delete("1.0", END)
    e.insert("1.0", "\n Turning off!!\n\nClick Start to turn on")


def show_history():
    if NAME.get() == "" or MSNV.get() =="" or combobox_key.get() =="" or combobox_DEPT.get() =="" :
        history.insert("1.0", "\n"+ "Not enough information")
    else:
        name = NAME.get()
        code = MSNV.get() 
        item_borrow = combobox_key.get()
        dept = combobox_DEPT.get()
        time_string = time.strftime('%H:%M:%S')
        history.insert("1.0", "\n"+ time_string +". "+ name +" Code :"+code+" , item borrow: "+item_borrow+ " ,Status:" +" requested!")
        update_time()

window = Frame(root, relief="sunken")    
window.pack(side="top", fill="both", expand=True)

# main label
label_masterkey = Label(window, text = "MASTER KEY", bg = "white", font =("Arial", 20), fg ="green")
label_masterkey.grid(row = 0, column = 0, columnspan=5)

label_time = Label(window, text ="", bg = "white")
label_time.grid(row =0, column = 0)

update_time()

# frame control 
frame_signup = LabelFrame(window, text = "sign up area", padx = 30, pady = 30)
frame_signup.grid(row =1, column = 0, columnspan = 5, sticky=(tk.N, tk.S, tk.W, tk.E))
frame_1 = LabelFrame(window, text = "1st frame", padx = 30, pady = 30)
frame_1.grid(row =2, column = 0, rowspan =2 , sticky=(tk.N, tk.S, tk.W, tk.E))
frame_2 = LabelFrame(window, text = "2nd frame", padx = 80, pady = 30)
frame_2.grid(row =2, column = 1, columnspan = 4, sticky=(tk.N, tk.S, tk.W, tk.E))
frame_4 = LabelFrame(window, text = "History frame", padx = 120, pady = 30)
frame_4.grid(row =3, column = 1, columnspan = 4, sticky=(tk.N, tk.S, tk.W, tk.E))


# component in frame sign up
label_key = Label(frame_signup, text = "KEY")
label_key.grid(row =0, column = 0)
label_name = Label(frame_signup, text = "NAME")
label_name.grid(row =0, column = 1)
label_code = Label(frame_signup, text = "CODE")
label_code.grid(row =0, column = 2)  
label_dept = Label(frame_signup, text = "DEPT")
label_dept.grid(row =0, column = 3)
      
item_key = [("key 1"),("key 2"),("key 3"),("key 4"),("key 5"),("key 6"),("key 7"),("key 8"),("key 9"),("key 10")]
current_key= "key 1"
combobox_key = ttk.Combobox(frame_signup, textvariable = current_key)
combobox_key["value"]=item_key
combobox_key.grid(row = 1, column = 0)


NAME = Entry(frame_signup, width = 20)
NAME.grid(row = 1, column = 1)
MSNV = Entry(frame_signup, width = 20)
MSNV.grid(row = 1, column = 2)

item_dept = [("TIM"),("PKE"),("PE1"),("MFE1"),("MFE2"),("PAE"),("PUR"),("PUS"),("PDC1"),("PDC2")]
current_DEPT= "SELECT DEPT"
combobox_DEPT = ttk.Combobox(frame_signup, textvariable = current_DEPT)
combobox_DEPT["value"]=item_dept
combobox_DEPT.grid(row = 1, column = 3)

button_request = Button(frame_signup, text = "Request", bg ="green", padx = 10, pady =10, command = show_history)
button_request.grid(row =1, column = 4)


# component in 1st frame
button_start = Button(frame_1, text ="start", command = click_start)
button_start.grid(row= 0, column = 0)
button_stop = Button(frame_1, text ="stop", command = click_stop)
button_stop.grid(row= 0, column = 1)

label_bt1= Label(frame_1, text = "    ")
label_bt1.grid(row=1, column=0, columnspan=2)

mycanvas = tk.Canvas(frame_1, height=30, width=30 )
coord = 1, 1, 15, 15
arc = mycanvas.create_arc(coord, start=0, extent=359.9999)
mycanvas.grid(row=2, column=0)
mycanvas.itemconfig(arc, fill = "red")

# component in 2nd frame
e = Text(frame_2, height= 5, width=10)
e.pack(fill= BOTH)


# component in 4th frame
sheet = tksheet.Sheet(frame_4)

sheet.grid()


sheet.total_columns(number =10)

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))


root.mainloop()