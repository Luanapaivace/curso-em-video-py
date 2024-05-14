print("-=-" * 7)
print("10 termos de uma PA")
print("-=-" * 7)
t = int(input("primeiro termo: "))
r = int(input("razão: "))
ter = 1
cont = 1
while cont <= 10:
    print("{} , ".format(ter), end="")
    ter += r
    cont += 1
print("FIM")