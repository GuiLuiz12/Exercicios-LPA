#include <stdio.h>
#include <math.h>

float circCirculo(int raio) {
    return 2 * 3.14159 * raio;
}

int main() {
    printf("Circunferência com raio 5: %.2f\n", circCirculo(5));
    printf("Circunferência com raio 10: %.2f\n", circCirculo(10));
    printf("Circunferência com raio 15: %.2f\n", circCirculo(15));
    return 0;
}