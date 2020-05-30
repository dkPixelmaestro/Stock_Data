import os
from pandas_datareader import data as pdr
from paths_code import create_dir # separate file
import pandas as pd   
import yfinance as yf

class Stock:
    def __init__(self, ticker, start_period, end_period):
        self.ticker = ticker
        self.start_period = start_period
        self.end_period = end_period

    def create_directory(self, users_path):
        data_dir = create_dir(users_path)
        return data_dir

    def input_to_csv(self, data, file_path):
        data.to_csv(f'{file_path}/{self.ticker}.csv')

    def obtain_data(self, file_path):
        df = pdr.get_data_yahoo(self.ticker, self.start_period, self.end_period)
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        self.input_to_csv(df, file_path)
              
        
