from operacoes import soma, subtracao, multiplicacao, divisao
from utils import exibir_resultado

def obter_numero(mensagem):
    """Obtém um número válido do usuário."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    operacoes = {
        '+': ('Soma', soma),
        '-': ('Subtração', subtracao),
        '*': ('Multiplicação', multiplicacao),
        '/': ('Divisão', divisao)
    }
    
    print("=== Calculadora Modular ===")
    
    # Selecionar operação
    print("\nOperações disponíveis:")
    for op in operacoes.keys():
        print(f"{op}: {operacoes[op][0]}")
    
    op = input("\nEscolha uma operação (+, -, *, /): ")
    if op not in operacoes:
        print("Operação inválida!")
        return
    
    # Obter números
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    
    # Executar operação e exibir resultado
    nome_op, funcao = operacoes[op]
    resultado = funcao(num1, num2)
    exibir_resultado(nome_op, resultado)

if __name__ == "__main__":
    main()