#Faça um programa que leia vários números, calcule e exiba a média desses números. Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser computado na média)
#ok
cont = soma = n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print(f'A média da soma dos {cont} números digitados é {soma/cont}')