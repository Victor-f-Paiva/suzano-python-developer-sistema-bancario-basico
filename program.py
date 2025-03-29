#1- Criar 3 operações (saque, deposito, extrato)
    #1.1 -DEPOSITOS = deve armazenar todos os depósitos para exibir no extrato
    #1.2-SAQUES = máx de 3 saques diarios com limites de 500 por saque
    #   1.2.1- caso não tenha saldo- printar msg de impossibilidade de sacar por falta de saldo
    # 1.3- EXTRATO = listar todos depósitos e saques. printar no fim o saldo atual.Se não houver movimentações exibir msg "Não foram realizadas movimentações."
#2- OBS: printar o extrato com movimentações em reais com formato R$ xxx.xx

from system import deposit, bank_statement, menu_operations, cash_withdrawal
withdrawal_counter = 0

while True:
    #entrada de dados
    menu_operations()
    choice = int(input())

    # processamento e saída de dados
    if choice not in [1,2,3,4]:
        print('Choose a valid option.')
    if choice == 1:
        while True:
            value = float(input('How much do you want to deposit? R$'))
            if value <= 0:
                print('Choose a valid amount to deposit.')
                continue
            else:
                deposit(value)
                break
    elif choice == 2:
        while withdrawal_counter <=3:
            value = float(input('How much do you want to withdraw? R$'))
            if value < 0:
                print('Choose a valid amount to deposit.')
                continue
            elif value > 500:
                print('It is not possible to withdraw more than R$500.00')
                continue
            else:
                cash_withdrawal(value)
                withdrawal_counter += 1
                break
    elif choice == 3:
        bank_statement()
    elif choice == 4:
        break

# saida do programa
bank_statement()