from datetime import datetime

operations = []
saldo = 0

def len_operations():
    return len(operations)

def deposit(value, /): #forçando argumentos POSICIONAIS
    global operations
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    operations.append({'operation': 'DEPOSIT', 'value':value, 'type': 'CREDIT', 'time':date})
    global saldo
    saldo += value
    return operations, saldo

def cash_withdrawal(*, value): #forçando argumentos NOMEADOS
    global operations
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    operations.append({'operation': 'WITHDRAWAL', 'value':- value, 'type': 'DEBIT', 'time':date})
    global saldo
    saldo -= value
    return operations, saldo

def bank_statement():
    print('+', '-'*65, '+') #linha de abertura
    for i, j in enumerate(operations):
        print(f'| {i+1:2} | {operations[i]['operation']:^10} | {operations[i]['type']:^10} | R$ {operations[i]['value']:>8.2f} | {operations[i]['time']} |')
    print(f'|{' '*67}|') # linha em branco
    print(f'| CLOSING BALANCE {'-'*36} R$ {saldo:8.2f}  |')
    print('+', '-'*65, '+') # linha de fechamento
    
def balance():
    return f'R$ {saldo:.2f}'

# teste das funções
if __name__ == '__main__':
    deposit(20)    
    cash_withdrawal(value=20)
    cash_withdrawal(value=10)
    deposit(550)    
    deposit(40)    
    deposit(1230)    
    cash_withdrawal(value=70)
    cash_withdrawal(value=80)
    cash_withdrawal(value=80)
    cash_withdrawal(value=890)
    cash_withdrawal(value=110)
    print(bank_statement())