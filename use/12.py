# -*- coding:utf-8 -*-
import datetime
import time
import requests
import re
import os
import threading
import queue
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
Note.write(']---root用户使用了Q绑查询\n')
Note.close()
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("Q绑查询")
print("该工具仅限查询自己QQ，该工具仅限查询自己手机号是否泄露，请勿用于违法！本工具作者金条k无任何法律责任！")
xx = input('请输入你想查询的QQ:')
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---查询的QQ为:'+xx)
Note.close()
qq = requests.get('https://api.xywlapi.cc/qqapi?qq='+xx)
print(qq.text)
