from user_models import UserModels


print("Welcome to the Application.\n Please choose an action:")
def choose_option():
    """Selecting an action to perform."""
    print("1. Register an account.")
    print("2. Login to your account.")
    option = input("Please choose an action: ")
    if isinstance(option, str):
        print("Please enter a valid action!")
    else: 
        if option == 1:
            UserModels.signup()
        elif option == 2:
            UserModels.login()
        else:
            print("Not a valid option. Please enter a valid option.")
choose_option()