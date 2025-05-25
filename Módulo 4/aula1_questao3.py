n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print ("Aprovado")
elif m >= 40:
    print ("Recuperação")
else:
    print ("Reprovado")

print ("Fim")