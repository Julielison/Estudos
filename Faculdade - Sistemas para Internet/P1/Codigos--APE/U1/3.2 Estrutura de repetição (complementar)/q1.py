#Faça um programa que leia um número N, calcule e mostre os N primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido para N sempre será maior ou igual a 2.
#ok - resposta não minha
n = int(input("Quantos termos da sequência de fibonacci você quer?: "))
termo = penultimo = 0
ultimo = 1
print('0, 1', end=', ')
for termo in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(f'{termo}', end=', ')