#include <stdio.h>
#include <string.h>

int main() {

    char texto[20] = "Cyber SENAI 2025";

    char senai[6];

    strncpy(senai, texto + 6, 5);
    senai[5] = '\0';

    printf("Texto original: %s\n", texto);
    printf("String extraída: %s\n", senai);
    
    return 0;
}