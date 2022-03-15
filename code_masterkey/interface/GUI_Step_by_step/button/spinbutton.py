#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:36:58 2022

@author: adveng
"""

import wx
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Spin Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        
        self.text = wx.TextCtrl(panel, value="1")
        self.spin = wx.SpinButton(panel, style=wx.SP_VERTICAL)
        self.spin.SetRange(1, 100)
        self.spin.SetValue(1)
        
        self.Bind(wx.EVT_SPIN, self.OnSpin, self.spin)
        
        vSizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.text, 0, wx.CENTER)
        sizer.Add(self.spin, 0, wx.CENTER)
        vSizer.Add(sizer, 1, wx.CENTER)
        panel.SetSizer(vSizer)

    def OnSpin(self, event):
        self.text.SetValue(str(event.GetPosition()))
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()