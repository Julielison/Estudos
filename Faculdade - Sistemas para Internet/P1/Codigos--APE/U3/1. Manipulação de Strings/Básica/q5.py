# Faça um programa que leia uma frase e a exiba com uma letra em cada linha.
#feita: ok
#corrigida: 

#com espaço
frase = input()
for i in range(len(frase)):
    print(frase[i])

#sem espaço
frase = input().replace(' ','')
for i in range(len(frase)):
    print(frase[i])