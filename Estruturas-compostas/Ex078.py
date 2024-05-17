n1 = list()
while True:
    n = int(input("Digite um número inteiro: "))
    if n not in n1:
        n1.append(n)
        print("Valor adicionado")
    else:
        print("Número repetido, não vou adicionar")
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print(f"Você adicionou os respectivos números: {n1}")
