# Definindo uma função que eleva um número ao quadrado
def quadrado(x):
    return x ** 2

# Aplicando a função a cada elemento de uma lista usando map
numeros = [1, 2, 3, 4, 5]
resultado = map(quadrado, numeros)

# Convertendo o objeto map para uma lista (opcional, dependendo do uso)
lista_resultado = list(resultado)

print(lista_resultado)
