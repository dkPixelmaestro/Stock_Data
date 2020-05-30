from Stock import Stock
from paths_code import *  

def menu():
    print("\n|***** Welcome to StockTrac *****|\n")
    print("What would you like to do today?\n1.) Create directory for data\n2.) Get data for stock\n3.) Check path for saving data\n4.) Quit App\n")

menu()
option_choice = input("Enter an menu option (1-4): ")
while(option_choice != '4'):
    if option_choice == '1':
        users_path = input("Enter the full path of where you want to create your new directory: ")
        create_dir(users_path)
        menu()
        option_choice = input("Enter an menu option (1-4): ")
    elif option_choice == '2':
        # gather info
        ticker = input("Ticker Symbol: ")
        start_date = input("Start Date (Format: YYYY-MM-DD): ")
        end_date = input("End Date (Format: YYYY-MM-DD): ")
        file_path = input("Input where you would like to save the csv file in (Enter the enitre path starting with root directory):  ")
        # initialize Stock object
        stock = Stock(ticker, start_date, end_date)
        stock.obtain_data(file_path)
        # confirm file created and saved
        print("File created and saved in provided directory")
        menu()
        option_choice = input("Enter an menu option (1-4): ")
    elif option_choice == '3':
        path_to_check = input("Please enter the full path you want ot check (From root to directory of choice): ")
        double_check_file_path(path_to_check)
        menu()
        option_choice = input("Enter an menu option (1-4): ")

print("\n|***** Program Terminated *****|\n")

