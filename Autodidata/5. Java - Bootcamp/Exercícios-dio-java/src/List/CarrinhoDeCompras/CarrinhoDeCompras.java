package List.CarrinhoDeCompras;

import java.util.ArrayList;
import java.util.List;

public class CarrinhoDeCompras {
    private List<Item> listaDeIntens;

    public CarrinhoDeCompras() {
        this.listaDeIntens = new ArrayList<>();
    }

    public void adicionarItem(String nome, double preco, int quantidade){
        this.listaDeIntens.add(new Item(nome, preco, quantidade));
    }

    public void removerItem(String nome){
        List<Item> remover = new ArrayList<>();
        for (Item item : this.listaDeIntens){
            if (item.getNome().equalsIgnoreCase(nome)){
                remover.add(item);
            }
        }
        listaDeIntens.removeAll(remover);
    }

    public double calcularValorTotal(){
        double valorTotal = 0d;
        for (Item intem : listaDeIntens){
            valorTotal += intem.getPreco() * intem.getQuantidade();
        }
        return valorTotal;
    }

    public void exibirItens(){
        System.out.println(listaDeIntens);
    }

    public static void main(String[] args) {
        // Criando uma instância do carrinho de compras
        CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();

        // Adicionando itens ao carrinho
        carrinhoDeCompras.adicionarItem("Lápis", 2.5, 3);
        carrinhoDeCompras.adicionarItem("Lápis", 2.5, 3);
        carrinhoDeCompras.adicionarItem("Caderno", 35.3, 1);
        carrinhoDeCompras.adicionarItem("Borracha", 2.1, 2);

        // Exibindo os itens no carrinho
        carrinhoDeCompras.exibirItens();

        // Removendo um item do carrinho
        carrinhoDeCompras.removerItem("Lápis");

        // Exibindo os itens atualizados no carrinho
        carrinhoDeCompras.exibirItens();

        // Calculando e exibindo o valor total da compra
        System.out.println("O valor total da compra é = " + carrinhoDeCompras.calcularValorTotal());
    }
}