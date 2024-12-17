import talib

def calculate_indicators(df):
    """Add technical indicators to stock data."""
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df
    