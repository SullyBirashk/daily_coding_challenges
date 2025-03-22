rt pytest

from main import BankAccountdef test_initial_balance():
account = BankAccount('John Doe', 1000)
assert account.get_balance() == 1000
