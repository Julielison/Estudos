# Conta Bancária - Terminal

Este é um programa simples em Java que simula uma conta bancária. Ele solicita informações do usuário, como número da conta, número da agência, nome do cliente e saldo. Em seguida, exibe uma mensagem de boas-vindas com os dados fornecidos.

## Como executar o programa

1. Baixe o arquivo clicando no botão verde `Code`, em seguida `Download ZIP` ou `Baixar ZIP`.

2. Extraia os arquivos do ZIP que baixou.

3. Certifique-se de ter uma JRE instala em seu Sistema Operacional, se não tiver, siga o [Tutorial](https://mauriciogeneroso.medium.com/configurando-java-1-instala%C3%A7%C3%A3o-do-jre-e-do-jdk-no-windows-38cacace0377).

4. Abra uma interface de linha de comandos de sua preferência, navegue até a pasta bin do arquivo que você baixou, digite a instrução a seguir e pressione `Enter`.
    ```
    java ContaTerminal
    ```

5. Siga as instruções no console para inserir os dados necessários.

## Descrição do código

1. **Configuração do Scanner:**
- O programa cria dois objetos `Scanner` para ler dados do console.
- O primeiro `Scanner` é configurado para usar o padrão de localidade dos EUA (ponto como separador decimal).

2. **Leitura dos dados do usuário:**
- Solicita e lê o número da conta e o número da agência.
- Cria um segundo `Scanner` para ler o nome do cliente.
- Solicita e lê o saldo do usuário.

3. **Exibição da mensagem de boas-vindas:**
- Utiliza os dados fornecidos para exibir uma mensagem personalizada ao cliente.

4. **Fechamento dos Scanners:**
- Fecha os objetos `Scanner` para liberar os recursos.

## Exemplo de uso
```
> Digite o número da Conta:
> 12345 
> Digite o número da Agência:
> XYZ Digite seu nome:
> João da Silva
> Digite seu saldo: 1500.50
> Olá João da Silva, obrigado por criar uma conta em nosso banco, sua agência é XYZ, conta 12345 e seu saldo 1500.5 já está disponível para saque
```
