class Person:
    def __init__(self):
        # self.name = name
        # self.bornYear = bornYear
        # self.diedYear = diedYear
        # self.anp = anp
        self.dba = dict()
        self.dbn = dict()
        self.dbp = dict()

    def add_to_tree(self, anp, name, bornYear):
        if anp == 'a':
            self.dba[name] = bornYear
        elif anp == 'p':
            self.dbp[name] = bornYear
        else:
            self.dbn[name] = bornYear


p = Person()
p.add_to_tree('n', 'kp', 1998)
p.add_to_tree('p', 'jp', 2008)
p.add_to_tree('a', 'rp', 1950)
print("ancestors are : ", p.dba)
print("current generation are : ", p.dbn)
print("Predecessor are are : ", p.dbp)

