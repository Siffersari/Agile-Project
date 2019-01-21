users, comments = [], []


class UserModels(object):
    """
    This class UserModels contains
    methods for user instances
    """

    def __init__(self, firstname, lastname, username, password, password2, role="user"):

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.password2 = password2
        self.role = role
        self.db = users

    def signup(self):
        """
        This method register user details
        that have been provided
        """

        pass

    @staticmethod
    def login(username, password):
        """
        This method checks if a user is in the users list
        """
        response = None
        for user in users:
            if user['username'] == username:
                if user['password'] == password:
                    response = "Logged in successfully"
                response = "wrong password"
            response = "wrong credentials. Signup if not already registered"
        return response

    def create_comment(self):
        pass

    def edit_comment(self):
        pass
