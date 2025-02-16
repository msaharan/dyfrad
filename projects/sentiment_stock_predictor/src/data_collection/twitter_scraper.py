import tweepy
import pandas as pd
from datetime import datetime
import yaml

class TwitterScraper:
    def __init__(self, config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f)['twitter']
        
        auth = tweepy.OAuthHandler(config['api_key'], config['api_secret'])
        auth.set_access_token(config['access_token'], config['access_token_secret'])
        self.api = tweepy.API(auth)

    def get_tweets(self, query, limit=100):
        tweets_data = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q=query, lang="en").items(limit):
            tweets_data.append({
                'timestamp': tweet.created_at,
                'text': tweet.text,
                'source': 'twitter'
            })
        return pd.DataFrame(tweets_data)