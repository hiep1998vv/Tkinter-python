#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:12:28 2022

@author: adveng
"""

import pigpio

class decoder:
     
     
     def __init__(self, pi, gpio_0, gpio_1, callback, bit_timeout = 2.86):
          
          self.pi = pi
          self.gpio_0 = gpio_0
          self.gpio_1 = gpio_1
          self.callback = callback
          self.bit_timeout = bit_timeout
          self.in_code = False
          
          pigpio.set_mode(gpio_0, pigpio.INPUT)
          pigpio.set_mode(gpio_1, pigpio.INPUT)
          
          pigpio.set_pull_up_down(gpio_0, pigpio.PUD_UP)
          pigpio.set_pull_up_down(gpio_1, pigpio.PUD_UP)
          
          self.cb_0 = pigpio.callback(gpio_0, pigpio.FALLING_EDGE, self._cb)
          self.cb_1 = pigpio.callback(gpio_1, pigpio.FALLING_EDGE, self._cb)
     
     def _cb(self, gpio, level, tick):
          # Accumulate bits ultil both gpios 0 and 1 timeout
          
          if level < gpio.TIMEOUT:
               if self.in_code == False:
                    self.bits = 1
                    self.num = 0
                    
                    self.in_code = True
                    self.code_timeout = 0
                    pigpio.set_watchdog(self.gpio_0, self.bit_timeout)
                    pigpio.set_watchdog(self.gpio_1, self.bit_timeout)
               else:
                    self.bits +=1
                    self.num = self.num << 1
               
               if gpio = self.gpio_0:
                    self.code_timeout = self.code_timeout & 2  # clear gpio 0 time out
               else:
                    self.code_timeout = self.code_timeout & 1  # clear gpio 1 time out 
                    
               if self.code_timeout == 3:                   # both gpios timeout
                    pigpio.set_watchdog(self.pigpio_0, 0)
                    pigpio.set_watchdog(self.pigpio_1, 0)
                    self.in_code = False
                    self.callback(self.bits, self.num)
          
     def cancel(self):
          
          # cancel Wiegand decoder
          self.cb_0.cancel()
          self.cb_1.cancel()
          
if __name__ = '__main__':
     import time
     import pigpio
     import wiegand
     
     def callback(bits, value):
          print('bits {} value {}'.format(bits, value))
     pigpio.start()
     
     w = wiegand.decoder(self, 14, 15, callback)
     
     time.sleep(300)
     
     w.cancel()
     
     pigpio.stop()

          



























