package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio13 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        /*
        Desafio 13 - Filtrar os números que estão dentro de um intervalo:
        Utilize a Stream API para filtrar os números que estão dentro de um intervalo específico (por exemplo, entre 5 e 10) e exiba o resultado no console.
        */

        numeros.stream()
            .filter(n -> n > 5 && n < 10)
            .toList()
            .forEach(System.out::println);

    }
}
