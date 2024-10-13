package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio15 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 29, 30, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, -1);
        /*
        Desafio 15 - Verifique se a lista contém pelo menos um número negativo:
        Utilizando a Stream API, verifique se a lista contém pelo menos um número negativo e exiba o resultado no console.
        */

        boolean result = numeros.stream()
                .anyMatch(n -> n < 0);
        System.out.println(result);

    }
}