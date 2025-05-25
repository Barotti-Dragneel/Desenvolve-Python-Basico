N = int(input("Quantidade de respondentes: "))
soma_idades = 0
contador = 0

while contador < N:
    idade = int(input("Idade: "))
    soma_idades += idade
    contador += 1

media = soma_idades / N
print(f"Média das idades: {media:.2f}")
