#Faça um programa que acompanhe um set de uma partida de vôlei. O programa deve ler o código da equipe (A ou B) que ganhou o ponto e responder quem ganha a partida. O set chega ao final se uma das equipes chega a 25 pontos e a diferença de pontos entre elas é maior ou igual a dois. A equipe que conseguir isso é a vencedora do set.
#ok - levei mais ou menos 30 min pra fazer
a = b = 0
while (a < 25 and b < 25) or ((a>=25 or b>=25) and (abs(a-b) < 2)):
    ponto = input('Quem ganhou o ponto? (A/B): ').upper()
    if ponto == 'A':
        a += 1
    else:
        b +=1
    print(f'Placar atual: A = {a}, B = {b}')
print(f'Placar final: A = {a}, B = {b}\nVencedor: ', end='')
if a > b:
    print('A')
else:
    print('B')