from datetime import date
maior = 0
for c in range(0, 7):
    idade = int(date.today().year - int(input("Digite o ano em que você nasceu: ")))
    if idade >= 18:
        maior += 1
print("Das 7 pessoas entrevistadas {} são maiores de idade e {} menores de idade".format(maior, 7 - maior))