from datetime import datetime

users, comments = [], []


class UserModels(object):
    """
    This class UserModels contains
    methods for user instances
    """

    def __init__(self, firstname, lastname, username, password, password2, role="user"):
        """Class constructor."""

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

        if not (self.password == self.password2):
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
        user_found = [
            person for person in users if person["username"] == username]

        if not user_found:
            return "wrong credentials. Signup if not already registered"

        if not user_found[0]["password"] == password:
            return "wrong password"

        UserModels.logged_in_at = datetime.now()

        return "Logged in successfully"

        return "The comment with id {} has been deleted successfully".format(comment_id)

    def create_comment(self, username):
<<<<<<< HEAD
       """Create a comment."""
       comment_id = len(self.comments) + 1
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
=======
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
>>>>>>> [Finishes #163362204]  Fix login

    def edit_comment(self):
        pass


class ModeratorUserModels(UserModels):
    """
    The moderator user model that defines the moderator user
    """

    def __init__(self):
        super.__init__(UserModels)
        self.role = "moderator"

    @staticmethod
    def edit_comment(comment_id, comment_title, comment_body):
        for comment in comments:
            if comment['id'] == comment_id:
                comment['title'] = comment_title
                comment['body'] = comment_body

        return comment

    def delete_comment(self, comment_id):
        """ 
        Deletes a comment given an id 
        """

        comment = [(index, item) for (index, item) in enumerate(
            comments) if item["id"] == comment_id]

        if not comment:
            return "No comment with id {} exists".format(comment_id)

        comments.remove(comments[comment[0][0]])

        return "The comment with id {} has been deleted successfully".format(comment_id)
