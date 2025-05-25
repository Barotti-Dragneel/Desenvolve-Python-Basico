N = int(input("Quantos experimentos foram realizados: "))

total = 0
coelhos = 0
ratos = 0
sapos = 0

for _ in range(N):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    total += quantia
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

percentual_c = (coelhos / total) * 100
percentual_r = (ratos / total) * 100
percentual_s = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_c:.2f} %")
print(f"Percentual de ratos: {percentual_r:.2f} %")
print(f"Percentual de sapos: {percentual_s:.2f} %")
