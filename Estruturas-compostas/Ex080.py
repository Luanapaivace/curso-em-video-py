n1 = list(int(input("Digite um número inteiro: "))for c in range(0, 5))
print(f"{n1}")
print("Foram digitados {} números".format(len(n1)))
n1.sort(reverse=True)
print(f"Os números em ordem decrescente ficam: {n1}")
if 5 in n1:
    print("O valor 5 foi digitado {} vezes".format(n1.count(5)))
else:
    print("O valor 5 não foi digitado")