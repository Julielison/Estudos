package Set.PesquisaEmSet;

import java.util.HashSet;
import java.util.Set;

public class ListaTarefas {
    private Set<Tarefa> tarefasSet;

    public ListaTarefas() {
        this.tarefasSet = new HashSet<>();
    }
    
    public void adicionarTarefa(String descricao){
        tarefasSet.add(new Tarefa(descricao, false));
    }

    public void removerTarefa(String descricao){
        Tarefa tarefaRemover = null;
        for (Tarefa t : tarefasSet){
            if (t.getDescricao().equalsIgnoreCase(descricao)){
                tarefaRemover = t;
                break;
            }
        }
        if (tarefaRemover.equals(null)){
            System.out.println("Tarefa não existe");
        } else {
            tarefasSet.remove(tarefaRemover);
        }
    }

    public void exibirTarefas(){
        System.out.println(tarefasSet);
    }

    public int contarTarefas(){
        return tarefasSet.size();
    }

    public Set<Tarefa> obterTarefasConcluidas(){
        Set<Tarefa> concluidas = new HashSet<>();
        
        for (Tarefa t : tarefasSet) {
            if (t.isStatus() == true)
                concluidas.add(t);
        }
        return concluidas;
    }

    public Set<Tarefa> obterTarefasPendentes(){
        Set<Tarefa> pendentes = new HashSet<>();
        
        for (Tarefa t : tarefasSet) {
            if (t.isStatus() == false)
                pendentes.add(t);
        }
        return pendentes;
    }

    public void marcarTarefaConcluida(String descricao){
        for (Tarefa t : tarefasSet){
            if (t.getDescricao().equalsIgnoreCase(descricao)){
                t.setStatus(true);
                break;
            }
        }
    }

    public void marcarTarefaPendente(String descricao){
        for (Tarefa t : tarefasSet){
            if (t.getDescricao().equalsIgnoreCase(descricao))
                t.setStatus(false);
                break;
        }
    }

    public void limparListaTarefas(){
        tarefasSet.clear();
    }

    public static void main(String[] args) {
        // Criando uma instância da classe ListaTarefas
        ListaTarefas listaTarefas = new ListaTarefas();
    
        // Adicionando tarefas à lista
        listaTarefas.adicionarTarefa("Estudar Java");
        listaTarefas.adicionarTarefa("Fazer exercícios físicos");
        listaTarefas.adicionarTarefa("Organizar a mesa de trabalho");
        listaTarefas.adicionarTarefa("Ler livro");
        listaTarefas.adicionarTarefa("Preparar apresentação");
    
        // Exibindo as tarefas na lista
        listaTarefas.exibirTarefas();
    
        // Removendo uma tarefa
        listaTarefas.removerTarefa("Fazer exercícios físicos");
        listaTarefas.exibirTarefas();
    
        // Contando o número de tarefas na lista
        System.out.println("Total de tarefas na lista: " + listaTarefas.contarTarefas());
    
        // Obtendo tarefas pendentes
        System.out.println(listaTarefas.obterTarefasPendentes());
    
        // Marcando tarefas como concluídas
        listaTarefas.marcarTarefaConcluida("Ler livro");
        listaTarefas.marcarTarefaConcluida("Estudar Java");
    
        // Obtendo tarefas concluídas
        System.out.println(listaTarefas.obterTarefasConcluidas());
    
        // Marcando tarefas como pendentes
        listaTarefas.marcarTarefaPendente("Estudar Java");
        listaTarefas.exibirTarefas();
    
        // Limpando a lista de tarefas
        listaTarefas.limparListaTarefas();
        listaTarefas.exibirTarefas();
      }
}
