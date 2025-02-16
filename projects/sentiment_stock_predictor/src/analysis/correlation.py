import pandas as pd
import numpy as np

class CorrelationAnalyzer:
    @staticmethod
    def calculate_correlation(sentiment_df, stock_data):
        correlations = {}
        for symbol, prices in stock_data.items():
            # Resample sentiment data to match stock data frequency
            daily_sentiment = sentiment_df.set_index('timestamp').resample('D').mean()
            
            # Align dates and calculate correlation
            merged_data = pd.merge(
                daily_sentiment['sentiment_score'],
                prices['Close'],
                left_index=True,
                right_index=True,
                how='inner'
            )
            
            correlations[symbol] = merged_data.corr().iloc[0, 1]
        
        return correlations