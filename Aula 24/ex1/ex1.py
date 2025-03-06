import argparse
from typing import List, Optional

def escrever_parametros(nome_arquivo: str, params: List[str]) -> None:
    """
    Escreve uma lista de parâmetros em um arquivo, cada um em sua própria linha.
    
    Args:
        nome_arquivo: Nome do arquivo onde os parâmetros serão escritos
        params: Lista de strings contendo os parâmetros
        
    Raises:
        IOError: Se ocorrer erro ao abrir ou escrever no arquivo
    """
    try:
        # Usando 'with' para garantir que o arquivo seja fechado corretamente
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # Escrevemos cada parâmetro seguido por uma nova linha
            for param in params:
                arquivo.write(f"{param}\n")
        print(f"Parâmetros escritos com sucesso no arquivo '{nome_arquivo}'")
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {str(e)}")

def main() -> None:
    """Função principal que processa os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Programa para gravar parâmetros em um arquivo",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "arquivo",
        help="Nome do arquivo onde os parâmetros serão gravados"
    )
    
    parser.add_argument(
        "params",
        nargs="+",
        help="Lista de parâmetros a serem gravados"
    )
    
    args = parser.parse_args()
    escrever_parametros(args.arquivo, args.params)

if __name__ == "__main__":
    main()