n = 0
i = 0
soma = 0

n = int(input("Digite a quantidade de números: "))

for i in range(1, n + 1):
    num = int(input(f"Digite o número {i}: "))
    soma += num

if soma % 2 == 0:
    print("A soma dos números é par.")
else:
    print("A soma dos números é ímpar.")