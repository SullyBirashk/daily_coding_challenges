import pytest
from main import BankAccount
def test_initial_balance():
    account = BankAccount('John Doe', 1000)
    assert account.get_balance() == 1000

def test_deposit():
    account = BankAccount('John Doe', 1000)
    account.deposit(500)
    assert account.get_balance() == 1500

def test_withdraw():
    account = BankAccount('John Doe', 1000)
    account.withdraw(300)
    assert account.get_balance() == 700

