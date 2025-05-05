# Lê o valor inteiro em reais
valor = int(input("Digite o valor:"))

# Calcula quantas notas de 100
notas_100 = valor // 100
valor %= 100  # Atualiza o valor restante

# Calcula quantas notas de 50
notas_50 = valor // 50
valor %= 50

# Calcula quantas notas de 20
notas_20 = valor // 20
valor %= 20

# Calcula quantas notas de 10
notas_10 = valor // 10
valor %= 10

# Calcula quantas notas de 5
notas_5 = valor // 5
valor %= 5

# Calcula quantas notas de 2
notas_2 = valor // 2
valor %= 2

# O que sobrar são notas de 1
notas_1 = valor

# Imprime o resultado no formato solicitado
print(f"{notas_100} nota(s) de R$100,00")
print(f"{notas_50} nota(s) de R$50,00")
print(f"{notas_20} nota(s) de R$20,00")
print(f"{notas_10} nota(s) de R$10,00")
print(f"{notas_5} nota(s) de R$5,00")
print(f"{notas_2} nota(s) de R$2,00")
print(f"{notas_1} nota(s) de R$1,00")
