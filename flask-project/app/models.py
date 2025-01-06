class User:
    def __init__(self, username, password, name, email, mobile):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.mobile = mobile

    def to_dict(self):
        return {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile
        }