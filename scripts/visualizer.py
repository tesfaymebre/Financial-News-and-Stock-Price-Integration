import matplotlib.pyplot as plt

def plot_with_sma(df, stock_name):
    """Plot stock close prices with SMA."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['SMA_20'], label='SMA 20', color='orange')
    plt.title(f"{stock_name}: Close Price and SMA")
    plt.legend()
    plt.show()

def plot_macd(df, stock_name):
    """Plot MACD and Signal Line."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='Signal Line', color='red')
    plt.title(f"{stock_name}: MACD and Signal Line")
    plt.legend()
    plt.show()