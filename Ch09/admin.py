from user import User
from priviledges import Priviledges

class Admin(User):
    """Class describing special type of user: Admin"""

    def __init__(self, first_name, last_name):
        """Initialize the Admin class object."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.priviledges = Priviledges('admin')