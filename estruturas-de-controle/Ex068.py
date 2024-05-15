qa = qh = qf = 0
while True:
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Qual o seu sexo?[F/M] ")).strip().upper()[0]
    conti = " "
    while conti not in "SN":
        print(f"Você tem {idade} e é do sexo {sexo}")
        conti = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
    if idade > 18:
        qa += 1
    if sexo == "M":
        qh += 1
    elif sexo == "F":
        if idade < 20:
         qf += 1
    if conti == "S":
        print("OK, VAMOS PARA A PRÓXIMA PESSOA")
    elif conti == "N":
        print("OK, FINALIZANDO A PESQUISA")
        break
print(f"PESSOAS COM MAIS DE 18 ANOS: {qa}")
print(f"QUANTIDADE DE HOMENS QUE RESPONDERAM A PESQUISA: {qh}")
print(f"QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS QUE RESPONDERAM A PESQUISA: {qf}")
print("FIM DA PESQUISA")