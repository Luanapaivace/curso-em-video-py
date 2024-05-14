from random import randint
computador = randint(0, 10)
print("-=-" * 18)
print("Vou pensar em um número entre 0 e 10, tente adivinhar!")
print("-=-" * 18)
jogador = int(input("Em qual número eu pensei? "))
palpite = 1
while jogador != computador:
    jogador = int(input("Em qual número eu pensei? "))
    palpite += 1
print("Você acertouuu! E teve que jogar {} vezes até acertar.".format(palpite))