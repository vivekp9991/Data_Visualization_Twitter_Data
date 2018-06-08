from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json
import csv
#Variables that contains the user credentials to access Twitter API
access_token = "xxxx"
access_token_secret = "xxxx"
consumer_key = "xxxx"
consumer_secret = "xxxx"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, result):
        print(result)

        mydata=json.loads(result)
        tweet=mydata['text'].encode("utf-8")
        time=mydata["created_at"]
        tweet_id=mydata["id"]
        user_id=mydata["user"]["id"]
        print(tweet,time,tweet_id,user_id)
        with open("alldata.csv",'a') as csvfile:
         myfile=csv.writer(csvfile)
         myfile.writerow([time,tweet,tweet_id,user_id])
        return True

def on_error(self, status):
    print(status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'])