# Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo abaixo.
# Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
# Exemplo:
# Entrada: FLAVIO RIBEIRO COUTINHO
# Saída: COUTINHO, F. R.
#feita: ok
#corrigida: 

#caso particular do exemplo
nome = input().upper().split()
print(f'{nome[-1]}, {nome[0][0]}. {nome[1][0]}.')

#caso geral
nome = input().upper().split()
print(f'{nome[-1]},',end='')
for i in range(len(nome)-1):
    print(f' {nome[i][0]}.',end='')