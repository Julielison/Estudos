# Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as suas vogais repetidas N vezes.
# Exemplo:
# Entrada: S: Hoje tem aula de Python N: 3
# Saída: Hooojeee teeem aaauuulaaa deee Pythooon
#feita: ok
#corrigida: 

string = input().capitalize().split()
numero = int(input())
for palavra in string:
    for caracter in palavra:
        if caracter in 'AaEeIiOoUu':
            print(caracter*numero,end='')
        else:
            print(caracter,end='')
    print(' ',end='')