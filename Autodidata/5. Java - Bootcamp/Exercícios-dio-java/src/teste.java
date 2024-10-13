import java.util.Optional;

public class teste {
    public static void main(String[] args) {
        Optional<String> optionalValue = Optional.ofNullable("oi");
        String result = optionalValue.orElse("Default"); 
        System.out.println(result);
    }
}
