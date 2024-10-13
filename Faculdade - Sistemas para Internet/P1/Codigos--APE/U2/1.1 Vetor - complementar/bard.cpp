#include <iostream>
#include <string>

using namespace std;

int main() {
  // Declara um vetor de 27 strings para armazenar as siglas dos estados
  string estados[27] = {
    "AM", "CE", "PB", "RN", "PA", "RR", "DF", "AC", "AP", "RO",
    "MA", "TO", "GO", "MS", "SP", "PR", "SC", "RS", "MG", "RJ",
    "ES", "BA", "SE", "AL", "PE", "PI", "MT"
  };

  // Declara um vetor de 27 inteiros para armazenar os votos de cada estado
  int votos[27] = {0};

  // Declara um vetor de strings para armazenar os estados mais votados
  string estadosMaisVotados[27] = {"-"};

  // Loop para coletar os votos
  while (true) {
    // Solicita a sigla de um estado
    string sigla;
    cout << "Digite a sigla de um estado: ";
    cin >> sigla;

    // Converte a sigla para maiúsculas
    sigla = sigla.toUpperCase();

    // Verifica se a sigla é válida
    bool siglaValida = false;
    for (int i = 0; i < 27; i++) {
      if (sigla == estados[i]) {
        siglaValida = true;
        break;
      }
    }

    // Se a sigla não for válida, termina o loop
    if (!siglaValida) {
      break;
    }

    // Incrementa o número de votos do estado correspondente
    votos[estados.indexOf(sigla)]++;
  }

  // Declara uma variável para armazenar o maior número de votos
  int maiorNumeroVotos = 0;

  // Loop para encontrar o estado com o maior número de votos
  for (int i = 0; i < 27; i++) {
    if (votos[i] > maiorNumeroVotos) {
      maiorNumeroVotos = votos[i];
    }
  }

  // Limpa o vetor de estados mais votados
  for (int i = 0; i < 27; i++) {
    estadosMaisVotados[i] = "-";
  }

  // Loop para adicionar os estados mais votados ao vetor
  for (int i = 0; i < 27; i++) {
    if (votos[i] == maiorNumeroVotos) {
      estadosMaisVotados[i] = estados[i];
    }
  }

  // Imprime o estado mais votado
  cout << "Estado mais votado: " << estados[votos.indexOf(max(votos))] << endl;

  // Imprime os estados mais votados
  for (int i = 0; i < 27; i++) {
    if (estadosMaisVotados[i] != "-") {
      cout << "Estado mais votado (empate): " << estadosMaisVotados[i] << endl;
    }
  }

  return 0;
}
