#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> vetor = {"AM", "CE", "PB", "RN", "PA", "RR", "DF", "AC", "AP", "RO", "MA", "TO", "GO", "MS", "SP", "PR", "SC", "RS", "MG", "RJ", "ES", "BA", "SE", "AL", "PE", "PI", "MT"};
    std::vector<int> voto(27, 0);
    std::vector<std::string> maxv(1, "-");

    while (true) {
        std::string sigla;
        std::cout << "Digite a sigla de um estado: ";
        std::cin >> sigla;
        for (char& c : sigla) {
            c = toupper(c);
        }

        if (std::find(vetor.begin(), vetor.end(), sigla) == vetor.end()) {
            break;
        }

        voto[std::distance(vetor.begin(), std::find(vetor.begin(), vetor.end(), sigla))] += 1;
    }

    int maior = 0;
    maxv[0] = "-";
    for (const std::string& i : vetor) {
        if (voto[std::distance(vetor.begin(), std::find(vetor.begin(), vetor.end(), i))] > maior) {
            maxv.clear();
            maior = voto[std::distance(vetor.begin(), std::find(vetor.begin(), vetor.end(), i))];
            maxv.push_back(i);
        } else if (voto[std::distance(vetor.begin(), std::find(vetor.begin(), vetor.end(), i))] == maior) {
            maxv.push_back(i);
        }
    }

    std::cout << "Estado(s) mais votado(s): ";
    for (const std::string& estado : maxv) {
        std::cout << estado << " ";
    }
    std::cout << std::endl;

    return 0;
}
