## Challenge of the day ## 
# Implement an abstract `BankAccount` class.
# This class should define a blueprint for different types of accounts
# by using abstract methods that must be implemented by subclasses.
# Create `SavingsAccount` and `CheckingAccount` as concrete subclasses.

#[{'input': "account = BankAccount('John Doe', 1000)", 'output': "TypeError: Can't instantiate abstract class BankAccount with abstract methods deposit, withdraw"}, {'input': "savings = SavingsAccount('Alice', 2000, 0.05)\nsavings.deposit(500)\nsavings.get_balance()", 'output': '2500'}, {'input': "checking = CheckingAccount('Bob', 1000, 500)\nchecking.withdraw(1200)\nchecking.get_balance()", 'output': '-200'}]## Challenge of the day ## 
# Implement an abstract `BankAccount` class.
# This class should define a blueprint for different types of accounts
# by using abstract methods that must be implemented by subclasses.
# Create `SavingsAccount` and `CheckingAccount` as concrete subclasses.

#[{'input': "account = BankAccount('John Doe', 1000)", 'output': "TypeError: Can't instantiate abstract class BankAccount with abstract methods deposit, withdraw"}, {'input': "savings = SavingsAccount('Alice', 2000, 0.05)\nsavings.deposit(500)\nsavings.get_balance()", 'output': '2500'}, {'input': "checking = CheckingAccount('Bob', 1000, 500)\nchecking.withdraw(1200)\nchecking.get_balance()", 'output': '-200'}]