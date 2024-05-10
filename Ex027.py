from random import randint
computador = randint(0, 5)
print('-_-' * 18)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
print('-_-' * 18)
jogador = int(input("Em que número eu pensei? "))
if jogador == computador:
    print("Parabéns!!! Você acertou!")
else:
    print("Que pena,não foi dessa vez... Eu pensei no número {} e não no núumero {}".format(computador, jogador))