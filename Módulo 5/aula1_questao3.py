import random

numero_secreto = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entrer 1 e 10: "))

    if palpite < numero_secreto:
        print("Muito baixo, tente novamente")
    
    elif palpite > numero_secreto:
        print("Muito alto, tente novamente")
    
    else:
        print(f"Correto, o número é {numero_secreto}")
        break