ctr = input('Digite um caractere: ').lower()
if ctr in 'aeiou':
    print('vogal')
elif ctr in 'qwrtyplkjhgfdszxcvbnm':
    print('consoante')
elif ctr in '1234567890':
    print('número')
else:
    print('caractere especial')