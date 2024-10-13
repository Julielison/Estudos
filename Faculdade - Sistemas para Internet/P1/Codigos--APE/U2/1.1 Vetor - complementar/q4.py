#Escreva um programa para ler 6 números distintos, ou seja, não podem repetir. Exiba os números lidos.
#ok
v = []
cont = 0
while cont < 6:
    rascunho = int(input(f'Digite o {cont+1}º valor: '))
    if v.count(rascunho) > 0:
        print('Valor já inserido, digite um valor diferente...')
        continue
    v.append(rascunho)
    cont += 1
print(f'Números lidos: {v}')