class BankAccount:

    def __init__(self, int_rate=.075, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
            self.balance+=-5
            return self
        self.balance-=amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance+={self.balance}*{self.int_rate}
        return self


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts=[]
        self.accounts.append(BankAccount(int_rate=.02,balance=1000))
        self.accounts.append(BankAccount(int_rate=.03,balance=600))
    
    def deposit(self, amount,accounts):
        self.accounts[accounts].deposit(amount)
        return self
    
    def withdraw(self, amount, accounts):
        self.accounts[accounts].withdraw(amount)
        return self
    
    def display_account_info(self):
        print(f"User: {self.name}, Checking Balance: {self.accounts[0].balance}, Savings Account:{self.accounts[1].balance}")
        return self
    
Adrien=User('Adrien','adrien@gmail.com')

Adrien.deposit(200,0).deposit(200,0).withdraw(600,1).display_account_info()

