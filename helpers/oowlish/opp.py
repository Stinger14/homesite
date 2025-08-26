"""
Define classes to model a basic banking system with accounts and transactions, 
and implement methods to deposit, withdraw, and check balance.
"""

class Account:
    def __init__(self, account_number, init_balance):
        self.account_number = account_number
        self.balance = init_balance
        self.transaction = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction += 1

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction += 1

    def get_balance(self):
        return self.balance

acc = Account("12345", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())