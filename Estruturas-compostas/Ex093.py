dados = dict()
gente = list()
cont = 0
soma = media = 0
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    cont += 1
    while True:
        dados["sexo"] = str(input("Sexo: "))
        if dados["sexo"] in "MmFf":
            break
        print("Erro! Digite apenas M ou F")
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    gente.append(dados.copy())
    while True:
        r = str(input("Quer continuar? [S/N]")).upper()
        if r in "SN":
            break
        print("Erro! Digite somente S ou N")
    if r == "N":
        break
print("-=-" * 20)
print(gente)
print(f"O grupo tem {cont} pessoas")
media = soma / len(gente)
print(f"A média de idade é de {media:5.2f} anos")
print(f"As mulheres cadastradas foram: ", end=" ")
for p in gente:
    if p["sexo"] in "Ff":
        print(f"{p["nome"]}", end=" ")
print()
print(f"Lista das pessoas que estão acima da média: ")
for p in gente:
    if p["idade"] >= media:
        print(" ")
        for k, v in p.items():
            print(f"{k} = {v}", end=" ")
        print()
print("ENCERRADO")