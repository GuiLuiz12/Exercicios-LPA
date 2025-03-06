#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <errno.h>

// Função para criar um diretório
static int criar_diretorio(const char *nome_dir) {
    // Tentativa de criar o diretório
    if (mkdir(nome_dir, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH) == -1) {
        fprintf(stderr, "Erro ao criar diretório '%s': %s\n", 
                nome_dir, strerror(errno));
        return 0;
    }
    printf("Diretório '%s' criado com sucesso\n", nome_dir);
    return 1;
}

// Função para listar conteúdo do diretório atual
static void listar_diretorio(void) {
    DIR *dir;
    struct dirent *ent;

    // Tentativa de abrir o diretório atual
    dir = opendir(".");
    if (dir == NULL) {
        fprintf(stderr, "Erro ao abrir diretório atual: %s\n", 
                strerror(errno));
        return;
    }

    printf("Conteúdo do diretório atual:\n");
    
    // Iteração sobre os itens do diretório
    while ((ent = readdir(dir)) != NULL) {
        printf("%s\n", ent->d_name);
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    int i;
    
    // Verificação se há argumentos suficientes
    if (argc < 2) {
        fprintf(stderr, "Uso: %s [-c nome_dir] [-l]\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Processamento dos argumentos
    for (i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            criar_diretorio(argv[++i]);
        } else if (strcmp(argv[i], "-l") == 0) {
            listar_diretorio();
        }
    }

    return EXIT_SUCCESS;
}