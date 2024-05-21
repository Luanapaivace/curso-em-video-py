dados = dict()
go = list()
dados["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {dados["nome"]} jogou? "))
for c in range(0, partidas):
    go.append(int(input(f"Quantos gols você fez na partida {c}: ")))
dados["gol"] = go[:]
dados["total"] = sum(go)
print("-=-" * 13)
print(dados)
print("-=-" * 13)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print("-=-" * 13)
print(f"O jogador {dados['nome']} jogou {partidas} partidas")
for i, v in enumerate(dados["gol"]):
    print(f"Na partida {i}, você fez {v} gols")
print(f"Com um total de {dados["total"]} gols")