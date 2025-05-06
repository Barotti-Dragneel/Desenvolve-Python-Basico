classe = input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

valido_guerreiro = classe == "guerreiro" and forca >= 15 and magia <= 10
valido_mago = classe == "mago" and forca <= 10 and magia >= 15
valido_arqueiro = classe == "arqueiro" and 5 < forca <= 15 and 5 < magia <= 15

valido = valido_guerreiro or valido_mago or valido_arqueiro

print(valido)
