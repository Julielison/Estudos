import java.util.Scanner;

abstract class Cofre {
  protected String tipo;
  protected String metodoAbertura;

  public Cofre(String tipo, String metodoAbertura) {
    this.tipo = tipo;
    this.metodoAbertura = metodoAbertura;
  }

  public void imprimirInformacoes() {
    System.out.println("Tipo: " + this.tipo);
    System.out.println("Metodo de abertura: " + this.metodoAbertura);
  }
}

class CofreDigital extends Cofre {

  private int senha;

  public CofreDigital(int senha) {
    super("Cofre Digital", "Senha");
    this.senha = senha;
}

public boolean validarSenha(int confirmacaoSenha) {
    return confirmacaoSenha == this.senha;
}
}

class CofreFisico extends Cofre {
    
    public CofreFisico() {
        super("Cofre Fisico", "Chave");
        imprimirInformacoes();
  }

}

public class Desafio {
    public static void main(String[] args) {
    // Lê o tipo de cofre (primeira linha da entrada)
    Scanner scanner = new Scanner(System.in);
    String tipoCofre = scanner.nextLine();

    if (tipoCofre.equalsIgnoreCase("digital")) {
        Integer senha = scanner.nextInt();
        CofreDigital digital = new CofreDigital(senha);
        digital.imprimirInformacoes();
        
        Integer senhaConfirmacao = scanner.nextInt();
        if (!digital.validarSenha(senhaConfirmacao))
            System.out.println("Senha incorreta!");
        else 
            System.out.println("Cofre aberto!");

    } else new CofreFisico();
    scanner.close();
    }
}