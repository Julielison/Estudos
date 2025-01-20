package dio.dio_spring_security.config;

import java.util.HashSet;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import dio.dio_spring_security.model.User;
import dio.dio_spring_security.repository.UserRepository;

@Service
public class SecurityDatabaseService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    // Método sobrescrito para carregar informações do usuário pelo nome de usuário
    @Override
    public UserDetails loadUserByUsername(String username) {
        // Busca o usuário no banco de dados pelo nome de usuário
        User userEntity = userRepository.findByUsername(username);

        // Se o usuário não for encontrado, lança uma exceção
        if (userEntity == null) {
            throw new UsernameNotFoundException(username);
        }

        // Cria um conjunto para armazenar as autoridades (roles) do usuário
        Set<GrantedAuthority> authorities = new HashSet<>();

        // Itera sobre as roles do usuário e adiciona cada uma ao conjunto de autoridades
        userEntity.getRoles().forEach(role -> {
            authorities.add(new SimpleGrantedAuthority("ROLE_" + role));
        });

        // Cria um objeto UserDetails com as informações do usuário e suas autoridades
        UserDetails user = new org.springframework.security.core.userdetails.User(
            userEntity.getUsername(), // Nome de usuário
            userEntity.getPassword(), // Senha
            authorities // Autoridades
        );

        // Retorna o objeto UserDetails
        return user;
    }
}
