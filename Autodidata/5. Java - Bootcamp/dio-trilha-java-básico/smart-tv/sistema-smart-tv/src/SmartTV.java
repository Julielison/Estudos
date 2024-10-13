public class SmartTV {
    boolean estado = false;
    int canal = 1;
    int volume = 20;

    public void mudarEstado(){
        this.estado = !this.estado;
    }

    public void aumentarVolume(){
        this.volume++;
    }

    public void diminuirVolume(){
        this.volume++;
    }

    public void mudarCanal(int canal){
        this.canal = canal;
    }

    public void aumentarCanal(){
        this.canal++;
    }

}
