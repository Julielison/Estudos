package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio18 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 1, 1);
        /*
        Desafio 18 - Verifique se todos os números da lista são iguais:
        Utilizando a Stream API, verifique se todos os números da lista são iguais e exiba o resultado no console.
        */
        boolean resultado = numeros.stream()
            .allMatch(n -> n.equals(numeros.get(0)));

        System.err.println(resultado);

    }
}