from models.transaction import Transaction
from models.account import Account

def make_deposit(account, amount):
    if amount <= 0:
        print("Invalid amount.")
        return
    
    account.balance += amount
    account.transactions.append(Transaction("DEPOSIT", amount))
    print("Successful deposit")

def make_withdraw(account, amount):
    if len(account.withdrawals) >=3:
        print("Daily withdrawal limit reached")
        return
    if amount > 500:
        print("Maximum value per withdrawal is R$500.00.")
        return
    if amount > account.balance:
        print("Insufficient balance to withdraw!")
        return
    
    account.balance -+ amount
    account.withdrawals.append(Transaction("WITHDRAWAL", amount))
    print("Successful withdrawal.")

def show_balance(account):
    if not account.transactions:
        print("No transactions were made.")
        return
    
    for transaction in account.transactions:
        print(f"{transaction.date} - {transaction.type}: R${transaction.amount:.2f}")
    print(f"\nCurrent balance: R${account.balance}")