from datetime import datetime

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
        self.logged_in_at = None
        self.role = role
        self.db = users
        self.comments = comments

    def signup(self):
        """
        This method register user details
        that have been provided
        """
        required = [self.firstname, self.lastname,
                self.username, self.password, self.password2]

        missing = [item for item in required if not item]

        if missing:
            return "Please make sure that all fields are not empty"

        if not self.password == self.password2:
            return "Please make sure that both passwords match"

        data = {
            "id": len(users) + 1,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

        users.append(data)

        return "You have been successfully registered. Your user id is {}".format(data["id"])

    @staticmethod
    def login(username, password):
        """
        This method checks if a user is in the users list
        """
        response = None
        for user in users:
            if user['username'] == username:
                if user['password'] == password:
                    UserModels.logged_in_at = datetime.now()
                    response = "Logged in successfully"
                response = "wrong password"
            response = "wrong credentials. Signup if not already registered"
        return response

    def create_comment(self, username):
       """Create a comment."""
       comment_id = len(self.comments)
       title = input("Enter comment title:  ")
       body = input("Enter comment body:    ")
       username = [user for user in users if user["username"] == username]
       created_at = datetime.now()
       comment = {
           "id": comment_id,
           "title": title,
           "body": body,
           "posted_by": username,
           "created_at": created_at
       }
       self.comments.append(comment)
       print("Comment created")
       print(comment)
       resp = str(input("Would you like to edit the comment(yes or no):"))

       if resp == "yes":
           UserModels.edit_comment(self)
       else:
           print("Sad to see you go!!")
        

    
    
        
       

    def edit_comment(self):
        pass
