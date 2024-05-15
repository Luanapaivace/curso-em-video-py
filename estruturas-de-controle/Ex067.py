from random import randint
print("-=-" * 7)
print("JOGO DO PAR OU ÍMPAR")
print("-=-" * 7)
v = 0
while True:
    n = int(input("Digite um número inteiro: "))
    computador = randint(0, 100)
    l = n + computador
    esc = " "
    while esc not in "PI":
        esc = str(input("Você quer ser par ou ímpar? [P/I]")).strip().upper()[0]
    print("Você jogou {} e o computador jogou {}. A soma entre os número deu {}".format(n, computador, l,))
    if esc == "P":
        if l % 2 == 0:
            print("VOCÊ VENCEU")
            v += 1
        else:
            print("VOCÊ PERDEU")
            break
    elif esc == "I":
        if l % 2 == 1:
            print("VOCÊ VENCEU")
            v += 1
        else:
            print("VOCÊ PERDEU")
            break
    print("Vamos jogar novamente")
print(f"Você venceu {v} vez(es)")
print("FIM DE JOGO")




