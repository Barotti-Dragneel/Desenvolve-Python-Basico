comprimento = int(input("Digite o comprimento do terreno (em metros): "))
#pede o comprimento do terreno em metros

largura = int(input("Digite a largura do terreno (em metros): "))
#pede a largura do terreno em metros

preco_m2 = float(input("Digite o preço do metro quadrado: "))
#pede o preço do metro quadrado

area = comprimento * largura
#calcula a area do terreno

valor_total = area * preco_m2
#calcula o valor total do terreno

print(f"O terreno possui {area}m2 e custa R${valor_total:,.2f}")
#mostra os resultados finais