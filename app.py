from exchange.binance_client import BinanceClient
from data.market_data import MarketData


class TradingBot:
    def __init__(self):
        self.client = BinanceClient()

    def run(self):
        print("=" * 60)
        print("Crypto Algo Trading Bot")
        print("=" * 60)

        klines = self.client.get_klines(
            symbol="ETHUSDT",
            interval="15m",
            limit=20
        )

        df = MarketData.format_klines(klines)

        print(df)