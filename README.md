# 🏦 Criando um Sistema Bancário Simples

Este projeto implementa um **sistema bancário básico em Python**, contendo três operações essenciais: **depósito, saque e extrato**.  

Na **versão 1 (V1)**, o sistema suporta apenas um usuário, portanto **não há autenticação de agência ou conta**.  

---

## 🚀 Desafio  
Criar a primeira versão do sistema bancário, implementando as seguintes operações:  

- **Depósito**  
- **Saque**  
- **Extrato**  

---

## 📌 Regras do Sistema  

1️⃣ **Operações**:  
   - 🔹 **Depósitos**: todos os depósitos devem ser armazenados para exibição no extrato.  
   - 🔹 **Saques**:  
     - **Limite de 3 saques diários**.  
     - **Máximo de R$500,00 por saque**.  
     - ❌ Caso o saldo seja insuficiente, exibir a mensagem: `"Saldo insuficiente para saque!"`.  
   - 🔹 **Extrato**:  
     - Listar todos os depósitos e saques.  
     - Exibir o **saldo atual** no final.  
     - Se não houver movimentações, exibir a mensagem: `"Não foram realizadas movimentações."`.  

2️⃣ **Formatação Monetária**:  
   - Os valores devem ser exibidos no formato **R$ XXX,XX**.  

---
## 📜 Licença
Este projeto é livre para uso e modificação.
