import pandas as pd
import os

def load_stock_data(file_path):
    """Load a single stock's data."""
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return df.dropna()

def load_all_data(folder_path):
    """Load all stock data from a folder."""
    data = {}
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            stock_name = file.split(".")[0]
            data[stock_name] = load_stock_data(os.path.join(folder_path, file))
    return data
