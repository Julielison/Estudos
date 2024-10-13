#Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver repetição). O programa deverá calcular e exibir a quantidade de números acertados em cada aposta.
#Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.
#
n = 8
apostador1 = [None]*n
apostador2 = [None]*n
aposta = []
sorteado = [6, 7, 13, 14, 26]
índice = 0

for i in range(2):
    while índice < 3:
        rascunho = int(input(f'Digite a {índice+1}ª dezena: '))
        if rascunho < 1 or rascunho > 80:
            print('Dezena inválida')
            continue
        elif aposta.count(rascunho) == 1:
            print('Dezena já lida, digite uma nova...')
            continue
        aposta.append(rascunho)
        índice += 1
    if i == 0:
        apostador1 = aposta
    else:
        apostador2 = aposta
    aposta.clear()
    índice = 0
print(apostador1)
print(apostador2)
