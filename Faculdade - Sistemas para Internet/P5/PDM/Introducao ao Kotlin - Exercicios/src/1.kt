/*
Créditos: Prof Edemberg Rocha - IFPB
Escreva uma função que receba um número e verifique se ele é positivo, negativo ou zero. Use o IF como expressão.
 */

fun main() {
    println(classficarNumero(-1.0))
    println(classficarNumero(1.0))
    println(classficarNumero(0.0))
}

fun classficarNumero(n: Double): String {
    return  if (n > 0) "Positivo" else if (n < 0) "Negativo" else "Zero"
}