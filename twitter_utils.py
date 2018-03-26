import tweepy
import os
import sys
import json



FILE='twitter_credentials.json'
 
class Tweet():
    def __init__(self):
        file_path = os.path.join(sys.path[0],FILE)
        config = self.read_config(file_path)
        self.consumer_key = config['consumer_key']
	self.consumer_secret = config['consumer_secret']
	self.access_token = config['access_token']
	self.access_token_secret = config['access_token_secret']
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    
    def send_tweet(self,content):
        self.api.update_status(content)

    def read_config(self,file_path):
        content = None
        with open(file_path) as json_data:
            content = json.load(json_data)
        return content
            
        


