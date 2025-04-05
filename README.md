# 🏦 Python Banking System
This project implements a basic banking system in **Python**.

- In **version 1 (V1)**, the system supports only one user, so there is no branch or account authentication. It includes three core operations: deposit, withdrawal, and statement, with a limit of 3 withdrawals;
- In **version 2 (V2)**, two new functions are added (register user and create bank account), along with a daily limit of 10 transactions and the inclusion of date and time in the statement;

## 🚀 Challenge
- **Create Deposit Function**
- **Create Withdrawal Function**
- **Create Statement Function**
- **Limit Daily Transactions**
- **Include Transaction Date and Time**

## 📌 System Rules
1️⃣ Operations:

- 🔹 Deposits: all deposits must be stored and displayed in the statement.

- 🔹 Withdrawals:

  - Limit of 3 withdrawals per day.
  - Maximum of R$500.00 per withdrawal.
  - ❌ If the balance is insufficient, display the message: `"Insufficient funds for withdrawal!"`.

- 🔹 Statement:

  - List all deposits and withdrawals.
  - Show the date and time of each transaction.
  - Display the current balance at the end.
  - If there are no transactions, show the message: `"No transactions have been made."`.

- 🔹 Transactions:
  - Only 10 transactions allowed per day.

- 🔹 User registration: Only one user per CPF.

- 🔹 Bank account registration: Each account can have only one user, but each user can have multiple accounts. 
- 🔹 The branch number is fixed as `0001`.

2️⃣ Currency Formatting:

-  Values must be displayed in Brazilian currency formatting **R$ XXX,XX**.

## 📜 License
This project is free to use and modify.
______________________________________
______________________________

# 🏦 Sistema Bancário em Python
Este projeto implementa um **sistema bancário básico em Python**.  

- Na **versão 1 (V1)**, o sistema suporta apenas um usuário, portanto **não há autenticação de agência ou conta**. Contém três operações essenciais: **depósito, saque e extrato** e um limite de 3 saques;
- Na **versão 2 (V2)**, cria duas novas funções (**cadastrar usuário e cadastrar conta bancária**)adiciona limite diário de **10 operações por dia** e inclui data e hora no extrato;

---

## 🚀 Desafio   

- **Criar função de Depósito**  
- **Criar função de Saque**  
- **Criar função de Extrato** 
- **Limitar operaçoes diários**
- **Incluir data e hora da transação** 

---

## 📌 Regras do Sistema  

1️⃣ **Operações**:  
   - 🔹 **Depósitos**: todos os depósitos devem ser armazenados para exibição no extrato.  
   - 🔹 **Saques**:  
     - **Limite de 3 saques**.  
     - **Máximo de R$500,00 por saque**.  
     - ❌ Caso o saldo seja insuficiente, exibir a mensagem: `"Saldo insuficiente para saque!"`.  
   - 🔹 **Extrato**:  
     - Listar todos os depósitos e saques.  
     - Exibir **data e hora** da transação.  
     - Exibir o **saldo atual** no final.  
     - Se não houver movimentações, exibir a mensagem: `"Não foram realizadas movimentações."`.  
   - 🔹 **Transações**:  
     - Listar todos os depósitos e saques.  
   - 🔹 **Cadastro de usuários**: Apenas um usuário por CPF
   - 🔹 **Cadastro de conta corrente**: Cada conta só pode ter um usuário, mas cada usuário pode ter mais de uma conta e o número de agência será fixo `0001`.

2️⃣ **Formatação Monetária**:  
   - Os valores devem ser exibidos no formato **R$ XXX,XX**.  

---
## 📜 Licença
Este projeto é livre para uso e modificação.

