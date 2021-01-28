from main import dbusers

class User:
    def __init__(self, admin=False, username="none", userid="none", email="none", registered="none", avatar="none"):
        self.registered = registered
        self.username = username
        self.transactions = []
        self.userid = userid
        self.admin = admin
        self.avatar = avatar
        self.email = email

    def save(self):
        dbusers.insert_one({
            "price": self.price[0],
            "name": self.name[0],
            "category": self.category[0],
            "description": self.description[0]
        })
