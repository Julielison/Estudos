# Faça um programa que leia uma frase e a exiba sem os espaços em branco.
#feita: ok
#corrigida: 

#Separando as palavras por espaço em uma lista e printando os elementos em sequência
frase = input('Digite uma frase: ').split()
for elemento in frase:
    print(elemento, end='')