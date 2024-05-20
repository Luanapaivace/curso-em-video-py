n1 = [[0, 0, 0], [0, 0 ,0], [0, 0, 0]]
n2 = 0
for l in range (0, 3):
    for c in range(0, 3):
        n1[l][c] = int(input(f"Digite um valor para {l} e {c}: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{n1[l][c]:^5}]", end=" ")
    print()
