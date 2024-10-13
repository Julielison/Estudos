#Faça um programa que leia a idade de várias pessoas visitantes de um show (a leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
#• A média de idade do público;
#• A porcentagem de pessoas com idade entre 18 e 21 anos;
#• Idade do visitante mais jovem.

menor = soma_idades = idade = int(input('Digite a idade: '))
npessoas = 1
jovens = 0
if idade >= 18 and idade <= 21:
    jovens = 1
while idade != 0:
    idade = int(input('Digite a idade: '))
    if idade != 0:
        soma_idades += idade
        npessoas += 1
        if idade < menor:
            menor = idade
        if idade >= 18 and idade <= 21:
            jovens += 1
print(f'Média das idades: {soma_idades/npessoas:.1f} anos\nPorcentagem de pessoas de 18-21 anos: {(jovens/npessoas)*100:.2f} %\nIdade do mais jovem: {menor} anos')