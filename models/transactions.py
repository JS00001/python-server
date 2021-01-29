from main import dbtransactions

class Transaction:
    def __init__(self, id="None", userid="None", subtotal="0", products=[]):
        self.id = id
        self.userid = userid
        self.subtotal = subtotal
        self.products = products

    def save(self):
        dbtransactions.insert_one({
            "transactionid": self.id,
            "userid": self.userid,
            "subtotal": self.subtotal,
            "products": self.products
        })
