import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入要翻译的英文单词或中文:  ")
dat={
	"kw":s
	}
resp=requests.post(url,data=dat)#发送post请求，发送的数据必须放在字典中，通过data参数进行传递
print(resp.json()) #将服务器返回的内容直接处理成json => dict
resp.close()