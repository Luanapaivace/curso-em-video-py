n1 = list()
p = list()
i = list()
while True:
    n1.append(int(input("Digite um número inteiro: ")))
    r = str(input("Quer continuar? "))
    if r in "Nn":
        break
for b, v in enumerate(n1):
    if v % 2 == 0:
        p.append(v)
    elif v % 2 == 1:
        i.append(v)
print(f"A lista completa: {n1}")
print(f"Os números pares: {p}")
print(f"Os números ímpares: {i}")

