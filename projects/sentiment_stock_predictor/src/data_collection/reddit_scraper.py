import praw
import pandas as pd
from datetime import datetime
import yaml

class RedditScraper:
    def __init__(self, config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f)['reddit']
        
        self.reddit = praw.Reddit(
            client_id=config['client_id'],
            client_secret=config['client_secret'],
            user_agent=config['user_agent']
        )
        self.subreddits = config['subreddits']

    def get_posts(self, limit=100):
        posts_data = []
        for subreddit_name in self.subreddits:
            subreddit = self.reddit.subreddit(subreddit_name)
            for post in subreddit.hot(limit=limit):
                posts_data.append({
                    'timestamp': datetime.fromtimestamp(post.created_utc),
                    'title': post.title,
                    'text': post.selftext,
                    'score': post.score,
                    'source': 'reddit'
                })
        return pd.DataFrame(posts_data)