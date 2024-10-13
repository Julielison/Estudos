# Faça um programa que leia o email de uma pessoa e mostre, separadamente, qual o login e qual o domínio. Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login será "fulano" e o domínio será "provedor.com.br".
#feita: ok
#corrigida: 

email = input('Digiite seu email: ').split('@')
print(f'Login: {email[0]}')
print(f'Domínio: {email[1]}')