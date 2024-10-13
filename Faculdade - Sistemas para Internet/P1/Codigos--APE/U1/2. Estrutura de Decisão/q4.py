nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo (M/F): ').upper()
if sexo == 'M':
    print(f'Olá, Sr. {nome}')
else:
    print(f'Olá, Sra. {nome}')