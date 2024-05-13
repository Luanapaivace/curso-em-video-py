frase = str(input("Digite uma frase: ")).upper().replace(" ","")
print(frase[::-1])
if frase == frase[::-1]:
    print("é um palíndromo")
else:
    print("não é um palíndromo")
