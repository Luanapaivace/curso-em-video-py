i = int(input("Digite um número inteiro: "))
tot = 0
for c in range(1, i +1):
    if i % c == 0:
        print("{} sim".format(c))
        tot += 1
    else:
        print("{} não".format(c))
print("Esse número {} foi dividido {} vezes".format(i, tot))
if tot == 2:
    print("é primo!")
else:
    print("não é primo!")