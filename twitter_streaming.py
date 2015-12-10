
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import read_data
import process_data

#Variables that contains the user credentials to access Twitter API 
access_token = "3929767222-GMfEim78KAQMqb4BP7gMva46kXXBrFt5HFr0kca"
access_token_secret = "UPnD92ncl5XSFvGrP8WKc5qOKdcPFtCQvrUhmGBOj91m3"
consumer_key = "Jh47JH54FQnQkCsDv7Kr2aq7d"
consumer_secret = "amXdnvILRcvrGM9iOhfVgQ8FnFSEkwrlNCXDXYaqS5tgHnRcwC"

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

    