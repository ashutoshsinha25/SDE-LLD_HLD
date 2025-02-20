# encapsulation example in python 

class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.__account_holder_name = account_holder_name
        self.__balance = balance 

    def get_account_holder_name(self):
        return self.__account_holder_name
    
    def set_account_holder_name(self, account_holder_name):
        self.__account_holder_name = account_holder_name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance 

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("Deposite amount should be greate than 0")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount 
        else:
            print("Withdraw amount should be greater than 0 and less than or equal to balance")

    
def main():
    account = BankAccount("John", 1000)
    print(account.get_account_holder_name())
    print(account.get_balance())
    account.deposite(100)
    print(account.get_balance())
    account.withdraw(200)
    print(account.get_balance())
    account.withdraw(1000)
    print(account.get_balance())
    account.deposite(-100)
    account.withdraw(-100)
    account.set_balance(500)
    print(account.get_balance())
    account.set_account_holder_name("Doe")
    print(account.get_account_holder_name())


if __name__ == '__main__':
    main()
            