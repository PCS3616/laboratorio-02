#include <stdio.h>

int fatorial(int n);

/**
* Ponto de entrada do programa (entry point).
*/
  int main(int argc, char** argv) {
  int n;
  scanf("%d", &n);

  printf("%dn", fatorial(n));

  return 0;
}

/**
* Calcula o fatorial do número recebido e retorna o resultado.
*/
int fatorial(int n) {
  // Por enquanto, essa função não faz nada de muito útil... Ela apenas
  // retorna o número recebido.
  // Altere esta implementação para retornar o resultado correto.
  return n;
}
