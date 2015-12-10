import json
import pandas as pd 

def makeTweetsTexts(tweets_file):
	tweets = []
	for line in tweets_file:
	    try:
	        tweet=json.loads(line)
	        # tweets_data.append(tweet)
	        tweets.append(tweet['text'].encode('utf-8'))
	    except:
	        continue
	return tweets