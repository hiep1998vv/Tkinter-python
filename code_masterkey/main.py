#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:49:11 2022

@author: adveng
"""

import RPi.GPIO as RPIO
import signal
import sys
from cardReader import CardReader 

BIT_TRANSMISSION_TIME = 0.002
FRAMESIZE = 26
FRAMETIME = FRAMESIZE + BIT_TRANSMISSION_TIME
ALLOWANCE = 10
TIMEOUT = FRAMETIME + (1+ ALLOWANCE/100)

# Creating readers
readerlist = [CardReader('reader', 23, 24, TIMEOUT), CardReader('arduino', 8, 7, TIMEOUT)]

def closeProgram(signal, frame):
     
     print('\nResseting GPIO...', end= '')
     RPIO.cleanup()      # reset every channel that has been set up by this program, and unexport interrupt gpio interface
     print('ok')
     print('exiting')
     
     sys.exit()
     
signal.signal(signal.SIGINT, closeProgram)

# start reader
readersCount = 1
for reader in readerlist:
     print('initializing reader '+ str(readersCount)+ '...', end = '')
     reader.registerReader()
     print('done!')
     readersCount +=1

# ready message
print('Ready to go!')

RPIO.wait_for_interrupts()












