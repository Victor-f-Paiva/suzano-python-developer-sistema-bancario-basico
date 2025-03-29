operations = []

def deposit(value):
    global operations
    operations.append({'operation': 'DEPOSIT', 'value':value, 'type': 'CREDIT'})
    return operations


def cash_withdrawal(value):
    global operations
    operations.append({'operation': 'WITHDRAWAL', 'value':- value, 'type': 'DEBIT'})
    return operations

def bank_statement():
    balance = 0
    print('+', '-'*41, '+')
    for i, j in enumerate(operations):
        print(f'| {i+1:2<} | {operations[i]['operation']:^10} | {operations[i]['type']:^10} | R$ {operations[i]['value']:>8.2f} |')
        balance += operations[i]['value']
    print(f'|{' '*43}|')
    print(f'| CLOSING BALANCE {'-'*14} R$ {balance:8.2f}|')
    print('+', '-'*41, '+')
    

# teste das funções
if __name__ == '__main__':
    deposit(20)    
    cash_withdrawal(20)
    cash_withdrawal(10)
    deposit(550)    
    deposit(40)    
    deposit(1230)    
    cash_withdrawal(70)
    cash_withdrawal(80)
    print(bank_statement())