nome = input('Digite seu nome: ')
conceito = input('Digite seu conceito: ').upper()
if conceito == 'A':
    print(f'O aluno {nome} é fortemente recomendado')
elif conceito == 'B' or conceito == 'C':
    print(f'O aluno {nome} é recomendado')
else:
    print(f'O aluno {nome} não é recomendado')