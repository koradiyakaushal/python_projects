class Database:
    def __init__(self):
        self.db = dict()
        self.db1 = dict()

    def __repr__(self):
        return str(self.__dict__)

    def add(self, name):
        self.db1.update({name: []})

    def add_ingredients(self, r, l):
        self.db1[r].append(l)

    def add_categories(self):
        l = ['veg', 'punjabi', 'gujarati', 'soup', 'desert', 'american', 'mexican', 'italian']
        for i in l:
            self.db.update({i: []})

    def add_to_cat(self, cat, recipe):
        self.db[cat].append(recipe)


class Recipe:
    def __init__(self, name, db):
        self.name = name
        self.db = db
        self.add_to_db()

    def add_to_db(self):
        self.db.add(self.name)

    def add_ingredients(self, l):
        self.db.add_ingredients(self.name, l)


class RecipeManager:
    def __init__(self, db):
        self.db = db
        self.add_categories()

    def add_categories(self):
        self.db.add_categories()

    def add_to_categories_list(self, cat, recipe):
        self.db.add_to_cat(cat, recipe)


db = Database()
db1 = Database()
r = Recipe("mava", db)
r.add_ingredients(['sopari', 'chuno', 'tamakoo'])
rc = RecipeManager(db)
rc.add_to_categories_list('veg', r.name)
rc.add_to_categories_list('veg', r.name)
rc.add_to_categories_list('veg', r.name)
print(db)
# print(db1)
