import requests
from bs4 import BeautifulSoup
import time
#需求：爬取三国演义小说所有的章节标题、章节内容

url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

response = requests.get(url, headers = headers)
response.encoding = "UTF-8"
# print(response.text) #打印源代码

#1. 在首页中解析出章节的标题、详情页的url链接
soup = BeautifulSoup(response.text, 'html.parser') #实例化了一个bs4
li_list = soup.find("div", class_ = "book-mulu").find("ul").find_all("li")

fp = open("sanguo.txt", "w", encoding="utf-8")
for li in li_list:
    # print(li)
    title = li.find("a").text #提取标题
    href ="https://www.shicimingju.com/" + li.find("a").attrs['href'] #提取链接
    print(title, href)
    # 2. 对详情页发起请求，解析出来具体章节内容
    detail_page = requests.get(href, headers = headers)
    detail_page.encoding = "UTF-8"
    # print(detail_page.text) #详情页源代码
    soup = BeautifulSoup(detail_page.text, "html.parser")
    detail_tag = soup.find("div", class_="chapter_content")
    print(detail_tag.text) #解析出章节内容
    fp.write(title+":"+detail_tag.text+"\n")
    time.sleep(3)

#3. 保存至文件中
print("结束")



