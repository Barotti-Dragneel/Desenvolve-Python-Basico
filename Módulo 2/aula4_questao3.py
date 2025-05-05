# Produto 1
nome1 = input("Digite o nome do produto 1:") #nome do produto 1
preco1 = float(input("Digite o preço unitário do produto 1:")) #preço do produto 1
quant1 = int(input("Digite a quantidade do produto 1: ")) #quantidade do produto 1

# Produto 2
nome2 = input("Digite o nome do produto 2:") #nome do produto 2
preco2 = float(input("Digite o preço unitário do produto 2:")) #preço do produto 2
quant2 = int(input("Digite a quantidade do produto 2: ")) #quantidade do produto 2

# Produto 3
nome3 = input("Digite o nome do produto 3:") #nome do produto 3
preco3 = float(input("Digite o preço unitário do produto 3:")) #preço do produto 3
quant3 = int(input("Digite a quantidade do produto 3: ")) #quantidade do produto 3

# Cálculo do total
total = (preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3)

# Saída formatada
print(f"Total: R${total:,.2f}")
