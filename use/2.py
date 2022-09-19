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

xx = input("请输入你想找的图片完整网站: ")
print("\n比如:/storage/emulated/0/x.txt")
cc = input("请输入源码保存位置和txt文件: ")

ssl = input("\n你是否会用于违法或侵犯他人？回车默认:\n[1]是\n[2]不会的\n")
if ssl in ["是", "1"]:
    print("是自己打110还是我打？")
    exit()

elif ssl in ["不会的", "2"]:

    print("获取源码中…")
    time.sleep(1)
   
# 请求获取HTML
html = urlopen(xx)
# 用BeautifulSoup解析html
obj = bf(html.read(),'html.parser')
# 从标签head、title里提取标题
title = obj.img
#直接打印到print
print(title)
#打印到文本
with open(cc,'w') as f:  # 设置文件对象
#设置打印的内容
    print(title,file = f)
    print("已完成打印自动保存至:")
    print(cc)
    print("\n期待您下次使用")
# 使用urlretrieve下载图片
#urlretrieve(logo_url, 'logo.png')

