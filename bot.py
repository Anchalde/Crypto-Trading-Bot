import logging
import sys
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.exceptions import BinanceAPIException, BinanceOrderException

# Configure logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1'
        logging.info("Initialized Binance Client with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Place an order on Binance Futures Testnet.
        :param symbol: Trading pair symbol, e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param order_type: 'MARKET', 'LIMIT', or 'STOP_LIMIT'
        :param quantity: Quantity of the asset to trade
        :param price: Price for LIMIT or STOP_LIMIT orders
        :param stop_price: Stop price for STOP_LIMIT orders
        :return: Order response dict or None if error
        """
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
                'timeInForce': 'GTC' if order_type == 'LIMIT' or order_type == 'STOP_LIMIT' else None,
            }
            if order_type == 'LIMIT':
                if price is None:
                    raise ValueError("Price must be specified for LIMIT orders")
                params['price'] = price
            if order_type == 'STOP_LIMIT':
                if price is None or stop_price is None:
                    raise ValueError("Price and stop_price must be specified for STOP_LIMIT orders")
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = 'GTC'

            # Remove None values from params
            params = {k: v for k, v in params.items() if v is not None}

            logging.info("Placing order: %s", params)
            order = self.client.futures_create_order(**params)
            logging.info("Order placed successfully: %s", order)
            return order
        except BinanceAPIException as e:
            logging.error("Binance API Exception: %s", e)
            print(f"API Error: {e}")
        except BinanceOrderException as e:
            logging.error("Binance Order Exception: %s", e)
            print(f"Order Error: {e}")
        except Exception as e:
            logging.error("Unexpected error: %s", e)
            print(f"Error: {e}")
        return None

def validate_input(prompt, valid_options=None, is_float=False, is_positive=False):
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input.upper() not in valid_options:
            print(f"Invalid input. Choose from {valid_options}")
            continue
        if is_float:
            try:
                val = float(user_input)
                if is_positive and val <= 0:
                    print("Value must be positive.")
                    continue
                return val
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            return user_input.upper()

def main():
    print("Welcome to Binance Futures Testnet Trading Bot")

    # User inputs API keys
    api_key = input("Enter your Binance Testnet API Key: ").strip()
    api_secret = input("Enter your Binance Testnet API Secret: ").strip()

    bot = BasicBot(api_key, api_secret, testnet=True)

    while True:
        print("\nPlace a new order or type 'exit' to quit.")
        symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
        if symbol.lower() == 'exit':
            print("Exiting...")
            break

        side = validate_input("Order side (BUY/SELL): ", valid_options=['BUY', 'SELL'])
        order_type = validate_input("Order type (MARKET/LIMIT/STOP_LIMIT): ", valid_options=['MARKET', 'LIMIT', 'STOP_LIMIT'])
        quantity = validate_input("Quantity: ", is_float=True, is_positive=True)

        price = None
        stop_price = None
        if order_type == 'LIMIT':
            price = validate_input("Limit price: ", is_float=True, is_positive=True)
        elif order_type == 'STOP_LIMIT':
            stop_price = validate_input("Stop price: ", is_float=True, is_positive=True)
            price = validate_input("Limit price: ", is_float=True, is_positive=True)

        order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
        if order:
            print("Order placed successfully!")
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")
            print(f"Executed Quantity: {order['executedQty']}")
        else:
            print("Failed to place order. Check logs for details.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)