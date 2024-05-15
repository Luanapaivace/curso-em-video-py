cont = 0
while cont <= 10:
    n = int(input("Digite um número para saber a sua tabuada: [digite 0 quando quiser encerrar]"))
    if n == 0:
        break
    print("-=-" * 15)
    for c in range(0, 11):
        print(f"{n} x {c} = {n * c}")
print("FIM DA TABUADA")