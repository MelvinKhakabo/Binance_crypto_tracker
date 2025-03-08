# Binance Crypto Tracker

This project fetches daily cryptocurrency rate changes from the Binance public API, processes the data, and exports it to an Excel file. It’s designed with a modular structure for maintainability and scalability, built using Python.

## Project Purpose
- Connect to the Binance API.
- Fetch daily price change data for specified cryptocurrency pairs (e.g., BTC/USDT).
- Process and calculate daily changes.
- Export the results to an Excel file.

## Folder Structure
binance_crypto_tracker/
├── config/          # Configuration settings (API endpoints, constants)
├── data/            # Raw and processed data storage
│   ├── raw/        # Raw API responses (optional)
│   └── processed/  # Exported Excel files
├── retrieval/       # API interaction logic
├── utils/           # Utility functions (Excel writing, helpers)
├── .env            # Environment variables (optional API key)
├── main.py         # Main script to run the program
├── requirements.txt # Project dependencies
└── README.md       # This file


## Prerequisites
- Python 3.8 or higher
- Visual Studio Code (or any IDE)
- Git (optional, for version control)

## Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/Binance_crypto_tracker.git
   cd Binance_crypto_tracker