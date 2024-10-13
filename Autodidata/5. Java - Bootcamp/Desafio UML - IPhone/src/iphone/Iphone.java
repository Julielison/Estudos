package iphone;

import interfaces.AparelhoTelefonico;
import interfaces.NavegadorDeInternet;
import interfaces.ReprodutorMusical;

public class Iphone implements ReprodutorMusical, AparelhoTelefonico, NavegadorDeInternet {
    public void adicionarNovaAba(){
        System.out.println("Adicionando nova aba");
    }

    public void exibirPagina() {
        System.out.println("Exibindo página");
    }

    public void atualizarPagina() {
        System.out.println("Atualizando página");
    }
    
    public void ligar() {
        System.out.println("Ligando...");
    }
    
    public void atender() {
        System.out.println("Atendido");
    }

    public void iniciarCorreioVoz() {
        System.out.println("Iniciando correio de voz");
    }
    
    public void tocar() {
        System.out.println("Tocando...");
    }
    
    public void pausar() {
        System.out.println("Música pausada");
    }
    
    public void selecionarMusica() {
        System.out.println("Música selecionada");
    }
}
