import os


def provide_option():
    print("Consider from the following options:\n\n1.) Create New Directory In Provided Path\n2.) Provide New Path\n")
    users_choice = input("Enter the number of the option you want to pick: ")
    return users_choice

# evaluate choice of user
def eval_choice(users_choice):
    if users_choice == '1':
        new_path = input("Enter the path where you want to store directory: ")
        create_dir(new_path)
    elif users_choice == '2':
        new_path = input("Enter a new path: ")
        check_users_path(new_path)
    else:
        print("Invalid option")
        eval_choice(provide_option())

# creates new directory
def create_dir(file_path):
    dir_name = input("Provide a directory name that you want to store the data in: ")
    try:
        if not os.path.exists(f'{file_path}/{dir_name}'):
            # creates directory on Desktop
            os.mkdir(f'{file_path}/{dir_name}')
            print(f'{dir_name} has been created. Full path: {file_path}/{dir_name}') 
    except FileExistsError:
        print(f'{dir_name} already exists on. Current path: {file_path}/{dir_name}')

    return f'{file_path}/{dir_name}'

# checks the path provided by user
def check_users_path(users_path):
    if os.path.exists(f'{users_path}'):
        print("Provided path available")
        eval_choice(provide_option())
    else:
        print("Provided file path unavailable")
        eval_choice(provide_option())

        
        