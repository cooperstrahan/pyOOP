class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = bankAccount(interest_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name,"has an account balance of",self.account.display_account_info())
        
    def transfer_money(self, other_user, amount):
        if(self.account.balance - amount < 0):
            print("Insufficient Funds")
            return self
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            return self

class bankAccount:
    def __init__(self,balance, interest_rate):
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
        return(self.balance)
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self

Cooper = User('Cooper','cooperstrahan@gmail.com')
Tom = User('Tom','tom@yahoo.com')
Jeff = User('Jeff', 'jeff@hotmail.com')

Cooper.make_deposit(100).make_deposit(50).make_deposit(83).make_withdrawal(35).display_user_balance()
Tom.make_deposit(1000).make_deposit(500).make_withdrawal(400).make_withdrawal(10).display_user_balance()
Jeff.make_deposit(2000).make_withdrawal(400).make_withdrawal(400).make_withdrawal(400).display_user_balance()
Cooper.transfer_money(other_user=Jeff, amount=100).display_user_balance()
Jeff.display_user_balance()