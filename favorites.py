# Get Text and URL in your Twitter favorites which contains URLs

from twitter import *
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

instance = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

favorites_list = instance.favorites.list(screen_name="TapasweniPathak", count=500)

for tweet in favorites_list:
	try:
		url = tweet['entities']['urls'][0]['expanded_url']
		print url
		tweet_text = tweet['text']
		print tweet_text
	except Exception, e:
		a = 1
