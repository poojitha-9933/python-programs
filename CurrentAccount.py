class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        overdraft_limit = 5000

        if self.balance - amount >= -overdraft_limit:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Overdraft limit exceeded")

account = CurrentAccount("Poojitha", 3000)

account.display()
account.withdraw(7000)   
account.display()

account.withdraw(2000)  
account.display()
