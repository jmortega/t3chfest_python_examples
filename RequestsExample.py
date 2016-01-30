# -*- encoding: utf-8 -*-

import requests, json

print "Requests Library tests."

#responseGet = requests.get("http://api.openweathermap.org/data/2.5/weather?&q=alicante&appid=0888d6d73eeb6588a5b5da08f4d32bb9")

responseGet = requests.get("http://api.openweathermap.org/data/2.5/weather", 
params = {"q":"malaga","appid":"0888d6d73eeb6588a5b5da08f4d32bb9"})

print responseGet.text.encode('utf-8')

print responseGet.json

print responseGet.encoding

print responseGet.content

print "Status code: "+str(responseGet.status_code)

print "Headers response: "
for header, value in responseGet.headers.items():
  print(header, '-->', value)
  
print "Headers request : "
for header, value in responseGet.request.headers.items():
  print(header, '-->', value)