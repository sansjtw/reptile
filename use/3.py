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

print("提示:如果显示图片剩于0的时候，你就CTRL+c自动退出，因为没有什么可抓取的图片\n抓住的图片会保存到/storage/emulated/0/\n似乎只能抓取jpg图片\n可能会发生错误，图片损坏或长时间不运行之类，部分链接有防爬，不过网易新闻的应该可以爬到")
     
xx = input("请输入你想爬取图片的完整网站: ")
print("开始运行爬虫…")
def get_urls():
  url = xx # 主网址
  pattern = "(http.*?jpg)"
  header = {
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
  }
  r = requests.get(url,headers=header)
  r.encoding = r.apparent_encoding
  html = r.text
  urls = re.findall(pattern,html)
  return urls
def download(url_queue: queue.Queue()):
  while True:
      url = url_queue.get()
      root_path = '/storage/emulated/0/xx图片' # 图片存放的文件夹位置
      file_path = root_path + url.split('/')[-1] #图片存放的具体位置
      try:
          if not os.path.exists(root_path):
              os.makedirs(root_path)
          if not os.path.exists(file_path):
              r = requests.get(url)
              with open(file_path,'wb') as f:
                  f.write(r.content)
                  f.close()
                  print('图片保存成功')
          else:
              print('图片已经存在')
      except Exception as e:
          print(e)
      print('爬虫名:', threading.current_thread().name,"检测到图片剩余：", url_queue.qsize())

if __name__ == "__main__":
	url_queue = queue.Queue()
	urls = tuple(get_urls())
	for i in urls:
	    url_queue.put(i)
	t1 = threading.Thread(target=download,args=(url_queue,),name="虫{}".format('大'))
	t2 = threading.Thread(target=download,args=(url_queue,),name="虫{}".format('二'))
	
	t1.start()
	t2.start()