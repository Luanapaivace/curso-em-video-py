from random import randint
con = 1
j = list()
jogos = list()
tot = 1
n1 = int(input("Quantos jogos você deseja que sejam sorteados? "))
while tot <= n1:
    cont = 0
    while True:
        ale = randint(1, 60)
        if ale not in j:
            j.append(ale)
            cont += 1
        if cont >= 6:
            break
    j.sort()
    jogos.append(j[:])
    j.clear()
    tot += 1
print(f"{jogos}")