import datetime
import requests
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('时间:['+other_StyleTime)
Note.write(']---root用户使用了百度翻译\n')
Note.close()
url="https://fanyi.baidu.com/sug"
s=input("请输入要翻译的英文单词或中文:  ")
dat={
	"kw":s
	}
resp=requests.post(url,data=dat)#发送post请求，发送的数据必须放在字典中，通过data参数进行传递
print(resp.json()) #将服务器返回的内容直接处理成json => dict
resp.close()