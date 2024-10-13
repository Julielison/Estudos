
public class Main {

	public static void main(String[] args) {
		Cliente venilton = new Cliente();
		venilton.setNome("Venilton");
		
		Conta cc = new ContaCorrente(venilton);
		Conta poupanca = new ContaPoupanca(venilton);

		cc.depositar(100);
		cc.transferir(100, poupanca);

		Cliente francisco = new Cliente();
		francisco.setNome("Francisco");

		Conta cc2 = new ContaCorrente(francisco);
		Conta poupanca2 = new ContaPoupanca(francisco);

		poupanca.transferir(50, poupanca2);
		
		cc.imprimirExtrato();
		cc2.imprimirExtrato();
		poupanca.imprimirExtrato();
		poupanca2.imprimirExtrato();

		Banco.exibirContas();
	}

}
