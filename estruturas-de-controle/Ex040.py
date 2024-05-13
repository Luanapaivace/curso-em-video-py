from datetime import date
ano = int(input("Em qual ano você nasceu? "))
a = date.today().year
idade = a - ano
if idade <= 9:
    print("Você está dentro da classificação mirim")
elif idade > 9 and idade <= 14:
    print("Você está dentro da classificação infantil")
elif idade > 14 and idade <= 19:
    print("Você está dentro da classificação junior")
elif idade > 19 and idade <= 20:
    print("Você está dentro da classificação sênior")
elif idade > 20:
    print("Você está dentro da classificação master")
