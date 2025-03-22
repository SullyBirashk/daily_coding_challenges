import pytest
from main import BankAccount
def test_initial_balance():
    account = BankAccount('John Doe', 1000)
    assert account.get_balance() == 1000

