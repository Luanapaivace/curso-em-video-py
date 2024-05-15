r = "S"
soma = quant = media = maior = menor = 0
while r in "Ss":
    n = int(input("Digite um número inteiro: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input("Quer continuar? [digite S/ N]")).upper().strip()[0]
media = soma / quant
print("Você digitou {} números e a média foi de {}".format(quant, soma / quant))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))