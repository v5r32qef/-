# 需求：爬取梨视频的视频链接，并下载
# url = "https://www.pearvideo.com/video_1763204"
url = "https://www.pearvideo.com/video_1763507"
video_id = url.split("_")[1]
print(video_id)
#1、爬取源代码，看源代码中是否有视频链接
# 结果：搜索".mp4"关键字，没有搜到，视频链接不在源代码中；

#2、通过查看Network面板-> XHR -> 发送视频的链接地址
video_url = "https://www.pearvideo.com/videoStatus.jsp?contId="+video_id

#3. 向url发送get请求，得到视频的信息
import requests
response = requests.get(video_url, #游戏机的详细信息，详情页
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",  #设置useragent
        "Referer": url #防盗链 京东首页
})
print(response.json()) #返回视频的信息，
#4、获取了视频的链接
srcUrl = response.json()['videoInfo']['videos']['srcUrl']
print(srcUrl) #404错误

# 将爬取的链接中的systemTime，替换成cont-video_id
systemTime = response.json()['systemTime']
print("系统时间：",systemTime)
newUrl = srcUrl.replace(systemTime, "cont-"+video_id)
print("新的链接：", newUrl)

# 爬取的链接：   https://video.pearvideo.com/mp4/adshort/20220524/1653618968522-15884803_adpkg-ad_hd.mp4
# 可以播放的链接：https://video.pearvideo.com/mp4/adshort/20220524/cont-1763204-15884803_adpkg-ad_hd.mp4
#5、进行视频的下载
video_content = requests.get(newUrl).content #视频的内容
with open("vido.mp4",mode="wb") as f:
    f.write(video_content)

print("结束！")