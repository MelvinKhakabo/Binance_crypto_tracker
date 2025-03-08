# retrieval/api_client.py

import requests
from config.settings import BASE_URL, KLINES_ENDPOINT, SYMBOLS, INTERVAL, LIMIT

class BinanceClient:
    """A client for interacting with the Binance public API."""
    
    def __init__(self):
        self.base_url = BASE_URL
        self.endpoint = KLINES_ENDPOINT
    
    def fetch_klines(self, symbol, interval=INTERVAL, limit=LIMIT):
        """
        Fetch candlestick (kline) data for a given trading pair.
        
        Args:
            symbol (str): Trading pair (e.g., "BTCUSDT").
            interval (str): Time interval (default: "1d" from settings).
            limit (int): Number of data points to fetch (default: 2 from settings).
        
        Returns:
            list: List of kline data points or None if the request fails.
        """
        url = f"{self.base_url}{self.endpoint}"
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()  # Returns list of [timestamp, open, high, low, close, ...]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
    
    def get_all_symbols_data(self):
        """
        Fetch kline data for all symbols specified in settings.
        
        Returns:
            dict: Mapping of symbol to its kline data.
        """
        all_data = {}
        for symbol in SYMBOLS:
            data = self.fetch_klines(symbol)
            if data:
                all_data[symbol] = data
        return all_data

if __name__ == "__main__":
    # Test the client
    client = BinanceClient()
    data = client.get_all_symbols_data()
    for symbol, klines in data.items():
        print(f"{symbol}: {klines}")