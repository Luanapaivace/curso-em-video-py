print("-=-" * 22)
print("Mostrando os 10 primeiros termos de uma PA (ou mais caso queira)")
print("-=-" * 22)
t = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão: "))
ter = t
cont = 1
q = 0
mais = 10
while cont != 0:
    q += mais
    while cont <= q:
        print("{} , ".format(ter), end="")
        ter += r
        cont += 1
    print("FIM")
    mais = int(input("Quantos termos você deseja adicionar? "))


