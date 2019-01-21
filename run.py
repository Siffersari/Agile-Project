from user_models import UserModels, users


print("Welcome to the Application.\n Please choose an action:")
def choose_option():
    """Selecting an action to perform."""
    print("1. Register an account.")
    print("2. Login to your account.")
    print("3. Add a comment.")
    option = int(input("Please choose an action: "))
    if option == 1:
        # firstname, lastname, username, password, password2,
        firstname = str(input("Enter first name:"))
        lastname = str(input("Enter last name:"))
        username = str(input("Enter username:"))
        password = str(input("Enter password:"))
        password2 = str(input("Confirm password:"))
        user = UserModels(firstname, lastname, username, password, password2)
        register_user = user.signup()
        print(register_user, "Please login.", users)
        print("2. Login to your account.\n")
        option = int(input("Please choose an action: "))
        print(users)
        username = str(input("Enter username:"))
        password = str(input("Enter password:"))
        # user = UserModels()
        login_user = UserModels.login(username, password)
        print(login_user)
    elif option == 2:
        username = str(input("Enter username:"))
        password = str(input("Enter password:")) 
        # user = UserModels()
        login_user = UserModels.login(username, password)
        return login_user
    elif option == 3:
        user = UserModels(firstname=None, lastname=None, username=None, password=None, password2=None)
        comments = user.create_comment(username=None)
    else:
        print("Not a valid option. Please enter a valid option.")
choose_option()
