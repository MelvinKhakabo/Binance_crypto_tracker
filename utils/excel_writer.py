# utils/excel_writer.py

import os
import pandas as pd
from datetime import datetime
from config.settings import OUTPUT_DIR

def calculate_daily_change(klines):
    """
    Calculate the daily price change from kline data.
    
    Args:
        klines (list): List of kline data [timestamp, open, high, low, close, ...].
    
    Returns:
        tuple: (date, previous_close, current_close, change_percent) or None if invalid.
    """
    if not klines or len(klines) < 2:
        return None
    
    prev_close = float(klines[0][4])  # Closing price of first day
    curr_close = float(klines[1][4])  # Closing price of second day
    change_percent = ((curr_close - prev_close) / prev_close) * 100
    date = datetime.fromtimestamp(int(klines[1][0]) / 1000).strftime('%Y-%m-%d')  # Current day
    
    return (date, prev_close, curr_close, change_percent)

def write_to_excel(symbol_data, output_dir=OUTPUT_DIR):
    """
    Process symbol data and write it to an Excel file.
    
    Args:
        symbol_data (dict): Dictionary of {symbol: klines} from BinanceClient.
        output_dir (str): Directory to save the Excel file.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Process data into a list of tuples
    data_rows = []
    for symbol, klines in symbol_data.items():
        result = calculate_daily_change(klines)
        if result:
            date, prev_close, curr_close, change_percent = result
            data_rows.append({
                "Date": date,
                "Symbol": symbol,
                "Previous Close": prev_close,
                "Current Close": curr_close,
                "Change (%)": change_percent
            })
    
    if not data_rows:
        print("No valid data to write to Excel.")
        return
    
    # Create DataFrame
    df = pd.DataFrame(data_rows)
    
    # Generate filename with current date
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"crypto_rates_{today}.xlsx"
    filepath = os.path.join(output_dir, filename)
    
    # Write to Excel
    df.to_excel(filepath, index=False)
    print(f"Data written to {filepath}")

if __name__ == "__main__":
    # Test data (replace with actual BinanceClient call later)
    test_data = {
        "BTCUSDT": [
            [1741305600000, "89931.88", "91283.02", "84667.03", "86801.75", ...],
            [1741392000000, "86801.74", "86897.25", "85218.47", "85955.89", ...]
        ]
    }
    write_to_excel(test_data)