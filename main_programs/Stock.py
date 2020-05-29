import pandas as pd   
import yfinance as yf
import csv
from path_status import check_path, check_data_path

class Stock:
    def __init__(self, ticker, start_period, end_period):
        self.ticker = ticker
        self.start_period = start_period
        self.end_period = end_period

    def get_stock_data(self):
        # gather the data and save into dataframe
        stock_data = yf.download(self.ticker, self.start_period, self.end_period)
        df = pd.DataFrame(data=stock_data)
        return df

    def create_directory(self):
        pass

    def input_to_csv(self):
        stock_df = self.get_stock_data()
        """
        Write to a csv file or xlsx file if the user chooses

        Send it to a directory created by user or an existing directory

        """

    def modify_file(self):
        """
        Allow user to either:
        - replace file for stock of choice
        - delete file for stock of choice

        """




    
    



    
