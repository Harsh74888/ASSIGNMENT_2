# create a class bank_account with attribues owner and balace,implement method of deposit,withdraw 
# and check the balance,also implement a method to transfer money from one account to another
class Bank_Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return( f"Deposited Rs{amount}. New balance: Rs{self.balance}")
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew Rs{amount}. New balance: RS{self.balance}"
            else:
                return "Insufficient funds for withdrawal."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def check_balance(self):
        return f"Account balance for {self.owner}: RS{self.balance}"

    def transfer(self, recipient, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                return f"Transferred Rs{amount} to {recipient.owner}. New balance: Rs{self.balance}"
            else:
                return "Insufficient funds for the transfer."
        else:
            return "Invalid transfer amount. Please enter a positive amount."

account1 = Bank_Account("John", 1000.0)
account2 = Bank_Account("Alice", 500.0)

print(account1.deposit(200))
print(account1.check_balance())
print(account1.withdraw(300))
print(account1.check_balance())

print(account2.deposit(300))
print(account2.check_balance())
print(account2.transfer(account1, 200))
print(account1.check_balance())
print(account2.check_balance())
