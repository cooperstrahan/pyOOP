class bankAccount:
    def __init__(self,balance=0, interest_rate=0.01):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if self.balance - amount < 0:
            print("Insufficient funds charging a $5 Fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("account balance is", self.balance)
        return(self)
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self

debit1 = bankAccount(200, 0.01)
debit2 = bankAccount()

debit1.deposit(220).deposit(300).deposit(500).withdraw(150).yield_interest().display_account_info()
debit2.deposit(180).deposit(400).withdraw(50).withdraw(60).withdraw(20).withdraw(20).yield_interest().display_account_info()