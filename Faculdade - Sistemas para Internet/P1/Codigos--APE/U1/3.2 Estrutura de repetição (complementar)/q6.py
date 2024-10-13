# Faça um programa que solicite ao usuário uma senha. Caso a senha digitada esteja correta, o programa deverá mostrar senha correta. Caso contrário, o programa deverá mostrar senha incorreta e pedir para o usuário tentar novamente digitar a senha correta. Mas, se o usuário fornecer três senhas incorretas, o programa deverá encerrar a sua execução. (Obs: a senha correta é “abcd”).
#ok
cont = 1
tentativas = 3
senha = 'abcd'
s = input('Digite uma senha: ')
while s != 'abcd' and cont < 3:
    tentativas -= 1
    cont += 1
    print(f'Senha incorreta, {tentativas} tentativas restantes...')
    s = input('Tente novamente: ')
if s == 'abcd':
    print('Senha correta!')
else:
    print('Limite de tentativas atingido')