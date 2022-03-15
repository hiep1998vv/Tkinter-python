#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:41:55 2022

@author: adveng
"""

#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
tx = Text(root, background='white', font='Courier 12')
tx.grid(column=0, row=0, sticky=(N, W, E, S))
ybar = ttk.Scrollbar(root, orient=VERTICAL, command=tx.yview)
ybar.grid(column=1, row=0, sticky=(N, W, E, S))
xbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=tx.xview)
xbar.grid(column=0, row=1, columnspan=2, sticky=(N, W, E, S))
tx["yscrollcommand"] = ybar.set
tx["xscrollcommand"] = xbar.set
tx.tag_config('hide', elide=1)
tx.tag_config('bold', font='Courier 12 bold')
lastplace=tx.index('1.0')
def boldit():
    global tx, lastplace
    nextplace = tx.search('[B]', lastplace, 'end')
    if nextplace:
        boldon = nextplace + ' +3c'
        tx.tag_add('hide', nextplace, boldon)
        boldoff = tx.search('[/B]', boldon, 'end')
        if boldoff:
            tx.tag_add('bold', boldon, boldoff) 
            codoff = boldoff + ' +4c'
            tx.tag_add('hide', boldoff, codoff)
        lastplace = codoff
        boldit()
    else:
        return
tx.insert('1.0', """When, in the course of [B]human events,[/B] it becomes [B]necessary[/B] for one people to [B]dissolve[/B] the political bands ...""")
boldit()        
root.mainloop()


# thay mauf background
from Tkinter import *

root = Tk()
t = Text(root)
t.pack()
t.insert(END, '''\
blah blah blah Failed blah blah
blah blah blah Passed blah blah
blah blah blah Failed blah blah
blah blah blah Failed blah blah
''')
t.tag_config('failed', background='red')
t.tag_config('passed', background='blue')

def search(text_widget, keyword, tag):
    pos = '1.0'
    while True:
        idx = text_widget.search(keyword, pos, END)
        if not idx:
            break
        pos = '{}+{}c'.format(idx, len(keyword))
        text_widget.tag_add(tag, idx, pos)

search(t, 'Failed', 'failed')
search(t, 'Passed', 'passed')

#t.tag_delete('failed')
#t.tag_delete('passed')

root.mainloop()