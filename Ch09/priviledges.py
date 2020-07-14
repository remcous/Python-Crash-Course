class Priviledges:
    """Class that defines user priviledges."""

    def __init__(self, user_type='user'):
        self.user_type = user_type
        if self.user_type == 'admin':
            self.priviledges = ['can add post', 'can delete post',
                        'can ban user']
        elif self.user_type == 'user':
            self.priviledges = ['can add post']

    def show_priviledges(self):
        """Print a list of Admin priviledges."""
        print(self.user_type.title() + " priviledges:")
        for priviledge in self.priviledges:
            print("- " + priviledge)