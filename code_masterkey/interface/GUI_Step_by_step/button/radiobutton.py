#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:35:23 2022

@author: adveng
"""

import wx
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Radio Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        
        radio1 = wx.RadioButton( panel, -1, " Radio1 ", style = wx.RB_GROUP )
        radio2 = wx.RadioButton( panel, -1, " Radio2 " )
        radio3 = wx.RadioButton( panel, -1, " Radio3 " )
        
        radio1.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        radio2.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        radio3.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(radio1, 0, wx.ALL, 5)
        sizer.Add(radio2, 0, wx.ALL, 5)
        sizer.Add(radio3, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        btn = event.GetEventObject()
        label = btn.GetLabel()
        message = "You just selected %s" % label
        dlg = wx.MessageDialog(None, message, 'Message', 
                               wx.OK|wx.ICON_EXCLAMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()