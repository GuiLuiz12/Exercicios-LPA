import math

def circCirculo(raio: int) -> float:
    """
    Calcula a circunferência de um círculo dado seu raio.
    
    Args:
        raio (int): Raio do círculo
        
    Returns:
        float: Circunferência do círculo
    """
    return 2 * math.pi * raio

print(f"Circunferência com raio 5: {circCirculo(5):.2f}")
print(f"Circunferência com raio 10: {circCirculo(10):.2f}")
print(f"Circunferência com raio 15: {circCirculo(15):.2f}")