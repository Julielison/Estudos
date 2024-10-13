#Faça um programa que leia um número inteiro e determine se ele é par ou ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser encerrado.

while input('Deseja inciar/continuar? (s/n): ').lower() != 'n':
    n = int(input('Digite um número inteiro: '))
    print(f'{n} é ', end='')
    if n%2 == 0:
        print('par')
    else:
        print('ímpar')
print('Fim')