__registered_cpfs = []
__registered_users = []
__registered_bank_account = []
__next_account_num = 1
AGENCY = '0001'

def create_bank_account(cpf):
    global __registered_bank_account
    global __next_account_num
    for i, key in enumerate(__registered_users):
        if cpf == __registered_users[i]['cpf']:
            __registered_bank_account.append({'agency': AGENCY, 'account number': __next_account_num, 'name': __registered_users[i]['name']})
            __next_account_num += 1

def colect_user_data():
    while True:
        while True: #1
            try:
                cpf = int(input('Insert your CPF (whithout especial caracters (.-)): '))
                break
            except ValueError:
                print('Insert a valid CPF..')
                continue #1
        if cpf in __registered_cpfs:
            print('CPF already registered.')
            break
        else:
            __registered_cpfs.append(cpf)
        name = input('Type your full name: ').strip().title()
        bday_day = input('Insert your birthday day: ').strip()
        bday_month = input('Insert your birthday month: ').strip()
        bday_year = input('Insert your birthday year: ').strip()
        bday_date = f'{bday_day}/{bday_month}/{bday_year}'
        street = input('Insert your street name: ').strip().title()
        num = input('Insert your house number: ').strip().title()
        nbhood = input('Insert your neighborhood name: ').strip().title()
        city = input('Insert the city: ').strip().title()
        state = input('Insert the state acronym: ').strip().upper()
        address = f'{street}, {num} - {nbhood} - {city}/{state}'
        return [name, bday_date, cpf, address]

def create_user_account(user_data_list):
    global __registered_users
    __registered_users.append({'name': user_data_list[0], 'bday date': user_data_list[1], 'cpf': user_data_list[2], 'address':user_data_list[3]})
    return __registered_users

def listar_bank_acocunts():
    print(f'========================================================')
    for i,j in enumerate(__registered_bank_account):
        print(f' Agency: {__registered_bank_account[i]['agency']}, Account: {__registered_bank_account[i]['account number']} - User: {__registered_bank_account[i]['name']}')
        print(f'========================================================')

#testes
if __name__ == '__main__':
    user_data1 = colect_user_data()
    user_data2 = colect_user_data()
    create_user_account(user_data1)
    create_user_account(user_data2)
    print()
    print()
    cpf = int(input('CPF PARA CADASTRAR UMA CONTA'))
    create_bank_account(cpf)
    cpf2 = int(input('CPF PARA CADASTRAR UMA CONTA'))
    create_bank_account(cpf2)
    print()
    print(__registered_users, 'USERS REGISTRADOS')
    print()
    print(__registered_bank_account, 'CONTAS REGISTRADAS')
    print()
    print(__next_account_num, 'NUMERO DA PROXIMA CONTA')
    print()
    listar_bank_acocunts()