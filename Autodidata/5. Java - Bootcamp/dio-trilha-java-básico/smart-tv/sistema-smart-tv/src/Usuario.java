
// Ela tenha as características: ligada (boolean), canal (int) e volume (int);

// Nossa TV poderá ligar e desligar e assim mudar o estado ligada;

// Nossa TV aumentará e diminuirá o volume sempre em +1 ou -1;

// Nossa TV poderá mudar de canal de 1 em 1 ou definindo o número correspondente

public class Usuario {
    public static void main(String[] args) throws Exception {
    SmartTV smartTV = new SmartTV();

    System.out.println(smartTV.estado);
    System.out.println(smartTV.canal);
    System.out.println(smartTV.volume);
    
    smartTV.mudarEstado();
    
    System.out.println(smartTV.estado);
    }

}
