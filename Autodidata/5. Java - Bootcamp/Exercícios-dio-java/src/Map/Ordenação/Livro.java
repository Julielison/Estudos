package Map.Ordenação;

import java.util.Comparator;

public class Livro {
    private String titulo;
    private String autor;
    private Double preco;
    
    public Livro(String titulo, String autor, Double preco) {
        this.titulo = titulo;
        this.autor = autor;
        this.preco = preco;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public Double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return "\n" + titulo + " - " + autor + " - " + preco + ", ";
    }
}

class ComparatorPorPreco implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        // Comparar por preço
        int priceComparison = l1.getPreco().compareTo(l2.getPreco());
        if (priceComparison != 0) {
            return priceComparison;
        }
        // Se os preços forem iguais, comparar por título para garantir unicidade
        return l1.getTitulo().compareTo(l2.getTitulo());
    }
}

class ComparatorPorAutor implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        // Comparar por preço
        int priceComparison = l1.getAutor().compareTo(l2.getAutor());
        if (priceComparison != 0) {
            return priceComparison;
        }
        // Se os preços forem iguais, comparar por título para garantir unicidade
        return l1.getTitulo().compareTo(l2.getTitulo());
    }
}