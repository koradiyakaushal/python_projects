class Database:
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        return str(self.__dict__)

    def get(self, id):
        return self.db.get(id, None)

    def add(self, id, position, salary, work_time):
        if work_time != 24:
            salary = work_time * int(salary)

        d1 = {id: [position, str(salary), work_time]}
        self.db.update(d1)
        # return {self.id: [self.position, self.final_salary, self.work_time]}

    def fire(self, id):
        self.db.pop(id)

    def promote(self, id, salary):
        d2 = self.db.pop(id)
        d2[1] = salary
        self.db.update({id: d2})


class Company:
    def __init__(self, id, Name, Location, work_time, db):
        self.id = id
        self.Name = Name
        self.Location = Location
        self.work_time = work_time
        self.db = db

    def add_employee(self, id, position, salary, work_time):
        self.db.add(id, position, salary, work_time)

    def fire(self, id):
        self.db.fire(id)

    def promote(self, id, salary):
        self.db.promote(id, salary)

    def get(self, id):
        return self.db.get(id)


def main():
    db = Database()
    e1 = Company(1, "AppScrip", "bangalore", 24, db)
    # print(e1.final_salary)
    db = {}
    e1.add_employee(1, "senior dev", '8000', 10)
    e1.add_employee(2, "trainee ", '25000', 24)
    e1.add_employee(3, "freelancer", '5000', 5)
    print(e1.db)
    e1.fire(3)
    e1.promote(2, '50000')
    print(e1.db)


if __name__ == "__main__":
    main()
