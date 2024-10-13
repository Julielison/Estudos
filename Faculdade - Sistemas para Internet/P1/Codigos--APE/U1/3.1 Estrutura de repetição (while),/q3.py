#Faça um programa que leia vários números, determine e mostre o maior e o menor deles. Obs: a leitura do número 0 (zero) encerra o programa.

n = int(input('Digite um número: '))
maior = menor = n
while n != 0:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    n = int(input('Digite um número: '))
print(f'Menor número: {menor}\nMaior número: {maior}')