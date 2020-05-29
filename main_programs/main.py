import os
import pandas as pd   
import yfinance as yf
import csv
from path_status import check_path, check_data_path

def ask_user():
    # request beginning and ending date, as well as ticker
    start_date = input("Enter the date you want the data to start from (Format: YYYY-MM-DD): ")
    end_date = input("Enter the date you want the data to end (Format: YYYY-MM-DD): ")
    stock_ticker = input("Enter the stock ticker symbol: ").upper()
    return stock_ticker, start_date, end_date

def get_data(ticker, start, end):
    # gather the data and save into dataframe
    stock_data = yf.download(ticker, start, end)
    df = pd.DataFrame(data=stock_data)

    # check if folder exists
    try:
        if check_path():
            os.mkdir('stock_tables') 
    except:
        print("Access available...")

    # check if stock file exists
    try:
        if not os.path.exists('stock_tables/{}.csv'.format(ticker)):
            df.to_csv('stock_tables/{}.csv'.format(ticker))
    except:
        print("Data for {} already exists".format(ticker))

    return df

print("****** Welcome to EquityTrac ******")
ask_question = input("Would you like to look up a stock (y/n)? ")
while(ask_question == 'y'):
    stock, start_date, end_date = ask_user()
    get_data(stock, start_date, end_date)
    ask_question = input("Would you like to look another stock (y/n)? ")



