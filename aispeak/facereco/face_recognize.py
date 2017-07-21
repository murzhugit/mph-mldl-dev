# @Author: mphz
# @Program: face_recognize.py                                                                                                   
# @Description: use Baidu Aipface to recognize face

from aip import AipFace
import time

class FaceReco:
	def __init__(self, appId, apiKey, secretKey):
		self.aipface = AipFace(appId, apiKey, secretKey)

	def beginReco(self, picfile):
		options = {
	        'max_face_num': 1,
	        'face_fields': "age,beauty,expression,faceshape",
	    }
		result = self.aipface.detect(self.get_file_content(picfile), options)
		return result

	def get_file_content(self, filepath):
		with open(filepath, 'rb') as fp:
			return fp.read()

if __name__ == "__main__":
	#init credential
	appId = '9918582'
	appKey = 'ZHQ69ptYV8OoqWee0ee6cGpS'
	secretKey = 'LbDFalAZIn1S3hlmMXCV9ImpqSia2oG7'

	#new object
	plz = FaceReco(appId, appKey, secretKey)

	#start
	start_time = time.time()
	print('-->begin!! to recognize-->')

	#text to reco
	ret = plz.beginReco('murphyface.jpg')

	#done
	elapsed_time = time.time() - start_time
	spendtime = round(elapsed_time, 2)
	print('-->done!! got you.-->')
	print('-->spend %s seconds to finish-->' % str(spendtime))
	print(ret)