# polymorphism example in python 

class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name 
        self.balance = balance  
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposite amount should be greate than 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdraw amount should be greater than 0 and less than or equal to balance")
        
    def __str__(self):
        return f"Account Holder Name: {self.account_holder_name}, Balance: {self.balance}"

class SavingAccount(BankAccount):
    def __init__(self, account_holder_name, balance, interest_rate):
        super().__init__(account_holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100

    def __str__(self):
        return f"Account Holder Name: {self.account_holder_name}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"
    
def main():
    account = SavingAccount("John", 1000, 5)
    print(account)
    account.deposite(100)
    print(account)
    account.withdraw(200)
    print(account)
    account.withdraw(1000)
    print(account)
    account.deposite(-100)
    account.withdraw(-100)
    account.balance = 500
    print(account)
    account.account_holder_name = "Doe"
    print(account)
    account.add_interest()
    print(account)
    
