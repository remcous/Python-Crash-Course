from admin import Admin
from user import User

admin = Admin("Remi", "Coussement")
admin.greet_user()
admin.priviledges.show_priviledges()

print()

user = User("Martin", "Figel")
user.greet_user()
user.priviledges.show_priviledges()