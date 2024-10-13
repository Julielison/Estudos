#include <iostream>
#include <algorithm>
using namespace std;

long int livros[100100];

int main() {
    long int i, j, n, tempo, resposta, soma;
    while (cin >> n >> tempo) {
        for (i = 0; i < n; i++) {
            cin >> livros[i];
        }
        
        j = -1;
        soma = 0;
        resposta = 0;

        for (i = 0; i < n; i++) {
            if (soma + livros[i] <= tempo)
                soma += livros[i];
            else {
                soma += livros[i];
                while (soma > tempo) {
                    j++;
                    soma -= livros[j];
                }
            }
            resposta = max(resposta, i - j);
        }
        cout << resposta << endl;
    }
    return 0;
}
