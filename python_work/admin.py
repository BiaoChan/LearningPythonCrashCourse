from user import UserProfile

class Admin(UserProfile):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin's privileges:")
        for privilege in self.privileges:
            print(privilege)
