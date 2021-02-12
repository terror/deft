from binance.client import Client as BinanceClient
from dotenv import load_dotenv
from config import get_config
import os

load_dotenv()


class Client:
    def __init__(self):
        self.client = BinanceClient(
            os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY")
        )
        self.config = get_config()

    # buy crypto at market price
    def buy(self, symbol: str, quantity: float):
        self.client.order_market_buy(symbol=symbol, quantity=quantity)

    # sell crypto at limit price
    def sell(self, symbol: str, quantity: float, price: str):
        self.client.order.limit_sell(
            symbol=symbol, quantity=quantity, price=price)
