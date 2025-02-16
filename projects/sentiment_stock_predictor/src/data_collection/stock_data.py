import yfinance as yf
import pandas as pd
import yaml

class StockDataFetcher:
    def __init__(self, config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f)['stocks']
        self.symbols = config['symbols']
        self.timeframe = config['timeframe']
        self.period = config['period']

    def get_stock_data(self):
        stock_data = {}
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            stock_data[symbol] = ticker.history(
                period=self.period,
                interval=self.timeframe
            )
        return stock_data