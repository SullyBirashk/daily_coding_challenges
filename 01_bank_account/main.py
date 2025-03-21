## Challenge of the day ## 
# Create a Python class called `BankAccount`.
# It should allow users to deposit, withdraw, and check their balance.
# Ensure that withdrawals do not exceed the available balance.

#[{'input': "account = BankAccount('John Doe', 1000)\naccount.deposit(500)\naccount.withdraw(300)\naccount.get_balance()", 'output': '1200'}, {'input': 'account.withdraw(1500)', 'output': 'Insufficient funds. Current balance: 1200'}]