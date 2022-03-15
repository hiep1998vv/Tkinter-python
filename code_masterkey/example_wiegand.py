#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:58:32 2022

@author: adveng
"""

import time
import wiegand
import pigpio

def callback(bits, value):
     print('bits {} value {}'.format(bits, value))
     
pigpio.start()

w = wiegand.decoder(14, 15, callback)

time.sleep(300)

w.cancel()

pigpio.stop()