from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from sys import exit

# khoi tao cua so giao dien
windown = Tk()
windown.geometry('700x400')
windown.title('Master Key')

# tao cac label
lbl = tkinter.Label(windown, text = "MASTER KEY", fg = "blue", font =('Arial', 20))
lbl.grid(column =10, row = 0)