#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Função para escrever parâmetros em um arquivo
static int escrever_parametros(const char *nome_arquivo, const char **params, size_t num_params) {
    FILE *arquivo;
    
    // Tentativa de abrir o arquivo em modo escrita
    arquivo = fopen(nome_arquivo, "w");
    if (arquivo == NULL) {
        fprintf(stderr, "Erro ao abrir arquivo '%s': %s\n", 
                nome_arquivo, strerror(errno));
        return 0;
    }

    // Escreve cada parâmetro em uma linha separada
    for (size_t i = 0; i < num_params; i++) {
        if (fprintf(arquivo, "%s\n", params[i]) < 0) {
            fprintf(stderr, "Erro ao escrever no arquivo\n");
            fclose(arquivo);
            return 0;
        }
    }

    fclose(arquivo);
    printf("Parâmetros escritos com sucesso no arquivo '%s'\n", nome_arquivo);
    return 1;
}

int main(int argc, char *argv[]) {
    int i;
    
    // Verificação de argumentos mínimos necessários
    if (argc < 3) {
        fprintf(stderr, "Uso: %s <nome_arquivo> <parametro1> [parametro2 ...]\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Chamada da função principal com os parâmetros fornecidos
    const char **params = &argv[2];
    size_t num_params = argc - 2;

    return !escrever_parametros(argv[1], params, num_params);
}