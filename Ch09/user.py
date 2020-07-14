from priviledges import Priviledges

class User():
    """Class that describes a user."""

    def __init__(self, first_name, last_name):
        """Initialize the information stored in a user account."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.priviledges = Priviledges('user')

    def describe_user(self):
        """Prints a summary of user information."""
        print("Name: " + self.last_name.title() + ", " + self.first_name.title())
        print("Login attempts: " + str(self.login_attempts))

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Increments the number of login attempts for the user account."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to zero."""
        self.login_attempts = 0

# me = User('remi', 'coussement')
# me.describe_user()
# me.greet_user()

# for ctr in range(0,9):
#     me.increment_login_attempts()

# me.describe_user()
# me.reset_login_attempts()
# me.describe_user()