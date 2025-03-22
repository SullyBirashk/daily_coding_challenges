class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be numeric")
        if amount < 0:
            raise ValueError("Deposit amount must be a positive number")
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be numeric")
        if amount < 0:
            raise ValueError("Withdrawal amount must be a positive number")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Current balance: {self.balance}")
        self.balance -= amount