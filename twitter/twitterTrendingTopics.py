#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from sys import exit
import tweepy
from json import loads
import json

########## CONFIG ##########
consumer_token = 'cRz70QuhNCGvFMlFHy3ARekMY'
consumer_secret = 'WBdhkig3nZ5DTFZS0UKN0k2HnmwgbQ39xQRN6kWzeE2DfvYztg'
access_token = '201832916-lLrZ1Qw4D5zQZii0k3RgOxuY0ymnyJfPkQSXu1sc'
access_secret = 'YLKNQfqIfgN9PK8IwYBd3TsSI3fkl1pfXgUkM3aP9Xgl8'
############################

def OAuth2():
	''' Returns api object '''
	cToken = consumer_token
	cSecret = consumer_secret
	aToken = access_token
	aSecret = access_secret
	# Instanciamos el gestor de autorización
	auth = tweepy.OAuthHandler(cToken, cSecret)

	'''En el caso de que no tengamos los tokens de autorización de nuestra cuenta 
	solicitaremos la url que nos generará el pin.'''

	if aToken == '' or aSecret == '':
		try:
			redirect_url = auth.get_authorization_url()
			print('Ve a Twitter y autoriza la aplicación: {0}'.format(redirect_url))
		except tweepy.TweepError:
			print('Error al solicitar el token.')

		# Le pasamos el PIN a auth para que solicite los tokens
		verifier = raw_input('Verificador: ').strip()
		auth.get_access_token(verifier)

		'''Guardamos nuestros tokens y los imprimimos en pantalla para añadirlos a las 
		   variables de configuración. Así la próxima vez no tendremos que realizar 
                   este paso.'''

		aToken = auth.access_token.key
		aSecret = auth.access_token.secret
		
	#print('Tu access_token: {0}'.format(aToken))
	#print('Tu access_secret: {0}'.format(aSecret))

	# Setea auth token y secret
	auth.set_access_token(aToken, aSecret)

	# Devolvemos una tupla para usarla con la API REST y la API de Streaming
	return (tweepy.API(auth), auth)

def getNameTrends():
	
	trends = api.trends_place(1)[0]['trends']
	
	# Extraemos el nombre de los trends y los devolvemos.
	trendList = [trend['name'] for trend in trends]
	return trendList

def getTrends():
	
	trends = api.trends_place(1)[0]['trends']
	
	# Extraemos el nombre de los trends y los devolvemos.
	return trends

api, auth = OAuth2()
trendingTopics = getTrends()
trendingTopicsNames = getNameTrends()

print json.dumps(trendingTopics,indent=1)

try:
	for topic in trendingTopicsNames:
		print(topic.encode('utf-8'))
	
except Exception,e:
	print e
	pass
	

