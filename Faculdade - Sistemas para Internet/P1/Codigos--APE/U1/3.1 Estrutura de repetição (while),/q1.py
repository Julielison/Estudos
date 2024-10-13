#Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles Obs: não use o comando for, use while.
#ok
cont = 0
soma = 0
while cont < 30:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
print(f'A soma dos {cont} números digitados corresponde a {soma}')