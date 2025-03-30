from datetime import datetime

operations = []

def len_operations():
    return len(operations)

def deposit(value):
    global operations
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    operations.append({'operation': 'DEPOSIT', 'value':value, 'type': 'CREDIT', 'time':date})
    return operations


def cash_withdrawal(value):
    global operations
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    operations.append({'operation': 'WITHDRAWAL', 'value':- value, 'type': 'DEBIT', 'time':date})
    return operations

def bank_statement():
    balance = 0
    print('+', '-'*65, '+') #linha de abertura
    for i, j in enumerate(operations):
        print(f'| {i+1:2} | {operations[i]['operation']:^10} | {operations[i]['type']:^10} | R$ {operations[i]['value']:>8.2f} | {operations[i]['time']} |')
        balance += operations[i]['value']
    print(f'|{' '*67}|') # linha em branco
    print(f'| CLOSING BALANCE {'-'*36} R$ {balance:8.2f}  |')
    print('+', '-'*65, '+') # linha de fechamento
    

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
    cash_withdrawal(80)
    cash_withdrawal(890)
    cash_withdrawal(110)
    print(bank_statement())