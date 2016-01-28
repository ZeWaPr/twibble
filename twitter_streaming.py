
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import read_data
import process_data
from config.py import access_token, access_token_secret, consumer_key, consumer_secret

# These are the hash tags that twibble will listen for sentiments 
hash_tags = ['#twibblets']
allTweets = []
light = -1
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        global allTweets
        # print data
        allTweets.append(data)
        if len(allTweets) == 1100:
            allTweets = allTweets[100:]

        if(len(allTweets) % 10 == 0):
            tws = read_Data.makeTweetsText(allTweets)
            light = process_data.display(tws)

        

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=hash_tags)

    