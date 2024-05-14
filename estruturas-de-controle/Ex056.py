s = str(input("Qual o seu sexo? (F/M): ")).strip().upper()[0]
while s not in "FfMm":
    s = str(input("Qual o seu sexo? (F/M): ")).strip().upper()[0]
print("Ok, registrado {} com sucesso".format(s))

