
import requests, json, datetime

access_token = "01cba6d9-0459-dc70-76d5-2c0021"
consumer_key = "68814-a021f707a60770b13553a55e"
get_url = 'https://getpocket.com/v3/get'


#Find the Unix Epoch timestamp exactly 24 hours before now
since = int(datetime.datetime.now().strftime("%s")) - 86400

#This HTTP POST request will return details of all Pocket articles favourited in the last 24 hours
params = {'consumer_key' : consumer_key , 'access_token' : access_token , 'favorite' : 1 , 'since' : str(since)}

a = requests.post(get_url, params=params)

response = json.loads(a.text)['list']

with open("favourited_urls","a") as file:
    for item in response:
        url = response.get(item).get('resolved_url')
        file.write(url+"\n")
        print (url) 
