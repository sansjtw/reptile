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
Note.write(']---root用户进入了工具1\n')
Note.close()
print("获取网页源码")
print("脚本由金条k制作，本人不承担任何法律责任")
print("https://cn-cd-dx-1.natfrp.cloud:60444/")
print("没有跳出已完成打印或出现了None，可能为打印失败，请那么请输入正确的网站")
print("建议使用完整的域名网站，否则可能失败率高")
xx = input("请输入完整的网站: ")
Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---root用户输入的网站为'+xx)
Note.close()
print("\n比如:/storage/emulated/0/x.txt")
cc = input("请输入源码保存位置和txt文件: ")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户输入的位置为'+cc)
Note.close()

ssl = input("\n你是否会用于违法或侵犯他人？回车默认:\n[1]是\n[2]不会的\n")
if ssl in ["是", "1"]:
    print("是自己打110还是我打？")
    exit()

elif ssl in ["不会的", "2"]:

    print("获取源码中…")
    time.sleep(1)
    Note=open("use/Reptile.txt",mode='a')
    Note.write('\n时间:['+other_StyleTime)
    Note.write(']---系统开始获取源码\n')
    Note.close()
   
# 请求获取HTML
html = urlopen(xx)
# 用BeautifulSoup解析html
obj = bf(html.read(),'html.parser')
# 从标签head、title里提取标题
title = obj.html
#直接打印到print
print(title)
#打印到文本
with open(cc,'w') as f:  # 设置文件对象
#设置打印的内容
    print(title,file = f)
    print("已完成打印自动保存至:")
    print(cc)
    print("\n期待您下次使用")
    Note=open("use/Reptile.txt",mode='a')
    Note.write('时间:['+other_StyleTime)
    Note.write(']---系统获取源码成功\n')
    Note.close()
# 使用urlretrieve下载图片
#urlretrieve(logo_url, 'logo.png')

