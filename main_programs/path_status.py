import os

def check_path():
    if os.path.exists("main_programs/stock_tables"):
        return True
    else:
        return False

def check_data_path(ticker):
    if os.path.exists("stock_tables/{}.csv".format(ticker)):
        return True
    else:
        return False
