class User:
    """
    Represents a user of the smart home system.
    """
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def authenticate(self, username, password):
        return self.username == username and self.password == password
