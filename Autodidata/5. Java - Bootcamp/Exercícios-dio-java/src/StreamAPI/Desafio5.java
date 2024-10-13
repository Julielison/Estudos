package StreamAPI;
import java.util.Arrays;
import java.util.List;
import java.util.OptionalDouble;

public class Desafio5 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3);
        /*
        Desafio 5 - Calcule a média dos números maiores que 5:
        Com a Stream API, calcule a média dos números maiores que 5 e exiba o resultado no console.
        */
        
        // Opcão 1 - Mais verbosa
        List<Integer> maioresQue5 = numeros.stream()
        .filter(n -> n > 5)
        .toList();

        Integer soma = maioresQue5.stream().reduce(0, Integer::sum);
        Long quantidade = maioresQue5.stream().count();
        Double media = soma / (double) quantidade;
        System.out.println(media);
        
        // Opção 2
        OptionalDouble media2 = numeros.stream()
        .filter(n -> n > 5)
        .mapToInt(num -> num)
        .average();

        System.out.println(media2.getAsDouble());
    }
}
