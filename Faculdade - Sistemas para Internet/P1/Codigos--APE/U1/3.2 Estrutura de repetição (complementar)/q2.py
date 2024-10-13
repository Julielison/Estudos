#Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um programa que mostre todos os números primos de 1 a N (obs: N será lido).
n = int(input('Digite um número: '))
cont = 2
for i in range(2, n):
    if i%cont != 0:
        print(i)
    cont += 1