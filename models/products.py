from main import dbproducts

class Product:
    def __init__(self, name="None", category="None", description="None", price=0):
        self.price = price,
        self.name = name,
        self.category = category,
        self.description = description,

    def save(self):
        dbproducts.insert_one({
            "price": self.price[0],
            "name": self.name[0],
            "category": self.category[0],
            "description": self.description[0]
        })
