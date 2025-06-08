from services.register_service import (
    register_client, create_account, fetch_account_by_number
    )
from services.transactions_service import (
    make_deposit, make_withdraw, show_balance
)

def show_menu():
    while True:
        print("\n=== DIGITAL BANK ===")
        print("1. Register client")
        print("2. Create account")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Balance")
        print("0. Exit")

        option = input("Choose an option: ")


        if option == "1":
            name = input("Customer name: ")
            cpf = input("CPF (numbers only): ")
            register_client(name, cpf)

        elif option == "2":
            cpf = input("Enter the customer's CPF: ")
            create_account(cpf)

        elif option == "3":
            number = int(input("Account number: "))
            account = fetch_account_by_number(number)
            if account:
                amount = float(input("Deposit amount: "))
                make_deposit(account, amount)
            else:
                print("Account not found.")

        elif option == "4":
            number = int(input("Account number: "))
            account = fetch_account_by_number(number)
            if account:
                amount = float(input("Withdrawal amount: "))
                make_withdraw(account, amount)
            else:
                print("Account not found.")

        elif option == "5":
            number = int(input("Account number: "))
            account = fetch_account_by_number(number)
            if account:
                show_balance(account)
            else:
                print("Account not found.")

        elif option == "0":
            print("Shutting down the system.")
            break

        else:
            print("Invalid option. Try again.")
