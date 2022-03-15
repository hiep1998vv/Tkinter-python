#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:36:08 2022

@author: adveng
"""

import RPi.GPIO as GPIO

GPIO_Sensor = 18
GPIO_LOCK = 16
GPIO_LED = 22
GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)

def Init():                               # void setup
     global GPIO_Sensor, GPIO_LOCK, GPIO_LED
     GPIO.setup(GPIO_Sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
     GPIO.setup(GPIO_LOCK, GPIO.OUT, initial = GPIO.HIGH)
     GPIO.setup(GPIO_LED, GPIO.OUT, initial = GPIO.HIGH)
     
def GetIOStatus(GPIO_name):              # digital read
     return GPIO.input(GPIO_name)

def SetIOOutput(GPIO_name, bool):        # digital write
     GPIO.output(GPIO_name, bool)

def EvenIO (channel, edge, callback, bouncetime):    # extenal interrupt
     GPIO.add_event_detect(channel, edge, callback, bouncetime)
     