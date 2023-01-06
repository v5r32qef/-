import requests
import json
#1.指定url
url = "https://fanyi.baidu.com/sug" #返回的是json对象
#2.
s = input("请输入你要翻译的英文单词：")
dat = {
    "kw": s
}
#3.发送post请求, 发送的数据必须放在字典中, 通过data参数进行传递
resp = requests.post(url, data=dat)
print(resp.json())  # 将服务器返回的内容直接处理成json()  => dict
#resp.text 源代码

f = open(".json",mode="w",encoding="utf-8")#点前面写要翻译的单词，要翻译什么就写什么
json.dump(resp.json(),fp=f,ensure_ascii=False)
#json.dumps 序列化时对中文默认使用的ascii编码.
# 想输出真正的中文需要指定ensure_ascii=False
