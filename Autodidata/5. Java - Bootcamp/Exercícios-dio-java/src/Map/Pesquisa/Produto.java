package Map.Pesquisa;

public class Produto {
    private String nome;
    private int qtd;
    private double preco;

    public Produto(String nome, int qtd, double preco) {
        this.nome = nome;
        this.qtd = qtd;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public int getQtd() {
        return qtd;
    }

    public double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return "Produto [nome=" + nome + ", qtd=" + qtd + ", preco=" + preco + "]";
    }

    
}
