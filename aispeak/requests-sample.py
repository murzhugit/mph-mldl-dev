import requests
page = requests.get('http://www.infosec-wiki.com/?cat=16')
contents = page.content
print(contents)