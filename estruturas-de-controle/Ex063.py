pa = 0
v = 0
soma = 0
while v != 999:
    v = int(input("Digite um número inteiro: [Para parar digite 999] "))
    pa += 1
    soma += v
print("FIM")
print("A quantidade de palpites que você deu foi de {}".format(pa - 1))
print("A soma entre eles é igual a {}".format(soma - 999))