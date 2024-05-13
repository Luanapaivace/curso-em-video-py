soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
print("A soma de todos os números impares entre 1 e 500 e que sejam divisiveis por 3 é igual a {}".format(soma))