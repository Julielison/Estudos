package Map.Ordenação;

public class Evento {
    private String nome, atração;

    public Evento(String nome, String atração) {
        this.nome = nome;
        this.atração = atração;
    }

    public String getNome() {
        return nome;
    }

    public String getAtração() {
        return atração;
    }

    @Override
    public String toString() {
        return nome + " - " + atração;
    }

    
}
