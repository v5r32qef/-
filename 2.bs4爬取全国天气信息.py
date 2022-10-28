import requests
from bs4 import BeautifulSoup
import csv
#1.用requests获取网页源代码

f = open("tianqi.csv", mode="a",newline='',encoding="utf-8") #打开一个csv文件，如果没有这个文件，就新建一个，返回文件句柄
csvwriter = csv.writer(f)

urls = [
    "http://www.weather.com.cn/textFC/hb.shtml",
    "http://www.weather.com.cn/textFC/hz.shtml",
    "http://www.weather.com.cn/textFC/xb.shtml",
    "http://www.weather.com.cn/textFC/hd.shtml"
]
for url in urls:
    print(url)
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    # print(response.text) #页面源代码

    #2.用bs4来提取天气：城市、最低气温
    soup = BeautifulSoup(response.text,'html.parser')
    tables = soup.find("div", class_="conMidtab").find_all('table')

    for table in tables: #table表示一个省
        tr_tags = table.find_all("tr")[2:] #tr_tags:表示所有的城市
        for index,tr in enumerate(tr_tags):
            tds = tr.find_all("td")
            if index==0:
                city = tds[1].text.strip()
            else:
                city = tds[0].text.strip()
            temp = tds[-2].text
            print(city,temp)
            arr = []
            arr.append(city)
            arr.append(temp)
            csvwriter.writerow(arr) #写入一个数组

print("结束！")
