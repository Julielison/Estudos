package StreamAPI;
import java.util.Arrays;
import java.util.List;

public class Desafio9 {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 20);
        /*
        Desafio 8 - Somar os dígitos de todos os números da lista:
        Utilizando a Stream API, realize a soma dos dígitos de todos os números da lista e exiba o resultado no console
        */
        int somaDosDigitos = numeros.stream()
                                    .map(Desafio8::somarDigitos)
                                    .reduce(0, Integer::sum);

        System.out.println("A soma dos dígitos de todos os números da lista é: " + somaDosDigitos);
    }

    // Método auxiliar para somar os dígitos de um número
    public static int somarDigitos(int numero) {
        int soma = 0;
        while (numero > 0) {
            soma += numero % 10;
            numero /= 10;
        }
        return soma;
    }

    }
