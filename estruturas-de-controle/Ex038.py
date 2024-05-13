from datetime import date
nasc = int(input("Em qual ano você nasceu? "))
atual = date.today().year
a = atual - nasc
print("Quem nasceu em {} terá {} anos em 2024".format(nasc, a))
if a == 18:
    print("Você tem que se alistar imediatamente!!!")
elif a < 18:
    ida = 18 - a
    print("Você ainda não tem a idade para se alistar (18 anos), você ainda tem {} ano até o alistamento".format(ida))
elif a > 18:
    print("Você já deveria ter se alistado!")