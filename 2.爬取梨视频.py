# 需求：爬取梨视频的视频链接，并下载

defurl = "https://www.pearvideo.com/video_1749834"
download_video(url)
def download_video(url):
    video_id = url.split("_")[1]
    print(video_id)

    video_url = "https://www.pearvideo.com/videoStatus.jsp?contId="+video_id

    import requests
    response = requests.get(video_url, #游戏机的详细信息，详情页
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",  #设置useragent
            "Referer": url #防盗链 京东首页
    })
    print(response.json()) #返回视频的信息，

    srcUrl = response.json()['videoInfo']['videos']['srcUrl']
    print(srcUrl) #404错误

    systemTime = response.json()['systemTime']
    print("系统时间：",systemTime)
    newUrl = srcUrl.replace(systemTime, "cont-"+video_id)
    print("新的链接：", newUrl)

    video_content = requests.get(newUrl).content #视频的内容
    with open("video_"+video_id+".mp4",mode="wb") as f:
        f.write(video_content)


print("结束！")