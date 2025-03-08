# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file (if any)
load_dotenv()

# Binance API settings
BASE_URL = "https://api.binance.com"  # Public API base URL
KLINES_ENDPOINT = "/api/v3/klines"    # Endpoint for candlestick data (daily rates)
SYMBOLS = ["BTCUSDT", "ETHUSDT"]      # Trading pairs to fetch (e.g., BTC/USDT, ETH/USDT)
INTERVAL = "1d"                       # Daily interval
LIMIT = 2                             # Number of data points (e.g., 2 days to calculate change)

# Optional API key (not required for public endpoints but included for scalability)
API_KEY = os.getenv("API_KEY", None)

# Data output settings
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "processed")