from gtts import gTTS
import os, json, requests, datetime
from bs4 import BeautifulSoup

#textfile = open("chinese.txt","r")
#readtexts = textfile.read()

url = "https://mp.weixin.qq.com/s?__biz=MzA3NTAwMzgzNQ==&mid=2651708492&idx=1&sn=5889e1aa7de7bd19a6413663466b8f6d&chksm=848e5e98b3f9d78ef55b639a80434322759e0747d39975918bae2c0fa41ae27b3721e99026b5&scene=0&key=9abd68f564ce3a5b5f4a5bb6e4399e09f04481b9e093274944b2eeb3ede26c5450494137df97cbae14b9e317259b2bf1e9b7c64047b4d983d8dda857cec7517e801a0eadc4cc3bba9b8cd5bb3cdb9415&ascene=0&uin=NDE5MjYwMDE1&devicetype=iMac+MacBookPro11%2C1+OSX+OSX+10.12.5+build(16F73)&version=12020810&nettype=WIFI&fontScale=100&pass_ticket=DM4Gr4jGAGO3Ogu5UavdhqJ9nUO8OyYqOd2bsbODlW%2FnmoLSyizHai1Ptd9zBPQC"

result = requests.get(url)
content = result.text
soup = BeautifulSoup(content, "html5lib")
readtexts = soup.find('h2', attrs={'class':'rich_media_title'}).text
#print(title.text)
#for span in soup.find_all('span'):
    #readtexts += span.text
    #print(readtexts)

tts = gTTS(text='你好阿 不要乱哈拉 家赛啦 要睡觉了', lang='zh-tw')
tts.save("chinese.mp3")
os.system("mpg123 chinese.mp3")

