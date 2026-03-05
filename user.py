class User:
    def __init__(self, username, is_admin=False):
        if not username:
            raise ValueError("username không được rỗng")
        self.username = username
        self.is_admin = is_admin

    def display_info(self):
        print(f"User: {self.username} - Admin: {self.is_admin}")

    