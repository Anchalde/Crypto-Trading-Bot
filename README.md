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
2. Blog Post Draft

Here’s a sample blog post for the project:

Automating Cryptocurrency Trading: Building a Binance Futures Testnet Bot with Python

Automating cryptocurrency trading is one of the most exciting ways to leverage programming skills in the world of finance. In this project, I built a Python-based trading bot for the Binance Futures Testnet that allows users to place market, limit, and stop-limit orders through an intuitive command-line interface.

The bot uses the python-binance library to interact with Binance’s API and ensures smooth execution by handling potential API exceptions and order failures. I also implemented logging with Python's built-in logging module to track all activities, making debugging and analysis much easier.

This project is a great way to learn:

How APIs work and how to authenticate them.

Exception handling in real-time applications.

Validating user input to ensure robustness.

Maintaining logs for monitoring and troubleshooting.

Check out the code on my GitHub
, try it out, and start experimenting with your own automated trading strategies!

Place market, limit, or stop-limit orders.

Check the trading_bot.log file for logs and errors.
3. Log Files

The logging is already handled in your bot.py script with this configuration:

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


You don’t need to manually create this file. It will automatically generate logs as you run and interact with the bot. Example entries might look like:
2025-09-08 20:15:34,123 - INFO - Initialized Binance Client with testnet=True
2025-09-08 20:16:12,456 - INFO - Placing order: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'LIMIT', 'quantity': 0.001, 'price': 30000.0, 'timeInForce': 'GTC'}
2025-09-08 20:16:12,789 - INFO - Order placed successfully: {'orderId': 123456789, 'status': 'NEW', ...}

