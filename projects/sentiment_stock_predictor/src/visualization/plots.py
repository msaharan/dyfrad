import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_sentiment_vs_price(sentiment_df, stock_data, symbol):
        plt.figure(figsize=(12, 6))
        
        # Plot stock price
        ax1 = plt.gca()
        ax2 = ax1.twinx()
        
        stock_data[symbol]['Close'].plot(ax=ax1, color='blue', label='Stock Price')
        sentiment_df.set_index('timestamp')['sentiment_score'].plot(ax=ax2, color='red', label='Sentiment')
        
        plt.title(f'{symbol} Stock Price vs Sentiment')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Stock Price')
        ax2.set_ylabel('Sentiment Score')
        
        plt.show()

    @staticmethod
    def plot_correlation_heatmap(correlations):
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlations, annot=True, cmap='RdYlGn')
        plt.title('Sentiment-Price Correlation Heatmap')
        plt.show()