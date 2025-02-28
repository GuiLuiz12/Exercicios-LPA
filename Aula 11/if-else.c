#include <stdio.h>

int main() {
    // if simples
    int numero = 5;
    if(numero > 10) {
        printf("%d é maior que 10\n", numero);
    }
    printf("Fim da verificação simples\n");

    // if-else
    int idade = 15;
    if(idade >= 18) {
        printf("A pessoa com %d anos é maior de idade\n", idade);
    } else {
        printf("A pessoa com %d anos é menor de idade\n", idade);
    }

    return 0;
}