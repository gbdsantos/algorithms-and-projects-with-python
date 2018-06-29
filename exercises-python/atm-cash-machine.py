class Account():

    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):

        self.dep_amt = dep_amt
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance.".format(self.dep_amt))

    def withdraw(self, wd_amt):

        self.wd.amt = wd_amt

        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdraw {wd_amt} to the balance.".format(self.wd_amt))
        else:
            print("Sorry non enought funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

a = Account("Guilherme", 1000)
a.owner
a.balance
a.deposit(100)
print(a)
a.withdraw(1100)
print(a)
a.withdraw(1)
print(a)

