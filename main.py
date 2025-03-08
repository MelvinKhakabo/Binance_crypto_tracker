# main.py

from retrieval.api_client import BinanceClient
from utils.excel_writer import write_to_excel

def main():
    """Fetch crypto rate data and export it to Excel."""
    # Initialize the Binance API client
    client = BinanceClient()
    
    # Fetch data for all symbols
    symbol_data = client.get_all_symbols_data()
    
    if not symbol_data:
        print("No data fetched. Exiting.")
        return
    
    # Write data to Excel
    write_to_excel(symbol_data)
    print("Program completed successfully.")

if __name__ == "__main__":
    main()