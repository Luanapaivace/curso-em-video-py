aluno = dict()
aluno["nome"] = str(input("Qual é o seu nome? "))
aluno["media"] = float(input(f"Qual foi a sua média, {aluno["nome"]}? "))
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["media"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"
print("-=-" * 20)
for k, v in aluno.items():
    print(f"{k} é igual a {v}")