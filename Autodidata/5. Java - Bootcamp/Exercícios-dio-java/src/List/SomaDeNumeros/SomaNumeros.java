package List.SomaDeNumeros;

import java.util.ArrayList;
import java.util.List;

public class SomaNumeros {
    private List<Integer> numerosInteiros;

    public SomaNumeros() {
        this.numerosInteiros = new ArrayList<>();
    }

    public void adicionarNumero(int numero){
        numerosInteiros.add(numero);
    }

    public int calcularSoma(){
        int soma = 0;
        for (Integer i : numerosInteiros){
            soma += i;
        }
        return soma;
    }

    public int encontrarMenorNumero(){
        int menor = Integer.MAX_VALUE;

        for (Integer i : numerosInteiros) {
            if (i < menor)
                menor = i;
        }
        return menor;
    }

    public void exibirNumeros(){
        System.out.println(numerosInteiros);
    }

    private int encontrarMaiorNumero() {
        int maior = Integer.MIN_VALUE;

        for (Integer i : numerosInteiros) {
            if (i > maior)
                maior = i;
        }
        return maior;
    }

    public static void main(String[] args) {
        // Criando uma instância da classe SomaNumeros
        SomaNumeros somaNumeros = new SomaNumeros();
    
        // Adicionando números à lista
        somaNumeros.adicionarNumero(5);
        somaNumeros.adicionarNumero(0);
        somaNumeros.adicionarNumero(0);
        somaNumeros.adicionarNumero(-2);
        somaNumeros.adicionarNumero(10);
    
        // Exibindo a lista de números adicionados
        System.out.println("Números adicionados:");
        somaNumeros.exibirNumeros();
    
        // Calculando e exibindo a soma dos números na lista
        System.out.println("Soma dos números = " + somaNumeros.calcularSoma());
    
        // Encontrando e exibindo o maior número na lista
        System.out.println("Maior número = " + somaNumeros.encontrarMaiorNumero());
    
        // Encontrando e exibindo o menor número na lista
        System.out.println("Menor número = " + somaNumeros.encontrarMenorNumero());
      

    }
}
