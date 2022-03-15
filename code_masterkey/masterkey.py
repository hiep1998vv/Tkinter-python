#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:06:14 2022

@author: adveng
"""

import wiegand
import time
import pigpio as gpio
import requests
import threading
import IO_init

#--------------------khai bao cac bien------------------------------------------
dem = 0
GPIO_SENSOR_ON = False
GPIO_LOCK_ON = False
GPIO_LOCK_status = False
CHUOI = None
wiegand_data = 0
w = None
pi = None
timer = 0

IO_init.Init()

# - ---------------------RFID handle--------------------------------------
def callback(bits, value):
     global CHUOI
     global IDCard_code
     print("bits {}, value {}".format( bits, bin(value)))
     IDCard_code = int(bin(value)[3:-1],2)
     print('ma ID', IDCard_code) # in ma ID code ra man hinh
     
     try:
          url = 'http://10.254.115.2:2000' + str(IDCard_code)
          print(url)
          response = requests.get(url, timeout = [1, 4]).text
          CHUOI = response
          print('chuoi nhan duoc la: ', CHUOI)
     except:
          print('khong ket noi duoc toi API')

# --Read data from RFID 
def readWiegand ():
     global w, pi
     pi = pigpio.pi()
     w = wiegand.decoder(pi, 14, 15, callback)

# ---------------------Lock handle -----------------------------
def LOCK_EVENT_DETECT():
     global GPIO_LOCK_status
     if CHUOI = None:
          GPIO_LOCK_status = False
     if CHUOI != None:
          GPIO_LOCK_status = True
          print ('Nhan chuoi oke!')
def LOCK_EVENT_handle():
     global dem
     if GPIO_LOCK_status == True and IO_init.GetIOStatus(IO_init.GPIO_Sensor) == 0 and dem ==0:  # cua dong va co tin hieu mo cua
          IO_init.SetIOOutput(IO_init.GPIO_LOCK, 1)
          dem =1
          print('state 1')                                  # activate relay
     elif GPIO_LOCK_status == True and IO_init.GetIOStatus(IO_init.GPIO_Sensor) == 1 and dem ==1:  # cua mo
          dem = 2
          IO_init.SetIOOutput(IO_init.GPIO_LOCK, 1)
          print('state 2')
     elif GPIO_LOCK_status == True and IO_init.GetIOStatus(IO_init.GPIO_Sensor) == 0 and dem ==1:  # cua mo roi lai dong lai
          dem = 0
          CHUOI = None
          GPIO_LOCK_status = False
          IO_init.SetIOOutput(IO_init.GPIO_LOCK, 1)
          print('state 3')
     elif GPIO_LOCK_status == False:
          dem = 0
          CHUOI = None
          IO_init.SetIOOutput(IO_init.GPIO_LOCK, 1) 
     else:
          dem = 0
          CHUOI = None
          IO_init.SetIOOutput(IO_init.GPIO_LOCK, 1)

# -----------------------------LED event--------------------------------
def led_alarm():
     global timer
     if IO_init.GetIOStatus(IO_init.GPIO_Sensor) == 1:
          timer +=1
     elif IO_init.GetIOStatus(IO_init.GPIO_Sensor) == 0:
          timer =0
     if timer > 20:
          timer = 21
     if timer == 21:
          IO_init.GetIOStatus(IO_init.GPIO_LED, 1-(IO_init.GetIOStatus(IO_init.GPIO_LED)))
     
# -----------------------------MAIN ------------------------------
if __name__ == '__main__':
     while True:
          try:
               readWiegand()
               
               while True:
                    if IO_init.GetIOStatus(18)== 0:
                         GPIO_SENSOR_ON = False
                         
                    LOCK_EVENT_DETECT()
                    LOCK_EVENT_handle()
                    led_alarm()
                    
                    print('---------DEBUG------------')
                    print('sensor: ', IO_init.GetIOStatus(IO_init.GPIO_Sensor))  # kiem tra sensor
                    print('lock: ', IO_init.GetIOStatus(IO_init.GPIO_LOCK))      # kiem tra Lock
                    print('LED: ', IO_init.GetIOStatus(IO_init.GPIO_LED))        # kiem tra LED
                    print('bien dem: ', dem)                                     # kiem tra gia tri bien dem
                    print('trang thai khoa: ', GPIO_LOCK_status)                 # kiem tra trangj thai Lock
                    print('trang thai cam bien: ', GPIO_SENSOR_ON)               # kiem tra trang thai cam bien
                    time.sleep(1)
          
          except:
               print('GPIO Reset') 
          finally:                       # if have bug so that make Code run to except --> turn off the GPIO and reloop by big 'while'
               print('done coding!')
               IDCard_code = 0
               IO_init.GPIO.cleanup()
                    
          
     








































          
     