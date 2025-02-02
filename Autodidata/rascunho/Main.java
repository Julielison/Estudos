public class Main {
    static int x = 0;
    
    public static void main(String[] args) {
        Main obj = new Main();
        obj.x = 12;
        System.out.println(obj.x);
        System.out.println(Main.x);
}
}