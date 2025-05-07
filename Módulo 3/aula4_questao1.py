numero_1 = int(input ("Primeiro número: ")) #pega o primeiro numero
numero_2 = int(input ("Segundo número: ")) #pega o segundo numero

soma = numero_1 + numero_2 #soma ambos os numeros
print (soma)

if soma % 2 == 0:
    print ("A soma é par")
else:
    print ("A soma é ímpar")