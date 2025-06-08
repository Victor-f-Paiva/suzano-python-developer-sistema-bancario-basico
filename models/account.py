from datetime import datetime

class Account:
    def __init__(self, number, client):
        self.number = number
        self.client = client
        self.agency = "0001"
        self.balance = 0
        self.transactions = []
        self.withdrawals = []