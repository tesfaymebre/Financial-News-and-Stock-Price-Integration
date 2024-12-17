import pynance as pn

def calculate_daily_returns(df):
    """Calculate daily returns."""
    df['Daily_Returns'] = df['Close'].pct_change()
    return df

def calculate_volatility(df):
    """Calculate volatility (standard deviation of daily returns)."""
    daily_returns = df['Close'].pct_change()
    return daily_returns.std()