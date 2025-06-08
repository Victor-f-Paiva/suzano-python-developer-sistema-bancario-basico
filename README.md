# 💰 Basic Banking System (CLI)

A simple command-line banking system written in Python, following clean code principles and basic business rules.

## 📌 Features

- Register clients (one client per CPF)
- Create multiple accounts per client (fixed agency number: `0001`)
- Deposit and withdraw with business constraints
- View statement with full transaction history and current balance

## ✅ Business Rules

- **Deposits**
  - All deposits must be recorded and shown in the statement

- **Withdrawals**
  - Limit of **3 withdrawals** per account
  - Maximum **R$500.00 per withdrawal**
  - If balance is insufficient, display: `"Insufficient balance to withdraw!"`

- **Statement**
  - Displays all deposits and withdrawals
  - Includes **date and time** of each transaction
  - Shows current balance at the end
  - If no transactions were made, display: `"No transactions were made."`

- **Clients and Accounts**
  - Only **one client per CPF**
  - One client can have **multiple accounts**
  - All accounts share the fixed agency number: `0001`

## 🗂️ Project Structure

```

suzano-python-developer-sistema-bancario-basico/
│
├── core/                   # Main CLI logic
│   ├── **init**.py
│   └── menu.py
│
├── models/                 # Business entities
│   ├── **init**.py
│   ├── client.py
│   ├── account.py
│   └── transaction/
│
├── services/               # Business logic (register, deposit, withdraw)
│   ├── **init**.py
│   ├── register\_service.py
│   └── transactions\_service.py
│
├── utils/                  # Utilities and helpers
│   ├── **init**.py
│   ├── formaters.py
│   └── validators/
│
├── .gitignore              # Git ignore list
├── LICENSE                 # License file
├── main.py                 # Entry point (if applicable)
└── requirements.txt        # Project dependencies

````

## 🚀 How to Run

1. Clone the repository:

```bash
   git clone https://github.com/Victor-f-Paiva/suzano-python-developer-sistema-bancario-basico.git
   cd suzano-python-developer-sistema-bancario-basico
```

2. Run the main menu:

```bash
   main.py
```

## 💡 Technologies Used

* Python 3.13.1
* Object-Oriented Programming
* Clean architecture and modular organization

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🧠 Author

Victor Paiva
[LinkedIn](https://www.linkedin.com/in/victor-paiva-b4392ab7/)

