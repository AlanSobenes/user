class User:
    
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname
        self.account_balance = 0
    
    def make_deposit(self, money):
        self.account_balance += money

    def make_withdrawal(self, money):
        self.account_balance -= money

    def display_user_balance(self):
        print(self.account_balance)

    def make_a_transfer(self, reciever, amount):
        reciever = reciever
        self.account_balance -= amount
        reciever.account_balance += amount
        print(self.fname, self.account_balance) 
        print(reciever.fname, reciever.account_balance)   




alan = User( 'Alan', 'Sobenes')
joe = User('Joe', 'Dirt')
Mike = User('Mike', 'Tyson')





alan.make_deposit(1000)  
alan.make_deposit(5000)  
alan.make_deposit(2500)
alan.make_withdrawal(1500)
print(alan.fname, alan.account_balance)

joe.make_deposit(300)
joe.make_deposit(200)
joe.make_withdrawal(50)
joe.make_withdrawal(10)
print(joe.fname, joe.account_balance)

Mike.make_deposit(50)
Mike.make_withdrawal(15)
Mike.make_withdrawal(20)
Mike.make_withdrawal(20)
print(Mike.fname, Mike.account_balance)

alan.make_a_transfer(joe, 700)