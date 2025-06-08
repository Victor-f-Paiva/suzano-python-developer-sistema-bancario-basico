from models.client import Client
from models.account import Account

clients = []
accounts = []
account_counter = 1

def register_client(name, cpf):
    from models.client import Client

    for c in clients:
        if c.cpf == cpf:
            print("CPF already registered.")
            return
        
    new_client = Client(name, cpf)
    clients.append(new_client)
    print("Client registered with success.")

def create_account(cpf):
    global account_counter

    client = fetch_cliente_by_cpf(cpf)
    if not client:
        print("Customer not found. Register the customer first")
        return
    
    new_account = Account(number= account_counter, client= client)
    client.accounts.append(new_account)
    accounts.append(new_account)
    account_counter += 1
    print(f"Account created successfully! Account number: {new_account.number}")

def fetch_cliente_by_cpf(cpf):
    for client in clients:
        if client.cpf == cpf:
            return client
    return None

def fetch_account_by_number(number):
    for account in accounts:
        if account.number == number:
            return account
    return None