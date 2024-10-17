import java.util.Locale;
import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) throws Exception {
        // Criando um objeto Scanner para ler dados do console e configurando para usar o padrão de localidade US (ponto como separador decimal)
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        
        // Solicitando e lendo o número da conta do usuário
        System.out.println("Digite o número da Conta:");
        int numero = scanner.nextInt();
        
        // Solicitando e lendo o número da agência do usuário
        System.out.println("Digite o número da Agência:");
        String agencia = scanner.next();
        
        // Criando um novo objeto Scanner para ler o nome do cliente do console e configurando para usar o padrão de localidade US
        Scanner scanner2 = new Scanner(System.in).useLocale(Locale.US);

        // Solicitando e lendo o nome do cliente do usuário
        System.out.println("Digite seu nome:");
        String nomeCliente = scanner2.nextLine();
        
        // Solicitando e lendo o saldo do usuário
        System.out.println("Digite seu saldo:");
        double saldo = scanner.nextDouble();

        // Exibindo uma mensagem de boas-vindas ao cliente com os dados fornecidos
        System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agência é " + agencia + ", conta " + numero + " e seu saldo " + saldo + " já está disponível para saque");
        
        // Fechando os objetos Scanner para liberar os recursos
        scanner.close();
        scanner2.close();
    }
}
