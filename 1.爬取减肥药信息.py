# """
# 要求：爬取药品的字段：名字，价钱，评论数量，药品链接
# 用re来进行匹配
# """
# import requests
# import re
# import csv
# #1.requests模块爬取网页源代码
# url = "http://www.111.com.cn/search/search.action?keyWord=%25E5%2587%258F%25E8%2582%25A5%25E8%258D%25AF"
# #设置user-agent
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
# }
# response = requests.get(url,headers = headers)
# # print(response.text) #得到网页的源代码
#
# #2.re模块对源代码进行解析，提取药品的参数
# pattern = re.compile('<li id="producteg_.*?".*?'
#                      '<img alt="(?P<name>.*?)".*?'
#                      '<span>(?P<price>.*?)</span>.*?'
#                      ' href="//(?P<href>.*?)".*?'
#                      '评论 <em>(?P<comment>.*?)</em>条',re.S) #预加载正则规则
# drug_list = pattern.finditer(response.text)  #使用finditer对源代码进行遍历，根据re规则，获取到了药品的列表
#
# f = open("yaopin.csv",mode="w",encoding="utf-8",newline="") #打开一个csv文件句柄
# csvwriter = csv.writer(f) #实例化
#
# for drug in drug_list:
#     dic = drug.groupdict()
#     dic["price"] = drug.group("price").strip()+"元"
#     dic["comment"] = drug.group("comment")+"条评论"
#     print(dic)  # 字典
#     csvwriter.writerow(dic.values())
#
# print("结束！")

'''
	要求：
		字段：总价，描述，评论数量，详情页链接
	用正则爬取。
'''
import requests, re,csv

url = 'https://www.111.com.cn/search/search.action?keyWord=%25E5%2587%258F%25E8%2582%25A5%25E8%258D%25AF'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
# }
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
response = requests.get(url, headers=headers)
# print(response.text)
# 字段：药名，总价，详情页链接,评论数量
pattern = re.compile('<li id="producteg_.*?".*?'
                     'alt="(?P<name>.*?)".*?'
                     '<span>(?P<price>.*?)</span>.*?'
                     ' href="//(?P<href>.*?)".*?'
                     '评论 <em>(?P<comment>.*?)</em>条',re.S) #预加载正则规则
Drugsli_list = pattern.finditer(response.text)  #使用finditer对源代码进行遍历，根据re规则，获取到了药品的列表

#将结果写入csv文件
f = open("yaopin.csv", mode="w",newline='',encoding="utf-8") #打开一个csv文件，如果没有这个文件，就新建一个，返回文件句柄
csvwriter = csv.writer(f)

for drug in Drugsli_list:
    dic = drug.groupdict()
    print(dic)
    dic['price'] = drug.group('price').strip()+"元"
    dic['href'] = 'https://' + drug.group('href')
    dic['comment'] = drug.group('comment')+"条评论"
    csvwriter.writerow(dic.values())  # 写入一行数据

print("结束！")




