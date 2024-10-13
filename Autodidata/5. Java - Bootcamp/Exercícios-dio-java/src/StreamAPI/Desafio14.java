package StreamAPI;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class Desafio14 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 29, 30, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17);
        /*
        Desafio 14 - Encontre o maior número primo da lista:
        Com a Stream API, encontre o maior número primo da lista e exiba o resultado no console.
        */

        Optional<Integer> result = numeros.stream()
            .filter(Desafio14::ehPrimo)
            .max(Comparator.naturalOrder());

        System.out.println(result.get());

    }

    public static boolean ehPrimo(int numero) {
        // Verifica se o número é menor ou igual a 1
        if (numero <= 1) {
            return false;
        }

        // Verifica se o número é 2 ou 3
        if (numero <= 3) {
            return true;
        }

        // Verifica se o número é divisível por 2 ou 3
        if (numero % 2 == 0 || numero % 3 == 0) {
            return false;
        }

        // Verifica divisões até a raiz quadrada do número
        for (int i = 5; i * i <= numero; i += 6) {
            if (numero % i == 0 || numero % (i + 2) == 0) {
                return false;
            }
        }

        // Se não encontrou divisores, é primo
        return true;
    }
}