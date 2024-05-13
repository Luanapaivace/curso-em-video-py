import random
n1 = str(input("Digite o nome de um aluno: "))
n2 = str(input("Digite o nome de mais um aluno: "))
n3 = str(input("Digite o nome de outro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print("a ordem de apresentação dos alunos será: ")
print(lista)