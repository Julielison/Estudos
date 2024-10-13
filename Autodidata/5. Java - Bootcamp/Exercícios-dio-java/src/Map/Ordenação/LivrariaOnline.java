package Map.Ordenação;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class LivrariaOnline {
    private Map<String, Livro> ebooks;

    public LivrariaOnline() {
        this.ebooks = new HashMap<>();
    }

    public void adicionarLivro(String link, String titulo, String autor, double preco){
    this.ebooks.put(link, new Livro(titulo, autor, preco));
    }

    public void removerLivro(String titulo){
        String tituloProcurado;
        String chaveProcurada = null; 

        for (var entry : this.ebooks.entrySet()){
            tituloProcurado = entry.getValue().getTitulo();
            if (tituloProcurado.equalsIgnoreCase(titulo)){
                chaveProcurada = entry.getKey();
                break;
            }
        }
        this.ebooks.remove(chaveProcurada);
    }

    public Map<Livro, String> exibirLivrosOrdenadosPorPreco() {
        // Criar um TreeMap com um comparador que ordena pelo preço
        Map<Livro, String> livrosOrdenados = new TreeMap<>(new ComparatorPorPreco());
        
        // Adiciona todos os livros do mapa original ao TreeMap
        for (var entry : this.ebooks.entrySet()) {
            livrosOrdenados.put(entry.getValue(), entry.getKey());
        }
        return livrosOrdenados;
    }

    public Map<Livro, String> exibirLivrosOrdenadosPorAutor() {
        // Criar um TreeMap com um comparador que ordena pelo preço
        Map<Livro, String> livrosOrdenados = new TreeMap<>(new ComparatorPorAutor());

        // Adiciona todos os livros do mapa original ao TreeMap
        for (var entry : this.ebooks.entrySet()) {
            livrosOrdenados.put(entry.getValue(), entry.getKey());
        }
        return livrosOrdenados;
    }

    public Map.Entry<String, Livro> obterLivroMaisCaro(){
        Double maisCaro = Double.NEGATIVE_INFINITY;
        Map.Entry<String, Livro> livroMaisCaro = null;

        for (Map.Entry<String, Livro> entry : ebooks.entrySet()){
            if (entry.getValue().getPreco() > maisCaro){
                maisCaro = entry.getValue().getPreco();
                livroMaisCaro = entry;
            }
        }
        return livroMaisCaro;
    }

    public Map.Entry<String, Livro> obterLivroMaisBarato(){
        Map.Entry<String, Livro> livroMaisBarato = null;
        Double maisBarato = Double.POSITIVE_INFINITY;

        for (Map.Entry<String, Livro> entry : ebooks.entrySet()){
            if (entry.getValue().getPreco() < maisBarato){
                maisBarato = entry.getValue().getPreco();
                livroMaisBarato = entry;
            }
        }
        return livroMaisBarato;
    }

    public Map<String, Livro> pesquisarLivrosPorAutor(String autor){
        Map<String, Livro> livrosPorAutor = new LinkedHashMap<>();

        for (var entry : ebooks.entrySet()){
            if (entry.getValue().getAutor().equalsIgnoreCase(autor)){
                livrosPorAutor.put(entry.getKey(), entry.getValue());
            }
        }
        return livrosPorAutor;
    }

    public static void main(String[] args) {
        LivrariaOnline livrariaOnline = new LivrariaOnline();
        // Adiciona os livros à livraria online
        livrariaOnline.adicionarLivro("https://amzn.to/3EclT8Z", "1984", "George Orwell", 50d);
        livrariaOnline.adicionarLivro("https://amzn.to/47Umiun", "A Revolução dos Bichos", "George Orwell", 7.05d);
        livrariaOnline.adicionarLivro("https://amzn.to/3L1FFI6", "Caixa de Pássaros - Bird Box: Não Abra os Olhos", "Josh Malerman", 19.99d);
        livrariaOnline.adicionarLivro("https://amzn.to/3OYb9jk", "Malorie", "Josh Malerman", 5d);
        livrariaOnline.adicionarLivro("https://amzn.to/45HQE1L", "E Não Sobrou Nenhum", "Agatha Christie", 50d);
        livrariaOnline.adicionarLivro("https://amzn.to/45u86q4", "Assassinato no Expresso do Oriente", "Agatha Christie", 5d);
    
        // Exibe todos os livros ordenados por preço
        System.out.println("Livros ordenados por preço: \n" + livrariaOnline.exibirLivrosOrdenadosPorPreco());
    
        //Exibe todos os livros ordenados por autor
        System.out.println("Livros ordenados por autor: \n" + livrariaOnline.exibirLivrosOrdenadosPorAutor());
    
        // Pesquisa livros por autor
        String autorPesquisa = "Josh Malerman";
        livrariaOnline.pesquisarLivrosPorAutor(autorPesquisa);
    
        // Obtém e exibe o livro mais caro
        System.out.println("Livro mais caro: " + livrariaOnline.obterLivroMaisCaro());
    
        // Obtém e exibe o livro mais barato
        System.out.println("Livro mais barato: " + livrariaOnline.obterLivroMaisBarato());
    
        // Remover um livro pelo título
        livrariaOnline.removerLivro("1984");
        System.out.println(livrariaOnline.ebooks);
    
      }
}