#include <stdio.h>
#include <stdlib.h>

int main() {
    int** matriz = (int**) malloc(10 * sizeof(int*));
    if(matriz == NULL) {
        printf("Erro na alocação das linhas\n");
        return 1;
    }

    for(int i = 0; i < 10; i++) {
        matriz[i] = (int*) malloc(10 * sizeof(int));
        if(matriz[i] == NULL) {
            printf("Erro na alocação das colunas\n");
            return 1;
        }
    }

    int valor = 100;
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            matriz[i][j] = valor--;
        }
    }

    printf("Matriz 10x10 (ordem inversa):\n");
    for(int i = 9; i >= 0; i--) {
        for(int j = 9; j >= 0; j--) {
            printf("%3d ", matriz[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < 10; i++) {
        free(matriz[i]);
    }
    free(matriz);
    
    return 0;
}