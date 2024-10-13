package Set.OrdenaçãoSet;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class CadastroProdutos {
    Set<Produto> produtosSet;

    public CadastroProdutos() {
        this.produtosSet = new HashSet<>();
    }

    public void adicionarProduto(long cod, String nome, double preco, int quantidade){
        produtosSet.add(new Produto(nome, cod, preco, quantidade));
    }

    public Set<Produto> exibirProdutosPorNome(){
        Set<Produto> ordenadoPorNome = new TreeSet<>(new CompararNome());
        ordenadoPorNome.addAll(produtosSet);
        return ordenadoPorNome;
    }

    public Set<Produto> exibirProdutosPorPreco(){
        Set<Produto> ordenadoPorPreco = new TreeSet<>(new CompararPreco());
        ordenadoPorPreco.addAll(produtosSet);
        return ordenadoPorPreco;
    }

    public void exibir(){
        System.err.println(produtosSet);
    }

    public static void main(String[] args) {
        // Criando uma instância do CadastroProdutos
        CadastroProdutos cadastroProdutos = new CadastroProdutos();
    
        // Adicionando produtos ao cadastro
        cadastroProdutos.adicionarProduto(1L, "Smartphone", 1000d, 10);
        cadastroProdutos.adicionarProduto(2L, "Notebook", 1500d, 5);
        cadastroProdutos.adicionarProduto(1L, "Mouse", 30d, 20);
        cadastroProdutos.adicionarProduto(4L, "Teclado", 50d, 15);
    
        // Exibindo todos os produtos no cadastro
        cadastroProdutos.exibir();

        System.out.println(cadastroProdutos);

        // Exibindo produtos ordenados por nome
        System.out.println(cadastroProdutos.exibirProdutosPorNome());
    
        // Exibindo produtos ordenados por preço
        System.out.println(cadastroProdutos.exibirProdutosPorPreco());
      }
}
