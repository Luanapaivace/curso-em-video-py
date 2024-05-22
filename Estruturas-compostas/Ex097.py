def contador(i, f, p):
    print(f"Contando de {i} até {f} pulando de {p} em {p}")
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ")
            cont -= p
        print("FIM")


contador(1, 10, 1)
contador(10, 1, 1)
print("-=-" * 12)
print("Sua vez de personalizar os números!")
i = int(input("Com qual número você deseja começar? "))
fim = int(input("Com qual número você deseja terminar? "))
pul = int(input("Com qual número vc deseja pular a sequência? "))
contador(i, fim, pul)
