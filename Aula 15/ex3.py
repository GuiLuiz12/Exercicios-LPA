numeros = list(range(1, 101))

print("=== Lista ===")
print("Ordem normal:", numeros)
print("Ordem inversa:", numeros[::-1])

dicionario = {i: i for i in range(1, 101)}
print("\n=== Dicionário ===")
print("Chaves (ordem inversa):", sorted(dicionario.keys(), reverse=True))

tupla = tuple(range(1, 101))
print("\n=== Tupla ===")
print("Ordem normal:", tupla)
print("Ordem inversa:", tupla[::-1])