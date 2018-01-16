# @Author: mphz
# @Program: new_text2speech.py                                                                                                   
# @Description: use Baidu AipSpeech to transfer text to speech

from aip import AipSpeech
from pymongo import MongoClient
from datetime import datetime
import time

class ReadPlz:
	def __init__(self, appId, apiKey, secretKey):
		self.aipSpeech = AipSpeech(appId, apiKey, secretKey)
		self.client = MongoClient()
		self.db = self.client.aispeak

	def getFileText(self, filepath):
		textdata = ''
		with open(filepath, 'r', encoding='utf8') as fp:
		    textdata = fp.read().replace('\n', '')
		    print('----text char size: %d----' % len(textdata))
		    print('----text byte size: %d----' % len(textdata.encode('utf8')))

		find = self.db.textbook.find({"content": textdata})
		if find:
			print('----skip insert text, already exists----')
		else:
			self.db.textbook.insert_one({
					"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
					"from": "textfile",
					"content": textdata
				})

		return textdata

	def beginSpeak(self, text):
		alltexts = self.splitTex(text, 500)
		texttospeak = bytearray()
		for t in alltexts:
			tresult = self.aipSpeech.synthesis(t, 'zh', 1, {
		    	'vol': 7,
		    	'per': 3,
		    	'pip': 3,
		    	'spd': 5
			})
			texttospeak.extend(tresult)
		
		if not isinstance(texttospeak, dict):
		    with open('text2speech.wav', 'wb') as f:
		        f.write(texttospeak)
			# findaudio = self.db.audiobook.find({"audio": f})
			# if findaudio:
			# 	print('----skip insert audio, already exists----')
			# else:
			# 	self.db.audiobook.insert_one( {
			# 		"time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			# 		"audio" :  f
			# 	})
		pass

	def splitTex(self, string, length):
		return (string[0+i:length+i] for i in range(0, len(string), length))

if __name__ == "__main__":
	#init credential
	appId = '9914369'
	appKey = '7MNFtgdN9hez3GIau2Gul2NG'
	secretKey = 'f188e57285c1719be04662485f0799e5'

	#new object
	plz = ReadPlz(appId, appKey, secretKey)

	#start
	start_time = time.time()
	print('----begin!! text to speech----')

	#getText
	textstospeak = plz.getFileText('text.txt')
	#text to audio
	plz.beginSpeak(textstospeak)

	#done
	elapsed_time = time.time() - start_time
	spendtime = round(elapsed_time, 2)
	print('----done!! enjoy your audio----')
	print('----spend %s seconds to finish----' % str(spendtime))
