#Faça um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as duas notas que ele obteve em suas avaliações. A condição de parada será a digitação de uma matrícula igual 0 (zero). O programa deverá mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a média for inferior a 7).

matrícula = int(input('Digite sua matrícula: '))
while matrícula != 0:
    nome = input('Digite seu nome: ')
    nota1 = int(input('Digite a 1ª nota: '))
    nota2 = int(input('Digite a 2ª nota: '))
    média = (nota1+nota2)/2
    if média >= 7:
        situação = 'aprovado'
    else:
        situação = 'reprovado'
    print(f'Matrícula: {matrícula}, Nome: {nome}, Média: {média}, Situação: {situação}')
    matrícula = int(input('Digite sua matrícula: '))
print('Fim')