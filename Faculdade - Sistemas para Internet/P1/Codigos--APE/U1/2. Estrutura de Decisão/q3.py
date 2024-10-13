numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite um terceiro numero: '))
print(f'O maior número é o ', end='' )
if numero1>numero2 and numero1>numero3:
    print(numero1)
elif numero2>numero1 and numero2>numero3:
    print(numero2)
else:
    print(numero3)