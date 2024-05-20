n1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n2 = n3 = n4 = 0
for l in range (0, 3):
    for c in range(0, 3):
        n1[l][c] = int(input(f"Digite um número inteiro para os valores {l} e {c}: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{n1[l][c]:^5}]", end=" ")
        if n1[l][c] % 2 == 0:
          n2 += n1[l][c]
    print()
print(f"A soma de todos os valores pares digitados é igual a: {n2}")
for l in range(0, 3):
    n4 += n1[l][2]
print(f"A soma dos valores da terceira coluna é igual a: {n4}")
for l in range(0, 3):
    if c == l:
        n3 = n1[1][c]
    elif n1[1][c] > n3:
        n3 = n1[1][c]
print(f"O maior valor da segundo linha é o: {n3}")