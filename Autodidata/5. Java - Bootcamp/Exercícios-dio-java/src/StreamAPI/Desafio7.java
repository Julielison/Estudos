package StreamAPI;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class Desafio7 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3);
        /*
        Desafio 7 - Encontrar o segundo número maior da lista:
        Com a ajuda da Stream API, encontre o segundo número maior da lista e exiba o resultado no console.
        */
        Optional<Integer> segundoMaior = numeros.stream()
                                                .distinct()  // Remove duplicatas
                                                .sorted(Comparator.reverseOrder())  // Ordena em ordem decrescente
                                                .skip(1)  // Pula o primeiro elemento (maior)
                                                .findFirst();  // Pega o segundo elemento
        System.out.println(segundoMaior.get());
    }

}
