def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna o produto de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão entre dois números.
    Retorna mensagem de erro se o divisor for zero."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida"
    return a / b