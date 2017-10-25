
import json
import time
import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


def loadKeys(key_file):
    f = open("keys.json", "r")
    s = f.read()
    keys = json.loads(s)
    return keys['api_key'], keys['api_secret'], keys['token'],keys['token_secret']


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    KEY_FILE = 'keys.json'
    api_key, api_secret, token, token_secret = loadKeys(KEY_FILE)
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['ETH','NEO','BTC','NAV'])



