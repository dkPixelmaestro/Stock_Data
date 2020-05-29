import pandas as pd   
import yfinance as yf
import csv
import os
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

    def create_directory(self, users_path):
        directory_name = input("Enter the name of directory: ")
        current_path = os.path.abspath('directory_name')
        try:
            # if not os.path.exists(directory_name):
            #     os.mkdir(directory_name)
            if os.path.exists(possible_path) == False:
                os.mkdir(f'{users_path}/{directory_name}')
                return os.path.abspath(directory_name)
        except:
            return os.path.abspath(directory_name)

    def provide_path(self, users_path):
        pass

    def input_to_csv(self, file_path):
        stock_df = self.get_stock_data()
        stock_df.to_csv(f'{file_path}/{self.ticker}.csv')

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
        pass




    
    



    
