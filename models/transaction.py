from datetime import datetime

class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        self.date = datetime.now()