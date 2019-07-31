class Database:
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        return str(self.__dict__)

    def add(self, name, quantity):
        self.db.update({name: quantity})

    def update_flowers(self, name, q):
        self.db[name] += q

    def check_stock(self, name):
        rf = self.db.get(name)
        if rf < 5:
            print("you need to add more flowers of", name)
        else:
            print("you have {} flowers".format(rf))


class FlowerShop:
    def __init__(self, db):
        self.db = db

    def add_flower(self, name, quantity):
        self.db.add(name, quantity)

    def update_flower(self, name, quantity):
        self.db.update_flowers(name, quantity)
        self.db.check_stock(name)


db = Database()
fs = FlowerShop(db)
fs.add_flower('mogra', 55)
fs.add_flower('rose', 25)
fs.update_flower('mogra', -51)
print(fs.db)



