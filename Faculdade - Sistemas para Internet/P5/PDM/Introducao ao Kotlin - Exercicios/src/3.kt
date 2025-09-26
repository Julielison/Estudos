/*
Crie uma  função que receba um valor e uma lista de valores (de tamanho indefinido e com valores de diferentes tipos de dados). A função deverá retornar quantas ocorrências do valor aparecem na lista.
 */

fun main() {
    val lista = listOf(3, 5, "r", 3.0, true, 3, 3.0, true, "r")
    println(contaroOcorrencias(3, lista))
    println(contaroOcorrencias(3.0, lista))
    println(contaroOcorrencias(true, lista))
    println(contaroOcorrencias("r", lista))
    println(contaroOcorrencias("5", lista))
}

fun contaroOcorrencias(valor: Any, lista: List<Any>) : Int {
    var qtd = 0
    lista.forEach { e ->
        if (e == valor){
            qtd += 1
        }
    }
    return qtd
}