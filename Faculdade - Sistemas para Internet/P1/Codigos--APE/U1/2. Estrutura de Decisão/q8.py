n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = input('Digite um operador: ').lower()
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == 'x' or op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
elif op == '%':
    print(n1%n2)
else:
    print('Operador desconhecido')