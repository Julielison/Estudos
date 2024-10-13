n = int(input('Digite um número inteiro: '))

if n == 1:
    primo = False
else:
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False

if primo == True:
    print(n,'é primo')
else:
    print(n,'não é primo')