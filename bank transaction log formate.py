class BankAccount:
    def __init__(self):
        self.balance=0
        print("Deposit and withdrawl withdrawl")
    def deposit(self):
        money=float(input("Enter amount your  deposit"))
        self.balance +=money
        print("amount deposited",money)
    def withdrawl(self):
         money=float(input("Enter amount yor withdrwal"))
         if self.balance >=money:
            self.balance -=money
            print("Amount withdrawl",money)
    def display(self):
        print("Your balance is ",self.balance)
v=BankAccount()
v.deposit()
v.withdrawl()
v.display()
