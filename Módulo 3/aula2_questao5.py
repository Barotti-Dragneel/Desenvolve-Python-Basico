genero = input ("Qual seu gênero? f ou m?")
idade = int(input ("Qual sua idade?"))
tempo = int(input ("Quanto tempo você trabalhou?"))

criterio_1 = (genero == 'f' and idade >= 60) or (genero == 'm' and idade >= 65)
criterio_2 = tempo >= 30
criterio_3 = idade >= 60 and tempo >= 25

pode_aposentar = criterio_1 or criterio_2 or criterio_3

print (pode_aposentar)