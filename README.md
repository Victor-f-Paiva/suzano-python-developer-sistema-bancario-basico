# 🏦 Criando um Sistema Bancário

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
