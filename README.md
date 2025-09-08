Project Title

Binance Futures Testnet Trading Bot

Description

This is a Python-based trading bot that interacts with Binance Futures Testnet to automate the placement of buy, sell, limit, and stop-limit orders. It uses the Binance API and handles API exceptions and order errors with detailed logging.

Features

Connects to Binance Futures Testnet using API keys.

Supports market, limit, and stop-limit orders.

Provides input validation for symbol, order type, and quantity.

Handles API and order exceptions gracefully.

Maintains detailed logs in trading_bot.log.

Technologies Used

Python

Binance API (python-binance library)

Logging with Python’s built-in logging module

Installation Instructions

Clone the repository:

git clone https://github.com/yourusername/binance-futures-bot.git
cd binance-futures-bot


Install dependencies:

pip install python-binance


Run the bot:

python bot.py

How to Use

Enter Binance Testnet API Key and Secret.

Choose a symbol (e.g., BTCUSDT).

Select order side, type, and quantity.

Place market, limit, or stop-limit orders.

Check the trading_bot.log file for logs and errors.
