import os
from path_status import check_path

def delete_file(ticker):
    if not check_path():
        print("Doesn't exist")
    else:
        os.remove('stock_tables/{}.csv'.format(ticker))

def replace_file(ticker):
    if not check_path():
        print("Doesn't exist")
    else:
        delete_file(ticker)
        


