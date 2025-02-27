# inheritance example in python 

class BankAccount:
    def __init__(self, account_holder_name, balance):
        self._account_holder_name = account_holder_name
        self._balance = balance

    def deposite(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposite amount should be greate than 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Withdraw amount should be greater than 0 and less than or equal to balance")

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self._account_holder_name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

class SavingAccount(BankAccount):
    def __init__(self, account_holder_name, balance, interest_rate):
        super().__init__(account_holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100
    
def main():
    account = SavingAccount("John", 1000, 5)
    print(account.account_holder_name)
    print(account.balance)
    account.deposite(100)
    print(account.balance)
    account.withdraw(200)
    print(account.balance)
    account.withdraw(1000) 
    print(account.balance)
    account.deposite(-100)
    account.withdraw(-100)
    account.balance = 500
    print(account.balance)
    account.account_holder_name = "Doe"
    print(account.account_holder_name)
    account.add_interest()
    print(account.balance)



if __name__ == '__main__':
    main()