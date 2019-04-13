import os
from emotion import EmotiRecog  
from flask import Flask,jsonify,request
import time
from threading import Thread
import json
obj1=EmotiRecog.Emotion()

#from werkzeug import secure_filename
#os.system("./ngrok http 5000")
class Function:
	def __init__(self):
		self.stop=False
		self.time=0
		self.rurl=None
	def Work(self):
		i=1
		while(i):
			if(self.stop):
				break
			obj1.capture()
			obj1.send()
			i+=1
		return
	def Loging(self,session,Time,hr,attention=None,Type=None,):
		with open("data.json") as json_file:
			data=json.load(json_file)
			l=len(data['today'])
			print(l)
			data['today'].append({})
			print(len(data['today']))
			data['today'][l]["session"] = session
			data['today'][l]["time"] = Time
			data['today'][l]["heartrate"] = hr
			if(attention):
				data['today'][l+1]["attention"] =attention
			if(Type):
				data['today'][l+1]["type"] = Type
			json_file.seek(0)
			json.dump(data, json_file, indent=4)
			json_file.truncate()
		pass

	def TrainigStencile(self):
		before=time.time()
		while(not self.stop):
			print("Stencile")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
		# obj.capture()
		# res=obj.send()
	def Rhymes(self):
		before=time.time()
		while(not self.stop):
			print(self.rurl)
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
	def Beats(self):
		before=time.time()
		while(not self.stop):
			print("Beates")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
	def Play(self):
		before=time.time()
		while(not self.stop):
			print("play")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
obj=Function()

app=Flask(__name__)

@app.route("/")
def hello():
	return "hello world!"

@app.route("/emotirecog/start")
def rec():
	thread=Thread(target=obj.Work)
	if(obj.stop):
		obj.stop=False
	thread.start()
	print("ended")
	return "started"

@app.route("/emotirecog/stop")
def stop():
	obj.stop=True
	return 'ended'

@app.route("/training/stensile/start")
def trainigStencileStart():
	thread=Thread(target=obj.TrainigStencile)
	if(obj.stop):
		obj.stop=False
	thread.start()
	value=None
	Type=request.args.get('name')
	if(Type=='English'):
		value="started english"
	elif Type=='Hindi':
		value="started Hindi"
	elif Type=='Maths':
		value="started Maths"
	
	return(value)
@app.route("/training/stensile/stop")
def trainigStencileStop():
	obj.stop=True
	return("stopped")

@app.route("/training/Rhymes/start")
def StartRhymes():
	obj.rurl=request.args.get("url")
	thread=Thread(target=obj.Rhymes)
	if(obj.stop):
		obj.stop=False
	thread.start()
	#send the hit the url to play video
	return("rhyme started")
@app.route("/training/Rhymes/stop")
def StopRhymes():
	obj.stop=True
	return("stopped")

@app.route('/beats/start')
def StartBeats():
	thread=Thread(target=obj.Beats)
	if(obj.stop):
		obj.stop=False
	thread.start()
	#send the hit the url to play video
	return("beat started")

@app.route('/beats/stop')
def StopBeats():
	obj.stop=True
	return("stopped")

@app.route('/play/start')
def StartPlay():
	thread=Thread(target=obj.Play)
	if(obj.stop):
		obj.stop=False
	thread.start()
	#send the hit the url to play video
	return("video started")

@app.route('/play/stop')
def StopPlay():
	obj.stop=True
	return("stopped")
	#stop video
	pass


