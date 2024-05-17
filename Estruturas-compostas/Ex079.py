n1 = list()
for c in range(0, 5):
    n = int(input("Digite um número inteiro: "))
    if c == 0 or n > n1[-1]:
        n1.append(n)
    else:
        pos = 0
        while pos < len(n1):
            if n <= n1[pos]:
                n1.insert(pos, n)
                break
            pos += 1
print(f"Os valores em organizados em oredem ficaram: {n1}")