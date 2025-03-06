#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

// Função para ler o número esperado do arquivo de configuração
static int ler_numero_config(const char *nome_arquivo) {
    FILE *arquivo;
    char linha[100];
    int numero;
    
    // Tentativa de abrir o arquivo de configuração
    arquivo = fopen(nome_arquivo, "r");
    if (arquivo == NULL) {
        fprintf(stderr, "Erro ao abrir arquivo '%s': %s\n", 
                nome_arquivo, strerror(errno));
        return -1;
    }

    // Leitura da primeira linha do arquivo
    if (fgets(linha, sizeof(linha), arquivo) == NULL) {
        fprintf(stderr, "Erro ao ler arquivo '%s'\n", nome_arquivo);
        fclose(arquivo);
        return -1;
    }

    // Fechamento do arquivo após leitura
    fclose(arquivo);

    // Verificação se começa com "num="
    if (strncmp(linha, "num=", 4) != 0) {
        fprintf(stderr, "Formato inválido no arquivo. Deve começar com 'num='\n");
        return -1;
    }

    // Converte o resto da linha para número
    char *ptr = &linha[4];
    numero = atoi(ptr);
    
    // Validação do número
    if (numero <= 0) {
        fprintf(stderr, "Número deve ser positivo\n");
        return -1;
    }

    printf("Número esperado de parâmetros: %d\n", numero);
    return numero;
}

int main(int argc, char *argv[]) {
    int num_esperado;

    // Verifica se tem argumentos suficientes (nome do programa + config.txt)
    if (argc < 2) {
        fprintf(stderr, "Uso: %s config.txt [parametros...]\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Lê o número esperado do arquivo de configuração
    num_esperado = ler_numero_config(argv[1]);
    if (num_esperado == -1) {
        return EXIT_FAILURE;
    }

    // Remove o nome do programa e o arquivo de config dos argumentos
    argc -= 2;
    argv += 2;

    // Verifica se o número de parâmetros corresponde ao esperado
    if (argc != num_esperado) {
        fprintf(stderr, "Erro: Esperava %d parâmetros, mas recebeu %d\n", 
                num_esperado, argc);
        return EXIT_FAILURE;
    }

    // Mostra os parâmetros recebidos
    printf("Parâmetros recebidos:\n");
    for (int i = 0; i < argc; i++) {
        printf("Parametro %d: %s\n", i + 1, argv[i]);
    }

    return EXIT_SUCCESS;
}