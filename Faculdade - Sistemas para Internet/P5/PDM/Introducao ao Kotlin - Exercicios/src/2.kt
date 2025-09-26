/*
Implemente uma função que receba a idade de uma pessoa e use o when para verificar e retornar à faixa etária de uma pessoa (criança, adolescente, adulto, idoso).
 */

fun main() {
    println(obterFaixaEtaria(5))
    println(obterFaixaEtaria(13))
    println(obterFaixaEtaria(18))
    println(obterFaixaEtaria(60))
}

fun obterFaixaEtaria(idade: Int): String {
    return when {
        idade >= 60 -> "Idoso"
        idade >= 18 -> "Adulto"
        idade >= 12 -> "Adolescente"
        else -> "Criança"
    }
}