import numpy as np

# Cria uma matriz 10x10 com valores de 100 até 0
matriz = np.arange(100, 0, -1).reshape(10, 10)

# Imprime a matriz em ordem inversa
print("Lista bidimensional 10x10 (ordem inversa):")
print(np.flipud(matriz))