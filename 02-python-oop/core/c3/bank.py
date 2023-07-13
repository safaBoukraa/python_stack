#  Create a BankAccount class 
class BankAccount:
    accounts=[]
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)
# deposit(self,amount)
    def deposit(self, amount):
        self.balance += amount
        return self
# withdraw(self,amount)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
        return self 
     
    def display_account_info(self):
        print("Balance: $"+str(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.int_rate
        return self
     
@classmethod
def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# Example usage:
account1 = BankAccount(0.01, 100) 
account1.deposit(50).deposit(100).deposit(60).withdraw(500).yield_interest().display_account_info() 
account2 = BankAccount(0.03, 50) 
account2.deposit(70).deposit(300).withdraw(50).withdraw(70).withdraw(20).withdraw(250).yield_interest().display_account_info() 
account3=BankAccount(0.03,300) 
BankAccount.print_all_accounts()            