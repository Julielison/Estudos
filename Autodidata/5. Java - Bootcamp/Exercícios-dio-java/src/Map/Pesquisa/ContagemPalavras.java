package Map.Pesquisa;

import java.util.HashMap;
import java.util.Map;

public class ContagemPalavras {
    private Map<String, Integer> contagemPalavras;

    public ContagemPalavras() {
        contagemPalavras = new HashMap<>();
    }

    public void adicionarPalavras(String palavra, int contagem){
        contagemPalavras.put(palavra, contagem);
    }

    public void removerPalavra(String palavra){
        if (contagemPalavras.containsKey(palavra)){
            contagemPalavras.remove(palavra);
        } else {
            System.out.println("Palavra não encontrada");
        }
    }

    public Map<String, Integer> exibirContagemPalavras(){
        return contagemPalavras;
    }

    public String encontrarPalavraMaisFrequente(){
        String maisFrequente = null;
        int contagem = 0;
        for (Map.Entry<String,Integer> entry : contagemPalavras.entrySet()){
            if (entry.getValue() > contagem){
                contagem = entry.getValue();
                maisFrequente =  entry.getKey();
            }
        }
        return maisFrequente;
    }

    public static void main(String[] args) {
        ContagemPalavras contagemLinguagens = new ContagemPalavras();
    
        // Adiciona linguagens e suas contagens
        contagemLinguagens.adicionarPalavras("Java", 2);
        contagemLinguagens.adicionarPalavras("Python", 8);
        contagemLinguagens.adicionarPalavras("JavaScript", 1);
        contagemLinguagens.adicionarPalavras("C#", 6);
    
        // Exibe a contagem total de linguagens
        System.out.println("Existem " + contagemLinguagens.exibirContagemPalavras() + " palavras.");
    
        // Encontra e exibe a linguagem mais frequente
        String linguagemMaisFrequente = contagemLinguagens.encontrarPalavraMaisFrequente();
        System.out.println("A linguagem mais frequente é: " + linguagemMaisFrequente);
      }
}
