print("-=-" * 16)
print("Seqência de fibonacci")
print("-=-" * 16)
v = int(input("Digite quantos termos você quer que apareça: "))
n1 = 0
n2 = 1
print("-=-" * 16)
print("{} -> {}".format(n1, n2), end="")
cont = 3
while cont <= v:
    n3 = n1 + n2
    print(" -> {}".format(n3), end="")
    n1 = n2
    n2 = n3
    cont += 1
print(" -> FIM")
