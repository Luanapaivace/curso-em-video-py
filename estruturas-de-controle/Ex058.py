from time import sleep
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite outro valor inteiro: "))
print("-=-" * 11)
print("""Escolha uma das operações abaixo:
[0] SOMAR
[1] MULTIPLCAR
[2] MAIOR
[3] NOVOS NÚMEROS
[4] SAIR DO PROGRAMA""")
print("-=-" * 11)
n3 = int(input("Qual é a sua escolha? "))
while n3 != 4:
    if n3 == 0:
        l1 = n1 + n2
        print("SOMA: {} + {} = {}".format(n1, n2, l1))
    elif n3 == 1:
        l2 = n1 * n2
        print("MULTIPLICAÇÃO: {} X {} = {}".format(n1, n2, l2))
    elif n3 == 2:
        if n1 > n2:
            print("O {} é maior que {}".format(n1, n2))
        elif n1 < n2:
            print("O {} é maior que {}".format(n2, n1))
    elif n3 == 3:
        print("Informe os números novos: ")
        n1 = int(input("Digite um novo número inteiro: "))
        n2 = int(input("Digite um segundo novo número inteiro: "))
    else:
        print("Opção inválida. Tente novamente")
    print("-=-" * 11)
    print("""Escolha uma das operações abaixo:
    [0] SOMAR
    [1] MULTIPLCAR
    [2] MAIOR
    [3] NOVOS NÚMEROS
    [4] SAIR DO PROGRAMA""")
    print("-=-" * 11)
    n3 = int(input("Qual é a sua escolha? "))
    sleep(1)
print("Finalizando...")
sleep(2)
print("Programa finalizado!")
