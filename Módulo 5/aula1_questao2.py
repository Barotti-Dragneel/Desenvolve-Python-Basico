import random
import math

n = int(input("Quantos números aleatórios voce quer gerar? "))

soma = 0

for i in range(n):
    numero = random.randint(0, 100)
    print(f"numero{i+1}: {numero}")
    soma += numero

raiz = math.sqrt(soma)

print("A raiz quadrada da soma dos números é: ", round(raiz, 2))