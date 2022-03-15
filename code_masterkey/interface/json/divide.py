#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:05:56 2022

@author: adveng
"""
# Python program to create a table

import json

# some JSON:
x =[{ "name":"John", "age":30, "city":"New York"},{ "name":"kera", "age":20, "city":"New York"}]

# parse x:
for i in range(len(x)):
    a = json.dumps(x[i])
    y=json.loads(a)
    print(y["name"])
    print(y["age"])
    print(y["city"])
    
    
    

