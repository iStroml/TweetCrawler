import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re



class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):
        # decode json
        dict_data = json.loads(data,"utf-8")
        if (re.match('^RT @', dict_data["text"], flags=0) or dict_data["retweeted"] == 'true'):
            print("RT")
        else:
            # write list to file
            with open('tweets.txt', 'a') as outfile:
                outfile.write(str(dict_data)+ "\n")
                print("valid, added to corpus")
    # on failure
    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    listener = TweetStreamListener()

    # Info about your twitter account
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    # stream.filter(track=[':)']) Suche nach speziellen Zeichenfolgen, wurde zum Testen verwendet
    # 25073877 = @realDonaldTrump
    # 813286 = @BarackObama
    # 50393960 = @BillGates
    # 428333 = @crnbrk CNN Breaking
    # 783214 = @Twitter
    stream.filter(follow=["25073877", "813286", "50393960", "428333", "783214"])
