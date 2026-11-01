class BankAccount:

    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        print("balance Add into the account of ",self.owner)
        self.balance+=amount

    def withdraw(self,amount):
        print("balance Removed From the account of ",self.owner)
        self.balance-=amount

    def checkBalance(self):
        return f"{self.owner} has Current Balance of  : {self.balance}"



account1 = BankAccount("Asfandyar", 10000)
account2 = BankAccount("Ali", 5000)


print(account1.checkBalance())  # 12000
print(account2.checkBalance())  # 5000

account1.deposit(2000)

account2.withdraw(500)

print(account1.checkBalance())  # 12000
print(account2.checkBalance())  # 5000