class User:
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, money):
        if money > self.balance:
            print("ValueError('not enough money to withdraw.')")
            pass
        self.balance -= money
        return f"{self.name} has {self.balance}."

    def check(self, other, money):
        if not other.checking_account:
            print("ValueError('not have permission for checking account.')")
            pass
        if money > other.balance:
            print("ValueError('not have enough money.')")
            pass
        self.balance += money
        other.balance -= money
        return f"{self.name} has {self.balance} and {other.name} has {other.balance}."

    def add_cash(self, money):
        self.balance += money
        return f"{self.name} has {self.balance}."

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

print(Jeff.withdraw(2))
print(Joe.check(Jeff, 50))
Joe.checking_account = True
print(Jeff.check(Joe, 80))
print(Joe.check(Jeff, 100))
print(Jeff.add_cash(20))
