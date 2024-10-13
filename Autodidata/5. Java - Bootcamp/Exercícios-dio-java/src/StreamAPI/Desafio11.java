package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio11 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        /*
        Desafio 11 - Encontre a soma dos quadrados de todos os números da lista:
        Utilizando a Stream API, encontre a soma dos quadrados de todos os números da lista e exiba o resultado no console. 
        */

        Integer resultado = numeros.stream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

        System.out.println(resultado);
    }
}
