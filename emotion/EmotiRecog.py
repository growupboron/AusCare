import requests
import simplejson as json
import operator
import os

subscription_key = '4548f53a00514d2e9fb1111ea292cf5c'
assert subscription_key
face_api_url = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/detect'

#image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

headers = {'Content-Type':'application/octet-stream', 
'Ocp-Apim-Subscription-Key': subscription_key }
    
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}
class Emotion:
	def capture(self):	
		print(os.getcwd())
		self.image_data=open('image.jpg','rb')
		print(self.image_data)
	def send(self):
		response = requests.post(face_api_url, params=params, headers=headers,data=self.image_data )
		print(response.text)
		text=json.dumps(response.json(), indent=4)
		text=json.dumps(response.json())
		print(text)
		final_dictionary = json.loads(text)
		emotions = final_dictionary[0]['faceAttributes']['emotion']
		print (emotions)
		predicted_emotion= max(emotions.items(), key=operator.itemgetter(1))[0]
		print(predicted_emotion)
		return final_dictionary


