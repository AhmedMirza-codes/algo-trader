"""
Trading Configuration
"""

# Trading Symbols
TRADING_PAIRS = [
    "ETHUSDT",
    "XRPUSDT",
]

# Timeframes
TIMEFRAMES = [
    "15m",
    "30m",
]

# Historical candles to download
CANDLE_LIMIT = 200

# Risk Management
RISK_PER_TRADE = 0.01      # 1%
MAX_OPEN_TRADES = 3
MAX_DAILY_LOSS = 0.03      # 3%
LEVERAGE = 5

# Strategy Parameters
EMA_FAST = 20
EMA_SLOW = 50
ATR_PERIOD = 14
ADX_PERIOD = 14
RSI_PERIOD = 14

# ATR Multipliers
STOP_LOSS_ATR = 2
TAKE_PROFIT_ATR = 4