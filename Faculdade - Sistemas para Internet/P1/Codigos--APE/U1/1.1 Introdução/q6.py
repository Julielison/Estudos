valor = int(input('Valor de saque: '))
n_cinquenta = valor//50
resto_n_cinquenta = valor%50
n_dez = resto_n_cinquenta//10
resto_dez = resto_n_cinquenta%10
n_cinco = resto_dez//5
n_um = resto_dez%5
print(f'''Saque: B$ {valor}, em:
    {n_cinquenta} notas de B$ 50
    {n_dez} notas de B$ 10
    {n_cinco} notas de B$ 5
    {n_um} notas de B$ 1''')