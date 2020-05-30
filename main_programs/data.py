import pandas as pd 
import pandas_datareader.data as pdr



def get_data(ticker, start, end):
    df = pdr.get_data_yahoo(ticker, start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df.to_csv('{}.csv'.format(ticker))


# get_data('goog', '2020-01-01', '2020-02-01')