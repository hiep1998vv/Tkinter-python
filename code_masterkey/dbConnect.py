#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:21:18 2022

@author: adveng
"""

import MySQLdb
import time
from datetime import datetime

def create_connection(host = 'localhost', user = 'root', passwd = 'hangmoon', db = 'dbUser'):
     
     try:
          dbConn = MySQLdb.connect(host=host,  #your host, usually local host
                                   user=user,  # your user name
                                   passwd=passwd  # your password
                                   db=db
                                   )
          # you must create a cursor object. it'll let you execute all the queries you need
          return dbConn
     except Exception as e:
          print(e)
     
     return None

def select_all_tasks(dbConn):
     
     cur = dbConn.cursor()
     cur.excute('select * from tbUser')
     
     rows = cur.fetchall()
     
     for row in rows:
          print(row)

def insert_task_history(dbConn, userIDCard, isCard):
     
     cur = dbConn.cursor()
     select_task_by_priority(dbConn, userIDCard)
     
     sq1 = "insert into dbHistory (userName, userIDCard, openwithIDCard, datetime) values (%s, %s, %s, %s)"
     val = ('peter', 'lowstreet 4')
     cur.excute(sq1, val)
     rows = cur.fetchall()
     
     for row in rows:
          print(row)
          
def select_task_by_priority(conn, priority):
     
     cur = conn.cursor()
     strCommand = "select * from tbUser where cardID {}".format(priority)
     cur.excute(strCommand)
     
     rows = cur.fetchall()
     
     for row in rows:
          print(row)
     return row

def get_userName(row):
     
     print(row[1])
     return row[1]

def get_permission(row):
     
     print(row[3])
     return row[3]

def inserdatetohistory(conn, username, cardid):
     try:
          timenow = str(datetime.now())
          cur = conn.cursor()
          strCommand = "insert into 'tbHistory'('historyID', 'userName', 'cardID', 'time')"\ "values (NULL, '{0}', '{1}', '{2}');".format(username, cardid, timenow)

          cur.excute(strCommand)
          print('insert ok')
          return 1
     except:
          print('insert NG')
          return 0

def main():
     try:
          conn = create_connection(host = 'localhost', user = 'root', passwd = 'hangmoon', db = 'dbUser')
          
          while(1):
               with conn:
                    print('1. Query task by priority:')
                    row = select_task_by_priority(conn, 12345)
                    print('user')
                    get_userName(row)
                    print('permission')
                    get_permission(row)
                    time.sleep(1)
                    
     finally:
          conn.close()
          
if __name__ = '__main__':
     main()

          
          
          
          
          


















