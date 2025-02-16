from src.data_collection.reddit_scraper import RedditScraper
from src.data_collection.twitter_scraper import TwitterScraper
from src.data_collection.stock_data import StockDataFetcher
from src.sentiment.analyzer import SentimentAnalyzer
from src.analysis.correlation import CorrelationAnalyzer
from src.visualization.plots import Visualizer

def main():
    # Initialize components
    reddit_scraper = RedditScraper('config/config.yaml')
    twitter_scraper = TwitterScraper('config/config.yaml')
    stock_fetcher = StockDataFetcher('config/config.yaml')
    sentiment_analyzer = SentimentAnalyzer()
    
    # Collect data
    reddit_data = reddit_scraper.get_posts()
    twitter_data = twitter_scraper.get_tweets("$GME OR $AMC")
    stock_data = stock_fetcher.get_stock_data()
    
    # Combine social media data
    social_data = pd.concat([reddit_data, twitter_data])
    
    # Analyze sentiment
    sentiment_data = sentiment_analyzer.analyze_dataframe(social_data, 'text')
    
    # Calculate correlations
    correlations = CorrelationAnalyzer.calculate_correlation(sentiment_data, stock_data)
    
    # Visualize results
    visualizer = Visualizer()
    for symbol in stock_data.keys():
        visualizer.plot_sentiment_vs_price(sentiment_data, stock_data, symbol)
    visualizer.plot_correlation_heatmap(correlations)

if __name__ == "__main__":
    main()