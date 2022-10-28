# 1. 通过requests模块拿到页面源代码

import requests
import re
import csv

url = "https://movie.douban.com/top250" #d豆瓣链接
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
} #反爬
response = requests.get(url,headers=headers)
# print(response.text)

# 2. 通过re模块正则从源代码中提取影片信息


#3. 用文件将这些信息保存起来，csv
f = open("douban.csv", mode="w", encoding="utf-8",newline="") #新建/打开一个文件，返回是一个文件句柄
csvwriter = csv.writer(f) #新建一个csvwriter对象

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;/&nbsp;'
r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
r'.*?<span>(?P<number>.*?)评价</span>',re.S)  #不考虑换行，默认可以匹配多行的情况
result = obj.finditer(response.text)
for li in result:
    # print(li.group("name"), li.group("year").strip(),li.group("score"),li.group("number"))
    dic = li.groupdict() #一次返回这个电影所有的信息，字典
    dic['year'] = dic['year'].strip()
    print(dic)
    csvwriter.writerow(dic.values())

print("结束！")