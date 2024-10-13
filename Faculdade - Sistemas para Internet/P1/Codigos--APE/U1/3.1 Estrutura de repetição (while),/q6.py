#Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e cresce 3 centímetros por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

h_zé = 110
h_chico = 150
anos = 0
while h_zé <= h_chico:
    h_zé += 3
    h_chico += 2
    anos += 1
print(f'Serão necessários {anos} anos para que Zé seja maior que Chico')