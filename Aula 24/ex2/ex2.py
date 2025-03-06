import argparse
from typing import Optional

def ler_numero_config(nome_arquivo: str) -> Optional[int]:
    """
    Lê o arquivo de configuração e retorna o número esperado de parâmetros.
    
    Args:
        nome_arquivo: Nome do arquivo de configuração
        
    Returns:
        int ou None: Número esperado de parâmetros, ou None em caso de erro
        
    Raises:
        IOError: Se ocorrer erro na leitura do arquivo
        ValueError: Se o formato do arquivo estiver incorreto
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readline().strip()
            
            # Verifica formato correto
            if not linha.startswith('num='):
                print(f"Formato inválido no arquivo. Deve começar com 'num='")
                return None
                
            # Extrai o número
            numero = int(linha[4:])
            
            # Valida o número
            if numero <= 0:
                print("Número deve ser positivo")
                return None
                
            print(f"Número esperado de parâmetros: {numero}")
            return numero
            
    except IOError as e:
        print(f"Erro ao ler arquivo: {str(e)}")
        return None
    except ValueError:
        print("Formato inválido: número não é um inteiro válido")
        return None

def main() -> None:
    """Função principal que processa os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Programa que valida número de parâmetros com base em config.txt",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "config",
        help="Nome do arquivo de configuração"
    )
    
    parser.add_argument(
        "params",
        nargs="*",
        help="Lista de parâmetros a serem validados"
    )
    
    args = parser.parse_args()
    
    # Lê o número esperado do arquivo de configuração
    num_esperado = ler_numero_config(args.config)
    if num_esperado is None:
        return
        
    # Verifica quantidade de parâmetros
    if len(args.params) != num_esperado:
        print(f"Erro: Esperava {num_esperado} parâmetros, mas recebeu {len(args.params)}")
        return
        
    # Mostra os parâmetros recebidos
    print("\nParâmetros recebidos:")
    for i, param in enumerate(args.params, 1):
        print(f"Parametro {i}: {param}")

if __name__ == "__main__":
    main()