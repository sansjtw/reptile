import datetime
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

now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---root用户使用了w3m浏览器\n')
Note.close()
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("w3m")
print("该工具为第三方工具，请认准原作者！\n使用说明:输入你想浏览的网站，回车开始浏览\n之后你可以使用CTRL+z来退出浏览器")
xx = input('请输入网站:  ')
Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---输入的网站为'+xx)
Note.close()
print("开始跳转w3m")
time.sleep(2)
os.system('w3m '+xx)
