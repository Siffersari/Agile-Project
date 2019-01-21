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

    def login(self):
        pass

    def create_comment(self):
        pass

    def edit_comment(self):
        pass
