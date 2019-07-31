WELCOME_MESSAGE = "\n" + "Welcome to HDFC, We care for you"
print(WELCOME_MESSAGE)


class Database:
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        return str(self.__dict__)

    def get(self, id):
        return self.db.get(id, None)

    def chk_balance(self, id):
        return self.db[id][1]

    def add(self, id, name, amount):
        return self.db.update({id: [name, amount]})

    def remove(self, id):
        return self.db.pop(id)

    def credit(self, id, cost):
        self.db[id][1] += cost
        return self.db[id][1]

    def debit(self, id, cost):
        self.db[id][1] -= cost
        return self.db[id][1]


class BankAccount:
    def __init__(self, db):
        self.db = db
        self.user_functions()

    def get_acc_detail(self, id):
        self.db.get(id)

    def user_functions(self):
        print("\nTo access any function below, enter the corresponding key")
        print("To:" + "\n"
              + "add new user,  press N" + "\n"
              + "Check Balance, press B" + "\n"
              + "Deposit cash:  press D" + "\n"
              + "Withdraw cash, press W" + "\n"
              + "Delete account press X" + "\n"
              + "Exit service,  press E" + "\n")

        functions = {
            'n': self.add_user,
            'b': self.check_balance,
            'd': self.deposit_cash,
            'w': self.withdraw_cash,
            'X': self.close_account
        }
        while True:
            answer = input("> ").lower()
            if answer in functions:
                id = int(input("enter your id: "))
                functions[answer](id)
            else:
                print("Thank you for using HDFC we value you. Have a good day.")
                return False

    def add_user(self, id):
        name = input("enter your name: ")
        amount = int(input("enter amount to credit your account: "))
        self.db.add(id, name, amount)

    def check_balance(self, id):
        print("Your account balance  is {balance}".format(balance=self.db.chk_balance(id)))

    def withdraw_cash(self, id):
        amount = float(input("Please enter amount to withdraw:" + "\n"))
        self.db.debit(id, amount)
        print("Your new account balance is ", end='')
        print(self.db.chk_balance(id))

    def deposit_cash(self, id):
        amount = float(input("Please enter amount to Deposit :" + "\n"))
        self.db.credit(id, amount)
        print("Your new account balance is ", end='')
        print(self.db.chk_balance(id))

    def close_account(self, id):
        print("{}, your account is being deleted".format(id))
        self.db.close(id)
        print("Your account has been successfully deleted, Goodbye.")


d = Database()
b = BankAccount(d)
