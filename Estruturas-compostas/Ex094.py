dados = dict()
go = list()
time = list()
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    go.clear()
    for c in range(0, partidas):
        go.append(int(input(f"Quantos gols vcoê fez na partida {c}? ")))
    dados["gol"] = go[:]
    dados["total"] = sum(go)
    time.append(dados.copy())
    while True:
        r = str(input("Quer continuar? ")).upper()[0]
        if r in "SN":
            break
        print("Erro! Digite somente S ou N")
    if r == "N":
        break
print("-=-" * 30)
print("cod ", end=" ")
for i in dados.keys():
    print(f"{i:<15}", end=" ")
print()
print("-=-" * 30)
for k, v in enumerate(time):
    print(f"{k:>3} ", end=" ")
    for d in v.values():
        print(f"{str(d):>15}", end=" ")
    print()
print("-=-" * 30)
while True:
    b = int(input("Mostrar qual dados de jogador mostrar: [999 para parar]"))
    if b == 999:
        break
    if b >= len(time):
        print(f"Erro! Não existe jogador com código {b}")
    else:
        print(f"Levantamento de dados do jogador {time[b]["nome"]}: ")
        for i, g in enumerate(time[b]["gol"]):
            print(f"   No jogo {i+1} fez {g} gols")
    print("-=-" * 30)
print("FIM")