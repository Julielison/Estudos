package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio16 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 29, 30, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, -1);
        /*
        Desafio 16 - Agrupe os números em pares e ímpares:
        Utilize a Stream API para agrupar os números em duas listas separadas, uma contendo os números pares e outra contendo os números ímpares da lista original, e exiba os resultados no console.
        */
        // Pares
        System.out.println("Pares:");
        numeros.stream()
            .filter(n -> n % 2 == 0)
            .toList()
            .forEach(n -> System.out.printf(n + ", "));

        // Impares
        System.out.println("\nÍmpares:");
        numeros.stream()
            .filter(n -> n % 2 != 0)
            .forEach(n -> System.out.printf(n + ", "));
    }
}