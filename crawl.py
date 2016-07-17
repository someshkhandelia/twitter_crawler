

import requests
from requests_oauthlib import OAuth1
from pprint import pprint
import json
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


SHOW_URL = 'https://api.twitter.com/1.1/users/show.json'


auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
session = requests.Session()
session.auth = auth


x=open("splitted.txt","r")

f=open("newdata.txt","a")


for line in x:
	l=map(str,line.split())
	user_id=str(l[1])
	params = {'user_id': user_id}


	while True:
		try:
			response = session.request('GET', SHOW_URL, params=params).json()


			f.write( "user-id: "+ str(response[u'id'])+
				" followers: "+ str(response[u'followers_count'])+
				" friends: "+ str(response[u'friends_count'])+
				" screen-name: "+str(response[u'screen_name'])+
				" time-zone: "+str(response[u'time_zone'])+
				" created_at: "+str(response[u'created_at'])+
				"\n")
			f.flush()
	
			sleep(5)
			
			break

		#if connection error we will wait for connection to establish (we will wait again and again till we get connection,(while loop))
		except requests.exceptions.ConnectionError as e1:
			
			sleep(180)

		#if some other error is there then we will skip that user_id
		except Exception as el:
			break
			

f.close()
x.close()

