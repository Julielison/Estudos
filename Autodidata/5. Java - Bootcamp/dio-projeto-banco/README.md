## Banco Digital usando OO

Este projeto é um sistema bancário simples desenvolvido em Java. Ele permite a criação de contas correntes e poupança para diferentes clientes, possibilitando operações como depósito, saque e transferência entre contas. Além disso, o sistema exibe extratos das contas e lista todas as contas criadas.

## Features

- **Criação de Contas**: Crie contas correntes e poupança para diferentes clientes.
- **Depósito**: Permite adicionar dinheiro às contas.
- **Saque**: Permite retirar dinheiro das contas, com verificação de saldo insuficiente.
- **Transferência**: Transfira dinheiro entre contas diferentes.
- **Extrato**: Exiba o extrato com informações das operações realizadas nas contas.
- **Lista de Contas**: Exibe todas as contas criadas no banco.

## Demonstração da Aplicação

1. **Criação de Clientes e Contas**
   - Dois clientes são criados: Venilton e Francisco.
   - Para cada cliente, são criadas uma conta corrente e uma conta poupança.

2. **Operações Financeiras**
   - Venilton deposita 100 unidades na sua conta corrente e transfere todo o valor para a sua conta poupança.
   - Francisco recebe uma transferência de 50 unidades da conta poupança de Venilton para sua própria conta poupança.

3. **Exibição de Extratos**
   - Extratos de todas as contas são impressos, mostrando o saldo e as informações da conta.

4. **Listagem de Contas Criadas**
   - Todas as contas criadas no banco são listadas.

## Como Executar

1. **Clone o repositório**:
    ```bash
    git clone <URL_do_repositório>
    ```
2. **Compile o código**:
    ```bash
    javac Main.java
    ```
3. **Execute a aplicação**:
    ```bash
    java Main
    ```

## Estrutura do Projeto

- `Main.java`: Classe principal onde a execução do programa inicia.
- `SaldoInsuficienteException.java`: Exceção personalizada para tratar casos de saldo insuficiente.
- `IConta.java`: Interface que define as operações básicas de uma conta bancária.
- `Conta.java`: Classe abstrata que implementa a interface `IConta` e serve como base para tipos específicos de contas.
- `ContaCorrente.java` e `ContaPoupanca.java`: Classes concretas que estendem `Conta` e implementam os métodos específicos de cada tipo de conta.
- `Cliente.java`: Classe que representa um cliente do banco.
- `Banco.java`: Classe que gerencia a lista de contas criadas.

## Exemplo de Saída

```
=== Extrato Conta Corrente ===
Titular: Venilton
Agencia: 1
Numero: 1
Saldo: 0.00

=== Extrato Conta Corrente ===
Titular: Francisco
Agencia: 1
Numero: 2
Saldo: 0.00

=== Extrato Conta Poupança ===
Titular: Venilton
Agencia: 1
Numero: 3
Saldo: 100.00

=== Extrato Conta Poupança ===
Titular: Francisco
Agencia: 1
Numero: 4
Saldo: 50.00

=== Contas criadas ===
Numero: 1 - Agência: 1 - Cliente: Venilton
Numero: 2 - Agência: 1 - Cliente: Francisco
Numero: 3 - Agência: 1 - Cliente: Venilton
Numero: 4 - Agência: 1 - Cliente: Francisco
```