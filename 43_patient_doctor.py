class Database:
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        return str(self.__dict__)

    def add(self, name):
        self.db.update({name: []})

    def assign_doctor(self, doctor_name, patient_name):
        if len(self.db[doctor_name]) <= 4:
            self.db[doctor_name].append(patient_name)
        else:
            print("doctor is very busy. come tomorrow")


class Patient:
    def __init__(self, name):
        self.name = name


class Doctor:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def add_doctor(self, name):
        self.db.add(name)

    def add_patient(self, p):
        self.db.assign_doctor(self.name, p.name)


db = Database()
p0 = Patient("vp")
p1 = Patient("vp")
p2 = Patient("vp")
p3 = Patient("vp")
p4 = Patient("vp")
p5 = Patient("vp")
d = Doctor("kp", db)
d.add_doctor("kp")
d.add_patient(p0)
d.add_patient(p1)
d.add_patient(p2)
d.add_patient(p3)
d.add_patient(p4)
d.add_patient(p5)

print(db)
