soma = n = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 999:
        break
    soma += n
print(f"A soma de todos os números digitados é igual a {soma}")