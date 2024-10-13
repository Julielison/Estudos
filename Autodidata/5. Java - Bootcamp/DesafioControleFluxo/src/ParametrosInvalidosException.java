public class ParametrosInvalidosException extends Exception {
    private String mensagem;

    // Construtor que aceita uma mensagem de erro
    public ParametrosInvalidosException(String mensagem) {
        // Atribui a mensagem fornecida ao campo mensagem
        this.mensagem = mensagem;
    }

    // Sobrescreve o método getMessage() para retornar a mensagem personalizada
    @Override
    public String getMessage() {
        return mensagem;
    }
}