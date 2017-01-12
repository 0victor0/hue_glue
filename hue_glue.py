import json
import requests
from requests.exceptions import ConnectionError

class api(object):

	def __init__(self, bridge=None,key=None,
		on=None,
		light=None,
		xy = [],
		bri = None,
		sat = None,
		ct = None,
		**kwargs):
		self.bri=bri,
		self.ct = ct,
		self.bridge=bridge,
		self.key =key,
		self.light=light,
		self.on=on,
		self.sat=sat,
		self.xy = xy

		#dictionary of colors for turn_color module
		self.colors = {
		"red": 		[0.3972, 0.4564],
		"yellow": 	[0.5425, 0.4196],
		"green":	[0.41, 0.51721],
		"blue":		[0.1691, 0.0441],
		"purple":	[0.4149, 0.1776]
		}

	# Weird fix for attributes being tuples
		for item in self.__dict__:
			if type(self.__dict__[item]) is tuple:
				self.__dict__[item] =  self.__dict__[item][0]

	# # #from Hue API
	# # color 	hue 	final-x	final-y
	# # red		0		0.3972	0.4564
	# # yellow	12750	0.5425	0.4196
	# # green 	25500	0.41	0.51721
	# # blue 	46920	0.1691	0.0441
	# # purple 	56100	0.4149	0.1776
	# # red 	65280	0.6679	0.3181

	def no_light(self):
		print "Must select a light."

	def turn_on(self):
		if self.light == None:
			self.no_light()
		else:
			self.on = True
			self.api_call()

	def turn_off(self):
		if self.light == None:
			self.no_light()
		else:
			self.on = False
			self.api_call()

	def turn_color(self, choice):
		if self.light == None:
			self.no_light()
		else:
			try:
				self.xy = self.colors[choice]
				self.api_call()
			except KeyError:
				print("ERROR: Try another color, don't know the color {0}".format(choice))

	def show(self):
	# call back
		print("bridge IP: ", self.bridge)
		print("key: ", self.key)
		print("on: ", self.on)
		print("light: ", self.light)
		print("xy: ", self.xy)
		print("bri: ", self.bri)
		print("sat: ", self.sat)

	def api_call(self):

	#create payload
		payload_input = {}
		if self.bri is not None:
			payload_input["bri"] = self.bri
		if self.on is not None:
			payload_input["on"] = self.on
		if self.sat is not None:
			payload_input["sat"] = self.sat
		if len(self.xy) > 0:
			payload_input["xy"] = self.xy

		payload = json.dumps(payload_input)
		print("Payload: ", payload)

		try:
			hue_ip = "http://"+self.bridge+"/api/"+self.key+"/lights/"+str(self.light)+"/state"
			print("IP addy: ", hue_ip)
			
			r = requests.put(hue_ip, data=json.dumps(payload))
			print(r.content)

		except ConnectionError, err:
			print("CONNECTION ERROR: \n\n", err, "\n\n ...are you connected to Hue Bridge at IP: {0}?".format(self.bridge))

		except TypeError, err:
			print("URL ERROR:", err, "\n Need: bridge IP, key, lights to make API call.")