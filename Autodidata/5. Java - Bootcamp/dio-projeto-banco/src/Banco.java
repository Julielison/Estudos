import java.util.ArrayList;
import java.util.List;

public class Banco {

	private String nome;
	private static List<Conta> contas = new ArrayList<>();

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public static void adicionarConta(Conta c){
		contas.add(c);
	}

	public static void exibirContas(){
		System.out.println("=== Contas criadas ===");
		contas.stream().forEach(System.out::println);
	}



}
