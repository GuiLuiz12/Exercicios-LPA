#include <stdio.h>

int main() {

    int numeros[100];

    for(int i = 0; i < 100; i++) {
        numeros[i] = i + 1;
    }

    printf("Números em ordem normal:\n");
    for(int i = 0; i < 100; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    printf("Números em ordem inversa:\n");
    for(int i = 99; i >= 0; i--) {
        printf("%d ", numeros[i]);
    }
    printf("\n");
    
    return 0;
}