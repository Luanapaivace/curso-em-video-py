import random
prinome = str(input("Digite o nome de um aluno: "))
segnome = str(input("Digite o nome de outro aluno: "))
ternome = str(input("Digite o nome de mais um aluno: "))
quanome = str(input("Digite o nome do quarto aluno: "))
lista = [prinome, segnome, ternome, quanome]
sorteado = random.choice(lista)
print("O aluno sorteado foi o/a {}".format(sorteado))