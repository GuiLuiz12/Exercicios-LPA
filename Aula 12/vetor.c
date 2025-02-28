#include <stdio.h>
#include <stdlib.h>

int main() {

    int* vetor = (int*) malloc(10 * sizeof(int));

    if(vetor == NULL) {
        printf("Erro na alocação de memória\n");
        return 1;
    }

    int valor = 11;
    for(int i = 0; i < 10; i++) {
        *(vetor + i) = valor++;
    }

    printf("Vetor: ");
    for(int i = 0; i < 10; i++) {
        printf("%d ", *(vetor + i));
    }
    printf("\n");

    free(vetor);
    
    return 0;
}