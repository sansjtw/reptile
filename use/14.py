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
Note.write(']---root用户使用了短链接生成\n')
Note.close()
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("短链接生成")
print("'短链接生成'该工具用于网站ssd.tw接口做成了该工具，输入你想生成的短链接后，自动开始转换，转换后会出现结果，结果的网站大概为https://aad.tw/****（参考），显示的结果包括原链接和短链接，复制后在浏览器打开，就ok啦！")
print("格式:tinyurl:短链接，longurl:原链接")
url="http://aad.tw/index.php?m=index&a=create"
xx = input("请输入你要生成短链接的网站: ")

Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---要生成短链接的链接为 %s\n'%(xx))
Note.close()

dat={
	"url":xx
	}
resp=requests.post(url,data=dat)
print(resp.json())
resp.close()