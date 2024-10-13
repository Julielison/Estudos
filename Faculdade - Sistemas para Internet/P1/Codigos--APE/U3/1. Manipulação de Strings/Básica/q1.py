# Faça um programa que leia uma frase e determine a quantidade de brancos contidos na mesma.
#feita: ok
#corrigida: 

#Percorendo todos os caracteres da string com um for
frase = input('Digite uma frase: ')
count = 0
for i in range(len(frase)):
    if frase[i] == ' ':
        count+=1
print(f'A frase possui {count} espaços')