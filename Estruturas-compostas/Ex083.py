n1 = list()
n2 = list()
ma = mi = 0
while True:
    n2.append(str(input("Digite o seu nome: ")))
    n2.append(float(input("Digite o seu peso: ")))
    if len(n1) == 0:
        ma = mi = n2[1]
    else:
        if n2[1] > ma:
            ma = n2[1]
        if n2[1] < mi:
            mi = n2[1]
    n1.append(n2[:])
    n2.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print(f"As informações guardadas foram: {n1}")
print(f"O total de pessoas cadastradas foram: {len(n1)}")
print(f"A pessoa com maior massa cadastrada foi igual a: {ma}")
print(f"A pessoa com menor massa cadastrada foi igual a: {mi}")
