from binance.client import Client
from config.settings import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
    BINANCE_TESTNET,
)


class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key=BINANCE_API_KEY,
            api_secret=BINANCE_API_SECRET,
        )

        if BINANCE_TESTNET:
            # Binance Futures Testnet
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_server_time(self):
        return self.client.get_server_time()

    def get_futures_balance(self):
        return self.client.futures_account_balance()

    def get_klines(self, symbol, interval="15m", limit=10):
        return self.client.futures_klines(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )