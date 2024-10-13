# Faça um programa que leia uma frase e a exiba criptografada. O método de criptografia será baseado na seguinte regra: trocar alguns caracteres por outros, conforme a tabela abaixo:
# Exemplo: "BOA NOITE" criptografado fica "BI ANIOTU"
#feita: ok
#corrigida: 

frase = input().upper()
for caracter in frase:
    match caracter:
        case 'A':
            print(' ',end='')
        case 'E':
            print('U', end='')
        case 'I':
            print('O',end='')
        case 'O':
            print('I', end='')
        case 'U':
            print('E', end='')
        case ' ':
            print('A', end='')
        case _:
            print(caracter, end='')