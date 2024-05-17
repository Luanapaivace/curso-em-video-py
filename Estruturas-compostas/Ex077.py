n1 = list(int(input("Digite um número inteiro: "))for c in range(0, 5))
print(f"Você digitou os números: {n1}")
print(f"O maior número foi: {max(n1)}")
print(f"O menor número foi: {min(n1)}")
for pos, c in enumerate(n1):
    print(f"Suas respectivas posições são: {c} na posição {pos}")