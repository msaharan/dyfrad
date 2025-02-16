from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_text(self, text):
        if pd.isna(text):
            return 0
        return self.analyzer.polarity_scores(text)['compound']

    def analyze_dataframe(self, df, text_column):
        df['sentiment_score'] = df[text_column].apply(self.analyze_text)
        return df