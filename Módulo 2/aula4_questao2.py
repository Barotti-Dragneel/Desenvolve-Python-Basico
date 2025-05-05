fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
#pega o valor da temperatura em Fahrenheit

celsius = int((fahrenheit - 32) * (5 / 9))
#converte o valor de Fahrenheit para celsius 

print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
#mostra os resultados finais