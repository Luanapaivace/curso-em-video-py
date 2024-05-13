from random import randint
itens = ("norte", "papel", "pedra", "tesoura")
computador = randint(1, 3)
print("=-=" * 5)
print("""Suas opções:
[1] PAPEL
[2] PEDRA 
[3] TESOURA""")
print("=-=" * 5)
jogador = int(input("Escolha umas das 3 opções a cima: "))
print("O jogador jogou {}".format(itens[jogador]))
print("O computador jogou {}".format(itens[computador]))
if computador == 1:
    if jogador == 1:
        print("EMPATE")
    if jogador == 2:
        print("COMPUTADOR GANHOU")
    if jogador == 3:
        print("JOGADOR VENCEU")
if computador == 2:
    if jogador == 1:
        print("JOGADOR GANHOU")
    if jogador == 2:
        print("EMPATE")
    if jogador == 3:
        print("COMPUTADOR GANHOU")
if computador == 3:
    if jogador == 1:
        print("COMPUTADOR GANHOU")
    if jogador == 2:
        print("JOGADOR GANHOU")
    if jogador == 3:
        print("EMPATE")
