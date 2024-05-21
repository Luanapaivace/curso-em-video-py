from random import randint
from time import sleep
from operator import itemgetter
j = {"jogador1" : randint(1, 6),
     "jogador2" : randint(1, 6),
     "jogador3" : randint(1, 6),
     "jogador4" : randint(1, 6)}
ranking = list()
print("Valores sorteados:")
print("-=-" * 9)
for k, v in j.items():
    print(f"{k} tirou o número {v}")
    sleep(1)
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)
print("-=-" * 9)
print("Ranking: ")
print("-=-" * 9)
for i, v in enumerate(ranking):
    print(f"O {i+1} lugar: {v[0]} com {v[1]}")
print("-=-" * 9)