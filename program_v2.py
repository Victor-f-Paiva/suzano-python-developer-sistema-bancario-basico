#1- implementart limite de 10 transações por dia
#2- printar msg se tentar saque após  atingir limite: "Você excedeu o numero de transações permitidas"
# 3- exibir data e hora das transações no extrato 

from system import *
from time import sleep
withdrawal_counter = 0

while True:
    #entrada de dados
    menu_operations()
    choice = int(input())

    # processamento e saída de dados
    if choice in (1,2) and len_operations() >= 10:
        print('You have reached the daily transaction limit.')
        sleep(2)
        continue

    if choice not in [1,2,3,4]:
        print('Choose a valid option.')
        sleep(2)

    if choice == 1:
        while True:
            value = float(input('How much do you want to deposit? R$'))
            if value <= 0:
                print('Choose a valid amount to deposit.')
                sleep(2)
                continue
            else:
                deposit(value)
                print('Deposit made successfully.')
                break
    elif choice == 2:
        while withdrawal_counter <3:
            value = float(input('How much do you want to withdraw? R$'))
            if value < 0:
                print('Choose a valid amount to deposit.')
                sleep(2)
                continue
            elif value > 500:
                print('It is not possible to withdraw more than R$500.00')
                sleep(2)
                continue
            else:
                cash_withdrawal(value=value)
                withdrawal_counter += 1
                print('Successful withdrawal.')
                break
        if withdrawal_counter >= 3:
            print('Maximum number of withdrawals has been exceeded')
            sleep(2)
    elif choice == 3:
        bank_statement()
    elif choice == 4:
        break

# saida do programa
bank_statement()