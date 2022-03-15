#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:02:18 2022

@author: adveng
"""

import tkinter
from tkinter import *
import json
import requests

url ="https://tools.learningcontainer.com/sample-json.json"
response = requests.get(url, timeout=10).text
print(response)

b = json.loads(response)
c = b["address"]
print(type(c))
#address = json.loads(c)
print(b["address"])
#print(adress["city"])