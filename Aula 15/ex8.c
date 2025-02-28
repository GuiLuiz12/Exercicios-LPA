#include <stdio.h>

void imprimir_string(char *texto) {
    printf("%s\n\n", texto);
}

int main() {
    imprimir_string("Hello, World!");
    imprimir_string("teste");
    return 0;
}