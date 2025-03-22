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

def test_withdraw_more_than_balance():
    account = BankAccount('John Doe', 1200)
    with pytest.raises(ValueError, match='Insufficient funds. Current balance: 1200'):
            account.withdraw(1500)
            assert account.get_balance() == 1200

def test_negative_deposit():
     account = BankAccount('John Doe', 1000)
     with pytest.raises(ValueError, match='Deposit amount must be a positive number'):
              account.deposit(-100)

def test_non_numeric_deposit():
     account = BankAccount('John Doe', 1000)
     with pytest.raises(TypeError, match='Deposit amount must be numeric'):
              account.deposit('five hundred')

def test_negative_withdraw():
      account = BankAccount('John Doe', 1000)
      with pytest.raises(ValueError, match='Withdrawal amount must be a positive number'):
                account.withdraw(-50)

def test_non_numeric_withdraw():
      account = BankAccount('John Doe', 1000)
      with pytest.raises(TypeError, match='Withdrawal amount must be numeric'):
                account.withdraw('two hundred')

