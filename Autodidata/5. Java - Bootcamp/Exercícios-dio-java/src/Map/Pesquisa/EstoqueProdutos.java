package Map.Pesquisa;

// ok
import java.util.HashMap;
import java.util.Map;

public class EstoqueProdutos {
    private Map<Long, Produto> produtos;

    public EstoqueProdutos() {
        produtos = new HashMap<>();
    }

    public void adicionarProduto(long cod, String nome, int quantidade, double preco){
        produtos.put(cod, new Produto(nome, quantidade, preco));
    }

    public void exibirProdutos(){
        System.out.println(produtos);
    }

    public double calcularValorTotalEstoque(){
        double valorEstoque = 0;

        for (Produto produto : produtos.values()){
            valorEstoque += produto.getPreco() * produto.getQtd();
        }
        return valorEstoque;
    }

    public Produto obterProdutoMaisCaro(){
        Produto maisCaro = new Produto(null, 0, 0);
        
        for (Produto produto : produtos.values()){
            if (produto.getPreco() > maisCaro.getPreco()){
                maisCaro = produto;
            }
        }
        return maisCaro;
    }

    public Produto obterProdutoMaisBarato(){
        Produto maisBarato = new Produto(null, 0, 999999999);
        for (Produto produto : produtos.values()){
            if (produto.getPreco() < maisBarato.getPreco()){
                maisBarato = produto;
            }
        }
        return maisBarato;
    }
    
    public Produto obterProdutoMaiorQuantidadeValorTotalNoEstoque(){
        Produto maiorTotal = new Produto(null, 0, 0);

        for (Produto produto : produtos.values()){
            if (produto.getPreco() * produto.getQtd() > maiorTotal.getPreco() * maiorTotal.getQtd()){
                maiorTotal = produto;
            }
        }
        return maiorTotal;
    }

    public static void main(String[] args) {
        EstoqueProdutos estoque = new EstoqueProdutos();
    
        // Exibe o estoque vazio
        estoque.exibirProdutos();
    
        // Adiciona produtos ao estoque
        estoque.adicionarProduto(1L, "Notebook", 1, 1500.0);
        estoque.adicionarProduto(2L, "Mouse", 5, 25.0);
        estoque.adicionarProduto(3L, "Monitor", 10, 400.0);
        estoque.adicionarProduto(4L, "Teclado", 2, 40.0);
    
        // Exibe os produtos no estoque
        estoque.exibirProdutos();
    
        // Calcula e exibe o valor total do estoque
        System.out.println("Valor total do estoque: R$" + estoque.calcularValorTotalEstoque());
    
        // Obtém e exibe o produto mais caro
        Produto produtoMaisCaro = estoque.obterProdutoMaisCaro();
        System.out.println("Produto mais caro: " + produtoMaisCaro);
    
        // Obtém e exibe o produto mais barato
        Produto produtoMaisBarato = estoque.obterProdutoMaisBarato();
        System.out.println("Produto mais barato: " + produtoMaisBarato);
    
        // Obtém e exibe o produto com a maior quantidade em valor no estoque
        Produto produtoMaiorQuantidadeValorTotal = estoque.obterProdutoMaiorQuantidadeValorTotalNoEstoque();
        System.out.println("Produto com maior quantidade em valor no estoque: " + produtoMaiorQuantidadeValorTotal);
      }
}
