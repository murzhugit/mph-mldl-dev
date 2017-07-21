# @Author: mphz
# @Program: new_recoaudio.py                                                                                                   
# @Description: use Baidu AipSpeech to recognize voice

from aip import AipSpeech
import time

class RecoVoice:
	def __init__(self, appId, apiKey, secretKey):
		self.aipSpeech = AipSpeech(appId, apiKey, secretKey)

	def beginReco(self, audiofile):
		result = self.aipSpeech.asr(self.get_file_content(audiofile), 'wav', 16000, {
    		'lan': 'zh',
		})
		return result

	def get_file_content(self, filepath):
		with open(filepath, 'rb') as fp:
			return fp.read()

if __name__ == "__main__":
	#init credential
	appId = '9914369'
	appKey = '7MNFtgdN9hez3GIau2Gul2NG'
	secretKey = 'f188e57285c1719be04662485f0799e5'

	#new object
	plz = RecoVoice(appId, appKey, secretKey)

	#start
	start_time = time.time()
	print('-->begin!! to recognize-->')

	#text to reco
	ret = plz.beginReco('murphyvoice.wav')

	#done
	elapsed_time = time.time() - start_time
	spendtime = round(elapsed_time, 2)
	print('-->done!! got you.-->')
	print('-->spend %s seconds to finish-->' % str(spendtime))
	print('-->the voice says: %s-->' % ret['result'])