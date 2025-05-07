distancia_km = int(input ("Qual a distância em quilômetros da entrega? "))
peso_kg = int(input ("Qual o peso em quilogramas do pacote? "))

if distancia_km <= 100:
    preco_kg = 1.0
elif distancia_km <= 300:
    preco_kg = 1.5
else:
    preco_kg = 2.0

frete = peso_kg * preco_kg

if peso_kg > 10:
    preco_kg += 10

print (f"Valor do frete: R${frete:.2f}")