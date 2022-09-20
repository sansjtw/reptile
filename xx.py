import requests
import re
import os
import threading
import queue
import time
import os
# 导入urlopen
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("Reptile")
print("\n金条k")
print("版本:1.1")
print("https://cn-cd-dx-1.natfrp.cloud:60444\n\n")

print("请输入你要干什么？")

ssl = input("\n[1]获取网页源码\n[2]网页图片源码搜索（测试阶段，不一定100%搜索到图片）\n[3]爬取网页图片\n[4]破解微信小游戏羊了个羊（成功率较低）\n[5]百度翻译\n[6]DOS压力攻击\n[7]ping（可用于寻查网站ip）\n[8]nmap（端口扫描器）\n[9]DDOS攻击 --rudyjs\n[10]关于工具和如何使用？\n[11]退出\n\n请选择（填数字）: ")

if ssl in ["1"]: 
    os.system('python use/1.py')
    
if ssl in ["2"]: 
    os.system('python use/2.py')

if ssl in ["3"]: 
    os.system('python use/3.py')

if ssl in ["4"]: 
    a = input("测试阶段，部分可能破解不成功，这工具难度对新手可能大，新手建议练习后用！\n[1]继续使用\n[2]不用了\n")
    if a in ["1"]: 
       os.system('python use/4.py')
    
if ssl in ["5"]: 
    os.system('python use/6.py')

if ssl in ["6"]: 
    os.system('python2 use/7.py')
    
if ssl in ["7"]: 
    os.system('python use/8.py')

if ssl in ["8"]: 
    b = input("该工具为第三方工具，你安装了nmap了吗\n[1]我已安装\n[2]还没有\n")
    if b in ["2"]: 
       os.system('pkg install nmap')
       os.system('python use/9.py')
       
    if b in ["1"]: 
        os.system('python use/9.py')
        
if ssl in ["9"]: 
    c = input("该工具为第三方工具，请确认你安装rudyjs了？\n[1]已安装\n[2]未安装\n")
    if c in ["1"]: 
       os.system('python use/10.py')
    
    if c in ["2"]: 
       os.system('npm install -g rudyjs')
       os.system('python use/10.py')

if ssl in ["10"]: 
    os.system('python use/5.py')

if ssl in ["11"]: 
    exit()