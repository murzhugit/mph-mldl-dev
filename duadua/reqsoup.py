from bs4 import BeautifulSoup
import requests

result = requests.get("https://mp.weixin.qq.com/s/mlkcNWZbk97uB0QoK3wYjg")
content = result.text
soup = BeautifulSoup(content, "html5lib")
#title = soup.find('h2', attrs={'class':'rich_media_title'})
#print(title.text)

file = open("gettext.txt", "w")
for span in soup.find_all('span'):
    file.write(span.text + "--")
file.close()
