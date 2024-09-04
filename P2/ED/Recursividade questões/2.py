# Faça uma função recursiva chamada printstr() que imprima na tela uma string (caractere a caractere na mesma linha).

def print_str(string: str) -> None:
    if string == '':
        return
    print(string[0], end='')
    print_str(string[1:])

nome = 'teste'
print_str(nome)