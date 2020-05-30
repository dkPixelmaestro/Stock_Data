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
        ticker = 

