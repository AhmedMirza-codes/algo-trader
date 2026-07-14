from exchange.binance_client import BinanceClient
from data.market_data import MarketData


def main():

    client = BinanceClient()

    print("=" * 60)
    print("Connected to Binance Futures Testnet")
    print("=" * 60)

    # Download candles
    klines = client.get_klines(
        symbol="ETHUSDT",
        interval="15m",
        limit=20,
    )

    # Convert to DataFrame
    df = MarketData.format_klines(klines)

    print(df)


if __name__ == "__main__":
    main()