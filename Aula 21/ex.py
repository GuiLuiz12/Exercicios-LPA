import os
from pathlib import Path
import argparse
from typing import Optional

def criar_diretorio(nome_dir: str) -> None:
    """
    Cria um novo diretório com tratamento de erros.
    
    Args:
        nome_dir: Nome do diretório a ser criado
        
    Raises:
        OSError: Se ocorrer erro na criação do diretório
    """
    try:
        os.mkdir(nome_dir)
        print(f"Diretório '{nome_dir}' criado com sucesso")
    except FileExistsError:
        print(f"Erro: O diretório '{nome_dir}' já existe")
    except PermissionError:
        print(f"Erro: Permissão negada para criar o diretório '{nome_dir}'")
    except OSError as e:
        print(f"Erro ao criar diretório '{nome_dir}': {str(e)}")

def listar_diretorio() -> None:
    """
    Lista o conteúdo do diretório atual.
    
    Raises:
        OSError: Se ocorrer erro ao acessar o diretório
    """
    try:
        # Usando Path para uma abordagem mais moderna e segura
        diretorio_atual = Path(".")
        
        print("Conteúdo do diretório atual:")
        for item in diretorio_atual.iterdir():
            print(item.name)
    except OSError as e:
        print(f"Erro ao listar diretório: {str(e)}")

def main() -> None:
    """Função principal que processa argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Programa para gerenciar diretórios",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "-c", "--criar",
        help="Criar um novo diretório",
        metavar="NOME_DIR"
    )
    parser.add_argument(
        "-l", "--listar",
        action="store_true",
        help="Listar conteúdo do diretório atual"
    )
    
    args = parser.parse_args()
    
    # Processamento dos argumentos
    if args.criar:
        criar_diretorio(args.criar)
    elif args.listar:
        listar_diretorio()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()