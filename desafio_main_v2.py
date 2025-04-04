#1- implementart limite de 10 transações por dia
#2- printar msg se tentar saque após  atingir limite: "Você excedeu o numero de transações permitidas"
# 3- exibir data e hora das transações no extrato 

from system import *
from time import sleep

withdrawal_counter = 0

while True:
    #entrada de dados
    menu_operations()
    try:
        choice = int(input())
        sleep(1)
    except ValueError:
        print('Choose a valid option...')
        continue

    # processamento e saída de dados
    if choice in (1,2) and len_operations() >= 10:
        print('You have reached the daily transaction limit.')
        sleep(1)
        continue

    if choice <= 0 and choice >= 8:
        print('Choose a valid option...')
        sleep(1)

    if choice == 1:
        while True:
            value = float(input('How much do you want to deposit? R$'))
            if value <= 0:
                print('Choose a valid amount to deposit.')
                sleep(1)
                continue
            else:
                deposit(value)
                print('Deposit made successfully.')
                print(f'Balance ===== {balance()}')

                break
    elif choice == 2:
        while withdrawal_counter <3:
            value = float(input('How much do you want to withdraw? R$'))
            if value < 0:
                print('Choose a valid amount to deposit.')
                sleep(1)
                continue
            elif value > 500:
                print('It is not possible to withdraw more than R$500.00')
                sleep(1)
                continue
            else:
                cash_withdrawal(value=value)
                withdrawal_counter += 1
                print('Successful withdrawal.')
                print(f'Balance ===== {balance()}')
                break
        if withdrawal_counter >= 3:
            print('Maximum number of withdrawals has been exceeded')
            sleep(1)
    elif choice == 3:
        bank_statement()
    elif choice == 4:
        try:
            data = colect_user_data()
            create_user_account(data)
        except TypeError:
            print('CPF is already registered...')
    elif choice == 5:
        while True:
            try:
                cpf = int(input('Insert your CPF (whithout especial caracters (.-)): '))
                break
            except ValueError:
                print('Insert a valid CPF..')
                continue
        create_bank_account(cpf)
    elif choice == 6:
        listar_bank_acocunts()
    elif choice == 7:
        list_user_accounts()
    elif choice == 8:
        break

# saida do programa
bank_statement()