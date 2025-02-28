def isTriangulo(a: int, b: int, c: int) -> bool:
    """
    Verifica se três lados podem formar um triângulo.
    
    Args:
        a (int): Primeiro lado
        b (int): Segundo lado
        c (int): Terceiro lado
        
    Returns:
        bool: True se formar um triângulo, False caso contrário
    """
    # Verifica se todos os lados são positivos
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Verifica se a soma de dois lados é maior que o terceiro
    return (abs(a + b) > c and 
            abs(a + c) > b and 
            abs(b + c) > a)

print("Teste 1:", isTriangulo(3, 4, 5)) 
print("Teste 2:", isTriangulo(1, 2, 4)) 
print("Teste 3:", isTriangulo(5, 5, 5)) 
print("Teste 4:", isTriangulo(0, 3, 4)) 