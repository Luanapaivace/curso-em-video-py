numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    esc = int(input("Digite um número inteiro entre 0 e 20: "))
    if 0 <= esc <= 20:
        break
    print("Tente novamente", end=" ")
print(f"Você digitou o número: {numeros[esc]}")