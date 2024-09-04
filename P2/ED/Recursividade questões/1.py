# 1) Faça uma função recursiva chamada recursiveLength() que retorne a quantidade de caracteres de um string.

def recursiveLength(string: str):
    if string == '':
        return 0
    return recursiveLength(string[1:]) + 1

string = '12345678'
print(recursiveLength(string))