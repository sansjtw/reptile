# -*- coding:utf-8 -*-
import datetime
import time
import requests
import re
import os
import threading
import queue
import os
# 导入urlopen
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve
# 获得当前时间
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户使用了reptile\n')
Note.close()
os.system("clear")
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("Reptile")
print("\n金条k")
print("版本:1.4")
print("https://cn-cd-dx-1.natfrp.cloud:60444")
print ("\033[1;34;40m ")
print("正在加载中…")
tq = requests.get('https://api.vvhan.com/api/weather')
print(tq.text)
print(" ")
qq = requests.get('http://api.btstu.cn/yan/api.php')
print(qq.text)
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---root用户进入了选择页\n')
Note.close()
print ("\033[1;33;40m ")
print("\n\n请输入你要干什么？")

ssl = input("\n[1]获取网页源码\n[2]网页图片源码搜索（测试阶段，不一定100%搜索到图片）\n[3]爬取网页图片\n[4]破解微信小游戏羊了个羊（成功率较低）\n[5]百度翻译\n[6]DOS压力攻击\n[7]ping（可用于寻查网站ip）\n[8]nmap（端口扫描器）\n[9]DDOS攻击 --rudyjs\n[10]w3m浏览器\n[11]Q绑查询\n[12]ip地址查询\n[13]短链接生成\n[14]手机号归属地查询\n[15]域名注册查询\n[16]信息轰炸1.0\n[17]关于工具和如何使用？\n[18]退出\n[19]查看日志\n\n请选择（填数字）: ")

if ssl in ["1"]: 
    os.system('python use/1.py')
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具1\n')
    Note.close()
if ssl in ["2"]: 
    os.system('python use/2.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具2\n')
    Note.close()
if ssl in ["3"]: 
    os.system('python use/3.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具3\n')
    Note.close()

if ssl in ["4"]: 
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具4\n')
    Note.close()
    a = input("测试阶段，部分可能破解不成功，这工具难度对新手可能大，新手建议练习后用！\n[1]继续使用\n[2]不用了\n")
    if a in ["1"]: 
       os.system('python use/4.py')
       now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具4，选择了1\n')
    Note.close()
    
if ssl in ["5"]: 
    os.system('python use/6.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具5\n')
    Note.close()

if ssl in ["6"]: 
    os.system('python2 use/7.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具6\n')
    Note.close()
    
if ssl in ["7"]: 
    os.system('python use/8.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具7\n')
    Note.close()

if ssl in ["8"]: 
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具8\n')
    Note.close()
    b = input("该工具为第三方工具，你安装了nmap了吗\n[1]我已安装\n[2]还没有\n")
    if b in ["2"]: 
       os.system('pkg install nmap')
       os.system('python use/9.py')
       now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具8，选择了2\n')
    Note.close()
       
    if b in ["1"]: 
        now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具8，选择了1\n')
    Note.close()
    os.system('python use/9.py')
        
if ssl in ["9"]: 
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具9\n')
    Note.close()
    c = input("该工具为第三方工具，请确认你安装rudyjs了？\n[1]已安装\n[2]未安装\n")
    if c in ["1"]: 
       os.system('python use/10.py')
       now = datetime.datetime.now()
       other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
       Note=open("use/Reptile.txt",mode='a')
       Note.write('时间:['+other_StyleTime)
       Note.write(']---root用户关闭了工具9，选择了1\n')
       Note.close()
    
    if c in ["2"]: 
       os.system('pkg install npm')
       os.system('npm install -g rudyjs')
       os.system('python use/10.py')
       now = datetime.datetime.now()
       other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
       Note=open("use/Reptile.txt",mode='a')
       Note.write('时间:['+other_StyleTime)
       Note.write(']---root用户关闭了工具9，选择了1\n')
       Note.close()

if ssl in ["10"]: 
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户使用了工具10\n')
    Note.close()
    pp = input('该工作于第三方工具，确认你安装了？\n[1]已安装\n[2]未安装\n')
    if pp in ["1"]: 
        os.system('python use/11.py')
        now = datetime.datetime.now()
        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        Note=open("use/Reptile.txt",mode='a')
        Note.write('时间:['+other_StyleTime)
        Note.write(']---root用户关闭了工具10\n')
        Note.close()
       
    if pp in ["2"]:
        os.system('pkg install w3m')
        os.system('python use/11.py')
        now = datetime.datetime.now()
        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        Note=open("use/Reptile.txt",mode='a')
        Note.write('时间:['+other_StyleTime)
        Note.write(']---root用户关闭了工具10\n')
        Note.close()

if ssl in ["11"]: 
    os.system('python use/12.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具11\n')
    Note.close()
    
if ssl in ["12"]: 
    os.system('python use/13.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具12\n')
    Note.close()

if ssl in ["13"]: 
    os.system('python use/14.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具13\n')
    Note.close()
    
if ssl in ["14"]: 
    os.system('python use/15.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具14\n')
    Note.close()
   
if ssl in ["15"]: 
    os.system('python use/16.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具15\n')
    Note.close()

if ssl in ["16"]: 
    os.system('python use/17.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了工具16\n')
    Note.close()
    
if ssl in ["17"]: 
    os.system('python use/5.py')
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户关闭了教程\n')
    Note.close()

if ssl in ["18"]: 
    exit()
    now = datetime.datetime.now()
    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---root用户使用了退出程序\n')
    Note.close()
    
if ssl in ["19"]: 
    print("你可以通过 rm -frv use/Reptile.txt 命令来清除日志")
    f = open("use/Reptile.txt",encoding = "utf-8")
    print(f.read(99999999))
    f.close()