from main import dbapikeys

class Apikey:
    def __init__(self, key="None", permissions=[]):
        self.permissions = permissions
        self.key = key

    def save(self):
        dbapikeys.insert_one({
            "key": self.key,
            "permissions": self.permissions
        })

    def pull(self):
        return {
            "permissions": self.permissions,
            "key": self.key
        }
