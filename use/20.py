# -*- coding:utf-8 -*-
import datetime
import time
import requests
import re
import os
import threading
import queue
import os
import wget
# 导入urlopen
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户使用了 wget下载器\n')
Note.close()
print ("\033[1;33;40m ")

print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("wget文件下载器")
print ("输入你想下载的文件链接后，回车开始下载！支持mp4、mp3、txt、png、apk等，几乎支持所有文件！")
print("文件下载完成后，可能会出现报错等情况，可能为正常行为，以实际情况为准！可以参考以下提示，查看文件是否存在")
print("手机:/storage/emulated/0/")
print("系统:D:/\n")
xx = input('输入你想下载文件的网站链接: ')
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---下载的链接为 %s\n'%(xx))
Note.close()
kk = input('请输入你的设备: \n[1]电脑\n[2]手机\n')
if kk in ["1"]: 
   a = "D:/"

if kk in ["2"]: 
   a = "/storage/emulated/0/"
print("开始下载")
url = xx # 目标路由，下载的资源是图片
path = a # 保存的路径
wget.download(url, path) # 下载
print("已保存文件至 "+a)