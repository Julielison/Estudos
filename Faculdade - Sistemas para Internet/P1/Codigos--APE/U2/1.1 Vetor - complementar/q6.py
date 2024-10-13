#O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades federativas. Escreva um programa para armazene, em um vetor, a sigla de todas as unidades federativas. O programa deverá obter de vários usuários qual é a unidade federativa ele acha mais interessante, informando a respectiva sigla. O programa encerra quando for digitada uma sigla inexistente. Ao final, o programa deverá exibir qual foi a sigla mais votada (considere possibilidade de empate).
vetor = ['AM','CE','PB','RN','PA','RR','DF','AC','AP','RO','MA','TO','GO','MS','SP','PR','SC','RS','MG','RJ','ES','BA','SE','AL','PE','PI','MT']
voto=[0]*27
maxv = []

while True:
    sigla = input('Digite a sigla de um estado: ').upper()
    if sigla not in vetor:
        break
    voto[vetor.index(sigla)] += 1

maior = 0
maxv[0] = '-'
for i in vetor:
    if voto[i] > maior:
        del(maxv[i])
        maior = voto[i]
        maxv.append(vetor[voto.index(maior)])
    elif voto[i] == maior:
        maxv.append(vetor[voto.index(maior)])

    print(f'Estado mais votado {vetor[voto.index(max(voto))]}')