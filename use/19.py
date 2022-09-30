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
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户使用了 多线程压力功击\n')
Note.close()
print ("\033[1;33;40m ")

print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("whois网站信息查询")
print("该工具仅限学习，显示的信息仅限参考！输入你想查询信息的网站后，回车开始查询")
print("部分网站可能会查询失败")
xx = input('请输入你想查询信息的网站: ')
aa = "https://www.whois.com.cn/%s"%(xx)
# 请求获取HTML
html = urlopen(aa)
# 用BeautifulSoup解析html
obj = bf(html.read(),'html.parser')
# 从标签head、title里提取标题
title = obj.tbody
#直接打印到print
print("以下为查询结果")
print(title)
print("欢迎下次使用Reptile！")