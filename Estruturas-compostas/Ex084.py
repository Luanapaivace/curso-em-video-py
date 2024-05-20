n1 = [[], []]
n2 = 0
for c in range (0, 7):
    n2 = int(input("Digite um número inteiro: "))
    if n2 % 2 == 0:
        n1[0].append(n2)
    else:
        n1[1].append(n2)
print(f"Os números pares são: {n1[0]}")
print(f"Os números impares são iguais a: {n1[1]}")