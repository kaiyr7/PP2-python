class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Account owner is: {self.owner}\nAccount balance: {self.balance}"
    def Deposit(self, cnt):
        self.balance+=cnt
        return cnt
    def Withdraw(self, cnt):
        if(cnt<=self.balance):
            self.balance-=cnt
            return cnt
acc=Account("Kaiyrzhan",36600)
print(acc)
print("Deposit: ",acc.Deposit(int(input())))
print("Withdraw: ",acc.Withdraw(int(input())))
print("Account balance: ", acc.balance)